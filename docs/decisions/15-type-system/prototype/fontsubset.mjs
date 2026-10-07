// PROTOTYPE (#15) — publish-time font subsetting, the shape of a future admin/services/fonts.js.
// Runs unchanged in Node 22 and in the browser. Needs only WebAssembly (CSP 'wasm-unsafe-eval')
// and a zlib "deflate" compressor (CompressionStream in browsers, node:zlib in Node).

const NUMERAL_FEATURES = ['tnum', 'pnum', 'lnum', 'onum', 'zero', 'case', 'frac', 'numr', 'dnom', 'sups', 'subs', 'ordn'];

const tag = (s) => ((s.charCodeAt(0) << 24) | (s.charCodeAt(1) << 16) | (s.charCodeAt(2) << 8) | s.charCodeAt(3)) >>> 0;

/** @param {BufferSource} wasmBytes harfbuzz-subset.wasm */
export async function createSubsetter(wasmBytes) {
  const { instance } = await WebAssembly.instantiate(wasmBytes, {});
  const x = instance.exports;
  const heap = () => new Uint8Array(x.memory.buffer);

  /**
   * @param {Uint8Array} font  TTF/OTF master
   * @param {Iterable<number>} codepoints
   * @param {Record<string, number>} [pin]  axis tag -> value, e.g. { wght: 400 }
   * @returns {Uint8Array} subset sfnt
   */
  function subset(font, codepoints, pin = {}) {
    const ptr = x.malloc(font.byteLength);
    heap().set(font, ptr);
    const blob = x.hb_blob_create(ptr, font.byteLength, 2 /* WRITABLE */, 0, 0);
    const face = x.hb_face_create(blob, 0);
    x.hb_blob_destroy(blob);
    const input = x.hb_subset_input_create_or_fail();
    const set = x.hb_subset_input_unicode_set(input);
    for (const cp of codepoints) x.hb_set_add(set, cp);
    // HarfBuzz's default feature list drops the numeral features, which would silently break
    // tabular and lining figures in tables (found in #15). Add them to the defaults.
    const features = x.hb_subset_input_set(input, 6 /* HB_SUBSET_SETS_LAYOUT_FEATURE_TAG */);
    for (const f of NUMERAL_FEATURES) x.hb_set_add(features, tag(f));
    for (const [axis, value] of Object.entries(pin)) x.hb_subset_input_pin_axis_location(input, face, tag(axis), value);
    const out = x.hb_subset_or_fail(face, input);
    x.hb_subset_input_destroy(input);
    if (!out) { x.hb_face_destroy(face); x.free(ptr); throw new Error('subset failed'); }
    const outBlob = x.hb_face_reference_blob(out);
    const off = x.hb_blob_get_data(outBlob, 0);
    const len = x.hb_blob_get_length(outBlob);
    const bytes = heap().slice(off, off + len);
    x.hb_blob_destroy(outBlob);
    x.hb_face_destroy(out);
    x.hb_face_destroy(face);
    x.free(ptr);
    return bytes;
  }
  return { subset };
}

/**
 * Wrap an sfnt as WOFF 1.0 (W3C), compressing each table with zlib.
 * @param {Uint8Array} sfnt
 * @param {(b: Uint8Array) => Promise<Uint8Array>} deflate  zlib-wrapped deflate
 */
export async function toWoff(sfnt, deflate) {
  const dv = new DataView(sfnt.buffer, sfnt.byteOffset, sfnt.byteLength);
  const numTables = dv.getUint16(4);
  const tables = [];
  for (let i = 0; i < numTables; i++) {
    const r = 12 + i * 16;
    const t = { tag: dv.getUint32(r), checksum: dv.getUint32(r + 4), offset: dv.getUint32(r + 8), length: dv.getUint32(r + 12) };
    const raw = sfnt.subarray(t.offset, t.offset + t.length);
    const z = await deflate(raw);
    t.data = z.byteLength < raw.byteLength ? z : raw;
    tables.push(t);
  }
  const pad4 = (n) => (n + 3) & ~3;
  let size = 44 + 20 * numTables;
  for (const t of tables) size = pad4(size) + t.data.byteLength;
  size = pad4(size);
  const out = new Uint8Array(size);
  const o = new DataView(out.buffer);
  let totalSfnt = 12 + 16 * numTables;
  for (const t of tables) totalSfnt += pad4(t.length);
  o.setUint32(0, 0x774f4646); // 'wOFF'
  o.setUint32(4, dv.getUint32(0)); // flavor
  o.setUint32(8, size);
  o.setUint16(12, numTables);
  o.setUint32(16, totalSfnt);
  o.setUint16(20, 1); // major version
  let at = 44 + 20 * numTables;
  tables.forEach((t, i) => {
    at = pad4(at);
    const d = 44 + i * 20;
    o.setUint32(d, t.tag);
    o.setUint32(d + 4, at);
    o.setUint32(d + 8, t.data.byteLength);
    o.setUint32(d + 12, t.length);
    o.setUint32(d + 16, t.checksum);
    out.set(t.data, at);
    at += t.data.byteLength;
  });
  return out;
}

/** Browser deflate (zlib wrapper), as WOFF requires. */
export async function browserDeflate(bytes) {
  const stream = new Blob([bytes]).stream().pipeThrough(new CompressionStream('deflate'));
  return new Uint8Array(await new Response(stream).arrayBuffer());
}

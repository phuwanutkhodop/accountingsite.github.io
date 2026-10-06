// Git blob SHA-1, computed the way git does: sha1("blob " + byteLength + "\0" + bytes).
// The length is the UTF-8 BYTE count, never the JavaScript string length (plan review M11):
// Thai and Chinese characters take 3 bytes each, so the two numbers differ.
// Pure module: runs unchanged in the browser and in Node (globalThis.crypto.subtle).

export async function gitBlobSha(bytes) {
  const header = new TextEncoder().encode(`blob ${bytes.length}\0`);
  const all = new Uint8Array(header.length + bytes.length);
  all.set(header, 0);
  all.set(bytes, header.length);
  const digest = await globalThis.crypto.subtle.digest('SHA-1', all);
  return [...new Uint8Array(digest)].map(b => b.toString(16).padStart(2, '0')).join('');
}

export const gitBlobShaOfText = text => gitBlobSha(new TextEncoder().encode(text));

// The mistake the Admin must never make, kept so the proof can show the difference.
export async function wrongShaUsingStringLength(text) {
  const bytes = new TextEncoder().encode(text);
  const header = new TextEncoder().encode(`blob ${text.length}\0`);
  const all = new Uint8Array(header.length + bytes.length);
  all.set(header, 0);
  all.set(bytes, header.length);
  const digest = await globalThis.crypto.subtle.digest('SHA-1', all);
  return [...new Uint8Array(digest)].map(b => b.toString(16).padStart(2, '0')).join('');
}

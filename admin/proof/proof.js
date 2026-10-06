// Ticket #20: browser-only publish proof. Hand-made test tool, not Admin code; removed when #20 closes.
// The key lives in one variable for the length of a run, is sent only to api.github.com, and is never stored.

import { gitBlobSha, gitBlobShaOfText, wrongShaUsingStringLength } from './gitsha.js';

const OWNER = 'phuwanutkhodop';
const SITE = 'accountingsite.github.io';
const DRAFTS = 'accountingsite-drafts';
const API = 'https://api.github.com';
const OUT = 'admin/proof/out';            // test files this page publishes and then removes
const LIVE_TIMEOUT_MS = 10 * 60 * 1000;
const POLL_MS = 3000;

if (window.top !== window.self) {
  document.body.textContent = 'This page refuses to run inside a frame.';
  throw new Error('framed');
}

const $ = id => document.getElementById(id);
const sleep = ms => new Promise(r => setTimeout(r, ms));
const now = () => performance.now();

let token = null;

class ApiError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}

async function api(method, path, body, extraHeaders = {}) {
  const res = await fetch(API + path, {
    method,
    cache: 'no-store',
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
      ...(body ? { 'Content-Type': 'application/json' } : {}),
      ...extraHeaders,
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  const json = text ? JSON.parse(text) : null;
  if (!res.ok) throw new ApiError(res.status, json?.message || res.statusText);
  return { json, res };
}

function explain(e) {
  if (e instanceof ApiError) {
    const hint = {
      401: 'กุญแจไม่ถูกต้องหรือหมดอายุ (bad or expired key)',
      403: 'กุญแจมีสิทธิ์ไม่พอ: ตรวจ Contents = Read and write และ Pages = Read-only (missing permission)',
      404: 'ไม่พบ: กุญแจอาจไม่ได้เลือกที่เก็บนี้ หรือชื่อที่เก็บไม่ตรง (repo not selected or not found)',
      409: 'ที่เก็บว่างเปล่า: สร้างใหม่โดยติ๊ก "Add a README file" (repository is empty)',
    }[e.status];
    return `HTTP ${e.status}: ${e.message}${hint ? ' · ' + hint : ''}`;
  }
  return `${e.name}: ${e.message}`;
}

// ---- step list in the page -------------------------------------------------

const report = { ticket: 20, runId: '', startedAt: '', userAgent: navigator.userAgent, tokenExpiryEnteredByOwner: '', steps: [], findings: {} };

function step(name) {
  const li = document.createElement('li');
  li.dataset.state = 'run';
  li.innerHTML = '<span class="n"></span> <span class="s">…</span><span class="d"></span>';
  li.querySelector('.n').textContent = name;
  $('steps').append(li);
  const t0 = now();
  const finish = (ok, detail) => {
    const ms = Math.round(now() - t0);
    li.dataset.state = ok ? 'ok' : 'bad';
    li.querySelector('.s').textContent = ok ? `✓ ${ms} ms` : '✗';
    li.querySelector('.d').textContent = detail || '';
    report.steps.push({ name, ok, ms, detail: detail || '' });
    return ok;
  };
  return { ok: d => finish(true, d), bad: d => finish(false, d) };
}

// ---- git helpers -----------------------------------------------------------

const repoPath = repo => `/repos/${OWNER}/${repo}`;

async function head(repo, branch) {
  const { json: ref } = await api('GET', `${repoPath(repo)}/git/ref/heads/${branch}`);
  const { json: commit } = await api('GET', `${repoPath(repo)}/git/commits/${ref.object.sha}`);
  return { commit: ref.object.sha, tree: commit.tree.sha };
}

async function commitFiles(repo, branch, base, entries, message) {
  const { json: tree } = await api('POST', `${repoPath(repo)}/git/trees`, { base_tree: base.tree, tree: entries });
  const { json: commit } = await api('POST', `${repoPath(repo)}/git/commits`, { message, tree: tree.sha, parents: [base.commit] });
  await api('PATCH', `${repoPath(repo)}/git/refs/heads/${branch}`, { sha: commit.sha, force: false });
  return { commit: commit.sha, tree: tree.sha };
}

const addFile = (path, content) => ({ path, mode: '100644', type: 'blob', content });
const removeFile = path => ({ path, mode: '100644', type: 'blob', sha: null });

function base64ToBytes(b64) {
  const bin = atob(b64.replace(/\n/g, ''));
  return Uint8Array.from(bin, c => c.charCodeAt(0));
}

// ---- the run ---------------------------------------------------------------

async function run() {
  const runId = [...crypto.getRandomValues(new Uint8Array(6))].map(b => b.toString(16).padStart(2, '0')).join('');
  report.runId = runId;
  report.startedAt = new Date().toISOString();
  report.tokenExpiryEnteredByOwner = $('expiry').value;

  let site, siteBranch, drafts, draftsBranch, base, published = null;

  // 1. identity and readable headers
  let s = step('1. ตรวจกุญแจ · identity');
  try {
    const { json, res } = await api('GET', '/user');
    report.findings.login = json.login;
    report.findings.rateLimitRemainingReadable = res.headers.get('x-ratelimit-remaining') !== null;
    report.findings.tokenExpiryHeaderReadable = res.headers.get('github-authentication-token-expiration') !== null;
    if (json.login !== OWNER) return s.bad(`เป็นบัญชี ${json.login} ไม่ใช่ ${OWNER} (wrong account)`);
    s.ok(`บัญชี ${json.login} · อ่านวันหมดอายุจาก GitHub ได้: ${report.findings.tokenExpiryHeaderReadable ? 'ได้' : 'ไม่ได้ (ตามคาด)'}`);
  } catch (e) { return s.bad(explain(e)); }

  // 2. site repo and Pages
  s = step('2. ที่เก็บเว็บไซต์ · site repo + Pages');
  try {
    ({ json: site } = await api('GET', repoPath(SITE)));
    siteBranch = site.default_branch;
    let pagesNote = '';
    try {
      const { json: pages } = await api('GET', `${repoPath(SITE)}/pages`);
      report.findings.pagesSource = pages.source;
      report.findings.pagesUrl = pages.html_url;
      pagesNote = ` · Pages: ${pages.source?.branch}${pages.source?.path}`;
    } catch (e) { report.findings.pagesReadError = explain(e); pagesNote = ' · Pages: อ่านไม่ได้'; }
    s.ok(`${site.full_name} (${site.visibility}) · branch ${siteBranch}${pagesNote}`);
  } catch (e) { return s.bad(explain(e)); }

  // 3. drafts repo
  s = step('3. ที่เก็บส่วนตัว · drafts repo');
  try {
    ({ json: drafts } = await api('GET', repoPath(DRAFTS)));
    draftsBranch = drafts.default_branch;
    report.findings.draftsPrivate = drafts.private;
    if (!drafts.private) return s.bad(`${drafts.full_name} เป็นสาธารณะ ต้องเป็น Private (must be private)`);
    s.ok(`${drafts.full_name} (private) · branch ${draftsBranch}`);
  } catch (e) { return s.bad(explain(e)); }

  // 4. read the whole tree
  s = step('4. อ่านโครงไฟล์ทั้งเว็บ · read tree');
  let entries;
  try {
    base = await head(SITE, siteBranch);
    const { json } = await api('GET', `${repoPath(SITE)}/git/trees/${base.tree}?recursive=1`);
    entries = json.tree;
    report.findings.treeEntries = entries.length;
    report.findings.treeTruncated = json.truncated;
    s.ok(`${entries.length} รายการ · truncated: ${json.truncated}`);
  } catch (e) { return s.bad(explain(e)); }

  // 5. blob SHA computed locally must equal git's
  s = step('5. ตรวจลายนิ้วมือไฟล์ · local blob SHA');
  try {
    const known = entries.find(e => e.path === 'en/index.html' && e.type === 'blob');
    const { json: blob } = await api('GET', `${repoPath(SITE)}/git/blobs/${known.sha}`);
    const existingOk = (await gitBlobSha(base64ToBytes(blob.content))) === known.sha;
    const text = `ทดสอบ 税务 ✓ ${runId}\n`;
    const local = await gitBlobShaOfText(text);
    const { json: made } = await api('POST', `${repoPath(SITE)}/git/blobs`, { content: text, encoding: 'utf-8' });
    const thaiOk = made.sha === local;
    const wrongDiffers = (await wrongShaUsingStringLength(text)) !== made.sha;
    Object.assign(report.findings, { hashExistingFileOk: existingOk, hashThaiChineseOk: thaiOk, stringLengthMethodWouldBeWrong: wrongDiffers });
    if (!existingOk || !thaiOk) return s.bad(`ไฟล์เดิม ${existingOk} · ไทย/จีน ${thaiOk}`);
    s.ok('ตรงกันทั้งไฟล์เดิมและข้อความไทย/จีน (UTF-8 bytes)');
  } catch (e) { return s.bad(explain(e)); }

  // 6. publish two files in one commit, fast-forward only
  s = step('6. Publish ไฟล์ทดสอบ 2 ไฟล์ · one commit');
  const stamp = JSON.stringify({ runId, note: 'Ticket #20 proof; removed again automatically' }) + '\n';
  const hello = `<!doctype html>\n<html lang="th"><meta charset="utf-8"><meta name="robots" content="noindex"><title>Proof ${runId}</title>\n<p>ทดสอบ · Test · 测试 ${runId}</p></html>\n`;
  let publishedAt;
  try {
    published = await commitFiles(SITE, siteBranch, base,
      [addFile(`${OUT}/stamp.json`, stamp), addFile(`${OUT}/hello.html`, hello)],
      `Proof #20: browser publish test (reverted automatically)\n\nBuilder-Proof: 20 ${runId}`);
    publishedAt = now();
    report.findings.publishCommit = published.commit;
    s.ok(`commit ${published.commit.slice(0, 7)}`);
  } catch (e) { s.bad(explain(e)); return; }

  try {
    // 7. a stale update must be refused
    s = step('7. กันเขียนทับ · stale update refused');
    try {
      const { json: stale } = await api('POST', `${repoPath(SITE)}/git/commits`,
        { message: 'Proof #20: stale commit (must be refused)', tree: base.tree, parents: [base.commit] });
      try {
        await api('PATCH', `${repoPath(SITE)}/git/refs/heads/${siteBranch}`, { sha: stale.sha, force: false });
        report.findings.fastForwardGuard = 'NOT refused';
        s.bad('GitHub ยอมรับการเขียนทับ (unexpected)');
      } catch (e) {
        report.findings.fastForwardGuard = e instanceof ApiError ? `refused HTTP ${e.status}` : explain(e);
        if (e instanceof ApiError && e.status === 422) s.ok('GitHub ปฏิเสธตามคาด (HTTP 422)'); else s.bad(explain(e));
      }
    } catch (e) { s.bad(explain(e)); }

    // 8. wait until the files are really served by Pages
    s = step('8. รอจนขึ้นเว็บจริง · wait until live');
    let live = false, lastBuild = null, nextBuildCheck = 0;
    while (now() - publishedAt < LIVE_TIMEOUT_MS) {
      try {
        const r = await fetch(`./out/stamp.json?r=${Date.now()}`, { cache: 'no-store' });
        if (r.ok && (await r.json()).runId === runId) { live = true; break; }
      } catch { /* not there yet */ }
      if (now() > nextBuildCheck) {
        try {
          const { json: b } = await api('GET', `${repoPath(SITE)}/pages/builds/latest`);
          lastBuild = { status: b.status, commit: b.commit?.slice(0, 7) };
        } catch (e) { lastBuild = { error: explain(e) }; }
        nextBuildCheck = now() + 15000;
      }
      $('steps').lastElementChild.querySelector('.d').textContent =
        `${Math.round((now() - publishedAt) / 1000)} วินาที · Pages build: ${lastBuild ? JSON.stringify(lastBuild) : '…'}`;
      await sleep(POLL_MS);
    }
    report.findings.lastPagesBuild = lastBuild;
    report.findings.secondsUntilLive = live ? Math.round((now() - publishedAt) / 1000) : null;
    if (live) s.ok(`ขึ้นเว็บจริงใน ${report.findings.secondsUntilLive} วินาที`); else s.bad('ยังไม่ขึ้นภายใน 10 นาที (not live within 10 min)');
  } finally {
    // 9. always remove the test files again
    s = step('9. ลบไฟล์ทดสอบออก · remove test files');
    for (let attempt = 1; attempt <= 3; attempt++) {
      try {
        const current = await head(SITE, siteBranch);
        const removed = await commitFiles(SITE, siteBranch, current,
          [removeFile(`${OUT}/stamp.json`), removeFile(`${OUT}/hello.html`)],
          `Proof #20: remove test files\n\nBuilder-Proof: 20 ${runId}`);
        report.findings.removeCommit = removed.commit;
        s.ok(`commit ${removed.commit.slice(0, 7)}${attempt > 1 ? ` (ครั้งที่ ${attempt})` : ''}`);
        break;
      } catch (e) {
        if (attempt === 3) s.bad(explain(e) + ' · แจ้ง Claude เพื่อลบไฟล์ admin/proof/out/ ด้วยมือ');
        else await sleep(2000);
      }
    }
  }

  // 10. drafts repo: write, read back, delete
  s = step('10. ที่เก็บส่วนตัว: เขียน อ่าน ลบ · drafts write/read/delete');
  try {
    const dBase = await head(DRAFTS, draftsBranch);
    const body = JSON.stringify({ runId, note: 'Ticket #20 proof draft' }) + '\n';
    const written = await commitFiles(DRAFTS, draftsBranch, dBase, [addFile('proof/draft-test.json', body)], `Proof #20: draft write ${runId}`);
    const { json: file } = await api('GET', `${repoPath(DRAFTS)}/contents/proof/draft-test.json?ref=${written.commit}`);
    const readBack = new TextDecoder().decode(base64ToBytes(file.content));
    await commitFiles(DRAFTS, draftsBranch, written, [removeFile('proof/draft-test.json')], `Proof #20: draft delete ${runId}`);
    report.findings.draftsRoundTripOk = readBack === body;
    if (readBack !== body) return s.bad('อ่านกลับมาไม่ตรง (read-back mismatch)');
    s.ok('เขียน อ่านกลับ และลบได้ครบ');
  } catch (e) { s.bad(explain(e)); }

  // 11. may the browser send the API version header?
  s = step('11. หัวข้อเวอร์ชัน API · X-GitHub-Api-Version');
  try {
    await api('GET', '/rate_limit', null, { 'X-GitHub-Api-Version': '2022-11-28' });
    report.findings.apiVersionHeaderAllowed = true;
    s.ok('ส่งได้ (allowed)');
  } catch (e) {
    report.findings.apiVersionHeaderAllowed = false;
    report.findings.apiVersionHeaderError = explain(e);
    s.ok('ส่งไม่ได้: ต้องละหัวข้อนี้ (blocked: the Admin must omit it)');
  }
}

$('form').addEventListener('submit', async ev => {
  ev.preventDefault();
  const value = $('token').value.trim();
  if (!/^github_pat_[A-Za-z0-9_]{20,}$/.test(value)) {
    alert('กุญแจต้องขึ้นต้นด้วย github_pat_ (fine-grained token)');
    return;
  }
  token = value;
  $('token').value = '';
  $('run').disabled = true;
  $('steps').replaceChildren();
  report.steps = []; report.findings = {};
  try {
    await run();
  } catch (e) {
    report.steps.push({ name: 'unexpected', ok: false, detail: explain(e) });
  } finally {
    token = null;
    $('report').value = JSON.stringify(report, null, 2);
    $('done').hidden = false;
    $('run').disabled = false;
  }
});

$('copy').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText($('report').value); $('copy').textContent = 'คัดลอกแล้ว ✓'; }
  catch { $('report').select(); document.execCommand('copy'); }
});

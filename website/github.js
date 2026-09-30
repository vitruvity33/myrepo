/* ============================================================================
   MyRepo prototype — GitHub API layer (PAT auth, browser-only)
   ----------------------------------------------------------------------------
   PROTOTYPE ONLY: the personal access token lives in localStorage in plain
   text. Fine for the owner's own testing; must be replaced by a GitHub App +
   backend token exchange before anyone else uses this. See AGENTS.md.
   api.github.com and raw.githubusercontent.com both allow CORS, so no server.
   Load order: github.js, then app.js (uses MyRepo from app.js at call time).
   ========================================================================== */

const GH_API = 'https://api.github.com';

/* the template every new repo is provisioned from — public, read without auth */
const TEMPLATE = {
  owner: 'vitruvity33',
  repo: 'myrepo',
  branch: 'main',
  exclude: ['website/'],               // the product site is not part of the template
};

/* fallback if the template tree can't be listed (keep in sync with the repo) */
const TEMPLATE_FALLBACK = [
  '.gitignore', 'AGENTS.md', 'LICENSE', 'README.md',
  '01_READ_FIRST/01_START_HERE.md', '01_READ_FIRST/02_AREA_MAP.md',
  '01_READ_FIRST/03_HOW_TO_USE_WITH_AI.md',
  '02_REFERENCES/AREA_TEMPLATE/README.md', '02_REFERENCES/CONTEXT_ITEM_SPEC.md',
  '02_REFERENCES/ID_REGISTRY.md', '02_REFERENCES/PUSH_BACK_PROTOCOL.md',
  '02_REFERENCES/preferences/README.md', '02_REFERENCES/prompts/CHAT_CONTEXT.md',
  '99_OTHER/AGENTS.md', '99_OTHER/README.md', '99_OTHER/01_RECORDS/00_INBOX/README.md',
];

/* top-level folders that come from the template (not user-built areas) */
const TEMPLATE_DIRS = ['01_READ_FIRST', '02_REFERENCES', '99_OTHER'];

class GitHubError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}

const GitHub = {
  token()   { return MyRepo.load('token', null); },
  user()    { return MyRepo.load('user', null); },    // { login, avatar_url, name }
  repo()    { return MyRepo.load('repo', null); },    // { owner, name, url }
  isLive()  { return !!(this.token() && this.user()); },

  /* fetch wrapper — auth header, JSON in/out, readable errors */
  async gh(path, opts = {}, token = this.token()) {
    const res = await fetch(path.startsWith('http') ? path : GH_API + path, {
      method: opts.method || 'GET',
      headers: {
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        ...(token ? { Authorization: 'Bearer ' + token } : {}),
        ...(opts.body ? { 'Content-Type': 'application/json' } : {}),
      },
      body: opts.body ? JSON.stringify(opts.body) : undefined,
    });
    if (res.status === 204) return null;
    const data = await res.json().catch(() => null);
    if (!res.ok) {
      let msg = (data && data.message) || res.statusText || 'Request failed';
      if (data && data.errors && data.errors[0]) msg += ' — ' + (data.errors[0].message || data.errors[0].code);
      if (res.status === 401) msg = 'Token rejected (401) — check it was copied fully and has not expired';
      throw new GitHubError(res.status, msg);
    }
    return data;
  },

  /* ── auth ── */
  async connect(token) {
    const u = await this.gh('/user', {}, token.trim());
    MyRepo.save('token', token.trim());
    MyRepo.save('user', { login: u.login, avatar_url: u.avatar_url, name: u.name });
    return u;
  },
  disconnect() {
    ['token', 'user', 'repo'].forEach(k => localStorage.removeItem('myrepo.' + k));
  },

  /* ── repos ── */
  getRepo(owner, name) { return this.gh(`/repos/${owner}/${name}`); },
  createRepo(name) {
    return this.gh('/user/repos', {
      method: 'POST',
      body: { name, private: true, description: 'My governed repo — built with MyRepo' },
    });
  },

  /* ── files ── */
  async getFile(owner, repo, path) {              // null when it doesn't exist
    try { return await this.gh(`/repos/${owner}/${repo}/contents/${encPath(path)}`); }
    catch (e) { if (e.status === 404) return null; throw e; }
  },
  getContents(owner, repo, path = '') {
    return this.gh(`/repos/${owner}/${repo}/contents/${encPath(path)}`);
  },
  putFile(owner, repo, path, base64, message, sha) {
    return this.gh(`/repos/${owner}/${repo}/contents/${encPath(path)}`, {
      method: 'PUT',
      body: { message, content: base64, ...(sha ? { sha } : {}) },
    });
  },

  /* every path in the repo — one call. [] for an empty repo */
  async listTree(owner, repo) {
    try {
      const t = await this.gh(`/repos/${owner}/${repo}/git/trees/HEAD?recursive=1`);
      return t.tree;
    } catch (e) { if (e.status === 409 || e.status === 404) return []; throw e; }
  },

  /* several files → ONE commit (git data API). Repo must already have a commit. */
  async commitFiles(owner, repo, files, message) {
    const base = `/repos/${owner}/${repo}`;
    const info = await this.gh(base);
    const branch = info.default_branch;
    const ref = await this.gh(`${base}/git/ref/heads/${branch}`);
    const parent = await this.gh(`${base}/git/commits/${ref.object.sha}`);
    const tree = await this.gh(`${base}/git/trees`, {
      method: 'POST',
      body: {
        base_tree: parent.tree.sha,
        tree: files.map(f => ({ path: f.path, mode: '100644', type: 'blob', content: f.text })),
      },
    });
    const commit = await this.gh(`${base}/git/commits`, {
      method: 'POST',
      body: { message, tree: tree.sha, parents: [parent.sha] },
    });
    await this.gh(`${base}/git/refs/heads/${branch}`, { method: 'PATCH', body: { sha: commit.sha } });
    return commit;
  },

  /* ── template ── */
  async templateManifest() {
    try {
      const t = await this.gh(`/repos/${TEMPLATE.owner}/${TEMPLATE.repo}/git/trees/${TEMPLATE.branch}?recursive=1`);
      const paths = t.tree.filter(n => n.type === 'blob').map(n => n.path)
        .filter(p => !TEMPLATE.exclude.some(x => p.startsWith(x)))
        .filter(p => !p.endsWith('.DS_Store'));
      if (paths.length) return paths;
    } catch (e) { /* fall through to the hardcoded list */ }
    return TEMPLATE_FALLBACK.slice();
  },
  /* raw bytes → base64, so the copy is byte-identical to the template */
  async templateFileBase64(path) {
    const url = `https://raw.githubusercontent.com/${TEMPLATE.owner}/${TEMPLATE.repo}/${TEMPLATE.branch}/${encPath(path)}`;
    const res = await fetch(url);
    if (!res.ok) throw new GitHubError(res.status, `Couldn't read template file ${path}`);
    return bytesToBase64(new Uint8Array(await res.arrayBuffer()));
  },
};

/* ── helpers ── */

function encPath(path) { return path.split('/').map(encodeURIComponent).join('/'); }

function bytesToBase64(bytes) {
  let bin = '';
  for (let i = 0; i < bytes.length; i += 0x8000) {
    bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  }
  return btoa(bin);
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

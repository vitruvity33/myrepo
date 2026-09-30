/* ============================================================================
   MyRepo prototype — shared state + interactions
   Vanilla JS, no build step. State lives in localStorage so the repo the user
   "builds" during onboarding persists across screens.
   Two modes: LIVE (a GitHub token is stored — github.js makes real calls) and
   DEMO (no token — the original mock behaviour, nothing leaves the browser).
   ========================================================================== */

const MyRepo = {
  load(key, fallback) {
    try { return JSON.parse(localStorage.getItem('myrepo.' + key)) ?? fallback; }
    catch { return fallback; }
  },
  save(key, value) { localStorage.setItem('myrepo.' + key, JSON.stringify(value)); },
};

const $ = id => document.getElementById(id);
const live = () => typeof GitHub !== 'undefined' && GitHub.isLive();
const today = () => new Date().toISOString().slice(0, 10);

/* ── screen 03 · connect ─────────────────────────────────────────────────── */

function initConnect() {
  const btn = $('connect-repo');
  const panel = $('token-panel');
  if (!btn || !panel) return;

  const status = $('token-status');
  const input = $('token-input');
  const go = $('token-connect');
  const next = $('token-continue');

  function showConnected(u) {
    panel.hidden = false;
    $('token-form').hidden = true;
    status.innerHTML = '';
    const img = document.createElement('img');
    img.className = 'avatar';
    img.src = u.avatar_url;
    img.alt = '';
    const who = document.createElement('span');
    who.textContent = `Connected as @${u.login}`;
    status.append(img, who);
    status.className = 'status status--ok';
    next.hidden = false;
  }

  btn.addEventListener('click', e => {
    e.preventDefault();
    panel.hidden = false;
    input.focus();
  });

  async function connect() {
    if (!input.value.trim()) { input.focus(); return; }
    go.textContent = 'Checking…';
    status.className = 'status';
    status.textContent = '';
    try {
      const u = await GitHub.connect(input.value);
      input.value = '';
      MyRepo.save('connected', true);
      showConnected(u);
    } catch (err) {
      status.className = 'status status--error';
      status.textContent = err.message;
    } finally {
      go.textContent = 'Connect';
    }
  }
  go.addEventListener('click', e => { e.preventDefault(); connect(); });
  input.addEventListener('keydown', e => { if (e.key === 'Enter') connect(); });

  $('token-disconnect').addEventListener('click', e => {
    e.preventDefault();
    GitHub.disconnect();
    MyRepo.save('connected', false);
    $('token-form').hidden = false;
    next.hidden = true;
    status.className = 'status';
    status.textContent = 'Disconnected — token removed from this browser.';
  });

  if (live()) showConnected(GitHub.user());
}

/* ── screen 07 · authorize ───────────────────────────────────────────────── */

function initAuthorize() {
  const el = $('auth-who');
  if (el && live()) {
    el.textContent = `Signed in to GitHub as @${GitHub.user().login} — using your access token.`;
    el.hidden = false;
  }
}

/* ── screen 08 · creating your repo ─────────────────────────────────────── */

/* one line in the checklist; states: pending → active → done | error */
function provRow(list, text) {
  const row = document.createElement('div');
  row.className = 'prov-row prov-row--active';
  const check = document.createElement('span');
  check.className = 'check';
  check.textContent = '…';
  const label = document.createElement('span');
  label.textContent = text;
  const detail = document.createElement('span');
  detail.className = 'detail';
  row.append(check, label, detail);
  list.appendChild(row);
  return {
    row,
    detail(t) { detail.textContent = t; },
    done(t) { row.className = 'prov-row prov-row--done'; check.textContent = '✓'; if (t != null) detail.textContent = t; },
    fail(t) { row.className = 'prov-row prov-row--error'; check.textContent = '✗'; detail.textContent = t; },
  };
}

const PROV_GROUPS = {
  '':              'Writing AGENTS.md + README.md at the root',
  '01_READ_FIRST': 'Installing 01_READ_FIRST orientation files',
  '02_REFERENCES': 'Installing 02_REFERENCES rule machinery',
  '99_OTHER':      'Creating the unsorted catch-all (99_OTHER)',
};

function initProvision() {
  const list = $('provision-list');
  const next = $('provision-next');
  if (!list) return;
  if (live()) return initProvisionLive(list, next);

  $('provision-demo').hidden = false;
  const steps = [
    'Creating private repo "my-repo" in your account',
    'Writing AGENTS.md + README.md at the root',
    'Installing 01_READ_FIRST orientation files',
    'Installing 02_REFERENCES rule machinery',
    'Creating the unsorted catch-all',
    'Your repo is live',
  ];
  list.innerHTML = '';
  let i = 0;
  (function tick() {
    if (i < steps.length) {
      provRow(list, steps[i++]).done();
      setTimeout(tick, 800);
    } else if (next) {
      next.hidden = false;
    }
  })();
}

function initProvisionLive(list, next) {
  const form = $('provision-form');
  const nameInput = $('repo-name');
  const owner = GitHub.user().login;
  form.hidden = false;
  $('repo-owner').textContent = `github.com/${owner}/`;
  nameInput.value = (GitHub.repo() && GitHub.repo().name) || 'my-repo';

  $('provision-start').addEventListener('click', e => {
    e.preventDefault();
    const name = nameInput.value.trim().replace(/[^A-Za-z0-9._-]+/g, '-');
    if (!name) return nameInput.focus();
    form.hidden = true;
    list.innerHTML = '';
    run(name).catch(() => { form.hidden = false; });   // errors already shown in-row
  });

  /* Step 1 — create the repo, or (on "already exists") let the user reuse it */
  function createOrReuse(name) {
    const r = provRow(list, `Creating private repo "${name}" in @${owner}`);
    return GitHub.createRepo(name).then(info => { r.done(); return info; }, err => {
      if (err.status !== 422) { r.fail(err.message); throw err; }
      r.fail('A repo with this name already exists in your account.');
      return new Promise((resolve, reject) => {
        const acts = document.createElement('span');
        acts.className = 'row-actions';
        const use = Object.assign(document.createElement('a'), { className: 'btn', href: '#', textContent: 'Use existing' });
        const other = Object.assign(document.createElement('a'), { className: 'btn btn--quiet', href: '#', textContent: 'Pick another name' });
        acts.append(use, other);
        r.row.appendChild(acts);
        use.addEventListener('click', ev => {
          ev.preventDefault(); acts.remove();
          GitHub.getRepo(owner, name).then(info => {
            r.done('Using the existing repo — files already there are left untouched.');
            resolve(info);
          }, e2 => { r.fail(e2.message); reject(e2); });
        });
        other.addEventListener('click', ev => { ev.preventDefault(); acts.remove(); reject(err); });
      });
    });
  }

  async function run(name) {
    const info = await createOrReuse(name);
    const repo = { owner: info.owner.login, name: info.name, url: info.html_url };
    MyRepo.save('repo', repo);

    const m = provRow(list, `Reading the template from ${TEMPLATE.owner}/${TEMPLATE.repo}`);
    let paths;
    try { paths = await GitHub.templateManifest(); m.done(`${paths.length} files`); }
    catch (err) { m.fail(err.message); throw err; }

    /* group by top-level folder; root README.md first — it creates the first commit */
    const groups = {};
    paths.forEach(p => {
      const top = p.includes('/') ? p.split('/')[0] : '';
      (groups[top] = groups[top] || []).push(p);
    });
    if (groups['']) groups[''].sort((a, b) => (b === 'README.md') - (a === 'README.md'));
    const order = ['', ...Object.keys(groups).filter(k => k).sort()].filter(k => groups[k]);

    for (const key of order) {
      const files = groups[key];
      const r = provRow(list, PROV_GROUPS[key] || `Installing ${key}`);
      let n = 0, skipped = 0;
      try {
        for (const path of files) {
          r.detail(`${n}/${files.length}`);
          if (await GitHub.getFile(repo.owner, repo.name, path)) { skipped++; }
          else {
            const b64 = await GitHub.templateFileBase64(path);
            await putWithRetry(repo, path, b64);
          }
          n++;
        }
        r.done(`${files.length} file${files.length === 1 ? '' : 's'}` + (skipped ? ` · ${skipped} already there` : ''));
      } catch (err) { r.fail(`${files[n]}: ${err.message}`); throw err; }
    }

    const last = provRow(list, 'Your repo is live');
    last.done('');
    const link = Object.assign(document.createElement('a'), {
      href: repo.url, target: '_blank', rel: 'noopener', textContent: repo.url.replace('https://', ''),
    });
    last.row.querySelector('.detail').appendChild(link);
    if (next) next.hidden = false;
  }

  /* a just-created repo can take a moment before it accepts writes */
  async function putWithRetry(repo, path, b64) {
    for (let attempt = 0; ; attempt++) {
      try { return await GitHub.putFile(repo.owner, repo.name, path, b64, `MyRepo setup: add ${path}`); }
      catch (err) {
        if (attempt >= 3 || ![404, 409, 502].includes(err.status)) throw err;
        await sleep(1000 * (attempt + 1));
      }
    }
  }
}

/* ── screen 05 · agents ──────────────────────────────────────────────────── */

const AGENT_TOOLS = ['ChatGPT', 'Claude', 'Devin', 'Gemini'];

function initAgents() {
  const list = $('agent-list');
  const connectedEl = $('connected-list');
  if (!list || !connectedEl) return;

  let connected = MyRepo.load('agents', []);

  function render() {
    list.innerHTML = '';
    AGENT_TOOLS.forEach(tool => {
      const row = document.createElement('div');
      row.className = 'agent-row';
      const isOn = connected.includes(tool);
      row.innerHTML = `<span>${tool}</span>`;
      const btn = document.createElement('a');
      btn.className = 'btn' + (isOn ? ' btn--connected' : '');
      btn.textContent = isOn ? 'Connected' : 'Connect';
      btn.addEventListener('click', e => {
        e.preventDefault();
        connected = isOn ? connected.filter(t => t !== tool) : [...connected, tool];
        MyRepo.save('agents', connected);
        render();
      });
      row.appendChild(btn);
      list.appendChild(row);
    });

    connectedEl.innerHTML = connected.length
      ? connected.map(t => `<span class="chip">${t}</span>`).join(' ')
      : '<span class="note note--small">Nothing connected yet</span>';
  }

  render();
}

/* ── screen 06 · done ────────────────────────────────────────────────────── */

function countFolders(folders) {
  return folders.reduce((n, f) => n + 1 + countFolders(f.children), 0);
}

async function initDone() {
  const el = $('repo-summary');
  if (!el) return;
  const agents = MyRepo.load('agents', []);
  const tail = agents.length ? ` · connected: ${agents.join(', ')}` : '';
  const plural = n => `${n} folder${n === 1 ? '' : 's'}`;

  const repo = live() && GitHub.repo();
  if (!repo) {
    el.textContent = plural(countFolders(MyRepo.load('folders', []))) + ' created' + tail;
    return;
  }

  const open = $('open-repo');
  open.href = repo.url;
  open.target = '_blank';
  open.rel = 'noopener';
  const link = $('repo-link');
  link.href = repo.url;
  link.textContent = repo.url.replace('https://', '');
  link.parentElement.hidden = false;

  el.textContent = 'Checking your repo on GitHub…';
  try {
    const tree = await GitHub.listTree(repo.owner, repo.name);
    const files = tree.filter(n => n.type === 'blob').length;
    const n = countFolders(areasFromTree(tree));
    el.textContent = `${plural(n)} built · ${files} files on GitHub` + tail;
  } catch (err) {
    el.textContent = `Couldn't read the repo: ${err.message}`;
  }
}

/* ── dispatch ────────────────────────────────────────────────────────────── */

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.page;
  if (page === 'connect') initConnect();
  if (page === 'authorize') initAuthorize();
  if (page === 'provision') initProvision();
  if (page === 'build') initBuild();
  if (page === 'agents') initAgents();
  if (page === 'done') initDone();
});

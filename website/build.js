/* ============================================================================
   MyRepo prototype — screen 04 · Build your repo (folder tree)
   ----------------------------------------------------------------------------
   DEMO: the tree lives in localStorage only.
   LIVE: on load the tree is read from the user's repo (GitHub is the source of
   truth); + Folder / + subfolder commits AGENTS.md + README.md +
   01_RECORDS/README.md for the new area in ONE commit — the "written in the
   same operation" rule from 02_REFERENCES/AREA_TEMPLATE.
   Load order: github.js, app.js, build.js.
   ========================================================================== */

/* folder glyph — inline SVG so it inherits ink + fill tokens */
const FOLDER_SVG =
  '<svg viewBox="0 0 88 72" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
  '<path d="M6 64 V16 Q6 8 14 8 H30 L40 18 H74 Q82 18 82 26 V56 Q82 64 74 64 Z" ' +
  'fill="var(--paper)" stroke="var(--ink)" stroke-width="2.5" stroke-linejoin="round"/></svg>';

function folderIcon(nested) {
  const icon = document.createElement('span');
  icon.className = 'folder-icon' + (nested ? ' folder-icon--sm' : '');
  icon.innerHTML = FOLDER_SVG;
  return icon;
}

/* repo tree → user-built areas: every folder holding an AGENTS.md, minus the
   root, the template's own folders, and 01_RECORDS/ + work/ internals */
function areasFromTree(tree) {
  const dirs = tree
    .filter(n => n.type === 'blob' && /(^|\/)AGENTS\.md$/.test(n.path) && n.path.includes('/'))
    .map(n => n.path.slice(0, -'/AGENTS.md'.length))
    .filter(d => !TEMPLATE_DIRS.includes(d.split('/')[0]))
    .filter(d => !d.split('/').some(s => s === '01_RECORDS' || s === 'work'))
    .sort((a, b) => a.split('/').length - b.split('/').length || a.localeCompare(b));

  const byPath = {};
  const roots = [];
  dirs.forEach(path => {
    const node = { name: path.split('/').pop(), children: [], open: false, synced: true };
    byPath[path] = node;
    const parts = path.split('/');
    let parent = null;
    for (let i = parts.length - 1; i > 0 && !parent; i--) parent = byPath[parts.slice(0, i).join('/')];
    (parent ? parent.children : roots).push(node);
  });
  return roots;
}

/* the three files every new area is born with */
function areaFiles(path, name) {
  const fm = title => `---\ntitle: ${title}\nstatus: draft\nreviewed_by: none\nlast_verified: ${today()}\n---\n\n`;
  const parent = path.includes('/') ? path.split('/').slice(0, -1).join('/') + '/AGENTS.md' : null;
  return [
    { path: `${path}/AGENTS.md`, text: fm(`Agents — ${name}`) +
`# AGENTS.md — \`${path}/\`

**Kind:** ${parent ? 'sub-area' : 'area'} · **ID prefix:** _not minted yet — register in \`02_REFERENCES/ID_REGISTRY.md\`_ · **Context reviewer:** the repo owner

## What belongs here

_Describe what this area owns — and what it doesn't._

## \`01_RECORDS/\` slots in use

None yet. Slots are a menu, not a mandate — create each on first use
(see \`02_REFERENCES/AREA_TEMPLATE/README.md\`). Always available:
\`00_INBOX/\`, \`03_REFERENCES/\`, \`99_ARCHIVE/\`.

## Rules

- Root \`AGENTS.md\` rules apply — read it first.${parent ? `\n- Parent area rules apply: \`${parent}\`.` : ''}
- Agents write \`status: draft\` and \`reviewed_by: none\`. Never \`canonical\`.

## Push-back

Disagreements about this area → \`${path}/01_RECORDS/05_PUSH_BACK/YYYY-MM-DD_TOPIC.md\`.
` },
    { path: `${path}/README.md`, text: fm(name) +
`# ${name}

_Orientation for people: what this area is for and where to start._

Agents: read \`${path}/AGENTS.md\` before working here.
` },
    { path: `${path}/01_RECORDS/README.md`, text: fm(`${name} — records`) +
`# 01_RECORDS

The governed layer for \`${path}/\`. Slot folders (\`00_INBOX/\`, \`01_GOALS/\`,
\`06_DECISIONS/\` …) are created on first use — see \`${path}/AGENTS.md\`.
` },
  ];
}

function initBuild() {
  const tree = $('folder-tree');
  const addBtn = $('add-folder');
  if (!tree || !addBtn) return;

  const repo = live() && GitHub.repo();
  const note = $('connected-note');
  let folders = MyRepo.load('folders', []);
  let queue = Promise.resolve();                 // commits run one at a time, in order

  if (repo) {
    note.textContent = `Connected to github.com/${repo.owner}/${repo.name} — new folders commit live.`;
    note.hidden = false;
  } else if (MyRepo.load('connected', false)) {
    note.hidden = false;
  }

  function persist() {
    MyRepo.save('folders', folders.filter(f => !f.editing));
  }

  function render() {
    tree.innerHTML = '';
    tree.appendChild(renderLevel(folders, ''));
    persist();
  }

  /* never redraw under a half-typed folder name — wait until it's committed */
  function renderSoon() {
    if (!tree.querySelector('.folder-input')) render();
  }

  function renderLevel(list, parentPath) {
    const wrap = document.createElement('div');
    wrap.className = 'folder-level';
    list.forEach(folder => wrap.appendChild(renderFolder(folder, list, parentPath)));
    return wrap;
  }

  function commitFolder(folder, path) {
    if (!repo) return;
    folder.synced = 'saving';
    folder.error = null;
    queue = queue
      .then(() => GitHub.commitFiles(repo.owner, repo.name, areaFiles(path, folder.name),
                                     `Add area ${path}/ — AGENTS.md + README.md`))
      .then(() => { folder.synced = true; },
            err => { folder.synced = 'error'; folder.error = err.message; })
      .then(renderSoon);
  }

  function miniBtn(text, title, onClick) {
    const b = document.createElement('span');
    b.className = 'mini-btn';
    b.textContent = text;
    b.title = title;
    b.addEventListener('click', e => { e.stopPropagation(); onClick(); });
    return b;
  }

  function renderFolder(folder, siblings, parentPath) {
    const path = parentPath ? `${parentPath}/${folder.name}` : folder.name;
    const row = document.createElement('div');
    row.className = 'folder-row';

    const box = document.createElement('div');
    box.className = 'folder' + (folder.open ? ' folder--open' : '');

    const nameCell = document.createElement('span');
    nameCell.className = 'folder-name';

    if (folder.editing) {
      box.appendChild(folderIcon(!!parentPath));
      const input = document.createElement('input');
      input.className = 'folder-input';
      input.placeholder = 'Folder name';
      input.value = folder.name;
      input.addEventListener('input', () => { folder.name = input.value; });
      let done = false;
      const commit = () => {
        if (done) return;
        done = true;
        const name = input.value.trim().replace(/[\\/]+/g, '-').replace(/\s+/g, '_').replace(/^\.+/, '');
        if (!name) { siblings.splice(siblings.indexOf(folder), 1); return render(); }
        if (siblings.some(s => s !== folder && s.name.toLowerCase() === name.toLowerCase())) {
          folder.name = name;
          folder.error = 'A folder with that name is already here';
          return render();
        }
        folder.name = name;
        folder.editing = false;
        folder.error = null;
        commitFolder(folder, parentPath ? `${parentPath}/${name}` : name);
        render();
      };
      input.addEventListener('keydown', e => {
        if (e.key === 'Enter') commit();
        if (e.key === 'Escape') { done = true; siblings.splice(siblings.indexOf(folder), 1); render(); }
      });
      input.addEventListener('blur', commit);
      nameCell.appendChild(input);
      if (folder.error) nameCell.appendChild(syncTag('error', folder.error));
      setTimeout(() => input.focus(), 0);
    } else {
      if (folder.children.length || folder.open !== undefined) {
        const caret = document.createElement('span');
        caret.className = 'caret';
        caret.textContent = folder.open ? 'v' : '>';
        caret.addEventListener('click', e => { e.stopPropagation(); folder.open = !folder.open; render(); });
        box.appendChild(caret);
      }
      box.appendChild(folderIcon(!!parentPath));

      const name = document.createElement('span');
      name.textContent = folder.name;
      nameCell.appendChild(name);

      if (repo && folder.synced === 'saving') nameCell.appendChild(syncTag('saving', 'saving…'));
      if (repo && folder.synced === true) nameCell.appendChild(syncTag('ok', '✓ on GitHub'));
      if (folder.synced === 'error') {
        nameCell.appendChild(syncTag('error', '✗ ' + folder.error));
        nameCell.appendChild(miniBtn('retry', 'Try the commit again', () => { commitFolder(folder, path); render(); }));
      }

      if (folder.synced !== 'saving' && folder.synced !== 'error') {
        const acts = document.createElement('span');
        acts.className = 'row-actions';
        acts.appendChild(miniBtn('+', 'Add a subfolder', () => {
          folder.open = true;
          folder.children.push({ name: '', children: [], open: true, editing: true });
          render();
        }));
        nameCell.appendChild(acts);
      }

      box.addEventListener('click', () => { folder.open = !folder.open; render(); });
    }

    box.appendChild(nameCell);
    row.appendChild(box);
    if (folder.open && folder.children.length) {
      const kids = document.createElement('div');
      kids.className = 'folder-children';
      kids.appendChild(renderLevel(folder.children, path));
      row.appendChild(kids);
    }
    return row;
  }

  function syncTag(kind, text) {
    const t = document.createElement('span');
    t.className = `sync sync--${kind}`;
    t.textContent = text;
    return t;
  }

  addBtn.addEventListener('click', e => {
    e.preventDefault();
    folders.push({ name: '', children: [], open: true, editing: true });
    render();
  });

  if (!repo) return render();

  /* LIVE — load the tree from GitHub, keeping each folder's open/closed state */
  tree.innerHTML = '<p class="note note--small">Loading your repo from GitHub…</p>';
  const openState = {};
  (function walk(list, p) {
    list.forEach(f => { const fp = p ? `${p}/${f.name}` : f.name; openState[fp] = f.open; walk(f.children, fp); });
  })(folders, '');
  GitHub.listTree(repo.owner, repo.name).then(t => {
    folders = areasFromTree(t);
    (function walk(list, p) {
      list.forEach(f => { const fp = p ? `${p}/${f.name}` : f.name; if (fp in openState) f.open = openState[fp]; walk(f.children, fp); });
    })(folders, '');
    render();
  }, err => {
    tree.innerHTML = '';
    tree.appendChild(syncTag('error', `Couldn't load the repo: ${err.message}`));
  });
}

/* BKP desk assembler.
   Builds every desk output from MASTER.md at the point of use.
   Runs unchanged in a web page (<script src>), a userscript (@require) and Node (require).
   No dependencies. The master is data; nothing here holds desk content. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.BKPAssemble = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const BLOCK_RE = /^<!-- @block (.+?) -->$/;
  const END_LINE = '<!-- @end -->';
  const ROUTE_RE = /^<!-- @route (\S+) -->$/;

  function attrs(s) {
    const out = {};
    s.replace(/([\w.-]+)=("([^"]*)"|\S+)/g, (_, k, v, q) => { out[k] = q !== undefined ? q : v; return ''; });
    return out;
  }

  function parse(text) {
    text = String(text || '').replace(/^﻿/, '').replace(/\r\n/g, '\n');
    const m = text.match(/<!-- @meta\n([\s\S]*?)\n-->/);
    if (!m) throw new Error('Not a desk master: no @meta block');
    const meta = JSON.parse(m[1]);
    const lines = text.split('\n'), blocks = {}, order = [];
    for (let i = 0; i < lines.length; i++) {
      const b = lines[i].match(BLOCK_RE);
      if (!b) continue;
      const a = attrs(b[1]), body = [];
      if (!a.id) throw new Error('Block without id at line ' + (i + 1));
      if (blocks[a.id]) throw new Error('Duplicate block id: ' + a.id);
      let j = i + 1;
      while (j < lines.length && lines[j] !== END_LINE) {
        if (BLOCK_RE.test(lines[j])) throw new Error('Block ' + a.id + ' is not closed before line ' + (j + 1));
        body.push(lines[j]); j++;
      }
      if (j >= lines.length) throw new Error('Block ' + a.id + ' has no @end');
      blocks[a.id] = { id: a.id, attrs: a, lines: body };
      order.push(a.id);
      i = j;
    }
    return { meta, blocks, order, edition: meta.edition || '' };
  }

  function resourceOf(master, block) {
    const p = block.attrs.part || '';
    return (master.meta.resources && master.meta.resources[p]) || p;
  }

  // Route table: built from @route markers (headings) and Directory YAML branches. Never typed.
  function routeEntries(master) {
    const heads = [], dirs = [];
    master.order.forEach(id => {
      const b = master.blocks[id], L = b.lines;
      for (let i = 0; i < L.length; i++) {
        const r = L[i].match(ROUTE_RE);
        if (r) {
          const h = (L[i + 1] || '').match(/^#{1,6}\s+(.+?)\s*$/);
          if (!h) throw new Error('@route ' + r[1] + ' is not followed by a heading');
          heads.push({ key: r[1], resource: resourceOf(master, b), heading: '"' + h[1] + '"', part: b.attrs.part });
        }
        if (L[i] === '```yaml' && L[i + 1] === 'directory:') {
          for (let j = i + 2; j < L.length && L[j] !== '```'; j++) {
            const k = L[j].match(/^  ([A-Za-z_]+):/);
            if (k) dirs.push({ key: 'directory.' + k[1], resource: resourceOf(master, b), heading: 'directory.' + k[1] });
          }
        }
      }
    });
    const bootRes = (master.meta.resources && master.meta.resources.boot) || 'boot';
    return [heads.filter(r => r.resource === bootRes), dirs, heads.filter(r => r.resource !== bootRes)];
  }

  function routesBlock(master) {
    const fmt = g => {
      const w = Math.max(27, ...g.map(r => r.key.length + 2));
      return g.map(r => '  ' + (r.key + ':').padEnd(w) + '{resource: ' + r.resource + ', heading: ' + r.heading + '}');
    };
    const groups = routeEntries(master).filter(g => g.length).map(fmt);
    return ['```yaml', 'routes:'].concat(...groups.map(g => g.concat(''))).concat('```');
  }

  function frontmatter(master, name) {
    const d = master.meta.skills && master.meta.skills[name];
    if (d === undefined) throw new Error('No skill metadata for ' + name);
    return ['---', 'name: ' + name, '', 'description: ' + d, '', '---'];
  }

  function blockLines(master, id) {
    const b = master.blocks[id];
    if (!b) throw new Error('Unknown block: ' + id);
    const out = [];
    b.lines.forEach(ln => {
      if (ROUTE_RE.test(ln)) return;
      if (ln === '<!-- @edition -->') return out.push('Edition: `' + master.edition + '`');
      if (ln === '<!-- @routes -->') return out.push(...routesBlock(master));
      out.push(ln);
    });
    return out;
  }

  function render(master, name, opts, skip) {
    const o = master.meta.outputs && master.meta.outputs[name];
    if (!o) throw new Error('Unknown output: ' + name);
    const out = [];
    o.blocks.forEach(sel => {
      if (skip && skip.has(sel)) return;
      if (sel.startsWith('@fm:')) out.push(...frontmatter(master, sel.slice(4)));
      else if (sel === '@addendum') {
        const a = opts && opts.addendum;
        if (!a || !String(a).trim()) throw new Error('Addendum not supplied');
        out.push(...String(a).replace(/\r\n/g, '\n').replace(/\s+$/, '').split('\n'));
      } else out.push(...blockLines(master, sel));
    });
    return out.join('\n').replace(/\s+$/, '') + '\n';
  }

  function file(master, name) { return master.meta.outputs[name].file; }

  function deployment(master, key, opts) {
    const d = master.meta.deployments && master.meta.deployments[key];
    if (!d) throw new Error('Unknown deployment: ' + key);
    const names = d.outputs || d.zips || [];
    // A deployment with "single" is one document: its outputs joined in the listed order.
    if (d.single) return [{ name: key, file: d.single, text: joined(master, names, opts) }];
    return names.map(n => ({ name: n, file: file(master, n), text: render(master, n, opts) }));
  }

  // Several outputs as one document. A block shared by more than one of them (House Essentials,
  // say) is kept once, at its last occurrence, so the document never repeats itself.
  function joined(master, names, opts) {
    const last = {};
    names.forEach((n, i) => master.meta.outputs[n].blocks.forEach(b => { if (!b.startsWith('@fm:')) last[b] = i; }));
    return names.map((n, i) => render(master, n, opts, new Set(Object.keys(last).filter(b => last[b] > i)))).join('\n');
  }

  // Single document from chosen custom units, always in the master's canonical unit order.
  function custom(master, picks, opts) {
    const want = new Set(picks.map(String));
    const units = master.meta.custom.filter(u => want.has(u[0]) || want.has(u[1]));
    if (!units.length) throw new Error('No units chosen');
    return joined(master, units.map(u => u[2]), opts);
  }

  // Plain standalone Directory copies for downloads and non-Markdown tools.
  // They are derived from the same master block as directory.md and are never
  // maintained as a second source.
  function directoryText(master) {
    const b = master.blocks.directory;
    if (!b) throw new Error('Directory block is missing');
    const start = b.lines.indexOf('```yaml');
    const end = start < 0 ? -1 : b.lines.indexOf('```', start + 1);
    if (start < 0 || end < 0) throw new Error('Directory YAML fence is missing');
    return '# ' + master.edition + '\n' + b.lines.slice(start + 1, end).join('\n') + '\n';
  }

  function outputs(master) { return Object.keys(master.meta.outputs); }
  function deployments(master) { return Object.keys(master.meta.deployments); }

  return { parse, render, deployment, custom, outputs, deployments, file, routeEntries, directoryText, version: '1.1.0' };
});

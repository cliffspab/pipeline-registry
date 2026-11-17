// ==UserScript==
// @name         DC-X Desk Hub: Grab + Tools 0-5 + Shift Pack
// @namespace    bkp-desk
// @version      2.0.7
// @description  One DC-X hub for story grabbing, the six desk tools, Grok handoff and verified Blueprint/Addendum/Tracker shift-pack building.
// @match        https://dcx.bangkokpost.co.th/*
// @match        http://dcx.bangkokpost.co.th/*
// @match        https://grok.com/*
// @inject-into  page
// @noframes
// @grant        GM_setClipboard
// @grant        GM_registerMenuCommand
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_deleteValue
// @grant        GM_openInTab
// @grant        GM_xmlhttpRequest
// @connect      raw.githubusercontent.com
// @connect      docs.google.com
// @connect      googleusercontent.com
// @connect      go.fuzzylogic.page
// ==/UserScript==

/*
  2.0.7: adds a Sync master index control for the 20-file Shift pickup across
  GitHub, Google Drive, OneDrive and pCloud.

  2.0.6: Copy/Download full pack and Download separate fetch any Blueprint or
  Addendum not yet stored before building, instead of stopping with
  NOT FETCHED. Module Copy/Save does the same for the Blueprint.

  2.0.5: DCX 0-5 tools (the old bookmarklets) sit in a collapsed drop-down.
  New Modules drop-down: BOOT, EDIT, CHECK, PHOTO, PR and DIRECTORY split from
  the fetched Blueprint by its component markers, each stamped with the
  Blueprint version; Copy and Save per module, plus Save EDIT + DIRECTORY.

  2.0.4: the Tracker goes into the pack as links only, never its content.
  The pack needs only Blueprint and Addendum; Download separate skips the
  Tracker. The panel can still fetch, copy and save the Tracker for the operator.

  2.0.3: opening prompt cut to the package line and the BOOT/EDIT sentence.

  2.0.2: no load, read, fetch or verify instructions go out to models. The
  opening prompt is descriptive only; "Copy prompt + links" is removed and
  model links are a bare list. Verification stays on the operator side: panel
  states, confirmations, and the manifest's counts and checksums as data.

  2.0.1 changes (shift-pack layer only; Story Grabber, Grok handoff, DCX 0-5,
  launcher and shortcuts are unchanged):
  - A failed refresh never overwrites the stored copy. Login pages, blocked
    HTML and empty responses can no longer enter the pack labelled CACHED.
  - The specific failure state (LOGIN PAGE, BLOCKED, EMPTY, ERROR, NOT
    CONFIGURED) is shown on the panel, with the cached copy's age when one
    is kept.
  - Login detection runs only on HTML responses, so plain text that mentions
    "sign in" is no longer misread as a login page.
  - Blueprint source corrected to Blueprint/BLUEPRINT.txt (the 3.1 path
    returned 404). Opening and closing markers are checked for all six
    components, the file must end at END COMPONENT: DIRECTORY, and the
    MASTER version marker is cross-checked against VERSION.txt.
  - Version markers in panel and manifest: Blueprint MASTER, Addendum
    "Last update", Tracker latest row date.
  - Tracker falls back TSV -> CSV -> gviz CSV, all on the tracker gid.
  - Copy/download of a pack containing CACHED, PARTIAL or MANUAL components
    asks for confirmation and lists them; the manifest labels each.
  - Verify button re-checks stored content (including pasted content).
  - Model links: public links any model can fetch.
  - Filename BP_SHIFT_PACK_YYYY-MM-DD_HHMM.txt; separate downloads staggered.
  - @connect googleusercontent.com added (Google export links redirect there).
  - Cache and config keys moved to V3, so any copy cached by 2.0.0 is dropped.
*/

(function () {
  'use strict';

  const VERSION = '2.0.7';
  const SYNC_MASTER_URL = 'https://github.com/cliffspab/pipeline-registry/blob/main/SYNC-MASTER.md';
  const GROK_URL = 'https://grok.com/project/be3fb1fa-1ecc-4f20-b883-80ed54504adf';
  const AUTO_SUBMIT = true;
  const SEND_ON_GRAB = false;
  const GROK_KEY = 'dcxGrokPending';
  const CACHE_KEY = 'dcxShiftPackCacheV3';
  const CONFIG_KEY = 'dcxShiftPackConfigV3';
  const PANEL_ID = 'dcx-desk-hub-panel';
  const BUTTON_ID = 'dcx-desk-hub-button';
  const REVIEW_ID = 'dcx-grab-review';
  const PREFIX = 'formengine[documents-story][tab_text][';
  const WHO = 'Rob Vass';
  const STATUS_RE = /^(Planning|Subeditor|Clean|Ready for Layout|Ready for output|Typeset|Published)$/i;
  const FINAL_RE = /^(Ready for output|Published)$/i;

  const KEYS = ['blueprint','addendum','tracker'];
  const PACK_KEYS = ['blueprint','addendum']; // Tracker is carried as links only
  const BP_COMPONENTS = ['BOOT','EDIT','CHECK','PHOTO','PR','DIRECTORY'];
  const TRACKER_ID = '1X-5vfO8lLYRxwgpyg3RDTqc9d8sz42WKUT4-b8X9DGw';
  const TRACKER_GID = '1313569477';
  const ADDENDUM_ID = '1KukKHnoSOAuZiyg_u1k1NiRAQDx4QbuePCVxz4ehXsk';
  const RAW_BP = 'https://raw.githubusercontent.com/cliffspab/pipeline-registry/refs/heads/main/Blueprint/';

  const DEFAULT_CONFIG = {
    blueprint: {
      label: 'Blueprint',
      url: RAW_BP + 'BLUEPRINT.txt',
      versionUrl: RAW_BP + 'VERSION.txt',
      openUrl: 'https://github.com/cliffspab/pipeline-registry/blob/main/Blueprint/BLUEPRINT.txt',
      shareUrl: RAW_BP + 'BLUEPRINT.txt',
      filename: 'BLUEPRINT.txt',
      markers: BP_COMPONENTS.flatMap(n => ['<!-- COMPONENT: ' + n + ' -->', '<!-- END COMPONENT: ' + n + ' -->']),
      endMarker: 'END COMPONENT: DIRECTORY',
      minChars: 20000
    },
    addendum: {
      label: 'Desk Addendum',
      url: 'https://docs.google.com/document/d/' + ADDENDUM_ID + '/export?format=txt',
      openUrl: 'https://docs.google.com/document/d/' + ADDENDUM_ID + '/edit',
      shareUrl: 'https://docs.google.com/document/d/' + ADDENDUM_ID + '/export?format=txt',
      altShareUrl: 'https://docs.google.com/document/d/' + ADDENDUM_ID + '/mobilebasic',
      filename: 'Desk_Addendum.txt',
      markers: ['DESK ADDENDUM'],
      minChars: 500
    },
    tracker: {
      label: 'Tracker',
      url: 'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/export?format=tsv&gid=' + TRACKER_GID,
      fallbackUrls: [
        'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/export?format=csv&gid=' + TRACKER_GID,
        'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/gviz/tq?tqx=out:csv&gid=' + TRACKER_GID
      ],
      openUrl: 'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/edit?gid=' + TRACKER_GID + '#gid=' + TRACKER_GID,
      shareUrl: 'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/gviz/tq?tqx=out:csv&gid=' + TRACKER_GID,
      altShareUrl: 'https://docs.google.com/spreadsheets/d/' + TRACKER_ID + '/export?format=csv&gid=' + TRACKER_GID,
      usageUrl: 'https://go.fuzzylogic.page/usage',
      filename: 'Desk_Tracker',
      markers: [],
      header: /^"?Status"?[\t,]"?Story"?[\t,]/,
      minChars: 500
    }
  };

  const FIELD_MAP = {
    tag_Title:'SLUG', tag_ng_CustomLabel:'LABEL', tag_Headline:'HEAD',
    tag_ng_CustomDeck:'DECK', tag_CF_Authors:'BYLINE', tag_ng_CustomDateline:'DATELINE',
    bodies:'BODY', tag_ng_CustomPullQuote:'PULL QUOTE', tag_ng_CustomPointer:'POINTER',
    tag_ng_CustomSidebarTitle:'SIDEBAR HEAD', tag_ng_CustomSidebarText:'SIDEBAR'
  };
  const FIELD_ORDER = ['SLUG','LABEL','HEAD','DECK','BYLINE','DATELINE','BODY','PULL QUOTE','POINTER','SIDEBAR HEAD','SIDEBAR'];
  const TOOL_NAMES = ['One story','My list','My sweep','Team list','Team sweep','Edition'];
  let fieldEls = {};
  let sourceState = loadCache();
  const busy = {};

  if (location.hostname === 'grok.com') { grokSide(); return; }

  function clone(x) { return JSON.parse(JSON.stringify(x)); }
  function getConfig() {
    // Saved overrides merge per source, so a partial override never drops defaults (header regex etc.).
    const base = { blueprint: { ...DEFAULT_CONFIG.blueprint }, addendum: { ...DEFAULT_CONFIG.addendum }, tracker: { ...DEFAULT_CONFIG.tracker } };
    try { const saved = JSON.parse(GM_getValue(CONFIG_KEY, '{}')) || {}; KEYS.forEach(k => { if (saved[k]) Object.assign(base[k], saved[k]); }); } catch (_) {}
    return base;
  }
  function saveConfig(c) { GM_setValue(CONFIG_KEY, JSON.stringify(c)); }
  function loadCache() {
    try { return JSON.parse(GM_getValue(CACHE_KEY, '{}')) || {}; }
    catch (_) { return {}; }
  }
  function saveCache() { GM_setValue(CACHE_KEY, JSON.stringify(sourceState)); }
  function clearCache() { sourceState = {}; GM_deleteValue(CACHE_KEY); renderPackPanel(); notify('Shift-pack cache cleared.'); }
  function nowISO() { return new Date().toISOString(); }
  function bkkParts(d) {
    const p = {};
    new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Bangkok',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'})
      .formatToParts(d || new Date()).forEach(x => { p[x.type] = x.value; });
    return p;
  }
  function bkk(d) { const p = bkkParts(d ? new Date(d) : new Date()); return p.year+'-'+p.month+'-'+p.day+' '+p.hour+':'+p.minute+':'+p.second; }
  function bangkokStamp() { return bkk(); }
  function ago(iso) {
    if (!iso) return '';
    const m = Math.max(0, Math.round((Date.now() - new Date(iso).getTime()) / 60000));
    if (m < 1) return 'just now';
    if (m < 60) return m + 'm ago';
    const h = Math.floor(m / 60); if (h < 48) return h + 'h ' + (m % 60) + 'm ago';
    return Math.floor(h / 24) + 'd ago';
  }
  function safeName(s) { return s.replace(/[^A-Za-z0-9._-]+/g,'_'); }
  function textCount(s) { return [...String(s || '')].length; }
  const sleep = ms => new Promise(r => setTimeout(r, ms));

  function copy(data, done) {
    let ok = false;
    try { if (typeof GM_setClipboard === 'function') { GM_setClipboard(data, 'text'); ok = true; } } catch (_) {}
    if (!ok) {
      const ta=document.createElement('textarea'); ta.value=data; ta.style.position='fixed'; ta.style.opacity='0'; document.body.appendChild(ta); ta.select();
      try { ok=document.execCommand('copy'); } catch (_) {} ta.remove();
    }
    if (done) done(ok);
  }
  function downloadText(filename, text, type='text/plain;charset=utf-8') {
    const blob=new Blob([text],{type}); const url=URL.createObjectURL(blob); const a=document.createElement('a');
    a.href=url; a.download=safeName(filename); document.body.appendChild(a); a.click(); a.remove(); setTimeout(()=>URL.revokeObjectURL(url),3000);
  }
  function openTab(url, active=false) {
    try { GM_openInTab(url,{active,insert:true}); } catch (_) { window.open(url,'_blank','noopener'); }
  }
  function notify(msg, ms=4500) {
    const n=document.createElement('div'); n.textContent=msg;
    n.style.cssText='position:fixed;z-index:2147483647;top:12px;left:50%;transform:translateX(-50%);background:#0b5a7a;color:#fff;padding:8px 14px;border-radius:6px;font:13px sans-serif;box-shadow:0 3px 12px rgba(0,0,0,.3);white-space:pre-line;max-width:80vw';
    document.body.appendChild(n); setTimeout(()=>n.remove(),ms);
  }

  // ---------- Grok handoff ----------
  function sendToGrok(data) {
    try { GM_setValue(GROK_KEY,JSON.stringify({text:data,ts:Date.now()})); GM_openInTab(GROK_URL,{active:true,insert:true}); }
    catch(e) { alert('Could not open Grok: '+e.message+'\nThe story remains on your clipboard.'); }
  }
  function grokSide() {
    const raw=GM_getValue(GROK_KEY,''); if(!raw)return; let job;
    try{job=JSON.parse(raw);}catch(_){GM_deleteValue(GROK_KEY);return;} GM_deleteValue(GROK_KEY);
    if(!job?.text || Date.now()-job.ts>120000)return;
    const start=Date.now();
    (function wait(){
      const boxes=document.querySelectorAll('textarea[aria-label],div[contenteditable="true"],.ProseMirror');
      const el=[...boxes].find(x=>x.getClientRects().length);
      if(!el){if(Date.now()-start>30000)return notify('Grok did not load in time. The story is on your clipboard.');return setTimeout(wait,400);}
      setTimeout(()=>{
        el.focus();
        if(el.tagName==='TEXTAREA') { const set=Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value').set; set.call(el,job.text); el.dispatchEvent(new Event('input',{bubbles:true})); }
        else { document.execCommand('selectAll',false,null); if(!document.execCommand('insertText',false,job.text)){const dt=new DataTransfer();dt.setData('text/plain',job.text);el.dispatchEvent(new ClipboardEvent('paste',{clipboardData:dt,bubbles:true,cancelable:true}));} }
        if(!AUTO_SUBMIT)return notify('Story pasted. Check it and press Send.');
        let tries=0;(function send(){const b=document.querySelector('button[data-testid="chat-submit"],button[type="submit"][aria-label="Submit"],button[aria-label="Submit"]');if(b&&!b.disabled){b.click();return notify('Story sent to Grok.');}if(++tries>40)return notify('Story pasted, but Send was not pressed.');setTimeout(send,250);})();
      },600);
    })();
  }

  // ---------- Story grabber ----------
  function txt(el){return el?el.textContent.replace(/\s+/g,' ').trim():'';}
  function clean(h){
    if(!h)return''; h=h.replace(/\r?\n/g,' ').replace(/<br\s*\/?\s*>/gi,'\n').replace(/<\/(p|div|h[1-6]|li|blockquote)>/gi,'\n\n').replace(/<[^>]+>/g,'');
    const t=document.createElement('textarea');t.innerHTML=h;
    return t.value.replace(/\u00a0/g,' ').split('\n').map(l=>l.replace(/[ \t]+/g,' ').trim()).join('\n').replace(/\n{3,}/g,'\n\n').trim();
  }
  function readFields(){
    const out={};fieldEls={};
    for(const el of document.querySelectorAll('[name^="'+PREFIX+'"]')){
      if(!/\[value\]$/.test(el.name)||el.tagName==='SELECT')continue;
      const raw=el.name.slice(PREFIX.length).split(']')[0],key=FIELD_MAP[raw];if(!key||out[key])continue;
      let val='';try{const ed=el.id&&window.tinymce&&window.tinymce.get(el.id);if(ed)val=ed.getContent();}catch(_){}if(!val)val=el.value||'';
      val=/<[a-z!\/]/i.test(val)?clean(val):val.trim();if(val){out[key]=val;fieldEls[key]=el;}
    }return out;
  }
  function readCounts(){
    const parts=[];let words='';
    ['BODY','HEAD','DECK'].concat(FIELD_ORDER.filter(k=>!['BODY','HEAD','DECK','SLUG'].includes(k))).forEach(k=>{
      const el=fieldEls[k];if(!el)return;const row=el.closest('tr')||el.parentNode;if(!row)return;
      const c=txt(row.querySelector('.dcx_mce-textlen'))||txt(row.querySelector('.charcount_container')).replace(/^Char count:\s*/i,'');if(c)parts.push(k[0]+k.slice(1).toLowerCase()+': '+c+'.');if(k==='BODY')words=txt(row.querySelector('.mce-wordcount'));
    });if(words)parts.unshift(words+'.');return parts.join(' ');
  }
  function storyPackage(){const f=readFields();if(!Object.keys(f).length)return null;const lines=[];FIELD_ORDER.forEach(k=>{if(f[k])lines.push(k==='BODY'?'BODY:\n'+f[k]:k+': '+f[k]);});const c=readCounts();if(c)lines.splice(f.SLUG?1:0,0,'COUNTS: '+c);return lines.join('\n\n');}
  function showGrab(data){
    document.getElementById(REVIEW_ID)?.remove();const box=document.createElement('div');box.id=REVIEW_ID;box.style.cssText='position:fixed;z-index:2147483647;top:20px;right:20px;width:480px;background:#fff;color:#000;border:2px solid #333;padding:10px;font:13px sans-serif;box-shadow:0 4px 20px rgba(0,0,0,.4)';
    const head=document.createElement('div');head.textContent='Review, then copy or send:';head.style.marginBottom='6px';box.appendChild(head);const ta=document.createElement('textarea');ta.value=data;ta.style.cssText='width:100%;height:300px;font:12px monospace';box.appendChild(ta);const bar=document.createElement('div');bar.style.cssText='margin-top:6px;display:flex;gap:8px';
    function add(label,fn,primary=false){const b=document.createElement('button');b.textContent=label;b.style.cssText='padding:4px 10px;cursor:pointer;'+(primary?'background:#0b5a7a;color:#fff;border:0;border-radius:4px':'');b.onclick=fn;bar.appendChild(b);}
    add('Copy',()=>copy(ta.value,ok=>{head.textContent=ok?'Copied to clipboard.':'Copy failed.';}),true);add('Copy + send to Grok',()=>copy(ta.value,()=>{box.remove();sendToGrok(ta.value);}),true);add('Close',()=>box.remove());box.appendChild(bar);document.body.appendChild(box);
  }
  function grab(){const data=storyPackage();if(!data)return alert('No open story found. Open it in Story Editor first.');if(SEND_ON_GRAB){copy(data);sendToGrok(data);}else showGrab(data);}

  // ---------- DC-X tools ----------
  function outputWindow(name){
    const w=window.open('',name,'width=900,height=700');if(!w){alert('Pop-up blocked: allow pop-ups for DC-X, then click again');return null;}
    const show=t=>{w.document.title=name;w.document.body.style.margin='0';w.document.body.innerHTML='<textarea style="width:100%;height:100vh;box-sizing:border-box;font:12px monospace"></textarea>';const a=w.document.querySelector('textarea');a.value=t;a.focus();a.select();try{w.document.execCommand('copy');}catch(_){}};return{w,show};
  }
  function askDay(prefix='Publication day'){const def=String(new Date(Date.now()+864e5).getDate()).padStart(2,'0');const x=prompt(prefix+' (e.g. 14), or all',def);return x===null?null:x.trim().toLowerCase();}
  function listRows(day,mine){
    const dd=day.padStart(2,'0'),view=(document.title.match(/"([^"]+)"/)||[,document.title])[1],map=new Map();
    document.querySelectorAll('li.document_data[data-doc_id]').forEach(r=>{const id=r.dataset.doc_id;if(map.has(id))return;const L=r.innerText.split('\n').map(s=>s.trim()).filter(Boolean),si=L.findIndex(s=>STATUS_RE.test(s));if(si<0||!FINAL_RE.test(L[si])||(mine&&!L.includes(WHO)))return;let i=si+1,sec='',date='',page='';if(/^\d\d \w{3} \d\d$/.test(L[i+1]||'')){sec=L[i];date=L[i+1];page=/^Page /.test(L[i+2]||'')?L[i+2]:'';i+=page?3:2;}const slug=L[i]||'?';const dg=date?date.slice(0,2):((slug.replace(/^\/\/\s*MERGED\s*\/\/\s*/i,'').match(/^\d+/)||[''])[0].slice(0,2).padStart(2,'0'));if(day!=='all'&&dg!==dd)return;map.set(id,{id,status:L[si],sec,date,page,slug,view});});return map;
  }
  function rowLine(x){return[x.id,x.status,x.sec,x.date,x.page,x.slug,x.view].join('\t');}
  async function historyDialog(id){
    const old=document.querySelector('#action-dialog .bd');if(old)old.innerHTML='';app.executeAction(null,'documentchangelog','',[id],true);let d=null;for(let i=0;i<40;i++){await new Promise(r=>setTimeout(r,250));d=document.querySelector('#action-dialog .bd');if(d?.querySelector('table'))break;}return d?.querySelector('table')?d:null;
  }
  function parseHistory(d){const E=[];let k=0;const time=s=>{const x=s.match(/(\d+) (\w{3}) (\d\d) (\d+):(\d\d) (AM|PM)/);if(!x)return 0;const hr=(+x[4]===12?0:+x[4])+(x[6]==='PM'?12:0);return new Date(2000+ +x[3],'JanFebMarAprMayJunJulAugSepOctNovDec'.indexOf(x[2])/3,+x[1],hr,+x[5]).getTime();};d.querySelectorAll('table').forEach(t=>{let h=t.previousElementSibling;while(h&&!h.innerText.trim())h=h.previousElementSibling;const head=h?h.innerText.trim():'',rows=[];t.querySelectorAll('tr').forEach(r=>{const c=[...r.children].map(x=>x.innerText.trim());if(c.length>=3&&!/^(Last edited by|dcx\.dbobject|Word count|Char count)/.test(c[0]))rows.push([c[0].replace(/:$/,''),c[1]||'—',c[2]||'—']);});E.push({head,time:time(head),k:k++,rows});});return E;}
  function closeHistory(){document.querySelector('#action-dialog .container-close')?.click();}
  async function tool0(){const o=outputWindow('DC-X history');if(!o)return;o.show('Working...');let id=(location.hash.match(/doc\w{15,}/)||[])[0];if(!id){const q=prompt('Doc ID or slug','');if(!q){o.w.close();return;}id=/^doc\w{15,}$/.test(q)?q:null;if(!id){const r=[...document.querySelectorAll('[data-doc_id]')].find(e=>e.textContent.replace(/\s+/g,' ').toLowerCase().includes(q.toLowerCase()));id=r?.dataset.doc_id;}if(!id)return o.show('Not found: '+q);}const d=await historyDialog(id);if(!d)return o.show('History did not load for '+id);const out=['DOC '+id];parseHistory(d).forEach(e=>{out.push('=== '+e.head);e.rows.forEach(([f,a,b])=>out.push(f+'\n  WAS: '+a+'\n  NOW: '+b));});o.show(out.join('\n'));o.w.focus();}
  function listTool(mine){const day=askDay(mine?'Publication day':'TEAM list - publication day');if(day===null)return;const o=outputWindow(mine?'DC-X my list':'DC-X team list');if(!o)return;const rows=listRows(day,mine);o.show('# '+(mine?'MY ':'TEAM ')+rows.size+' found, day '+day+'\n'+[...rows.values()].map(rowLine).join('\n'));o.w.focus();}
  async function sweepTool(mine){if(typeof app==='undefined')return alert('Run this in DC-X with a story list showing');const day=askDay(mine?'Publication day':'TEAM sweep - publication day');if(day===null)return;const o=outputWindow(mine?'DC-X my sweep':'DC-X team sweep');if(!o)return;const rows=listRows(day,mine),ids=[...rows.keys()],out=[];if(!ids.length)return o.show('0 stories for day '+day+' in this view');for(let n=0;n<ids.length;n++){const id=ids[n],meta=rows.get(id);o.show('Found '+ids.length+'. Reading '+(n+1)+' of '+ids.length+'...');const d=await historyDialog(id);if(!d){out.push('### '+rowLine(meta)+'\nHISTORY DID NOT LOAD');continue;}const E=parseHistory(d),block=['### '+rowLine(meta)];if(mine){const saves=E.filter(e=>/Document updated \(Rob Vass\)/.test(e.head)).map(e=>e.time);if(!saves.length)block.push('No Rob Vass save in history');else{const t0=Math.min(...saves);E.filter(e=>/Document/.test(e.head)&&e.time>=t0&&e.rows.length).sort((a,b)=>a.time-b.time||b.k-a.k).forEach(e=>{block.push('=== '+e.head);e.rows.forEach(([f,a,b])=>block.push(f+'\n  WAS: '+a+'\n  NOW: '+b));});}}else{const last={};E.filter(e=>/Document/.test(e.head)&&e.rows.length).sort((a,b)=>a.time-b.time||b.k-a.k).forEach(e=>{block.push('=== '+e.head);e.rows.forEach(([f,a,b])=>{block.push(f+'\n  '+(a===last[f]?'NOW: '+b:'WAS: '+a+'\n  NOW: '+b));last[f]=b;});});}out.push(block.join('\n'));closeHistory();}o.show('# '+(mine?'MY ':'TEAM ')+ids.length+' stories, day '+day+'\n\n'+out.join('\n\n'));o.w.focus();}
  async function editionTool(){if(typeof app==='undefined')return alert('Run this in DC-X with a story list showing');const day=askDay('EDITION final copy - publication day');if(day===null)return;const o=outputWindow('DC-X edition');if(!o)return;const rows=listRows(day,false),ids=[...rows.keys()],out=[],fields=['Label','Headline','Deck','Byline','Body ()','Caption'];for(let n=0;n<ids.length;n++){const id=ids[n],meta=rows.get(id);o.show('Found '+ids.length+'. Reading '+(n+1)+' of '+ids.length+'...');const d=await historyDialog(id);if(!d){out.push('### '+meta.page+'  '+meta.slug+'\nHISTORY DID NOT LOAD');continue;}const fin={};parseHistory(d).filter(e=>/Document/.test(e.head)).sort((a,b)=>a.time-b.time||b.k-a.k).forEach(e=>e.rows.forEach(([f,a,b])=>fin[f]=b==='—'?'':b));const block=['### '+[meta.page,meta.slug].filter(Boolean).join('  ')];fields.forEach(f=>{const v=(fin[f]||'').trim();if(v)block.push('['+f.replace(' ()','')+'] '+v);});out.push(block.join('\n'));closeHistory();}o.show('# EDITION '+ids.length+' stories, day '+day+'\n\n'+out.join('\n\n'));o.w.focus();}
  function runTool(id){try{if(id===0)return tool0();if(id===1)return listTool(true);if(id===2)return sweepTool(true);if(id===3)return listTool(false);if(id===4)return sweepTool(false);if(id===5)return editionTool();}catch(e){alert('DCX '+id+' failed: '+e.message);console.error(e);}}

  // ---------- Shift-pack builder ----------
  // PURE-START (no DOM or GM calls between these markers)
  const MONTHS = 'JanFebMarAprMayJunJulAugSepOctNovDec';
  function htmlLike(s) { return /<(?:!doctype|html|head|body|form|script)\b/i.test(String(s).slice(0,3000)); }
  function loginLike(s) { return /accounts\.google\.com|ServiceLogin|Sign in - Google|request access|you need permission|access denied/i.test(String(s).slice(0,20000)); }
  function firstLine(text) { return String(text).replace(/^﻿/,'').split(/\r?\n/,1)[0]; }
  function versionOf(key, text) {
    text = String(text || '');
    if (key === 'blueprint') {
      const m = text.match(/<!--\s*MASTER\s+(\S+?)\s*-->/) || text.match(/^﻿?<!--\s*(\S+?)\s*-->/);
      return m ? m[1] : '';
    }
    if (key === 'addendum') {
      const m = text.match(/Last update:\s*([^\r\n]+)/i);
      return m ? 'Last update ' + m[1].trim() : '';
    }
    if (key === 'tracker') {
      let best = 0, label = '';
      const re = /\b(\d{2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (20\d\d)\b/g; let m;
      while ((m = re.exec(text))) { const t = Date.UTC(+m[3], MONTHS.indexOf(m[2]) / 3, +m[1]); if (t > best) { best = t; label = m[0]; } }
      return label ? 'latest row ' + label : '';
    }
    return '';
  }
  function classify(key, res, cfg) {
    const text = String(res.text || ''), ct = String(res.contentType || '').toLowerCase(), fu = String(res.finalUrl || '');
    if (/accounts\.google\.com|ServiceLogin/i.test(fu)) return { state:'LOGIN PAGE', detail:'Redirected to Google sign-in' };
    if (!text.trim()) return { state:'EMPTY', detail:'No content returned' };
    if (ct.includes('text/html') || htmlLike(text)) {
      if (loginLike(text)) return { state:'LOGIN PAGE', detail:'Sign-in or permission page returned' };
      return { state:'BLOCKED', detail:'HTML page returned instead of source text' };
    }
    const n = text.length;
    if (cfg.minChars && n < cfg.minChars) return { state:'PARTIAL', detail:'Only ' + n + ' chars; expected at least ' + cfg.minChars };
    const missing = (cfg.markers || []).filter(m => !text.includes(m));
    if (missing.length) return { state:'PARTIAL', detail:'Missing ' + missing.length + ' marker(s): ' + missing.join(', ').replace(/<!--\s*|\s*-->/g,'') };
    if (cfg.endMarker && !text.slice(-1500).includes(cfg.endMarker)) return { state:'PARTIAL', detail:'Does not end at ' + cfg.endMarker + ' (possibly truncated)' };
    if (cfg.header && !(cfg.header instanceof RegExp ? cfg.header : new RegExp(cfg.header)).test(firstLine(text))) return { state:'PARTIAL', detail:'Unexpected header row: ' + firstLine(text).slice(0,60) };
    if (key === 'blueprint') return { state:'READY', detail:'6/6 components; ends at DIRECTORY' };
    return { state:'READY', detail:'Verified' };
  }
  // PURE-END

  const STATE_COLOURS = { READY:'#137333', MANUAL:'#137333', CACHED:'#b45309', PARTIAL:'#b45309', FETCHING:'#2563eb' };
  function usableState(x) { return !!(x && x.text && ['READY','CACHED','PARTIAL','MANUAL'].includes(x.state)); }
  function needsWarning(x) { return usableState(x) && !(x.state === 'READY' && x.contentState === 'READY'); }

  function requestText(url) {
    return new Promise((resolve, reject) => GM_xmlhttpRequest({
      method:'GET', url, anonymous:false, timeout:30000,
      headers:{ Accept:'text/plain,text/tab-separated-values,text/csv,*/*' },
      onload:r => {
        const ct = ((r.responseHeaders || '').match(/content-type:\s*([^\r\n]+)/i) || [,''])[1];
        if (r.status >= 200 && r.status < 300) resolve({ text:r.responseText || '', status:r.status, finalUrl:r.finalUrl || url, contentType:ct });
        else { const e = new Error('HTTP ' + r.status); e.finalUrl = r.finalUrl || url; reject(e); }
      },
      onerror:() => reject(new Error('Network/CORS error')),
      ontimeout:() => reject(new Error('Timed out'))
    }));
  }
  function trackerExt(text) { return firstLine(text).includes('\t') ? 'tsv' : 'csv'; }
  function fileNameFor(key, s) { const c = getConfig()[key]; return key === 'tracker' ? c.filename + '.' + trackerExt(s.text || '') : c.filename; }
  function labelFromUrl(url) {
    if (/format=tsv/.test(url)) return 'TSV'; if (/gviz/.test(url)) return 'gviz CSV'; if (/format=csv/.test(url)) return 'CSV';
    return 'primary';
  }

  async function refreshSource(key, quiet=false) {
    const cfg = getConfig()[key];
    const prev = sourceState[key] && sourceState[key].text ? { ...sourceState[key] } : null;
    const urls = [cfg.url, ...(cfg.fallbackUrls || [])].filter(Boolean);
    if (!urls.length) {
      sourceState[key] = { ...(prev || {}), state: prev ? 'CACHED' : 'NOT CONFIGURED', detail:'No source URL configured' + (prev ? '; stored copy kept' : '') };
      saveCache(); renderPackPanel(); return sourceState[key];
    }
    busy[key] = true; renderPackPanel();
    const fails = []; let partial = null;
    try {
      for (const url of urls) {
        let r, check;
        try { r = await requestText(url); check = classify(key, r, cfg); }
        catch (e) { fails.push({ state:'ERROR', detail:labelFromUrl(url) + ': ' + e.message }); continue; }
        const fresh = { state:check.state, contentState:check.state, detail:check.detail, text:r.text, url:r.finalUrl, requestUrl:url,
                        retrieved:nowISO(), lastAttempt:nowISO(), chars:textCount(r.text), version:versionOf(key, r.text), manual:false };
        if (check.state === 'READY') {
          if (fails.length) fresh.detail += ' (via ' + labelFromUrl(url) + ' fallback)';
          if (key === 'blueprint' && cfg.versionUrl) {
            try { const v = (await requestText(cfg.versionUrl)).text.trim().split(/\s+/)[0]; fresh.versionFile = v;
                  if (v && fresh.version && v !== fresh.version) fresh.detail += ' · VERSION.txt says ' + v + ' (raw cache lag or stale file)'; } catch (_) {}
          }
          sourceState[key] = fresh; saveCache(); return fresh;
        }
        if (check.state === 'PARTIAL') { if (!partial) partial = fresh; continue; }
        fails.push({ state:check.state, detail:labelFromUrl(url) + ': ' + check.detail });
      }

      // No READY result.
      const keepPrev = prev && (prev.contentState === 'READY' || prev.state === 'MANUAL');
      if (partial && !keepPrev) {
        partial.detail += fails.length ? ' · other routes: ' + fails.map(f => f.detail).join('; ') : '';
        sourceState[key] = partial; saveCache();
        if (!quiet) notify(cfg.label + ': PARTIAL. ' + partial.detail, 8000);
        return partial;
      }
      const why = partial ? 'fresh copy PARTIAL (' + partial.detail + ')' : fails.map(f => f.state + ' — ' + f.detail).join('; ');
      if (prev) {
        const manual = prev.state === 'MANUAL';
        sourceState[key] = { ...prev, state: manual ? 'MANUAL' : 'CACHED', lastAttempt:nowISO(),
          lastFailState: partial ? 'PARTIAL' : (fails[0] && fails[0].state) || 'ERROR',
          detail: 'Refresh failed: ' + why + (manual ? '; manual content kept' : '; showing copy retrieved ' + ago(prev.retrieved)) };
      } else {
        const st = (fails[0] && fails[0].state) || 'ERROR';
        sourceState[key] = { state:st, detail:why || 'Retrieval failed', text:'', chars:0, lastAttempt:nowISO(), lastFailState:st };
      }
      saveCache();
      if (!quiet) notify(cfg.label + ': ' + sourceState[key].state + '. ' + sourceState[key].detail, 9000);
      return sourceState[key];
    } finally { busy[key] = false; renderPackPanel(); }
  }
  async function refreshAll() {
    for (const k of KEYS) await refreshSource(k, true);
    notify(KEYS.map(k => getConfig()[k].label + ': ' + ((sourceState[k] || {}).state || 'NOT FETCHED')).join('\n'), 7000);
  }
  function verifyAll() {
    const cfgAll = getConfig(), lines = [];
    KEYS.forEach(k => {
      const s = sourceState[k];
      if (!s || !s.text) { lines.push(cfgAll[k].label + ': no stored content'); return; }
      const check = classify(k, { text:s.text, contentType:'text/plain', finalUrl:'' }, cfgAll[k]);
      s.contentState = check.state; s.version = versionOf(k, s.text); s.chars = textCount(s.text);
      if (s.state === 'READY' && check.state !== 'READY') { s.state = check.state === 'PARTIAL' ? 'PARTIAL' : check.state; s.detail = check.detail; }
      else if (s.state === 'MANUAL') s.detail = 'Manually supplied · check: ' + check.state + ' (' + check.detail + ')';
      else if (s.state === 'CACHED') s.detail = s.detail.replace(/ · check: .*$/,'') + ' · check: ' + check.state;
      lines.push(cfgAll[k].label + ': ' + s.state + ' / content ' + check.state + (s.version ? ' · ' + s.version : ''));
    });
    saveCache(); renderPackPanel(); notify(lines.join('\n'), 8000);
  }
  async function sha256(text) { const b = new TextEncoder().encode(text), h = await crypto.subtle.digest('SHA-256', b); return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2,'0')).join(''); }

  async function manifest() {
    const cfg = getConfig(), lines = ['Bangkok Post Desk Shift Pack', 'Built: ' + bangkokStamp() + ' Thailand time', 'Desk Hub: v' + VERSION, ''];
    for (const key of PACK_KEYS) {
      const c = cfg[key], s = sourceState[key] || {};
      lines.push(c.label.toUpperCase());
      lines.push('State: ' + (s.state || 'NOT FETCHED') + (s.contentState && s.contentState !== s.state ? ' (content check: ' + s.contentState + ')' : ''));
      lines.push('Version: ' + (s.version || 'not found') + (s.versionFile ? ' (VERSION.txt: ' + s.versionFile + ')' : ''));
      lines.push('Source: ' + (s.manual ? 'manual paste' : (s.requestUrl || c.url)));
      lines.push('Public link: ' + c.shareUrl);
      lines.push('Retrieved: ' + (s.retrieved ? bkk(s.retrieved) + ' Thailand time (' + ago(s.retrieved) + ')' : 'not available'));
      lines.push('Characters: ' + (s.chars || 0));
      if (s.text) lines.push('SHA-256: ' + await sha256(s.text));
      lines.push('Cached: ' + (s.state === 'CACHED' ? 'YES — last refresh failed (' + (s.lastFailState || 'ERROR') + ') at ' + bkk(s.lastAttempt) : 'no'));
      lines.push('Manual: ' + (s.manual ? 'YES' : 'no'));
      if (s.detail) lines.push('Note: ' + s.detail);
      lines.push('');
    }
    lines.push('TRACKER', 'Included as links only; no Tracker content in this pack.', 'Sheet: ' + cfg.tracker.openUrl, 'CSV: ' + cfg.tracker.shareUrl);
    return lines.join('\n').trim();
  }
  function trackerLinks() {
    const c = getConfig().tracker;
    return ['Tracker sheet: ' + c.openUrl, 'Tracker CSV: ' + c.shareUrl].join('\n');
  }
  function openingPrompt() {
    return `Bangkok Post desk package for this chat.

BOOT routes each job and EDIT is the base every job builds on.`;
  }
  function modelLinks() {
    const c = getConfig();
    return ['Blueprint (plain text): ' + c.blueprint.shareUrl,
            'Desk Addendum (plain text): ' + c.addendum.shareUrl,
            'Desk Addendum (web view fallback): ' + c.addendum.altShareUrl,
            'Tracker (CSV): ' + c.tracker.shareUrl,
            'Tracker (CSV fallback): ' + c.tracker.altShareUrl].join('\n');
  }
  function editorLinks() {
    const c = getConfig();
    return ['Blueprint: ' + c.blueprint.openUrl, 'Desk Addendum: ' + c.addendum.openUrl, 'Tracker: ' + c.tracker.openUrl, 'Tracker usage: ' + c.tracker.usageUrl].join('\n');
  }
  async function ensurePackSources() {
    const need = PACK_KEYS.filter(k => !usableState(sourceState[k]));
    if (!need.length) return;
    notify('Fetching ' + need.map(k => getConfig()[k].label).join(' and ') + '...', 3000);
    for (const k of need) await refreshSource(k, true);
  }
  async function buildPack() {
    const cfg = getConfig();
    await ensurePackSources();
    const missing = PACK_KEYS.filter(k => !usableState(sourceState[k]));
    if (missing.length) throw new Error('Unavailable: ' + missing.map(k => cfg[k].label + ' (' + ((sourceState[k] || {}).state || 'NOT FETCHED') + ')').join(', ') + '\nRefresh, or Paste the content manually.');
    const warn = PACK_KEYS.filter(k => needsWarning(sourceState[k]));
    if (warn.length) {
      const list = warn.map(k => { const s = sourceState[k]; return '- ' + cfg[k].label + ': ' + s.state + (s.contentState && s.contentState !== s.state ? ' / content ' + s.contentState : '') + (s.retrieved ? ', retrieved ' + ago(s.retrieved) : ''); }).join('\n');
      if (!confirm('This pack includes components that are not fresh verified copies:\n\n' + list + '\n\nBuild anyway? Each is labelled in the manifest.')) return null;
    }
    const man = await manifest();
    return ['===== BEGIN MANIFEST =====', man, '===== END MANIFEST =====', '',
            '===== BEGIN OPENING PROMPT =====', openingPrompt(), '===== END OPENING PROMPT =====', '',
            '===== BEGIN BLUEPRINT =====', sourceState.blueprint.text, '===== END BLUEPRINT =====', '',
            '===== BEGIN DESK ADDENDUM =====', sourceState.addendum.text, '===== END DESK ADDENDUM =====', '',
            '===== BEGIN TRACKER =====', trackerLinks(), '===== END TRACKER ====='].join('\n');
  }
  function manualSource(key) {
    const cfg = getConfig()[key], old = (sourceState[key] && sourceState[key].text) || '';
    const w = window.open('', 'dcxmanual', 'width=900,height=760'); if (!w) return alert('Pop-up blocked.');
    w.document.body.innerHTML = '<h3></h3><p style="font:12px sans-serif;color:#555"></p><textarea style="width:100%;height:76vh;box-sizing:border-box;font:12px monospace"></textarea><br><button id="save">Use this content</button> <button id="cancel">Cancel</button>';
    w.document.querySelector('h3').textContent = 'Paste ' + cfg.label + ' content';
    w.document.querySelector('p').textContent = 'Stored as MANUAL and checked against the same markers as a fetched copy.';
    const ta = w.document.querySelector('textarea'); ta.value = old;
    w.document.querySelector('#save').onclick = () => {
      const text = ta.value; if (!text.trim()) return w.alert('Nothing pasted.');
      const check = classify(key, { text, contentType:'text/plain', finalUrl:'' }, cfg);
      sourceState[key] = { state:'MANUAL', contentState:check.state, detail:'Manually supplied · check: ' + check.state + ' (' + check.detail + ')', text,
                           retrieved:nowISO(), chars:textCount(text), url:'manual', requestUrl:'manual', version:versionOf(key, text), manual:true };
      saveCache(); renderPackPanel(); w.close(); notify(cfg.label + ' stored as MANUAL · check: ' + check.state);
    };
    w.document.querySelector('#cancel').onclick = () => w.close(); ta.focus();
  }
  function sourceAction(key, action) {
    const cfg = getConfig()[key], s = sourceState[key] || {};
    if (action === 'refresh') return refreshSource(key);
    if (action === 'open') return openTab(cfg.openUrl || cfg.url, true);
    if (action === 'link') return copy(cfg.shareUrl, ok => notify(ok ? cfg.label + ' public link copied.' : 'Copy failed.'));
    if (action === 'copy') { if (!s.text) return notify(cfg.label + ' has no stored content.'); if (needsWarning(s)) notify(cfg.label + ' copied, but it is ' + s.state + '.'); return copy(s.text, ok => { if (!needsWarning(s)) notify(ok ? cfg.label + ' copied.' : 'Copy failed.'); }); }
    if (action === 'download') { if (!s.text) return notify(cfg.label + ' has no stored content.'); return downloadText(fileNameFor(key, s), s.text); }
    if (action === 'manual') return manualSource(key);
  }
  function renderPackPanel() {
    const host = document.getElementById('dcx-shift-pack'); if (!host) return; host.innerHTML = ''; const cfg = getConfig();
    KEYS.forEach(key => {
      const c = cfg[key], s = sourceState[key] || {}, state = busy[key] ? 'FETCHING' : (s.state || 'NOT FETCHED');
      const row = document.createElement('div'); row.style.cssText = 'border:1px solid #d7dee8;border-radius:5px;padding:6px;margin-top:6px';
      const top = document.createElement('div'); top.style.cssText = 'display:flex;justify-content:space-between;gap:8px;font-weight:600';
      const name = document.createElement('span'); name.textContent = c.label;
      const st = document.createElement('span'); st.textContent = state + (s.state === 'CACHED' && s.lastFailState ? ' · ' + s.lastFailState : ''); st.style.color = STATE_COLOURS[state] || '#b91c1c';
      top.append(name, st); row.appendChild(top);
      const meta = document.createElement('div'); meta.style.cssText = 'font-size:10px;color:#64748b;margin:3px 0;line-height:1.35';
      meta.textContent = [s.version, s.chars ? Number(s.chars).toLocaleString() + ' chars' : '', s.retrieved ? (s.manual ? 'pasted ' : 'retrieved ') + bkk(s.retrieved).slice(5,16) + ' (' + ago(s.retrieved) + ')' : '', s.detail].filter(Boolean).join(' · ');
      row.appendChild(meta);
      const bar = document.createElement('div'); bar.style.cssText = 'display:flex;flex-wrap:wrap;gap:4px';
      [['Refresh','refresh'],['Copy','copy'],['Save','download'],['Open','open'],['Link','link'],['Paste','manual']].forEach(([lab, act]) => {
        const b = document.createElement('button'); b.textContent = lab; b.style.cssText = 'font-size:10px;padding:3px 6px;cursor:pointer'; b.onclick = () => sourceAction(key, act); bar.appendChild(b);
      });
      row.appendChild(bar); host.appendChild(row);
    });
    renderModules();
  }
  async function packAction(action) {
    try {
      if (action === 'refresh') return refreshAll();
      if (action === 'verify') return verifyAll();
      if (action === 'prompt') return copy(openingPrompt(), ok => notify(ok ? 'Opening prompt copied.' : 'Copy failed.'));
      if (action === 'modellinks') return copy(modelLinks(), ok => notify(ok ? 'Public model links copied.' : 'Copy failed.'));
      if (action === 'links') return copy(editorLinks(), ok => notify(ok ? 'Editor links copied.' : 'Copy failed.'));
      if (action === 'syncmaster') return openTab(SYNC_MASTER_URL, true);
      if (action === 'open') { const c = getConfig(); KEYS.forEach(k => openTab(c[k].openUrl || c[k].url, false)); return; }
      if (action === 'usage') return openTab(getConfig().tracker.usageUrl, true);
      if (action === 'copy') { const p = await buildPack(); if (p === null) return; return copy(p, ok => notify(ok ? 'Complete shift pack copied (' + textCount(p).toLocaleString() + ' chars).' : 'Copy failed.')); }
      if (action === 'download') { const p = await buildPack(); if (p === null) return; const t = bkkParts(); return downloadText('BP_SHIFT_PACK_' + t.year + '-' + t.month + '-' + t.day + '_' + t.hour + t.minute + '.txt', p); }
      if (action === 'separate') {
        await ensurePackSources();
        const ks = PACK_KEYS.filter(k => usableState(sourceState[k])); if (!ks.length) return notify('No stored content to download.');
        const warn = ks.filter(k => needsWarning(sourceState[k]));
        if (warn.length && !confirm('Not fresh verified copies: ' + warn.map(k => getConfig()[k].label + ' (' + sourceState[k].state + ')').join(', ') + '\n\nDownload anyway?')) return;
        for (const k of ks) { downloadText(fileNameFor(k, sourceState[k]), sourceState[k].text); await sleep(900); }
        return notify('Downloaded ' + ks.length + ' file(s). If only one arrived, allow multiple downloads for this site in Chrome.', 7000);
      }
      if (action === 'clear') { if (confirm('Clear all cached shift-pack content?')) clearCache(); return; }
    } catch (e) { alert('Shift Pack: ' + e.message); }
  }

  // ---------- Blueprint modules ----------
  function blueprintModules() {
    const s = sourceState.blueprint, out = {};
    if (!s || !s.text) return out;
    BP_COMPONENTS.forEach(n => {
      const m = s.text.match(new RegExp('<!-- COMPONENT: ' + n + ' -->\\r?\\n([\\s\\S]*?)\\r?\\n<!-- END COMPONENT: ' + n + ' -->'));
      if (m) out[n] = (s.version ? '<!-- ' + s.version + ' -->\n' : '') + m[1] + '\n';
    });
    return out;
  }
  function moduleFile(n) { const v = (sourceState.blueprint || {}).version; return n + (v ? '_' + v : '') + (n === 'DIRECTORY' ? '.txt' : '.md'); }
  function moduleGuard() {
    const s = sourceState.blueprint;
    if (!s || !s.text) { notify('No Blueprint stored. Refresh it first.'); return false; }
    if (needsWarning(s) && !confirm('The Blueprint is ' + s.state + (s.contentState && s.contentState !== s.state ? ' / content ' + s.contentState : '') + '. Use these modules anyway?')) return false;
    return true;
  }
  async function moduleAction(names, action) {
    if (!usableState(sourceState.blueprint)) { notify('Fetching Blueprint...', 3000); await refreshSource('blueprint', true); }
    if (!moduleGuard()) return;
    const mods = blueprintModules(), missing = names.filter(n => !mods[n]);
    if (missing.length) return notify('Not found in stored Blueprint: ' + missing.join(', '), 7000);
    if (action === 'copy') return copy(mods[names[0]], ok => notify(ok ? names[0] + ' copied (' + textCount(mods[names[0]]).toLocaleString() + ' chars).' : 'Copy failed.'));
    for (let i = 0; i < names.length; i++) { downloadText(moduleFile(names[i]), mods[names[i]]); if (i < names.length - 1) await sleep(900); }
    if (names.length > 1) notify('Saved ' + names.join(' + ') + '. If only one arrived, allow multiple downloads for this site in Chrome.', 7000);
  }
  function renderModules() {
    const host = document.getElementById('dcx-modules'); if (!host) return; host.innerHTML = '';
    const mods = blueprintModules(), v = (sourceState.blueprint || {}).version;
    const info = document.createElement('div'); info.style.cssText = 'font-size:10px;color:#64748b;margin:4px 0';
    info.textContent = Object.keys(mods).length ? 'From stored Blueprint' + (v ? ' ' + v : '') + ' · ' + ((sourceState.blueprint || {}).state || '') : 'No Blueprint stored yet.';
    host.appendChild(info);
    BP_COMPONENTS.forEach(n => {
      const row = document.createElement('div'); row.style.cssText = 'display:flex;align-items:center;gap:4px;margin-top:3px;font-size:11px';
      const lab = document.createElement('span'); lab.style.cssText = 'flex:1'; lab.textContent = n + (mods[n] ? ' · ' + textCount(mods[n]).toLocaleString() : ' · —');
      row.appendChild(lab);
      [['Copy','copy'],['Save','save']].forEach(([l, a]) => { const b = document.createElement('button'); b.textContent = l; b.style.cssText = 'font-size:10px;padding:2px 6px;cursor:pointer'; b.disabled = !mods[n]; b.onclick = () => moduleAction([n], a); row.appendChild(b); });
      host.appendChild(row);
    });
    const pair = button('Save EDIT + DIRECTORY', () => moduleAction(['EDIT','DIRECTORY'], 'save'), '#475569'); pair.style.cssText += ';width:100%;margin-top:6px'; pair.disabled = !(mods.EDIT && mods.DIRECTORY);
    host.appendChild(pair);
  }
  function dropdown(title, open) {
    const d = document.createElement('details'); d.open = !!open; d.style.cssText = 'margin:6px 0;border:1px solid #d7dee8;border-radius:5px;padding:4px 6px';
    const sm = document.createElement('summary'); sm.textContent = title; sm.style.cssText = 'cursor:pointer;font-weight:600;font-size:12px;user-select:none';
    d.appendChild(sm); return d;
  }

  // ---------- UI ----------
  function closePanel(){document.getElementById(PANEL_ID)?.remove();}
  function button(label,fn,color='#2563eb'){const b=document.createElement('button');b.type='button';b.textContent=label;b.style.cssText='padding:6px;border:0;border-radius:5px;background:'+color+';color:#fff;cursor:pointer;font:11px sans-serif';b.onclick=fn;return b;}
  function openPanel(){
    closePanel();const p=document.createElement('div');p.id=PANEL_ID;p.style.cssText='position:fixed;left:12px;bottom:48px;z-index:2147483647;width:370px;max-height:86vh;overflow:auto;background:#fff;color:#222;border:1px solid #64748b;border-radius:8px;box-shadow:0 5px 20px rgba(0,0,0,.28);padding:10px;font:13px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif';
    const title=document.createElement('div');title.innerHTML='<b>DC-X Desk Hub v'+VERSION+'</b><button style="float:right" id="dcxhub-close">×</button>';p.appendChild(title);
    const grabBtn=button('Grab open story',()=>{closePanel();grab();},'#0b5a7a');grabBtn.style.cssText+=';width:100%;padding:8px;font-weight:700;margin:8px 0';p.appendChild(grabBtn);
    const grid=document.createElement('div');grid.style.cssText='display:grid;grid-template-columns:1fr 1fr;gap:6px';for(let i=0;i<=5;i++)grid.appendChild(button('DCX '+i+' '+TOOL_NAMES[i],()=>{closePanel();runTool(i);},i===4?'#b45309':i===5?'#7c3aed':'#2563eb'));const tools=dropdown('DCX tools 0-5',false);grid.style.marginTop='6px';tools.appendChild(grid);p.appendChild(tools);
    const hr=document.createElement('hr');hr.style.margin='10px 0';p.appendChild(hr);const h=document.createElement('div');h.innerHTML='<b>SHIFT PACK</b><span style="float:right;font-size:10px;color:#64748b">logged-in sources</span>';p.appendChild(h);const host=document.createElement('div');host.id='dcx-shift-pack';p.appendChild(host);const modsBox=dropdown('Blueprint modules',false);const modsHost=document.createElement('div');modsHost.id='dcx-modules';modsBox.appendChild(modsHost);p.appendChild(modsBox);
    const actions=document.createElement('div');actions.style.cssText='display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:8px';
    [['Refresh all','refresh','#0b5a7a'],['Verify sources','verify','#0b5a7a'],
     ['Copy full pack','copy','#137333'],['Download full pack','download','#137333'],
     ['Copy opening prompt','prompt','#0b5a7a'],['Copy model links','modellinks','#475569'],
     ['Copy editor links','links','#475569'],
     ['Download separate','separate','#475569'],['Open sources','open','#475569'],
     ['Sync master index','syncmaster','#475569'],
     ['Tracker usage','usage','#475569'],['Clear cache','clear','#b91c1c']].forEach(([l,a,c])=>actions.appendChild(button(l,()=>packAction(a),c)));p.appendChild(actions);
    const note=document.createElement('div');note.textContent='DCX 4 remains the broad team-history sweep. Narrow broad views before DCX 5. A failed refresh never replaces a stored copy; CACHED, PARTIAL and MANUAL components are labelled and need confirmation before they go into a pack. The pack carries the Tracker as links only.';note.style.cssText='font-size:10px;color:#64748b;margin-top:8px;line-height:1.3';p.appendChild(note);document.body.appendChild(p);document.getElementById('dcxhub-close').onclick=closePanel;renderPackPanel();
  }
  function addLauncher(){if(!document.body||document.getElementById(BUTTON_ID))return;const style=document.createElement('style');style.textContent='#dcx-grab-btn,#dcx-desk-tools-button{display:none!important}';document.head.appendChild(style);const b=document.createElement('button');b.id=BUTTON_ID;b.type='button';b.textContent='DCX';b.title='Open DC-X Desk Hub (Alt+Shift+X)';b.style.cssText='position:fixed;left:8px;bottom:8px;z-index:2147483646;padding:5px 10px;font:12px sans-serif;background:#0f3d56;color:#fff;border:0;border-radius:5px;cursor:pointer;opacity:.9';b.onclick=()=>document.getElementById(PANEL_ID)?closePanel():openPanel();document.body.appendChild(b);}

  if(typeof GM_registerMenuCommand==='function'){
    GM_registerMenuCommand('Grab open story (Alt+B)',grab);for(let i=0;i<=5;i++)GM_registerMenuCommand('DCX '+i+' '+TOOL_NAMES[i],()=>runTool(i));
    GM_registerMenuCommand('Shift Pack: refresh all',refreshAll);GM_registerMenuCommand('Shift Pack: copy opening prompt',()=>packAction('prompt'));GM_registerMenuCommand('Shift Pack: copy model links',()=>packAction('modellinks'));GM_registerMenuCommand('Shift Pack: copy full pack',()=>packAction('copy'));GM_registerMenuCommand('Shift Pack: download full pack',()=>packAction('download'));
    GM_registerMenuCommand('Shift Pack: open sync master index',()=>packAction('syncmaster'));
  }
  document.addEventListener('keydown',e=>{if(e.altKey&&!e.shiftKey&&!e.ctrlKey&&e.code==='KeyB'){e.preventDefault();grab();}if(e.altKey&&e.shiftKey&&!e.ctrlKey&&e.code==='KeyX'){e.preventDefault();document.getElementById(PANEL_ID)?closePanel():openPanel();}},true);
  setInterval(()=>{if(!window.tinymce||!tinymce.editors)return;for(const ed of tinymce.editors){if(ed._deskHubHooked)continue;ed._deskHubHooked=true;ed.on('keydown',e=>{if(e.altKey&&!e.shiftKey&&!e.ctrlKey&&e.code==='KeyB'){e.preventDefault();grab();}});}},1500);
  addLauncher();setInterval(addLauncher,3000);console.log('[DC-X Desk Hub] loaded v'+VERSION);
})();

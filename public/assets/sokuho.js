(function(){
  var btn=document.getElementById('sokuhoBtn'),dr=document.getElementById('sokuhoDrawer'),bk=document.getElementById('sokuhoBack'),cl=document.getElementById('sokuhoClose');
  function open(){ if(!dr){return} dr.classList.add('open'); bk.classList.add('open'); document.body.classList.add('sk-lock'); }
  function close(){ if(!dr){return} dr.classList.remove('open'); bk.classList.remove('open'); document.body.classList.remove('sk-lock'); }
  if(btn){btn.addEventListener('click',open)}
  if(cl){cl.addEventListener('click',close)}
  if(bk){bk.addEventListener('click',close)}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){close()}});
})();
/* 画像の長押し・右クリック保存メニューを抑止（ドロワー動作とは独立） */
document.addEventListener('contextmenu',function(e){var t=e.target;if(t&&t.tagName==='IMG'){e.preventDefault()}});

/* 速報フィード読み込み（2026-11-17 自動更新化）: /feed/sokuho.json を読み、投稿時刻を過ぎた最新3件を表示 */
(function(){
  var box=document.getElementById('skFeed');
  if(!box){return}
  var loaded=false;
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
  function fmt(iso){var d=new Date(iso);if(isNaN(d.getTime())){return ''}return (d.getMonth()+1)+'月'+d.getDate()+'日'}
  var ICONS={
    comment:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    repost:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>',
    heart:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    share:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>'
  };
  function render(items){
    var now=Date.now();
    var list=(items||[]).filter(function(it){return it&&it.datetime&&new Date(it.datetime).getTime()<=now}).sort(function(a,b){return new Date(b.datetime).getTime()-new Date(a.datetime).getTime()}).slice(0,3);
    if(!list.length){box.innerHTML='<p class="sk-note">最新の速報はXでご覧ください。</p>';return}
    box.innerHTML=list.map(function(it){
      var text=esc(it.text||'').replace(/\n/g,'<br>');
      var link='';
      if(it.url){
        var disp=esc(it.url.replace(/^https?:\/\//,''));
        link='<a class="sk-card-link" href="'+esc(it.url)+'" target="_blank" rel="noopener">'+disp+'</a>';
      }
      return '<article class="sk-card"><img class="sk-ava" src="/assets/img/profile-icon.png" alt="" width="40" height="40"><div class="sk-main"><div class="sk-row"><span class="sk-name">カイカタ｜Amazonセール速報</span><span class="sk-meta">@A_KAIKATA ・ '+fmt(it.datetime)+'</span><span class="sk-dots" aria-hidden="true">…</span></div><p class="sk-text">'+text+'</p>'+link+'<div class="sk-actions" aria-hidden="true"><span>'+ICONS.comment+'</span><span>'+ICONS.repost+'</span><span>'+ICONS.heart+'</span><span>'+ICONS.share+'</span></div></div></article>';
    }).join('');
  }
  function load(){
    if(loaded){return}
    loaded=true;
    fetch('/feed/sokuho.json?v='+Math.floor(Date.now()/60000),{cache:'no-store'}).then(function(r){if(!r.ok){throw new Error('bad')}return r.json()}).then(function(d){render(d.items)}).catch(function(){box.innerHTML='<p class="sk-note">読み込めませんでした。最新の速報はXでご覧ください。</p>'});
  }
  var btn=document.getElementById('sokuhoBtn');
  if(btn){btn.addEventListener('click',load)}
})();

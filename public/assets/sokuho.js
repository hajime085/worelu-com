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
  function fmt(iso){var d=new Date(iso);if(isNaN(d.getTime())){return ''}var w=['日','月','火','水','木','金','土'][d.getDay()];var hh=('0'+d.getHours()).slice(-2),mm=('0'+d.getMinutes()).slice(-2);return (d.getMonth()+1)+'月'+d.getDate()+'日（'+w+'）'+hh+':'+mm}
  function render(items){
    var now=Date.now();
    var list=(items||[]).filter(function(it){return it&&it.datetime&&new Date(it.datetime).getTime()<=now}).sort(function(a,b){return new Date(b.datetime).getTime()-new Date(a.datetime).getTime()}).slice(0,3);
    if(!list.length){box.innerHTML='<p class="sk-note">最新の速報はXでご覧ください。</p>';return}
    box.innerHTML=list.map(function(it){
      var text=esc(it.text||'').replace(/\n/g,'<br>');
      var link=it.url?'<a class="sk-card-link" href="'+esc(it.url)+'" target="_blank" rel="noopener">リンクを開く</a>':'';
      var label=it.label?'<span class="sk-label">'+esc(it.label)+'</span>':'';
      return '<article class="sk-card"><div class="sk-card-head"><img class="sk-ava" src="/assets/img/profile-icon.png" alt="" width="40" height="40"><div class="sk-card-who"><div class="sk-name">カイカタ｜Amazonセール速報</div><div class="sk-meta">@A_KAIKATA ・ '+fmt(it.datetime)+'</div></div>'+label+'</div><p class="sk-text">'+text+'</p>'+link+'</article>';
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

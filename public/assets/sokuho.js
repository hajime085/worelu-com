(function(){
  var btn=document.getElementById('sokuhoBtn'),dr=document.getElementById('sokuhoDrawer'),bk=document.getElementById('sokuhoBack'),cl=document.getElementById('sokuhoClose'),inited=false;
  function init(){
    if(inited){return} inited=true;
    var body=document.getElementById('sokuhoBody');
    var h=Math.max(320, body.clientHeight|| (window.innerHeight-170));
    body.innerHTML='';
    var a=document.createElement('a');
    a.className='twitter-timeline';
    a.setAttribute('data-height', String(h));
    a.setAttribute('data-chrome','noheader nofooter');
    a.setAttribute('data-lang','ja');
    a.setAttribute('data-dnt','true');
    a.href='https://x.com/A_KAIKATA';
    a.textContent='@A_KAIKATA のポストを読み込み中…';
    body.appendChild(a);
    var s=document.createElement('script');
    s.async=true; s.src='https://platform.x.com/widgets.js'; s.charset='utf-8';
    document.body.appendChild(s);
  }
  function open(){ if(!dr){return} dr.classList.add('open'); bk.classList.add('open'); document.body.classList.add('sk-lock'); init(); }
  function close(){ if(!dr){return} dr.classList.remove('open'); bk.classList.remove('open'); document.body.classList.remove('sk-lock'); }
  if(btn){btn.addEventListener('click',open)}
  if(cl){cl.addEventListener('click',close)}
  if(bk){bk.addEventListener('click',close)}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){close()}});
})();

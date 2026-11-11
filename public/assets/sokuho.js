(function(){
  var btn=document.getElementById('sokuhoBtn'),dr=document.getElementById('sokuhoDrawer'),bk=document.getElementById('sokuhoBack'),cl=document.getElementById('sokuhoClose'),inited=false;
  function note(txt){
    var n=document.getElementById('sokuhoNote');
    if(n){ n.textContent=txt; }
  }
  function init(){
    if(inited){return} inited=true;
    var body=document.getElementById('sokuhoBody');
    var h=Math.max(320,(body.clientHeight||(window.innerHeight-170)));
    body.innerHTML='<p class="sk-loading" id="sokuhoNote">読み込み中…</p>';
    var done=false;
    function go(){
      if(!(window.twttr&&twttr.widgets&&twttr.widgets.createTimeline)){ setTimeout(go,300); return; }
      twttr.widgets.createTimeline(
        {sourceType:'profile',screenName:'A_KAIKATA'},
        body,
        {height:h,chrome:'noheader nofooter',lang:'ja',dnt:true}
      ).then(function(el){
        done=true;
        var n=document.getElementById('sokuhoNote');
        if(el){ if(n){n.remove();} }
        else{ note('読み込めませんでした。下のボタンからXでご覧ください。'); }
      }).catch(function(){ note('読み込めませんでした。下のボタンからXでご覧ください。'); });
    }
    if(window.twttr&&twttr.ready){ twttr.ready(go); }
    else if(window.twttr){ go(); }
    else{
      var s=document.createElement('script');
      s.async=true; s.src='https://platform.x.com/widgets.js'; s.charset='utf-8';
      s.onload=function(){ if(window.twttr&&twttr.ready){twttr.ready(go);} else {go();} };
      s.onerror=function(){ note('読み込めませんでした。下のボタンからXでご覧ください。'); };
      document.body.appendChild(s);
    }
    setTimeout(function(){ if(!done && !body.querySelector('iframe')){ note('読み込みに時間がかかっています。下のボタンからXでも見られます。'); } },10000);
  }
  function open(){ if(!dr){return} dr.classList.add('open'); bk.classList.add('open'); document.body.classList.add('sk-lock'); init(); }
  function close(){ if(!dr){return} dr.classList.remove('open'); bk.classList.remove('open'); document.body.classList.remove('sk-lock'); }
  if(btn){btn.addEventListener('click',open)}
  if(cl){cl.addEventListener('click',close)}
  if(bk){bk.addEventListener('click',close)}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){close()}});
})();

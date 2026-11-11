(function(){
  var btn=document.getElementById('sokuhoBtn'),dr=document.getElementById('sokuhoDrawer'),bk=document.getElementById('sokuhoBack'),cl=document.getElementById('sokuhoClose');
  function open(){ if(!dr){return} dr.classList.add('open'); bk.classList.add('open'); document.body.classList.add('sk-lock'); }
  function close(){ if(!dr){return} dr.classList.remove('open'); bk.classList.remove('open'); document.body.classList.remove('sk-lock'); }
  if(btn){btn.addEventListener('click',open)}
  if(cl){cl.addEventListener('click',close)}
  if(bk){bk.addEventListener('click',close)}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){close()}});
})();

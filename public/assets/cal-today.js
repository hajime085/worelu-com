/* カレンダーの「今日」マーカーを自動で付ける（2026-11-17）
   .mcal の見出し（○年○月）と今日の日付が一致する月だけ、その日のセルに
   「今日」タグと枠線を付ける。静的HTMLに焼き込まないための仕組み。 */
(function(){
  var now=new Date();
  var y=now.getFullYear(), m=now.getMonth()+1, d=now.getDate();
  var cals=document.querySelectorAll('.mcal');
  for(var i=0;i<cals.length;i++){
    var hd=cals[i].querySelector('.mc-hd span');
    if(!hd){continue}
    var hit=/(\d{4})年(\d{1,2})月/.exec(hd.textContent||'');
    if(!hit){continue}
    if(parseInt(hit[1],10)!==y||parseInt(hit[2],10)!==m){continue}
    var cells=cals[i].querySelectorAll('td');
    for(var j=0;j<cells.length;j++){
      var num=cells[j].querySelector('.d');
      if(num&&parseInt(num.textContent,10)===d){
        cells[j].classList.add('today');
        if(!cells[j].querySelector('.mtag')){
          var tag=document.createElement('span');
          tag.className='mtag';
          tag.textContent='今日';
          cells[j].appendChild(tag);
        }
        break;
      }
    }
  }
})();

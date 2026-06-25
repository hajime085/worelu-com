---
title: あなたはもうブラック企業に洗脳されている？感覚麻痺度診断
description: 「自分が甘えているだけ？」その疑問に答える感覚麻痺度診断。20問の4択で、あなたの職場感覚がどれだけ麻痺しているかをLV1〜4で判定します。
slug: black-kigyo-shindan
category: quit
tags: [ブラック企業, 診断, 洗脳, 感覚麻痺, 転職]
date: 2026-06-17
updated: 2026-06-17
draft: false
eyecatch: ""
canonical: https://worelu.com/articles/quit/black-kigyo-shindan/
---

「自分が甘えているだけなのか、それとも会社がおかしいのか…」

そう悩んでいるなら、この診断を受けてみてください。

ブラック企業に長くいると、おかしな職場環境が「普通」に見えてきます。これは意志の弱さではなく、**人間が環境に順応する本能**によるものです。気づかないうちに価値観が書き換えられ、感覚が麻痺していく——これが「洗脳」の正体です。

この診断では、会社を評価するのではなく、**あなた自身の感覚がどれだけ麻痺しているか**を測ります。

<div style="background:#FFF8F8;border-left:4px solid #E11D48;border-radius:0 8px 8px 0;padding:16px 20px;margin:20px 0;font-size:14px;line-height:1.8;color:#9F1239;">
<strong>この診断は医療的な判断ではありません</strong><br>
心身の不調が続いている場合は、医療機関や専門家への相談を優先してください。
</div>

## あなたはもうブラック企業に洗脳されている？感覚麻痺度診断

各質問について、今のあなたの感覚に最も近いものを選んでください。

<style>
.shindan-wrap { font-family: sans-serif; max-width: 680px; margin: 0 auto; }
.shindan-q { background: #fff; border: 1px solid #E2E8F0; border-radius: 10px; padding: 20px; margin-bottom: 16px; }
.shindan-q-num { font-size: 11px; font-weight: 700; color: #2563EB; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.05em; }
.shindan-q-text { font-size: 15px; font-weight: 600; color: #1E293B; margin-bottom: 14px; line-height: 1.6; }
.shindan-q-section { font-size: 11px; color: #94A3B8; margin-bottom: 10px; }
.shindan-options { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
@media(max-width:480px){ .shindan-options { grid-template-columns: 1fr; } }
.shindan-btn {
  padding: 10px 8px; border: 1.5px solid #E2E8F0; border-radius: 8px;
  background: #F8FAFC; cursor: pointer; font-size: 13px; color: #475569;
  text-align: center; transition: all 0.15s; line-height: 1.4;
  -webkit-tap-highlight-color: transparent;
}
.shindan-btn:hover { border-color: #2563EB; background: #EFF6FF; color: #1E40AF; }
.shindan-btn.selected { border-color: #2563EB; background: #2563EB; color: #fff; font-weight: 600; }
.shindan-progress-wrap { background: #E2E8F0; border-radius: 99px; height: 6px; margin: 20px 0 8px; }
.shindan-progress-bar { background: #2563EB; height: 6px; border-radius: 99px; transition: width 0.3s; width: 0%; }
.shindan-progress-text { font-size: 12px; color: #64748B; text-align: right; margin-bottom: 20px; }
#shindan-submit {
  display: block; width: 100%; padding: 16px; margin-top: 24px;
  background: #2563EB; color: #fff; border: none; border-radius: 10px;
  font-size: 16px; font-weight: 700; cursor: pointer; letter-spacing: 0.03em;
}
#shindan-submit:disabled { background: #CBD5E1; cursor: not-allowed; }
#shindan-result { display: none; margin-top: 24px; }
.result-card {
  border-radius: 12px; padding: 28px 24px; text-align: center; margin-bottom: 20px;
}
.result-lv { font-size: 13px; font-weight: 700; letter-spacing: 0.1em; margin-bottom: 8px; }
.result-title { font-size: 24px; font-weight: 900; margin-bottom: 12px; line-height: 1.3; }
.result-score { font-size: 13px; margin-bottom: 16px; opacity: 0.8; }
.result-desc { font-size: 14px; line-height: 1.8; text-align: left; }
.result-advice { background: #F8FAFC; border-radius: 10px; padding: 16px 20px; margin-top: 16px; font-size: 14px; line-height: 1.8; color: #334155; text-align: left; }
#shindan-retry { display: block; width: 100%; padding: 14px; margin-top: 16px; background: #F1F5F9; color: #475569; border: none; border-radius: 10px; font-size: 14px; font-weight: 600; cursor: pointer; }
.share-btn { display: block; text-align: center; padding: 14px 20px; border-radius: 8px; font-size: 15px; font-weight: 700; text-decoration: none; color: #fff; background: #2563EB; margin-top: 12px; letter-spacing: 0.03em; }
</style>

<div class="shindan-wrap">
  <div class="shindan-progress-wrap"><div class="shindan-progress-bar" id="s-prog"></div></div>
  <div class="shindan-progress-text" id="s-prog-text">0 / 20問 回答済み</div>
  <div id="shindan-questions"></div>
  <button id="shindan-submit" disabled>結果を見る</button>
  <div id="shindan-result"></div>
</div>

<script>
(function(){
var QS = [
  {s:'労働環境の感覚',q:'サービス残業は、社会人なら当然のことだと思う'},
  {s:'労働環境の感覚',q:'有給休暇を全部使い切る人は、協調性がないと思う'},
  {s:'労働環境の感覚',q:'休日出勤を断るのは、チームへの裏切りだと思う'},
  {s:'労働環境の感覚',q:'定時で帰る人は、仕事への意識が低いと思う'},
  {s:'労働環境の感覚',q:'人手不足は、残った社員が頑張って補うべきだと思う'},
  {s:'労働環境の感覚',q:'休憩を取らずに働く人の方が、真面目で優秀だと思う'},
  {s:'労働環境の感覚',q:'月に何十時間も残業するのは、頑張っている証拠だと思う'},
  {s:'労働環境の感覚',q:'プライベートの時間に仕事の連絡が来るのは、仕方がないと思う'},
  {s:'労働環境の感覚',q:'体調が悪くても、よほどのことがない限り出勤すべきだと思う'},
  {s:'労働環境の感覚',q:'仕事量が多すぎても、文句を言わずこなすのが社会人だと思う'},
  {s:'思考・価値観の麻痺',q:'上司に怒鳴られたり詰められたりするのは、指導の一環だと思う'},
  {s:'思考・価値観の麻痺',q:'会社のために私生活を犠牲にするのは、当然のことだと思う'},
  {s:'思考・価値観の麻痺',q:'辞めたいと思う自分が、甘えていると感じる'},
  {s:'思考・価値観の麻痺',q:'転職を繰り返す人は、根性がないと思う'},
  {s:'思考・価値観の麻痺',q:'精神論・根性論で乗り越えることが、成長につながると思う'},
  {s:'思考・価値観の麻痺',q:'辛い環境に耐えることが、社会人としての鍛錬だと思う'},
  {s:'思考・価値観の麻痺',q:'会社への不満を口にするのは、プロ意識が低いと思う'},
  {s:'思考・価値観の麻痺',q:'「うちの会社もそんなもの」と、他社と比較することに意味を感じない'},
  {s:'思考・価値観の麻痺',q:'会社に人生を捧げることが、社会人として正しいあり方だと思う'},
  {s:'思考・価値観の麻痺',q:'職場環境が辛くても、自分が変わることで解決できると思う'}
];
var OPTS = [
  {t:'全く思わない',v:0},
  {t:'あまり思わない',v:1},
  {t:'少し思う',v:2},
  {t:'強く思う',v:3}
];
var RESULTS = [
  {min:0,max:19,lv:'LV 1',title:'正常な感覚を保っています',catch:'自分の感覚を、信じていい。',
   color:'#DCFCE7',border:'#86EFAC',text:'#166534',img:'/images/shindan/lv1_card.png',
   desc:'あなたの職場感覚は健全です。ブラック企業的な価値観に染まっておらず、自分を守る判断軸がしっかりしています。今の職場環境に不満があるなら、その感覚は正しい可能性が高いです。',
   advice:'自分の感覚を信じてください。違和感を覚えたら、それは大切なサインです。ただし、環境によっては知らず知らずのうちに感覚が麻痺していくことも。定期的にこの診断でチェックすることをおすすめします。',
   related:[
     {url:'/articles/quit/black-kigyo-aruaru/',text:'ブラック企業あるある20選｜あなたの会社は大丈夫？診断付きでチェック'},
     {url:'/articles/quit/kaisha-yabai/',text:'「この会社やばい」と感じたとき。その直感を言語化する方法'},
     {url:'/articles/stress/shigoto-genkai-sign/',text:'仕事の限界サインとは？「もう無理」と心が叫ぶ前に知ってほしいこと'}
   ]},
  {min:20,max:39,lv:'LV 2',title:'少し感覚が麻痺し始めています',catch:'「これくらい普通かな」と思い始めていませんか？',
   color:'#FEF9C3',border:'#FDE047',text:'#854D0E',img:'/images/shindan/lv2_card.png',
   desc:'いくつかの場面で、ブラック企業的な価値観を「普通」だと感じ始めているかもしれません。まだ感覚は残っていますが、このまま放置すると徐々に麻痺が進む可能性があります。',
   advice:'「これって本当に普通なんだろうか？」と一度立ち止まって考えましょう。転職経験者の話を聞いたり、口コミサイトで他社の環境を調べたりすることで、正常な基準を取り戻せます。早めの気づきが、未来を守ります。',
   related:[
     {url:'/articles/quit/kaisha-yabai/',text:'「この会社やばい」と感じたとき。その直感を言語化する方法'},
     {url:'/articles/quit/shigoto-yametai-amae/',text:'「仕事辞めたい」は甘えじゃない。後悔しないための見極め方と次の一歩'},
     {url:'/articles/stress/shigoto-genkai-sign/',text:'仕事の限界サインとは？「もう無理」と心が叫ぶ前に知ってほしいこと'}
   ]},
  {min:40,max:49,lv:'LV 3',title:'かなりブラック企業文化に染まっています',catch:'その常識、本当に世間の常識ですか？',
   color:'#FFE4E6',border:'#FCA5A5',text:'#9F1239',img:'/images/shindan/lv3_card.png',
   desc:'多くの場面で、本来おかしな価値観を「当たり前」として受け入れています。自分が消耗していても「頑張りが足りない」と思ってしまっていませんか？その感覚こそが、麻痺のサインです。あなたは悪くありません。',
   advice:'今すぐ外部の視点を取り入れてください。転職エージェントへの無料相談、信頼できる友人への相談、職場口コミサイトの閲覧など。「自分がおかしい」のではなく「環境がおかしい」可能性が高いです。',
   related:[
     {url:'/articles/quit/shigoto-yametai-amae/',text:'「仕事辞めたい」は甘えじゃない。後悔しないための見極め方と次の一歩'},
     {url:'/articles/quit/yameru-yuuki/',text:'仕事を辞める勇気が出ない人へ。踏み出せない5つの理由と現実的な答え'},
     {url:'/articles/burnout/kyushoku-amae/',text:'休職したいのは甘え？罪悪感を消して自分を守るための判断基準'}
   ]},
  {min:50,max:60,lv:'LV 4',title:'危険です。感覚が完全に麻痺している可能性があります',catch:'あなたは悪くありません。今すぐ動いてください。',
   color:'#1C1917',border:'#EF4444',text:'#FEF2F2',img:'/images/shindan/lv4_card.png',
   desc:'ブラック企業的な価値観が、あなたの「常識」になってしまっています。それはあなたが弱いからでも、甘えているからでもありません。長期間にわたりおかしい環境に晒され続けた結果です。今すぐ自分を守る行動が必要です。',
   advice:'まず信頼できる人に話してみてください。転職・休職・退職代行の利用も含めて、選択肢を具体的に調べ始めましょう。あなたの人生は、あなたのものです。一人で抱え込まないでください。',
   related:[
     {url:'/articles/quit/taisyoku-daikou-moumuri/',text:'退職代行モームリに何があったのか。今選ぶべきサービスを整理する'},
     {url:'/articles/quit/20dai-shigoto-yametai/',text:'20代で仕事辞めたいのは甘えじゃない。リスクゼロで動き出す具体的なステップ'},
     {url:'/articles/quit/30dai-shigoto-yametai/',text:'30代で仕事辞めたいのは甘えじゃない。キャリアと生活を守りながら動く方法'}
   ]}
];
var answers = new Array(QS.length).fill(null);

function buildQ(){
  var wrap = document.getElementById('shindan-questions');
  wrap.innerHTML = '';
  QS.forEach(function(q,qi){
    var div = document.createElement('div');
    div.className = 'shindan-q';
    div.innerHTML = '<div class="shindan-q-num">Q' + (qi+1) + '</div>'
      + '<div class="shindan-q-section">' + q.s + '</div>'
      + '<div class="shindan-q-text">' + q.q + '</div>'
      + '<div class="shindan-options" id="opts-' + qi + '"></div>';
    wrap.appendChild(div);
    var optsWrap = document.getElementById('opts-'+qi);
    OPTS.forEach(function(opt,oi){
      var btn = document.createElement('button');
      btn.className = 'shindan-btn';
      btn.textContent = opt.t;
      btn.addEventListener('click', function(){
        answers[qi] = opt.v;
        var btns = optsWrap.querySelectorAll('.shindan-btn');
        btns.forEach(function(b){ b.classList.remove('selected'); });
        btn.classList.add('selected');
        updateProgress();
      });
      optsWrap.appendChild(btn);
    });
  });
}

function updateProgress(){
  var done = answers.filter(function(a){ return a !== null; }).length;
  var pct = Math.round(done / QS.length * 100);
  document.getElementById('s-prog').style.width = pct + '%';
  document.getElementById('s-prog-text').textContent = done + ' / ' + QS.length + '問 回答済み';
  document.getElementById('shindan-submit').disabled = done < QS.length;
}

function showResult(){
  var total = answers.reduce(function(s,a){ return s + a; }, 0);
  var r = RESULTS[0];
  for(var i=0;i<RESULTS.length;i++){
    if(total >= RESULTS[i].min && total <= RESULTS[i].max){ r = RESULTS[i]; break; }
  }
  var res = document.getElementById('shindan-result');
  var lvNum = r.lv.replace('LV ','');
  var shareText = encodeURIComponent('感覚麻痺度診断結果：' + r.lv + ' ' + r.catch + ' #Worelu #感覚麻痺度診断');
  var shareUrl = encodeURIComponent('https://worelu.com/shindan/kanmahi/level' + lvNum + '/');
  var lv4bg = r.lv === 'LV 4' ? 'background:#1C1917;' : 'background:' + r.color + ';';
  res.innerHTML = '<div class="result-card" style="' + lv4bg + 'border:2px solid ' + r.border + '">'
    + '<div class="result-lv" style="color:' + r.text + '">' + r.lv + '</div>'
    + '<div class="result-title" style="color:' + r.text + '">' + r.title + '</div>'
    + '<div class="result-score" style="color:' + r.text + '">合計スコア：' + total + ' / 60点</div>'
    + '<div style="font-size:16px;font-weight:700;color:' + r.text + ';margin-bottom:12px;line-height:1.5;border-bottom:1px solid ' + r.border + ';padding-bottom:12px;">'
    + r.catch + '</div>'
    + '<div class="result-desc" style="color:' + r.text + '">' + r.desc + '</div>'
    + '<div class="result-advice"><strong>次のステップ</strong><br>' + r.advice + '</div>'
    + '</div>'
    + '<img src="' + r.img + '" alt="感覚麻痺度診断 ' + r.lv + ' 結果カード" style="width:100%;border-radius:10px;margin-top:16px;display:block;" onerror="this.style.display=\'none\';document.getElementById(\'img-fallback\').style.display=\'block\'">'
    + '<div id="img-fallback" style="display:none;text-align:center;padding:12px;font-size:12px;color:#94A3B8;margin-top:8px;">※ 診断カード画像を準備中です</div>'
    + '<a class="share-btn" href="https://twitter.com/intent/tweet?text=' + shareText + '&url=' + shareUrl + '" target="_blank" rel="noopener">X(Twitter)でシェアする</a>';
  res.style.display = 'block';
  document.getElementById('shindan-submit').style.display = 'none';
  document.getElementById('shindan-retry').style.display = 'block';
  res.scrollIntoView({behavior:'smooth', block:'start'});
}

document.getElementById('shindan-submit').addEventListener('click', showResult);

var retryBtn = document.createElement('button');
retryBtn.id = 'shindan-retry';
retryBtn.textContent = 'もう一度診断する';
retryBtn.style.display = 'none';
retryBtn.addEventListener('click', function(){
  answers = new Array(QS.length).fill(null);
  buildQ();
  updateProgress();
  document.getElementById('shindan-result').style.display = 'none';
  document.getElementById('shindan-submit').style.display = 'block';
  retryBtn.style.display = 'none';
  window.scrollTo({top: document.querySelector('.shindan-wrap').offsetTop - 80, behavior:'smooth'});
});
document.querySelector('.shindan-wrap').appendChild(retryBtn);

buildQ();
updateProgress();
})();
</script>

## 診断結果の見方

<svg width="100%" viewBox="0 0 680 220" role="img" style="display:block;max-width:100%;margin:24px 0"><title>感覚麻痺度レベル早見表</title>
<rect x="0" y="0" width="680" height="220" rx="12" fill="#F8FAFC"/>
<text x="340" y="28" text-anchor="middle" font-size="15" font-weight="600" fill="#1E3A5F" font-family="sans-serif">感覚麻痺度レベル早見表</text>
<rect x="16" y="44" width="152" height="152" rx="10" fill="#DCFCE7" stroke="#86EFAC" stroke-width="0.5"/>
<text x="92" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#166534" font-family="sans-serif">LV 1</text>
<text x="92" y="100" text-anchor="middle" font-size="12" font-weight="600" fill="#166534" font-family="sans-serif">正常</text>
<text x="92" y="118" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">0〜19点</text>
<text x="92" y="140" text-anchor="middle" font-size="10" fill="#16A34A" font-family="sans-serif">感覚は健全。</text>
<text x="92" y="156" text-anchor="middle" font-size="10" fill="#16A34A" font-family="sans-serif">自分を信じてOK</text>
<rect x="180" y="44" width="152" height="152" rx="10" fill="#FEF9C3" stroke="#FDE047" stroke-width="0.5"/>
<text x="256" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#854D0E" font-family="sans-serif">LV 2</text>
<text x="256" y="100" text-anchor="middle" font-size="12" font-weight="600" fill="#854D0E" font-family="sans-serif">少し麻痺</text>
<text x="256" y="118" text-anchor="middle" font-size="10" fill="#854D0E" font-family="sans-serif">20〜39点</text>
<text x="256" y="140" text-anchor="middle" font-size="10" fill="#A16207" font-family="sans-serif">要注意。外部の</text>
<text x="256" y="156" text-anchor="middle" font-size="10" fill="#A16207" font-family="sans-serif">視点を取り入れて</text>
<rect x="344" y="44" width="152" height="152" rx="10" fill="#FFE4E6" stroke="#FCA5A5" stroke-width="0.5"/>
<text x="420" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#9F1239" font-family="sans-serif">LV 3</text>
<text x="420" y="100" text-anchor="middle" font-size="12" font-weight="600" fill="#9F1239" font-family="sans-serif">かなり麻痺</text>
<text x="420" y="118" text-anchor="middle" font-size="10" fill="#9F1239" font-family="sans-serif">40〜49点</text>
<text x="420" y="140" text-anchor="middle" font-size="10" fill="#E11D48" font-family="sans-serif">転職相談を</text>
<text x="420" y="156" text-anchor="middle" font-size="10" fill="#E11D48" font-family="sans-serif">今すぐ始めて</text>
<rect x="508" y="44" width="156" height="152" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="1"/>
<text x="586" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#B91C1C" font-family="sans-serif">LV 4</text>
<text x="586" y="100" text-anchor="middle" font-size="12" font-weight="600" fill="#B91C1C" font-family="sans-serif">完全麻痺</text>
<text x="586" y="118" text-anchor="middle" font-size="10" fill="#B91C1C" font-family="sans-serif">50〜60点</text>
<text x="586" y="140" text-anchor="middle" font-size="10" fill="#DC2626" font-family="sans-serif">危険。今すぐ</text>
<text x="586" y="156" text-anchor="middle" font-size="10" fill="#DC2626" font-family="sans-serif">環境を変える行動を</text>
</svg>

## なぜ感覚麻痺が起きるのか

<div style="border-radius:10px;padding:16px 20px;margin:16px 0;display:flex;align-items:flex-start;gap:16px">
  <div style="flex-shrink:0;text-align:center">
    <img src="/images/characters/character_34.webp" alt="Aさん" style="width:72px;height:72px;object-fit:cover;border-radius:50%;border:2px solid #FECACA">
    <div style="font-size:11px;color:#64748B;margin-top:4px;font-weight:600">Aさん・31歳<br>転職経験者</div>
  </div>
  <div style="flex:1;position:relative;padding-left:8px">
    <div style="position:absolute;left:-1px;top:20px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #FECACA"></div>
    <div style="position:absolute;left:1px;top:21px;width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-right:7px solid #FFF8F8"></div>
    <div style="background:#FFF8F8;border:1px solid #FECACA;border-radius:0 10px 10px 10px;padding:14px 16px;font-size:14px;color:#334155;line-height:1.75">「転職して初めてわかったんですが、前の会社では『定時で帰ること』に罪悪感を感じていました。転職先では定時退社が当たり前で、むしろ残業する人が注意される。世界が全然違いました。」</div>
  </div>
</div>

感覚麻痺は、段階的に起きるため自分では気づきにくいのが特徴です。その仕組みは大きく3つです。

**正常化バイアス**として、人間の脳は「これは普通のことだ」と判断することでストレスを軽減しようとします。ブラック企業に慣れると、異常な状況を「普通」として処理するようになります。

**比較対象の消失**として、同じ職場にいると、その環境しか知らないため「他もこんなもの」という思い込みが強まります。外部との接触が減るほど、麻痺が進みやすくなります。

**責任の内在化**として、「会社がおかしい」ではなく「自分が弱い・甘えている」と考えるよう、知らず知らずのうちに誘導されていきます。特に「根性」「チームワーク」という言葉で正当化されます。

## 感覚を取り戻すための5つの方法

<svg width="100%" viewBox="0 0 680 200" role="img" style="display:block;max-width:100%;margin:24px 0"><title>感覚を取り戻す5つの方法</title>
<defs><marker id="kaifukuArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#94A3B8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="0" y="0" width="680" height="200" rx="12" fill="#F8FAFC"/>
<text x="340" y="28" text-anchor="middle" font-size="15" font-weight="600" fill="#1E3A5F" font-family="sans-serif">感覚を取り戻すための5つの方法</text>
<rect x="12" y="48" width="120" height="120" rx="10" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
<text x="72" y="84" text-anchor="middle" font-size="11" font-weight="600" fill="#1E40AF" font-family="sans-serif">1. 外の人と</text>
<text x="72" y="102" text-anchor="middle" font-size="11" font-weight="600" fill="#1E40AF" font-family="sans-serif">話す</text>
<text x="72" y="122" text-anchor="middle" font-size="10" fill="#3B82F6" font-family="sans-serif">転職経験者・</text>
<text x="72" y="138" text-anchor="middle" font-size="10" fill="#3B82F6" font-family="sans-serif">異業種の友人</text>
<rect x="144" y="48" width="120" height="120" rx="10" fill="#DCFCE7" stroke="#86EFAC" stroke-width="0.5"/>
<text x="204" y="84" text-anchor="middle" font-size="11" font-weight="600" fill="#166534" font-family="sans-serif">2. 口コミを</text>
<text x="204" y="102" text-anchor="middle" font-size="11" font-weight="600" fill="#166534" font-family="sans-serif">読む</text>
<text x="204" y="122" text-anchor="middle" font-size="10" fill="#16A34A" font-family="sans-serif">他社の実態を</text>
<text x="204" y="138" text-anchor="middle" font-size="10" fill="#16A34A" font-family="sans-serif">客観的に知る</text>
<rect x="276" y="48" width="128" height="120" rx="10" fill="#FEF9C3" stroke="#FDE047" stroke-width="0.5"/>
<text x="340" y="84" text-anchor="middle" font-size="11" font-weight="600" fill="#854D0E" font-family="sans-serif">3. 休む</text>
<text x="340" y="102" text-anchor="middle" font-size="11" font-weight="600" fill="#854D0E" font-family="sans-serif">（有給を使う）</text>
<text x="340" y="122" text-anchor="middle" font-size="10" fill="#A16207" font-family="sans-serif">距離を置くと</text>
<text x="340" y="138" text-anchor="middle" font-size="10" fill="#A16207" font-family="sans-serif">見えてくるものがある</text>
<rect x="416" y="48" width="120" height="120" rx="10" fill="#EDE9FE" stroke="#C4B5FD" stroke-width="0.5"/>
<text x="476" y="84" text-anchor="middle" font-size="11" font-weight="600" fill="#6D28D9" font-family="sans-serif">4. エージェントに</text>
<text x="476" y="102" text-anchor="middle" font-size="11" font-weight="600" fill="#6D28D9" font-family="sans-serif">相談する</text>
<text x="476" y="122" text-anchor="middle" font-size="10" fill="#7C3AED" font-family="sans-serif">無料で市場の</text>
<text x="476" y="138" text-anchor="middle" font-size="10" fill="#7C3AED" font-family="sans-serif">基準を知れる</text>
<rect x="548" y="48" width="120" height="120" rx="10" fill="#FFE4E6" stroke="#FCA5A5" stroke-width="0.5"/>
<text x="608" y="84" text-anchor="middle" font-size="11" font-weight="600" fill="#9F1239" font-family="sans-serif">5. この診断を</text>
<text x="608" y="102" text-anchor="middle" font-size="11" font-weight="600" fill="#9F1239" font-family="sans-serif">定期的にやる</text>
<text x="608" y="122" text-anchor="middle" font-size="10" fill="#E11D48" font-family="sans-serif">3ヶ月ごとに</text>
<text x="608" y="138" text-anchor="middle" font-size="10" fill="#E11D48" font-family="sans-serif">変化を確認する</text>
</svg>

最も効果的なのは**外部の視点を取り入れること**です。同じ職場にいると比較対象がないため、どんどん麻痺が進みます。転職エージェントへの無料相談は、今の自分の市場価値と、他社の労働環境を同時に知れる最も手軽な方法です。転職するかどうかに関係なく、「外の世界」を知るだけで感覚は取り戻せます。

## まとめ

この診断でわかることは、**あなたが弱いかどうかではなく、環境に感覚を書き換えられていないかどうか**です。

LV2以上だったあなたへ伝えたいのは、それはあなたの責任ではないということです。長い時間をかけて、じわじわと価値観を書き換えられてきた結果です。気づいた今が、変わるチャンスです。

「辞めたいと思う自分が甘えている」のではなく、「辞めたいと思うほどの環境にいる」という可能性を、一度真剣に考えてみてください。

---

## あわせて読みたい

- [ブラック企業あるある20選｜あなたの会社は大丈夫？診断付きでチェック](/articles/quit/black-kigyo-aruaru/)
- [「この会社やばい」と感じたとき。その直感を言語化する方法](/articles/quit/kaisha-yabai/)
- [仕事を辞める勇気が出ない人へ。踏み出せない5つの理由と、それぞれへの現実的な答え](/articles/quit/yameru-yuuki/)
- [サービス残業は違法。残業代を取り戻す全手順と対処法【完全版】](/articles/work/service-zangyo/)

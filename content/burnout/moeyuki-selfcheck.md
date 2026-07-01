---
title: 燃え尽き症候群のセルフチェック｜10の質問で今の状態を確認する
description: 燃え尽き症候群かどうかを10問のセルフチェックで確認。結果別の対処法と診断ツールへの導線を整理します。
slug: moeyuki-selfcheck
category: burnout
tags: [燃え尽き症候群, セルフチェック, バーンアウト, 診断]
date: 2026-06-17
updated: 2026-06-17
draft: false
eyecatch: ""
canonical: https://worelu.com/articles/burnout/moeyuki-selfcheck/
---

「最近、仕事にやる気が出ない」「何だか疲れているのに休めない」

<div style="border-radius:10px;padding:16px 20px;margin:16px 0;display:flex;align-items:flex-start;gap:16px">
  <div style="flex-shrink:0;text-align:center">
    <img src="/images/characters/character_34.webp" alt="Cさん" style="width:72px;height:72px;object-fit:cover;border-radius:50%;border:2px solid #FECACA">
    <div style="font-size:11px;color:#64748B;margin-top:4px;font-weight:600">Cさん・33歳<br>介護職</div>
  </div>
  <div style="flex:1;position:relative;padding-left:8px">
    <div style="position:absolute;left:-1px;top:20px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #FECACA"></div>
    <div style="position:absolute;left:1px;top:21px;width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-right:7px solid #FFF8F8"></div>
    <div style="background:#FFF8F8;border:1px solid #FECACA;border-radius:0 10px 10px 10px;padding:14px 16px;font-size:14px;color:#334155;line-height:1.75">「利用者さんのために頑張ってきたのに、最近は業務をこなすだけで感情が動かなくなってきました。これって、ただの疲れなんでしょうか。」</div>
  </div>
</div>

それは、もしかしたら燃え尽き症候群（バーンアウト）のサインかもしれません。燃え尽き症候群は、真面目で責任感が強い人ほど陥りやすい心の状態です。

この記事では、10の簡単な質問であなたの燃え尽き度をセルフチェックし、今の状態を客観的に把握する方法を解説します。

## 燃え尽き症候群とは？あなたの心と体が発するSOS

燃え尽き症候群（バーンアウト）とは、仕事や活動に熱心に取り組んでいた人が、心身の極度の疲労により意欲を失い、社会生活に適応できなくなる状態を指します。強いストレス状態が続くと、心身の消耗が続いている状態のことがあります。

特に、医療・介護職、教師、営業職など、人と接する機会が多く、感情労働の負担が大きい職種の人に多く見られる傾向があります。燃え尽き症候群は、あなたの心と体が「もう限界だ」と発しているSOSのサインなのです。

## 燃え尽き症候群セルフチェック：10の質問で今の状態を確認

以下の質問について、当てはまるものにチェックを入れてください。正直な気持ちで回答することが大切です。

<style>
.moe-check-list { list-style: none; padding: 0; margin: 20px 0; border: 1px solid #E2E8F0; border-radius: 10px; overflow: hidden; }
.moe-check-item { display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-bottom: 1px solid #E2E8F0; cursor: pointer; font-size: 14px; color: #334155; line-height: 1.6; transition: background 0.15s; -webkit-tap-highlight-color: transparent; }
.moe-check-item:last-child { border-bottom: none; }
.moe-check-item:hover { background: #F8FAFC; }
.moe-check-item.checked { background: #FFF7ED; color: #9A3412; font-weight: 600; }
.moe-check-box { width: 20px; height: 20px; border: 2px solid #CBD5E1; border-radius: 4px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
.moe-check-item.checked .moe-check-box { background: #EA580C; border-color: #EA580C; }
.moe-check-mark { display: none; color: #fff; font-size: 13px; font-weight: 700; }
.moe-check-item.checked .moe-check-mark { display: block; }
.moe-counter { text-align: right; font-size: 13px; color: #64748B; padding: 8px 0 4px; }
.moe-counter span { font-weight: 700; color: #EA580C; font-size: 16px; }
.moe-result { border-radius: 10px; padding: 20px 24px; margin-top: 16px; display: none; }
.moe-result.show { display: block; }
.moe-total { font-size: 17px; font-weight: 800; margin-bottom: 8px; }
.moe-judge { font-size: 14px; font-weight: 700; margin-bottom: 10px; }
.moe-desc { font-size: 14px; line-height: 1.8; }
</style>

<div id="moe-wrap">
<ul class="moe-check-list" id="moe-list">
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>以前は好きだった仕事が、最近は面倒に感じる日が増えた</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>朝、仕事のことを考えると気持ちが重く、起き上がるのがつらい</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>仕事中に集中力が続かず、ミスが増えたと感じる</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>些細なことでイライラしたり、怒りっぽくなったりすることが増えた</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>仕事が終わっても、心身の疲れがなかなか取れない</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>趣味や好きなことに対しても、以前ほど楽しめなくなった</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>人との交流を避け、一人でいる時間が増えた</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>食欲不振や過食、不眠や過眠など、生活習慣に変化があった</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>「自分はもうダメだ」「何もできない」と自己否定的な感情にとらわれることがある</li>
<li class="moe-check-item" onclick="moeCheck(this)"><div class="moe-check-box"><span class="moe-check-mark">✓</span></div>仕事に対して「どうでもいい」という無関心な気持ちになることがある</li>
</ul>
<div class="moe-counter">チェックした数：<span id="moe-count">0</span> / 10項目</div>

<button onclick="moeJudge()" style="display:block;width:100%;padding:16px;background:#EA580C;color:#fff;border:none;border-radius:10px;font-size:16px;font-weight:700;cursor:pointer;margin-top:8px;">結果を見る</button>

<div class="moe-result" id="moe-result"></div>
</div>

<script>
function moeCheck(el) {
  el.classList.toggle('checked');
  var count = document.querySelectorAll('#moe-list .checked').length;
  document.getElementById('moe-count').textContent = count;
}

function moeJudge() {
  var count = document.querySelectorAll('#moe-list .checked').length;
  var result = document.getElementById('moe-result');
  var bg, border, color, judge, desc;

  if (count >= 7) {
    bg = '#FEF2F2'; border = '#EF4444'; color = '#B91C1C';
    judge = '燃え尽きが進んでいる可能性があります';
    desc = '多くの項目に当てはまっています。これは意志の弱さではなく、心身が限界を超えているサインです。今すぐ休息を最優先にし、心療内科や産業医への相談も検討してください。一人で抱え込まないでください。';
  } else if (count >= 4) {
    bg = '#FFF7ED'; border = '#FDBA74'; color = '#9A3412';
    judge = '燃え尽き傾向が見られます';
    desc = '複数の項目に当てはまっています。放置すると悪化する可能性があるため、早めのケアが大切です。休息を取る、仕事とプライベートの境界線を引くなど、今日からできることを始めてみましょう。';
  } else if (count >= 1) {
    bg = '#EFF6FF'; border = '#93C5FD'; color = '#1E40AF';
    judge = '軽度のサインが出ています';
    desc = 'まだ軽度ですが、疲れが蓄積し始めているかもしれません。休息・睡眠・趣味の時間を意識的に確保し、定期的にこのチェックで状態を確認しましょう。';
  } else {
    bg = '#F0FDF4'; border = '#86EFAC'; color = '#166534';
    judge = '大きなサインは見られません';
    desc = '現時点では燃え尽きのサインは少ないようです。今の状態を保てるよう、無理のない働き方を心がけてください。';
  }

  result.className = 'moe-result show';
  result.style.background = bg;
  result.style.border = '2px solid ' + border;
  result.innerHTML = '<div class="moe-total" style="color:' + color + '">チェック数：' + count + ' / 10項目</div>'
    + '<div class="moe-judge" style="color:' + color + '">' + judge + '</div>'
    + '<div class="moe-desc" style="color:#334155">' + desc + '</div>';
  result.scrollIntoView({behavior:'smooth', block:'nearest'});
}
</script>

## チェックリストで「これ自分だ」と感じたら：燃え尽き傾向への対処法

セルフチェックで燃え尽き傾向が見られた場合、早めに対処することが重要です。

<div class="svg-lightbox-wrap">
<svg width="100%" viewBox="0 0 680 170" role="img" style="display:block;max-width:100%"><title>燃え尽き傾向への3つの対処法</title>
<rect x="0" y="0" width="680" height="170" rx="12" fill="#F8FAFC"/>
<text x="340" y="28" text-anchor="middle" font-size="15" font-weight="600" fill="#1E3A5F" font-family="sans-serif">燃え尽き傾向への3つの対処法</text>
<rect x="24" y="44" width="196" height="104" rx="10" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
<text x="122" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#1E40AF" font-family="sans-serif">休息を最優先に</text>
<text x="122" y="96" text-anchor="middle" font-size="11" fill="#3B82F6" font-family="sans-serif">有給・休職を活用し</text>
<text x="122" y="112" text-anchor="middle" font-size="11" fill="#3B82F6" font-family="sans-serif">仕事から距離を置く</text>
<rect x="242" y="44" width="196" height="104" rx="10" fill="#DCFCE7" stroke="#86EFAC" stroke-width="0.5"/>
<text x="340" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#166534" font-family="sans-serif">境界線を引く</text>
<text x="340" y="96" text-anchor="middle" font-size="11" fill="#16A34A" font-family="sans-serif">退勤後は仕事の</text>
<text x="340" y="112" text-anchor="middle" font-size="11" fill="#16A34A" font-family="sans-serif">連絡を見ない</text>
<rect x="460" y="44" width="196" height="104" rx="10" fill="#FEF9C3" stroke="#FDE047" stroke-width="0.5"/>
<text x="558" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#854D0E" font-family="sans-serif">完璧主義を手放す</text>
<text x="558" y="96" text-anchor="middle" font-size="11" fill="#A16207" font-family="sans-serif">「これで十分」と</text>
<text x="558" y="112" text-anchor="middle" font-size="11" fill="#A16207" font-family="sans-serif">割り切る</text>
</svg>
<p class="svg-lightbox-hint">タップして拡大</p>
</div>

#### まずは休息を最優先に

何よりもまず、心身の休息を最優先に考えましょう。有給休暇を取得したり、可能であれば休職を検討したりして、仕事から一時的に離れる時間を作ることが大切です。十分な睡眠をとり、栄養のある食事を心がけましょう。

#### 仕事とプライベートの境界線を引く

仕事とプライベートの区別が曖昧になっていると、常に仕事モードから抜け出せなくなり、心身が休まりません。退勤後は仕事の連絡を見ない、休日は仕事のことを考えないなど、意識的に境界線を引くようにしましょう。

#### 完璧主義を手放す

真面目な人ほど、完璧に仕事をこなそうとして自分を追い詰めてしまいがちです。しかし、時には「これで十分」と割り切ることも必要です。全てのタスクを完璧にこなすことよりも、心身の健康を保つことの方がはるかに重要です。

## 「休むべきか、まだ続けられるか」の判断が自分ではしにくいあなたへ

その状態だと「休むべきか、まだ続けられるか」の判断が自分ではしにくくなります。まず状態を数字で見ておくと、休む判断がしやすくなります。

Woreluのストレスチェック診断（無料・約1分）で、燃え尽き傾向や心身への負荷を数値で確認してみてください。

---

## あわせて読みたい

- [バーンアウトの症状チェックリスト。燃え尽きのサインと段階的な回復法](/articles/burnout/burnout-symptoms/)
- [仕事の限界サインとは？「もう無理」と心が叫ぶ前に知ってほしいこと](/articles/stress/shigoto-genkai-sign/)
- [休職したいのは甘え？罪悪感を消して自分を守るための判断基準](/articles/burnout/kyushoku-amae/)
- [仕事のやる気が出ないのはなぜ？「怠け」じゃない3つの原因と対処法](/articles/stress/shigoto-yaruki-denai/)

## まとめ

燃え尽き症候群は、誰にでも起こりうる心の状態です。10の質問でセルフチェックを行い、自分の燃え尽き傾向を客観的に把握することが、回復への第一歩となります。

もし燃え尽き傾向が見られたら、自分を責めずに、まずは休息を最優先に考え、仕事とプライベートの境界線を明確にしましょう。必要であれば、専門家のサポートを積極的に活用し、あなたの心と体を守る選択をしてください。

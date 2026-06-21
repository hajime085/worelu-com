from pathlib import Path

md_path = Path.home() / 'Desktop/worelu/content/stress/shigoto-genkai-sign.md'
text = md_path.read_text()

# チェックリスト診断UIのHTML（MD内に埋め込み）
checklist_html = '''
<div id="genkai-check" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:28px 24px;margin:32px 0;font-family:inherit">
<div style="font-size:13px;font-weight:800;color:#2563EB;letter-spacing:0.06em;margin-bottom:6px">SELF CHECK</div>
<div style="font-size:20px;font-weight:900;color:#0F172A;margin-bottom:6px">限界サイン チェックリスト</div>
<div style="font-size:13px;color:#64748B;margin-bottom:24px">当てはまる項目にチェックを入れてください</div>

<div style="font-size:14px;font-weight:800;color:#EF4444;margin:16px 0 10px;padding:6px 12px;background:#FEF2F2;border-radius:6px">🔴 体のサイン</div>
<div id="body-checks">
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 朝、ベッドから起き上がるのがつらい・体が重い</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 寝ても疲れが取れない・常にだるい</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 夜なかなか寝付けない・夜中に目が覚める</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 食欲がない、または過食に走ってしまう</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 胃痛・胃もたれ・吐き気など胃腸の不調が続く</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 頭痛・肩こり・腰痛が慢性的に続く</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 動悸・息苦しさ・めまいが頻繁に起こる</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 風邪をひきやすくなった・なかなか治らない</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="body"> 原因不明のじんましんや皮膚炎が出た</label>
</div>

<div style="font-size:14px;font-weight:800;color:#F59E0B;margin:20px 0 10px;padding:6px 12px;background:#FFFBEB;border-radius:6px">🟡 感情のサイン</div>
<div id="emotion-checks">
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 以前楽しかったことに興味が持てない・やる気が出ない</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 常に気分が沈んでいる・憂鬱な気持ちが続く</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 何事にも無関心・感情が麻痺したように感じる</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 自分を責める気持ちが強い・自己肯定感が低い</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 些細なことでイライラ・怒りっぽくなった</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 家族や友人・同僚に八つ当たりしてしまう</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 感情のコントロールが難しくなった</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 些細なことで涙が出る・涙もろくなった</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="emotion"> 悲しくもないのに涙が止まらないことがある</label>
</div>

<div style="font-size:14px;font-weight:800;color:#7C3AED;margin:20px 0 10px;padding:6px 12px;background:#F5F3FF;border-radius:6px">🟣 行動のサイン</div>
<div id="action-checks">
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 集中力が続かず・仕事のミスが増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 仕事の効率が著しく落ちた・時間がかかる</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 簡単な業務でも判断に迷うことが増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 仕事の締め切りを守れないことが増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 仕事への責任感が薄れた・どうでもいいと感じる</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 朝起きるのがつらく遅刻が増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 体調不良を理由に欠勤することが増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 無断欠勤をしてしまうことがある</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 出勤前に吐き気や腹痛を感じることがある</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 人との交流を避けるようになった</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 友人や家族からの誘いを断ることが増えた</label>
<label class="gc-item"><input type="checkbox" class="gc-cb" data-group="action"> 会話が億劫になった・話すのがつらい</label>
</div>

<div id="gc-result" style="display:none;margin-top:24px;padding:20px;border-radius:10px;border:2px solid"></div>

<div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap">
<button onclick="calcGenkai()" style="background:#2563EB;color:#fff;border:none;border-radius:8px;padding:12px 28px;font-size:15px;font-weight:800;cursor:pointer;font-family:inherit">診断する</button>
<button onclick="resetGenkai()" style="background:#fff;color:#64748B;border:1px solid #E2E8F0;border-radius:8px;padding:12px 20px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit">リセット</button>
</div>
</div>

<style>
.gc-item{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border-radius:8px;cursor:pointer;font-size:14px;color:#334155;line-height:1.5;margin-bottom:4px;transition:background 0.15s;border:1px solid transparent}
.gc-item:hover{background:#F1F5F9}
.gc-item input[type=checkbox]{width:18px;height:18px;min-width:18px;accent-color:#2563EB;margin-top:1px;cursor:pointer}
.gc-item.checked{background:#EFF6FF;border-color:#BFDBFE}
</style>

<script>
function calcGenkai(){
  var body=document.querySelectorAll('[data-group="body"]:checked').length;
  var emotion=document.querySelectorAll('[data-group="emotion"]:checked').length;
  var action=document.querySelectorAll('[data-group="action"]:checked').length;
  var total=body+emotion+action;
  var r=document.getElementById('gc-result');
  var msg='',bg='',border='',icon='';
  if(total===0){
    msg='チェックがありません。もう一度見直してみてください。'; bg='#F8FAFC'; border='#E2E8F0'; icon='📋';
  } else if(total<=5){
    msg='<strong>今のところ、心身のバランスは保てています。</strong><br>気になる症状がある場合は、早めに休息を取るよう心がけましょう。'; bg='#F0FDF4'; border='#86EFAC'; icon='✅';
  } else if(total<=10){
    msg='<strong>心身に疲れがたまってきているサインです。</strong><br>'+
    '体・感情・行動に変化が出始めています。今すぐ休息を増やし、一人で抱え込まないようにしましょう。'+
    '特に気になるカテゴリ：'+(body>=3?'🔴体 ':'')+(emotion>=3?'🟡感情 ':'')+(action>=3?'🟣行動 '':'')+'<br><br>→ <a href="/stress-check/" style="color:#2563EB;font-weight:700">AIコーチに相談する（無料）</a>'; 
    bg='#FFFBEB'; border='#FCD34D'; icon='⚠️';
  } else if(total<=19){
    msg='<strong>心身がかなり疲弊しています。限界サインが出ています。</strong><br>'+
    '全'+total+'項目が当てはまりました。仕事のペースを落とすか、信頼できる人や専門家への相談を強くおすすめします。一人で解決しようとしないでください。'+
    '<br><br>→ <a href="/stress-check/" style="color:#DC2626;font-weight:700">今すぐAI診断で状態を確認する（無料）</a>'; 
    bg='#FEF2F2'; border='#FCA5A5'; icon='🚨';
  } else {
    msg='<strong>深刻な限界サインです。今すぐ休んでください。</strong><br>'+
    '全'+total+'項目が当てはまりました。これだけ多くのサインが出ているなら、あなたの心身は今、本当に限界です。医療機関への受診や、信頼できる人への相談を最優先にしてください。仕事よりも、あなた自身が大切です。'+
    '<br><br>→ <a href="/stress-check/" style="color:#DC2626;font-weight:700">AIコーチに相談する（無料）</a>'; 
    bg='#FEF2F2'; border='#EF4444'; icon='🆘';
  }
  r.style.display='block';
  r.style.background=bg;
  r.style.borderColor=border;
  r.innerHTML='<div style="font-size:22px;margin-bottom:8px">'+icon+'</div>'+
    '<div style="font-size:13px;color:#64748B;margin-bottom:4px">チェック結果：計<strong style="font-size:18px;color:#0F172A;margin:0 2px">'+total+'</strong>項目（体:'+body+'/ 感情:'+emotion+'/ 行動:'+action+'）</div>'+
    '<div style="font-size:15px;color:#0F172A;line-height:1.7;margin-top:8px">'+msg+'</div>';
  r.scrollIntoView({behavior:'smooth',block:'nearest'});
}
function resetGenkai(){
  document.querySelectorAll('.gc-cb').forEach(function(cb){cb.checked=false});
  document.querySelectorAll('.gc-item').forEach(function(el){el.classList.remove('checked')});
  document.getElementById('gc-result').style.display='none';
}
document.querySelectorAll('.gc-cb').forEach(function(cb){
  cb.addEventListener('change',function(){
    this.closest('.gc-item').classList.toggle('checked',this.checked);
  });
});
</script>
'''

# チェックリストの挿入位置：「身体が出すサイン」の見出しの後
insert_after = '## 身体が出すサイン：あなたの体は、正直に「もう無理」と訴えていませんか？'

if insert_after in text:
    new_text = text.replace(insert_after, insert_after + '\n' + checklist_html)
    md_path.write_text(new_text)
    print('✅ チェックリスト挿入完了')
else:
    print('❌ 挿入位置が見つかりません')
    # 代替：まとめセクションの前に挿入
    alt = '## まとめ'
    if alt in text:
        new_text = text.replace(alt, checklist_html + '\n\n' + alt)
        md_path.write_text(new_text)
        print('✅ まとめ前に挿入しました')


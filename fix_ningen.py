from pathlib import Path

path = Path.home() / 'Desktop/worelu/content/stress/shokuba-ningen-kankei-tsukareta.md'
text = path.read_text()

# 1. ケーススタディを引用ボックスに
old1 = '''「中間管理職になってから、上司と部下の板挟みで毎日胃がキリキリしています。上からは『もっと部下を厳しく指導しろ』と言われ、下からは『Aさんは私たちの気持ちを分かってくれない』と反発される。<br><br>
どちらの意見も理解できるだけに、どう動けばいいのか分からず、精神的に参ってしまっています。休日も仕事のことが頭から離れず、心から休まることがありません。」'''

new1 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「中間管理職になってから、上司と部下の板挟みで毎日胃がキリキリしています。上からは『もっと部下を厳しく指導しろ』と言われ、下からは『Aさんは私たちの気持ちを分かってくれない』と反発される。どちらの意見も理解できるだけに、どう動けばいいのか分からず、精神的に参ってしまっています。」
</div>'''

old2 = '''「入社してまだ半年ですが、職場の陰口や悪口がひどくて毎日会社に行くのが憂鬱です。特に、特定の先輩がいつも誰かの悪口を言っていて、聞いているだけで気分が悪くなります。自分もいつターゲットになるかと思うと怖くて、発言するのもためらってしまいます。こんな環境で働き続けるのは本当に辛いです。」'''

new2 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「入社してまだ半年ですが、職場の陰口や悪口がひどくて毎日会社に行くのが憂鬱です。自分もいつターゲットになるかと思うと怖くて、発言するのもためらってしまいます。こんな環境で働き続けるのは本当に辛いです。」
</div>'''

old3 = '''「職場の飲み会や休日のイベントへの参加が半ば強制で、正直疲れています。上司や同僚は『これもコミュニケーションの一環だ』と言いますが、私はプライベートは自分の時間として大切にしたいんです。断ると『付き合いが悪い』と思われそうで、無理して参加していますが、そのたびにストレスが溜まります。仕事とプライベートの境界線が曖昧で、息苦しさを感じています。」'''

new3 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「職場の飲み会への参加が半ば強制で、正直疲れています。断ると『付き合いが悪い』と思われそうで、無理して参加していますが、そのたびにストレスが溜まります。仕事とプライベートの境界線が曖昧で、息苦しさを感じています。」
</div>'''

# 2. ミスマッチの説明にポイントボックスを追加
old4 = '''例えば、以下のような状況に心当たりはありませんか？<br><br>

*   **繊細な気質（HSPなど）:** 他人の感情に敏感で、職場のピリピリした雰囲気に影響されやすい。<br><br>
*   **協調性を重んじる文化:** 自分の意見を主張しにくい環境で、ストレスを感じる。<br><br>
*   **競争が激しい職場:** 常に他人と比較され、精神的に疲弊する。<br><br>
*   **ハラスメントが横行:** パワハラやモラハラが日常的にあり、精神的に追い詰められている。<br><br>
*   **コミュニケーション不足:** 報連相が不足し、誤解や不信感が生まれやすい。'''

new4 = '''以下のような状況に心当たりはありませんか？

<div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:16px 20px;margin:16px 0">
<div style="font-size:12px;font-weight:800;color:#2563EB;margin-bottom:10px">こんな環境でストレスを感じやすい</div>

- **繊細な気質（HSPなど）** 他人の感情に敏感で、ピリピリした雰囲気に影響されやすい
- **協調性を重んじる文化** 自分の意見を主張しにくく、ストレスを感じる
- **競争が激しい職場** 常に他人と比較され、精神的に疲弊する
- **ハラスメントが横行** パワハラ・モラハラが日常的にあり追い詰められている
- **コミュニケーション不足** 報連相が不足し、誤解や不信感が生まれやすい
</div>'''

# 3. 「疲れやすい人の特徴」に警告ボックスを追加
old5 = '''**人間関係で疲れやすい人の特徴:**<br><br>

*   **共感性が高い:** 他人の感情に深く共感し、相手の気持ちを自分のことのように感じてしまう。<br><br>
*   **責任感が強い:** 自分の役割を全うしようとし、他人の分まで背負い込んでしまう。<br><br>
*   **完璧主義:** 人間関係においても完璧を求め、小さな摩擦も許せない。<br><br>
*   **自己肯定感が低い:** 他人の評価を気にしすぎ、自分に自信が持てない。<br><br>
*   **断れない性格:** 頼まれごとを断れず、自分のキャパシティを超えてしまう。'''

new5 = '''<div style="background:#FEF2F2;border:1px solid #FECACA;border-radius:8px;padding:16px 20px;margin:16px 0">
<div style="font-size:12px;font-weight:800;color:#DC2626;margin-bottom:10px">人間関係で疲れやすい人の特徴</div>

- **共感性が高い** 他人の感情に深く共感し、相手の気持ちを自分のことのように感じてしまう
- **責任感が強い** 自分の役割を全うしようとし、他人の分まで背負い込んでしまう
- **完璧主義** 人間関係においても完璧を求め、小さな摩擦も許せない
- **自己肯定感が低い** 他人の評価を気にしすぎ、自分に自信が持てない
- **断れない性格** 頼まれごとを断れず、自分のキャパシティを超えてしまう
</div>'''

# 4. 環境を変える選択肢をカードスタイルに
old6 = '''#### 1. 部署異動や配置転換

もし、社内に部署異動や配置転換の制度があるなら、まずはそれを検討してみるのも一つの手です。人間関係の悩みが特定の部署やチームに起因している場合、環境が変わるだけで驚くほど心が軽くなることがあります。新しい部署では、人間関係も一から築き直せるため、心機一転、リフレッシュできるチャンスにもなります。まずは、上司や人事担当者に相談し、可能性を探ってみましょう。<br><br>

#### 2. 休職

精神的に「もう限界だ」と感じているなら、休職も大切な選択肢の一つです。休職は、決して「逃げ」ではありません。心身が悲鳴を上げている時に、無理をして働き続けることは、あなたの健康をさらに損ねてしまいます。休職期間中は、仕事から完全に離れて心身を休ませ、冷静に今後のキャリアや人生について考える貴重な時間を得られます。([休職1ヶ月でどう変わる？お金・過ごし方・復職の判断を整理する](/worelu_articles/article_11.md)も参考に、休職中の過ごし方や復職の判断について理解を深めましょう。)<br><br>

#### 3. 転職

根本的に職場環境や企業文化があなたの価値観や特性に合わないと感じる場合、転職は非常に有効な選択肢です。人間関係の悩みは、多くの場合、あなたの性格の問題ではなく、職場とのミスマッチから生じます。あなたの強みや個性を活かせる、より良い人間関係を築ける職場は必ず存在します。転職は大きな決断ですが、あなたの人生をより豊かにするための前向きな一歩となり得ます。'''

new6 = '''<div style="display:grid;gap:12px;margin:16px 0">

<div style="background:#F0FDF4;border:1px solid #86EFAC;border-radius:8px;padding:16px 20px">
<div style="font-size:13px;font-weight:800;color:#16A34A;margin-bottom:6px">① 部署異動・配置転換</div>
<div style="font-size:14px;color:#334155;line-height:1.7">人間関係の悩みが特定の部署に起因している場合、環境が変わるだけで心が軽くなることがあります。まず上司や人事担当者に相談してみましょう。</div>
</div>

<div style="background:#FFFBEB;border:1px solid #FCD34D;border-radius:8px;padding:16px 20px">
<div style="font-size:13px;font-weight:800;color:#D97706;margin-bottom:6px">② 休職</div>
<div style="font-size:14px;color:#334155;line-height:1.7">「もう限界だ」と感じているなら、休職は決して「逃げ」ではありません。心身を休ませ、冷静に今後を考える大切な時間になります。</div>
</div>

<div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:16px 20px">
<div style="font-size:13px;font-weight:800;color:#2563EB;margin-bottom:6px">③ 転職</div>
<div style="font-size:14px;color:#334155;line-height:1.7">職場環境があなたの価値観に合わない場合、転職は前向きな選択肢です。あなたの強みを活かせる職場は必ず存在します。</div>
</div>

</div>'''

# 5. まとめの前にストレスチェックCTAボックスを追加
old7 = '''## まとめ：人間関係の疲れは、あなたのせいじゃない'''

new7 = '''<div style="background:#EFF6FF;border:2px solid #2563EB;border-radius:10px;padding:20px 24px;margin:32px 0;text-align:center">
<div style="font-size:13px;font-weight:800;color:#2563EB;margin-bottom:6px">まずは今の状態を確認してみましょう</div>
<div style="font-size:15px;font-weight:700;color:#0F172A;margin-bottom:12px">あなたの職場ストレスを無料でチェック</div>
<div style="font-size:13px;color:#64748B;margin-bottom:16px">10問・約1分で、仕事ストレス・燃え尽き傾向・転職意向を数値化します</div>
<a href="/stress-check/" style="display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:14px;padding:12px 28px;border-radius:8px;text-decoration:none">無料でストレスチェックを受ける →</a>
</div>

## まとめ：人間関係の疲れは、あなたのせいじゃない'''

# 適用
replacements = [
    (old1, new1), (old2, new2), (old3, new3),
    (old4, new4), (old5, new5), (old6, new6), (old7, new7)
]

count = 0
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        count += 1
        print(f'✅ 修正{count}箇所完了')
    else:
        print(f'❌ 該当箇所が見つかりません（{old[:30]}...）')

path.write_text(text)
print(f'\n合計{count}箇所修正完了')

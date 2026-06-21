from pathlib import Path

path = Path.home() / 'Desktop/worelu/content/stress/shokuba-ningen-kankei-tsukareta.md'
text = path.read_text()

# ケース1：Aさん（男性・左キャラ・右吹き出し）
old1 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「中間管理職になってから、上司と部下の板挟みで毎日胃がキリキリしています。上からは『もっと部下を厳しく指導しろ』と言われ、下からは『Aさんは私たちの気持ちを分かってくれない』と反発される。どちらの意見も理解できるだけに、どう動けばいいのか分からず、精神的に参ってしまっています。」
</div>'''

new1 = '''<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:16px 20px;margin:16px 0;display:flex;align-items:flex-start;gap:16px">
  <div style="flex-shrink:0;text-align:center">
    <img src="/images/characters/character_009.webp" alt="Aさん" style="width:72px;height:72px;object-fit:cover;border-radius:50%;border:2px solid #E2E8F0">
    <div style="font-size:11px;color:#64748B;margin-top:4px;font-weight:600">Aさん・30代<br>営業職</div>
  </div>
  <div style="flex:1;position:relative;padding-left:8px">
    <div style="position:absolute;left:-1px;top:20px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #E2E8F0"></div>
    <div style="position:absolute;left:1px;top:21px;width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-right:7px solid #F8FAFC"></div>
    <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:0 10px 10px 10px;padding:14px 16px;font-size:14px;color:#334155;line-height:1.75">
      「中間管理職になってから、上司と部下の板挟みで毎日胃がキリキリしています。上からは『もっと部下を厳しく指導しろ』と言われ、下からは反発される。どちらの意見も理解できるだけに、どう動けばいいのか分からず、精神的に参ってしまっています。」
    </div>
  </div>
</div>'''

# ケース2：Bさん（女性・右キャラ・左吹き出し）
old2 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「入社してまだ半年ですが、職場の陰口や悪口がひどくて毎日会社に行くのが憂鬱です。自分もいつターゲットになるかと思うと怖くて、発言するのもためらってしまいます。こんな環境で働き続けるのは本当に辛いです。」
</div>'''

new2 = '''<div style="background:#FFF8F8;border:1px solid #FECACA;border-radius:10px;padding:16px 20px;margin:16px 0;display:flex;align-items:flex-start;gap:16px;flex-direction:row-reverse">
  <div style="flex-shrink:0;text-align:center">
    <img src="/images/characters/character_59.webp" alt="Bさん" style="width:72px;height:72px;object-fit:cover;border-radius:50%;border:2px solid #FECACA">
    <div style="font-size:11px;color:#64748B;margin-top:4px;font-weight:600">Bさん・20代<br>ITエンジニア</div>
  </div>
  <div style="flex:1;position:relative;padding-right:8px">
    <div style="position:absolute;right:-1px;top:20px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:8px solid #FECACA"></div>
    <div style="position:absolute;right:1px;top:21px;width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-left:7px solid #FFF8F8"></div>
    <div style="background:#FFF8F8;border:1px solid #FECACA;border-radius:10px 0 10px 10px;padding:14px 16px;font-size:14px;color:#334155;line-height:1.75">
      「入社してまだ半年ですが、職場の陰口や悪口がひどくて毎日会社に行くのが憂鬱です。自分もいつターゲットになるかと思うと怖くて、発言するのもためらってしまいます。こんな環境で働き続けるのは本当に辛いです。」
    </div>
  </div>
</div>'''

# ケース3：Cさん（女性・左キャラ・右吹き出し）
old3 = '''<div style="background:#F8FAFC;border-left:4px solid #2563EB;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;font-size:14px;color:#334155;line-height:1.7">
「職場の飲み会への参加が半ば強制で、正直疲れています。断ると『付き合いが悪い』と思われそうで、無理して参加していますが、そのたびにストレスが溜まります。仕事とプライベートの境界線が曖昧で、息苦しさを感じています。」
</div>'''

new3 = '''<div style="background:#FFFBF0;border:1px solid #FDE68A;border-radius:10px;padding:16px 20px;margin:16px 0;display:flex;align-items:flex-start;gap:16px">
  <div style="flex-shrink:0;text-align:center">
    <img src="/images/characters/character_24.webp" alt="Cさん" style="width:72px;height:72px;object-fit:cover;border-radius:50%;border:2px solid #FDE68A">
    <div style="font-size:11px;color:#64748B;margin-top:4px;font-weight:600">Cさん・40代<br>管理職</div>
  </div>
  <div style="flex:1;position:relative;padding-left:8px">
    <div style="position:absolute;left:-1px;top:20px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #FDE68A"></div>
    <div style="position:absolute;left:1px;top:21px;width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-right:7px solid #FFFBF0"></div>
    <div style="background:#FFFBF0;border:1px solid #FDE68A;border-radius:0 10px 10px 10px;padding:14px 16px;font-size:14px;color:#334155;line-height:1.75">
      「職場の飲み会への参加が半ば強制で、正直疲れています。断ると『付き合いが悪い』と思われそうで、無理して参加していますが、そのたびにストレスが溜まります。仕事とプライベートの境界線が曖昧で、息苦しさを感じています。」
    </div>
  </div>
</div>'''

count = 0
for old, new in [(old1, new1), (old2, new2), (old3, new3)]:
    if old in text:
        text = text.replace(old, new)
        count += 1
        print(f'✅ ケース{count} 吹き出し適用')
    else:
        print(f'❌ ケース{count+1} 該当箇所が見つかりません')

path.write_text(text)
print(f'\n合計{count}箇所修正完了')

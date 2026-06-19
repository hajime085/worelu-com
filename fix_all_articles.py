#!/usr/bin/env python3
"""
Worelu 全記事一括修正スクリプト
実行: python3 fix_all_articles.py
対象: ~/Desktop/worelu/content/ 以下の全MDファイル
"""

import re, os, glob
from pathlib import Path

CONTENT_DIR = Path.home() / 'Desktop' / 'worelu' / 'content'

# 正しいURLマッピング（間違ったURL → 正しいURL）
URL_MAP = {
    'https://worelu.com/moeyuki-selfcheck/':        '/articles/burnout/moeyuki-selfcheck/',
    'https://worelu.com/burnout-symptoms/':          '/articles/burnout/burnout-symptoms/',
    'https://worelu.com/kyushoku-1month/':           '/articles/burnout/kyushoku-1month/',
    'https://worelu.com/nemurenai-asa/':             '/articles/stress/nemurenai-asa/',
    'https://worelu.com/doki-ga-suru/':              '/articles/stress/doki-ga-suru/',
    'https://worelu.com/namida-ga-deru/':            '/articles/stress/namida-ga-deru/',
    'https://worelu.com/service-zangyo/':            '/articles/work/service-zangyo/',
    'https://worelu.com/service-zangyo-voluntary/':  '/articles/work/service-zangyo-voluntary/',
    'https://worelu.com/service-zangyo-atarimae/':   '/articles/work/service-zangyo-atarimae/',
    'https://worelu.com/black-kigyo-shindan/':       '/articles/quit/black-kigyo-shindan/',
    'https://worelu.com/black-kigyo-aruaru/':        '/articles/quit/black-kigyo-aruaru/',
    'https://worelu.com/kaisha-yabai/':              '/articles/quit/kaisha-yabai/',
    'https://worelu.com/yameru-yuuki/':              '/articles/quit/yameru-yuuki/',
    'https://worelu.com/hyouka-sarenai/':            '/articles/quit/hyouka-sarenai/',
    'https://worelu.com/taishoku-daikou-moumuri/':   '/articles/quit/taisyoku-daikou-moumuri/',
    'https://worelu.com/taisyoku-daikou-moumuri/':   '/articles/quit/taisyoku-daikou-moumuri/',
    '/worelu_articles/article_01.md':                '/articles/stress/nemurenai-asa/',
    '/worelu_articles/article_11.md':                '/articles/burnout/kyushoku-1month/',
    '/worelu_articles/article_12.md':                '/articles/burnout/moeyuki-selfcheck/',
}

def fix_article(path: Path) -> dict:
    original = path.read_text()
    content = original
    changes = []

    # ① 末尾の「関連記事」ブロックを除去（--- の後）
    if re.search(r'\n---\n\n\*\*関連記事\*\*', content):
        content = re.sub(r'\n---\n\n\*\*関連記事\*\*[\s\S]*$', '', content)
        changes.append('関連記事ブロック除去')

    # ② 末尾の「メタディスクリプション」ブロックを除去
    if re.search(r'\n---\n\n\*\*メタディスクリプション', content):
        content = re.sub(r'\n---\n\n\*\*メタディスクリプション[\s\S]*$', '', content)
        changes.append('メタディスクリプション除去')

    # ③ ▼ から始まるCTAブロックを除去
    if '▼' in content:
        content = re.sub(
            r'\n▼[^\n]*\n(?:[^\n]*\n)?→ 無料でストレスチェックを受ける[^\n]*\n?',
            '\n',
            content
        )
        changes.append('▼CTAブロック除去')

    # ④ 末尾の単独 --- を除去
    content = re.sub(r'\n---\s*$', '', content)

    # ⑤ テキストリンク化（本文中の → ストレスチェック）
    if '→ 無料でストレスチェックを受ける（worelu.com）' in content:
        content = content.replace(
            '→ 無料でストレスチェックを受ける（worelu.com）',
            '→ [無料でストレスチェックを受ける（worelu.com）](/stress-check/)'
        )
        changes.append('ストレスチェックリンク化')

    # ⑥ 関連記事URLの修正（本文中に残ったもの）
    for wrong, correct in URL_MAP.items():
        if wrong in content:
            content = content.replace(wrong, correct)
            changes.append(f'URL修正: {wrong.split("/")[-2]}')

    # ⑦ 末尾の余分な空行を整理
    content = content.rstrip() + '\n'

    if content != original:
        path.write_text(content)
        return {'file': path.name, 'changes': changes, 'status': '✅ 修正'}
    else:
        return {'file': path.name, 'changes': [], 'status': '⬛ 変更なし'}

def main():
    md_files = list(CONTENT_DIR.rglob('*.md'))
    if not md_files:
        print(f'❌ ファイルが見つかりません: {CONTENT_DIR}')
        return

    print(f'対象ファイル: {len(md_files)}本\n')
    total_fixed = 0

    for path in sorted(md_files):
        result = fix_article(path)
        rel = path.relative_to(CONTENT_DIR)
        if result['changes']:
            print(f"{result['status']} {rel}")
            for c in result['changes']:
                print(f"    → {c}")
            total_fixed += 1
        else:
            print(f"{result['status']} {rel}")

    print(f'\n修正完了: {total_fixed}/{len(md_files)}本を更新')
    print('\n次のステップ:')
    print('  cd ~/Desktop/worelu')
    print('  python3 build.py')
    print('  git add .')
    print('  git commit -m "全記事：CTAリンク化・URL修正・重複ブロック除去"')
    print('  git push')

if __name__ == '__main__':
    main()

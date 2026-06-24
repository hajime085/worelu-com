#!/usr/bin/env python3
"""
Worelu ビルドスクリプト
実行: python3 build.py
生成物: public/ 以下に全ファイルを出力

生成するもの:
  - 記事HTML (/articles/{category}/{slug}/index.html)
  - 記事一覧 (/articles/index.html)
  - カテゴリ一覧 (/articles/{category}/index.html)
  - sitemap.xml
  - RSS (feed.xml)
  - robots.txt
"""

import os
import sys
import shutil
import yaml
import markdown
from datetime import datetime, timezone
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# ===== 設定 =====
BASE_URL = "https://worelu.com"
OGP_WORKER_URL = "https://worelu-ogp-next.vercel.app/api/og"
CONTENT_DIR = Path("content")
TEMPLATE_DIR = Path("templates")
OUTPUT_DIR = Path("public")

CATEGORY_LABELS = {
    "stress":  "症状・ストレス",
    "burnout": "燃え尽き・休職",
    "work":    "労働問題",
    "quit":    "転職・退職",
}

CATEGORY_DESCS = {
    "stress": {
        "desc": "仕事のストレスは、眠れない、涙が出る、動悸、吐き気、朝起きられないなど、さまざまな心身の不調として現れることがあります。このカテゴリーでは、仕事によるストレス症状や限界サイン、原因、セルフチェック、対処法について分かりやすく解説しています。「仕事がつらい」「最近体調がおかしい」と感じている方が、自分の状態を整理し、次の一歩を考えるための情報をまとめています。",
        "lead": "気になる症状から記事を探してください。",
    },
    "burnout": {
        "desc": "仕事による燃え尽き症候群（バーンアウト）は、長期間にわたるストレスによって心身のエネルギーが枯渇してしまう状態です。このカテゴリーでは、バーンアウトの症状やセルフチェック、休職の判断・手続き、適応障害との違い、回復方法について解説しています。「甘えかな」と思いながら限界を迎えている方へ、休むための判断基準と具体的なステップをお届けします。",
        "lead": "今の自分の状態を確認することから始めましょう。",
    },
    "work": {
        "desc": "仕事でのサービス残業・長時間労働・有給休暇の未取得・パワハラなど、労働基準法に関わる問題は多くの職場で起きています。このカテゴリーでは、残業代の取り戻し方や、職場の問題に直面したときの対処法、労働基準監督署への相談方法など、働く人が自分の権利を守るための情報を解説しています。",
        "lead": "「これっておかしいのかな？」と感じたらまず確認してみてください。",
    },
    "quit": {
        "desc": "「仕事を辞めたい」「転職したいけれど不安」「退職を切り出せない」と悩んでいる方向けに、退職・転職に関する情報をまとめています。退職代行サービスの活用法やブラック企業の見分け方、転職活動の進め方など、次の一歩を安心して踏み出すための情報を分かりやすく解説しています。仕事を辞めるタイミングや退職後の手続きについても紹介しています。",
        "lead": "状況に近い悩みの記事からご覧ください。",
    },
}

# カテゴリ別カード表示設定
CAT_CARD_STYLES = {
    "stress":  {"bg": "#FEF2F2", "circle": "#FECACA", "fill": "#F87171", "badge_bg": "#FEE2E2", "badge_color": "#B91C1C"},
    "burnout": {"bg": "#FFFBEB", "circle": "#FDE68A", "fill": "#F59E0B", "badge_bg": "#FEF3C7", "badge_color": "#92400E"},
    "work":    {"bg": "#EFF6FF", "circle": "#BFDBFE", "fill": "#2563EB", "badge_bg": "#DBEAFE", "badge_color": "#1D4ED8"},
    "quit":    {"bg": "#F5F3FF", "circle": "#DDD6FE", "fill": "#A78BFA", "badge_bg": "#EDE9FE", "badge_color": "#5B21B6"},
}
CAT_ICONS = {
    "stress":  '<circle cx="26" cy="26" r="18" fill="{circle}"/><path d="M26 10c0 8-12 10-12 18a12 12 0 0024 0c0-8-12-10-12-18z" fill="{fill}"/>',
    "burnout": '<circle cx="26" cy="26" r="18" fill="{circle}"/><path d="M26 10c0 8-12 10-12 18a12 12 0 0024 0c0-8-12-10-12-18z" fill="{fill}"/><path d="M26 22c0 4-4 6-4 10a4 4 0 008 0c0-4-4-6-4-10z" fill="#FCD34D"/>',
    "work":    '<circle cx="26" cy="26" r="18" fill="{circle}"/><circle cx="26" cy="26" r="10" stroke="{fill}" stroke-width="2" fill="none"/><path d="M26 18v8l5 3" stroke="{fill}" stroke-width="2" stroke-linecap="round"/>',
    "quit":    '<circle cx="26" cy="26" r="18" fill="{circle}"/><rect x="16" y="14" width="20" height="24" rx="3" fill="{fill}"/><path d="M20 22h12M20 28h8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
}

def make_art_card(art: dict) -> str:
    """記事カードHTMLを生成"""
    cat = art['category']
    c = CAT_CARD_STYLES.get(cat, CAT_CARD_STYLES['stress'])
    cat_label = CATEGORY_LABELS.get(cat, cat)
    icon = CAT_ICONS.get(cat, CAT_ICONS['stress']).format(circle=c['circle'], fill=c['fill'])
    date_disp = art['date'].replace('-', '.')
    desc = art['description'][:60] + ('…' if len(art['description']) > 60 else '')
    return f'''      <a href="{art['url']}" class="art-card">
        <div class="art-thumb" style="background:{c['bg']}">
          <svg width="52" height="52" viewBox="0 0 52 52" fill="none" aria-hidden="true">{icon}</svg>
          <div class="art-thumb-cat" style="background:{c['badge_bg']};color:{c['badge_color']}">{cat_label}</div>
        </div>
        <div class="art-body">
          <div class="art-title">{art['title']}</div>
          <div class="art-desc">{desc}</div>
          <div class="art-footer"><span class="art-date">{date_disp}</span><span class="art-link">読む <svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8M7 3l3 3-3 3"/></svg></span></div>
        </div>
      </a>'''


def build_top(articles: list):
    """TOPページ（index.html）を記事データから自動生成"""
    # 人気記事：固定3本（最初期から読まれている代表記事）
    popular_slugs = ["nemurenai-asa", "moeyuki-selfcheck", "yameru-yuuki"]
    popular = [a for slug in popular_slugs for a in articles if a['slug'] == slug]

    # 新着記事：日付順で最新3本（人気記事と被らないもの）
    popular_set = {a['slug'] for a in popular}
    recent = [a for a in articles if a['slug'] not in popular_set][:3]

    popular_html = '\n'.join(make_art_card(a) for a in popular)
    recent_html = '\n'.join(make_art_card(a) for a in recent)

    # TOPページHTMLを読み込んで該当セクションを置き換え
    top_src = OUTPUT_DIR / "index.html"
    if not top_src.exists():
        print("  警告: public/index.html が見つかりません。スキップします。")
        return

    html = top_src.read_text(encoding="utf-8")

    # 人気記事セクションを置き換え
    import re
    html = re.sub(
        r'(<!-- 人気記事 -->.*?<div class="art-grid">)\s*.*?(\s*</div>\s*<div class="sec-more">)',
        lambda m: m.group(1) + '\n' + popular_html + '\n    ' + m.group(2).lstrip(),
        html, flags=re.DOTALL
    )

    # 新着記事セクションを置き換え
    html = re.sub(
        r'(<!-- 新着記事 -->.*?<div class="art-grid">)\s*.*?(\s*</div>\s*<div class="sec-more">)',
        lambda m: m.group(1) + '\n' + recent_html + '\n    ' + m.group(2).lstrip(),
        html, flags=re.DOTALL
    )

    top_src.write_text(html, encoding="utf-8")
    print(f"  TOPページ: {top_src}")
    print(f"    人気記事: {[a['slug'] for a in popular]}")
    print(f"    新着記事: {[a['slug'] for a in recent]}")

def parse_markdown(filepath: Path) -> dict:
    """Markdownファイルをパースしてフロントマターと本文を返す"""
    text = filepath.read_text(encoding="utf-8")

    if not text.startswith("---"):
        print(f"  警告: フロントマターが見つかりません: {filepath}")
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"  警告: フロントマターが不正です: {filepath}")
        return None

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        print(f"  エラー: YAML解析失敗 {filepath}: {e}")
        return None

    body_md = parts[2].strip()
    md = markdown.Markdown(extensions=["extra", "toc"])
    body_html = md.convert(body_md)

    # ① 本文中の重複リンク・誘導文を除去
    import re as _re

    # ストレスチェックへのリンクを含む段落を全パターン除去
    body_html = _re.sub(
        r'<p[^>]*>(?:(?!<p).)*?/stress-check/(?:(?!<p).)*?</p>\s*',
        '', body_html, flags=_re.DOTALL
    )
    # 「今の状態が〜」「最近ストレスや〜」「眠れない日が〜」等の誘導段落を除去
    body_html = _re.sub(
        r'<p[^>]*>(?:今の状態が|最近ストレスや疲れが|眠れない日が続いて)[^<]{0,300}</p>\s*',
        '', body_html, flags=_re.DOTALL
    )

    # ② 「あわせて読みたい」セクションをカード型タイルに変換
    def convert_also_read(html):
        pattern = _re.compile(
            r'<h2[^>]*>あわせて読みたい</h2>\s*<ul>(.*?)</ul>',
            _re.DOTALL
        )
        cat_labels = {
            'stress': '症状・ストレス',
            'burnout': '燃え尽き・休職',
            'work': '労働問題',
            'quit': '転職・退職',
        }
        def make_cards(m):
            items_html = m.group(1)
            links = _re.findall(r'<a href="([^"]+)">([^<]+)</a>', items_html)
            cards = ''
            for url, title in links:
                # URLからカテゴリを推定
                cat_key = 'stress'
                for k in cat_labels:
                    if f'/{k}/' in url:
                        cat_key = k
                        break
                cat_label = cat_labels[cat_key]
                cards += (
                    f'<a href="{url}" class="also-read-card">'
                    f'<span class="also-read-cat">{cat_label}</span>'
                    f'<span class="also-read-text">{title}</span>'
                    f'<span class="also-read-arrow">→ 読む</span>'
                    f'</a>'
                )
            return (
                '<div class="also-read-section">'
                '<div class="also-read-title"><span class="also-read-bar"></span>あわせて読みたい</div>'
                f'<div class="also-read-grid">{cards}</div>'
                '</div>'
            )
        return pattern.sub(make_cards, html)
    body_html = convert_also_read(body_html)

    category = meta.get("category", filepath.parent.name)
    slug = meta.get("slug", filepath.stem)

    # 読了時間の計算（HTMLタグ・script・styleを除外した実質テキストで計算）
    import re as _re2
    clean_md = _re2.sub(r'<style[^>]*>.*?</style>', '', body_md, flags=_re2.DOTALL)
    clean_md = _re2.sub(r'<script[^>]*>.*?</script>', '', clean_md, flags=_re2.DOTALL)
    clean_md = _re2.sub(r'<[^>]+>', '', clean_md)
    char_count = len(clean_md)
    read_time = min(10, max(1, round(char_count / 500)))

    from urllib.parse import quote
    ogp_image = f"{OGP_WORKER_URL}/?title={quote(meta.get('title', ''))}&category={category}&slug={slug}"

    return {
        "title":        meta.get("title", ""),
        "description":  meta.get("description", ""),
        "slug":         slug,
        "category":     category,
        "category_label": CATEGORY_LABELS.get(category, category),
        "tags":         meta.get("tags", []),
        "date":         str(meta.get("date", "")),
        "updated":      str(meta.get("updated", meta.get("date", ""))),
        "draft":        meta.get("draft", False),
        "eyecatch":     meta.get("eyecatch", ""),
        "canonical":    meta.get("canonical", f"{BASE_URL}/articles/{category}/{slug}/"),
        "url":          f"/articles/{category}/{slug}/",
        "full_url":     f"{BASE_URL}/articles/{category}/{slug}/",
        "content":      body_html,
        "read_time":    read_time,
        "ogp_image":    ogp_image,
    }


def collect_articles() -> list:
    """content/ 以下の全Markdownを収集（draft除外）"""
    articles = []
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        art = parse_markdown(md_file)
        if art is None:
            continue
        if art["draft"]:
            print(f"  スキップ（draft）: {md_file}")
            continue
        articles.append(art)

    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles


def get_related(article: dict, all_articles: list, max_count: int = 3) -> list:
    """同じカテゴリの関連記事を返す（自身を除く）"""
    related = [
        a for a in all_articles
        if a["slug"] != article["slug"] and a["category"] == article["category"]
    ]
    if len(related) < max_count:
        others = [
            a for a in all_articles
            if a["slug"] != article["slug"] and a["category"] != article["category"]
        ]
        related += others
    return related[:max_count]


def write_file(path: Path, content: str):
    """ファイルを書き出す（ディレクトリ自動作成）"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ===== 生成処理 =====

def build_articles(env: Environment, articles: list):
    """記事HTMLを生成"""
    import json
    tpl = env.get_template("article.html")
    # 全記事の軽量JSONを作成（タイトル・URL・カテゴリのみ）
    all_articles_json = json.dumps([
        {"slug": a["slug"], "title": a["title"], "url": a["url"], "category": a["category"]}
        for a in articles
    ], ensure_ascii=False)
    for art in articles:
        related = get_related(art, articles)
        html = tpl.render(**art, related_articles=related, all_articles_json=all_articles_json)
        out = OUTPUT_DIR / "articles" / art["category"] / art["slug"] / "index.html"
        write_file(out, html)
        print(f"  記事: {out}")


def build_article_list(env: Environment, articles: list):
    """記事一覧ページをページネーション付きで生成"""
    PER_PAGE = 10
    tpl = env.get_template("article-list.html")
    cats = [
        {"slug": slug, "label": label}
        for slug, label in CATEGORY_LABELS.items()
    ]
    total = len(articles)
    total_pages = max(1, -(-total // PER_PAGE))  # 切り上げ

    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * PER_PAGE
        end = start + PER_PAGE
        page_articles = articles[start:end]

        # 表示するページ番号リスト（前後2ページ）
        pages = sorted(set(
            [1, total_pages] +
            [p for p in range(page_num - 2, page_num + 3) if 1 <= p <= total_pages]
        ))

        pagination = {
            "current": page_num,
            "total": total_pages,
            "pages": pages,
            "base_url": "/articles/",
            "has_prev": page_num > 1,
            "has_next": page_num < total_pages,
            "prev_url": "/articles/" if page_num == 2 else f"/articles/page/{page_num - 1}/",
            "next_url": f"/articles/page/{page_num + 1}/",
        }

        html = tpl.render(articles=page_articles, categories=cats, pagination=pagination)

        if page_num == 1:
            out = OUTPUT_DIR / "articles" / "index.html"
        else:
            out = OUTPUT_DIR / "articles" / "page" / str(page_num) / "index.html"

        write_file(out, html)
        print(f"  記事一覧 p{page_num}: {out}")


# カテゴリーごとのおすすめ記事（固定表示・スラッグで指定）
CATEGORY_FEATURED = {
    "stress": [
        "nemurenai-asa",
        "shigoto-genkai-sign",
        "shigoto-utsu",
    ],
    "burnout": [
        "moeyuki-selfcheck",
        "kyushoku-amae",
        "burnout-symptoms",
    ],
    "work": [
        "service-zangyo",
        "service-zangyo-atarimae",
        "service-zangyo-voluntary",
    ],
    "quit": [
        "yameru-yuuki",
        "black-kigyo-shindan",
        "taisyoku-daikou-moumuri",
    ],
}


def build_category_pages(env: Environment, articles: list):
    """カテゴリ別一覧ページを生成"""
    tpl = env.get_template("article-list.html")
    cats = [
        {"slug": slug, "label": label}
        for slug, label in CATEGORY_LABELS.items()
    ]
    for cat_slug, cat_label in CATEGORY_LABELS.items():
        cat_articles = [a for a in articles if a["category"] == cat_slug]
        if not cat_articles:
            continue
        cat_desc = CATEGORY_DESCS.get(cat_slug, {})
        featured_slugs = CATEGORY_FEATURED.get(cat_slug, [])
        featured_articles = [a for slug in featured_slugs for a in articles if a["slug"] == slug]
        html = tpl.render(articles=cat_articles, categories=cats, cat_desc=cat_desc, current_cat=cat_slug, featured_articles=featured_articles)
        out = OUTPUT_DIR / "articles" / cat_slug / "index.html"
        write_file(out, html)
        print(f"  カテゴリ: {out}")


def build_sitemap(articles: list):
    """sitemap.xmlを生成"""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    def entry(url, lastmod=None, priority="0.8"):
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    today = datetime.now().strftime("%Y-%m-%d")
    entry(f"{BASE_URL}/", today, "1.0")
    entry(f"{BASE_URL}/articles/", today, "0.9")

    for cat_slug in CATEGORY_LABELS:
        entry(f"{BASE_URL}/articles/{cat_slug}/", today, "0.8")

    for art in articles:
        entry(art["full_url"], art["updated"] or art["date"], "0.7")

    lines.append("</urlset>")
    out = OUTPUT_DIR / "sitemap.xml"
    write_file(out, "\n".join(lines))
    print(f"  sitemap.xml: {out}")


def build_rss(articles: list):
    """RSS (feed.xml) を生成"""
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">')
    lines.append("  <channel>")
    lines.append("    <title>Worelu — 仕事で壊れる前に。</title>")
    lines.append(f"    <link>{BASE_URL}</link>")
    lines.append("    <description>仕事のストレス・燃え尽き・転職に関する記事</description>")
    lines.append("    <language>ja</language>")
    lines.append(f"    <lastBuildDate>{now}</lastBuildDate>")
    lines.append(f'    <atom:link href="{BASE_URL}/feed.xml" rel="self" type="application/rss+xml"/>')

    for art in articles[:20]:
        lines.append("    <item>")
        lines.append(f"      <title><![CDATA[{art['title']}]]></title>")
        lines.append(f"      <link>{art['full_url']}</link>")
        lines.append(f"      <guid>{art['full_url']}</guid>")
        lines.append(f"      <description><![CDATA[{art['description']}]]></description>")
        lines.append(f"      <pubDate>{art['date']}</pubDate>")
        lines.append("    </item>")

    lines.append("  </channel>")
    lines.append("</rss>")
    out = OUTPUT_DIR / "feed.xml"
    write_file(out, "\n".join(lines))
    print(f"  feed.xml: {out}")


def build_shindan_pages():
    """ブラック企業診断レベル別OGPページを生成"""
    levels = [
        {
            "level": 1,
            "title": "LEVEL1 正常な感覚の持ち主｜ブラック企業あるある診断",
            "desc": "ブラック企業とは無縁の職場にいるようです。ブラック企業度：低",
            "image": "/images/shindan/black_lv001.png",
        },
        {
            "level": 2,
            "title": "LEVEL2 感覚が麻痺し始めています｜ブラック企業あるある診断",
            "desc": "「これくらい普通かな」と思い始めていたら要注意。ブラック企業度：注意",
            "image": "/images/shindan/black_lv002.png",
        },
        {
            "level": 3,
            "title": "LEVEL3 その当たり前、本当に普通ですか？｜ブラック企業あるある診断",
            "desc": "感覚がかなり麻痺している可能性があります。ブラック企業度：高",
            "image": "/images/shindan/black_lv003.png",
        },
        {
            "level": 4,
            "title": "LEVEL4 あなたの感覚はかなり麻痺しています｜ブラック企業あるある診断",
            "desc": "ここまで多いと心身への影響が出ている可能性があります。ブラック企業度：危険",
            "image": "/images/shindan/black_lv004.png",
        },
    ]

    for lv in levels:
        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lv['title']}</title>
<meta name="description" content="{lv['desc']}">
<meta name="robots" content="noindex,follow">
<meta property="og:title" content="{lv['title']}">
<meta property="og:description" content="{lv['desc']}">
<meta property="og:image" content="https://worelu.com{lv['image']}">
<meta property="og:url" content="https://worelu.com/shindan/black/level{lv['level']}/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{lv['title']}">
<meta name="twitter:description" content="{lv['desc']}">
<meta name="twitter:image" content="https://worelu.com{lv['image']}">
<link rel="canonical" href="https://worelu.com/articles/quit/black-kigyo-aruaru/">
<meta http-equiv="refresh" content="0;url=/articles/quit/black-kigyo-aruaru/">
</head>
<body>
<p>リダイレクト中... <a href="/articles/quit/black-kigyo-aruaru/">こちら</a>をクリックしてください。</p>
</body>
</html>"""
        out = OUTPUT_DIR / "shindan" / "black" / f"level{lv['level']}" / "index.html"
        write_file(out, html)
        print(f"  診断ページ level{lv['level']}: {out}")


def build_robots():
    """robots.txtを生成"""
    content = f"""User-agent: *
Allow: /
Disallow: /drafts/

Sitemap: {BASE_URL}/sitemap.xml
"""
    out = OUTPUT_DIR / "robots.txt"
    write_file(out, content)
    print(f"  robots.txt: {out}")


# ===== エントリーポイント =====

def main():
    print("=== Worelu ビルド開始 ===\n")

    if not CONTENT_DIR.exists():
        print("エラー: content/ ディレクトリが見つかりません")
        sys.exit(1)

    if not TEMPLATE_DIR.exists():
        print("エラー: templates/ ディレクトリが見つかりません")
        sys.exit(1)

    # テンプレートエンジン初期化
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))

    # 記事収集
    print("記事を収集中...")
    articles = collect_articles()
    print(f"  {len(articles)}本の記事を発見\n")

    if not articles:
        print("警告: 記事が1本もありません")

    # 各種ファイル生成
    print("記事HTMLを生成中...")
    build_articles(env, articles)

    print("\n記事一覧を生成中...")
    build_article_list(env, articles)

    print("\nカテゴリページを生成中...")
    build_category_pages(env, articles)

    print("\nsitemap.xmlを生成中...")
    build_sitemap(articles)

    print("\nRSSを生成中...")
    build_rss(articles)

    print("\n診断OGPページを生成中...")
    build_shindan_pages()

    print("\nrobots.txtを生成中...")
    build_robots()

    print("\nTOPページを更新中...")
    build_top(articles)

    print(f"\n=== ビルド完了: {len(articles)}本の記事を生成しました ===")
    print(f"出力先: {OUTPUT_DIR.resolve()}/")


if __name__ == "__main__":
    main()

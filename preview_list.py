#!/usr/bin/env python3
"""
記事一覧テンプレートのプレビュー用ビルド
build.py の全記事ビルドは走らせず、記事一覧・カテゴリページだけ再生成する。
実行: python3 preview_list.py
"""
import os, re, sys, yaml, markdown
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

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
    "stress":  {"desc": "仕事のストレスは、眠れない、動悸、吐き気など様々な心身の不調として現れます。このカテゴリでは症状・限界サイン・対処法を解説します。", "lead": "気になる症状から記事を探してください。"},
    "burnout": {"desc": "燃え尽き症候群（バーンアウト）の症状・休職の判断・回復方法について解説しています。", "lead": "今の自分の状態を確認することから始めましょう。"},
    "work":    {"desc": "残業代・有給・パワハラなど、労働基準法に関わる問題の対処法を解説します。", "lead": "「これっておかしいのかな？」と感じたらまず確認してみてください。"},
    "quit":    {"desc": "転職・退職に関する情報をまとめています。次の一歩を安心して踏み出すための情報を分かりやすく解説しています。", "lead": "状況に近い悩みの記事からご覧ください。"},
}

CATEGORY_FEATURED = {
    "stress":  ["nemurenai-asa", "shigoto-genkai-sign", "shigoto-utsu"],
    "burnout": ["moeyuki-selfcheck", "kyushoku-amae", "burnout-symptoms"],
    "work":    ["service-zangyo", "service-zangyo-atarimae", "service-zangyo-voluntary"],
    "quit":    ["yameru-yuuki", "black-kigyo-shindan", "taisyoku-daikou-moumuri"],
}

def load_articles():
    arts = []
    for cat in CATEGORY_LABELS:
        d = CONTENT_DIR / cat
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md"), reverse=True):
            text = f.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            parts = text.split("---", 2)
            if len(parts) < 3:
                continue
            try:
                meta = yaml.safe_load(parts[1])
            except Exception:
                continue
            if not meta or not meta.get("title"):
                continue
            date_val = meta.get("date", "")
            if hasattr(date_val, "strftime"):
                date_str = date_val.strftime("%Y.%m.%d")
                sort_key = date_val.strftime("%Y-%m-%d")
            else:
                date_str = str(date_val).replace("-", ".")
                sort_key = str(date_val)
            wc = len(parts[2])
            read_time = max(1, round(wc / 600))
            arts.append({
                "slug": f.stem,
                "category": cat,
                "category_label": CATEGORY_LABELS[cat],
                "title": meta.get("title", ""),
                "description": meta.get("description", ""),
                "date": date_str,
                "sort_key": sort_key,
                "read_time": read_time,
                "url": f"/articles/{cat}/{f.stem}/",
            })
    arts.sort(key=lambda a: a["sort_key"], reverse=True)
    return arts

def write_file(path: Path, html: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"  → {path}")

def build_list(env, articles):
    PER_PAGE = 10
    tpl = env.get_template("article-list.html")
    total = len(articles)
    total_pages = max(1, -(-total // PER_PAGE))
    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * PER_PAGE
        page_articles = articles[start:start + PER_PAGE]
        pages = list(range(1, total_pages + 1))
        pagination = {
            "current": page_num, "total": total_pages, "pages": pages,
            "base_url": "/articles/",
            "has_prev": page_num > 1, "has_next": page_num < total_pages,
            "prev_url": "/articles/" if page_num == 2 else f"/articles/page/{page_num-1}/",
            "next_url": f"/articles/page/{page_num+1}/",
        }
        html = tpl.render(articles=page_articles, pagination=pagination)
        out = OUTPUT_DIR / "articles" / "index.html" if page_num == 1 else OUTPUT_DIR / "articles" / "page" / str(page_num) / "index.html"
        write_file(out, html)

def build_categories(env, articles):
    PER_PAGE = 10
    tpl = env.get_template("article-list.html")
    for cat_slug in CATEGORY_LABELS:
        cat_arts = [a for a in articles if a["category"] == cat_slug]
        if not cat_arts:
            continue
        cat_desc = CATEGORY_DESCS.get(cat_slug, {})
        featured_slugs = CATEGORY_FEATURED.get(cat_slug, [])
        featured_articles = [a for slug in featured_slugs for a in articles if a["slug"] == slug]
        total = len(cat_arts)
        total_pages = max(1, -(-total // PER_PAGE))
        base_url = f"/articles/{cat_slug}/"
        for page_num in range(1, total_pages + 1):
            start = (page_num - 1) * PER_PAGE
            page_articles = cat_arts[start:start + PER_PAGE]
            pages = sorted(set([1, total_pages] + list(range(max(1, page_num-2), min(total_pages, page_num+2)+1))))
            pagination = {
                "current": page_num, "total": total_pages, "pages": pages,
                "base_url": base_url,
                "has_prev": page_num > 1, "has_next": page_num < total_pages,
                "prev_url": base_url if page_num == 2 else f"{base_url}page/{page_num-1}/",
                "next_url": f"{base_url}page/{page_num+1}/",
            }
            html = tpl.render(
                articles=page_articles, cat_desc=cat_desc,
                current_cat=cat_slug, featured_articles=featured_articles,
                pagination=pagination,
            )
            out = OUTPUT_DIR / "articles" / cat_slug / "index.html" if page_num == 1 else OUTPUT_DIR / "articles" / cat_slug / "page" / str(page_num) / "index.html"
            write_file(out, html)

if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    print("記事を読み込み中...")
    articles = load_articles()
    print(f"  {len(articles)} 記事")
    print("記事一覧ページをビルド中...")
    build_list(env, articles)
    build_categories(env, articles)
    print("完了。ブラウザで確認: open public/articles/index.html")

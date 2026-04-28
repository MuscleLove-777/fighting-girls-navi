"""fighting-girls-blog (fighting-girls-navi) 自動記事生成エントリ"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, r"C:\Users\atsus\000_ClaudeCode\007_自動投稿ブログ")
import fitness_auto_post_lib as lib  # noqa: E402

CLAUDE_MD = (HERE / "CLAUDE.md").read_text(encoding="utf-8") if (HERE / "CLAUDE.md").exists() else ""

CFG = {
    "site_dir": HERE,
    "blog_name": "ファイティングガールズ",
    "site_url": "https://musclelove-777.github.io/fighting-girls-navi",
    "twitter_site": "@MuscleGirlLove7",
    "accent_color": "#ff3d00",
    "categories": [
        "MMA選手紹介", "ボクシング", "キックボクシング", "総合格闘技大会レポート",
        "テクニック解説", "コラム",
    ],
    "seed_topics": CLAUDE_MD,
    "image_query": "fighting women mma",
}

if __name__ == "__main__":
    res = lib.run(CFG)
    print(res)

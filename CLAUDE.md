# 格闘女子ナビ - リモートエージェント用ガイド

## プロジェクト概要
「格闘女子ナビ」は、RIZIN・DEEP JEWELS・ONE Championship等で活躍する女子格闘家の最新情報を毎日自動更新するファンブログサイト。
GitHub Pages でホスティングし、スケジュールエージェントが毎日記事を自動生成・公開する。

## ブランド
- サイト名: 格闘女子ナビ
- 運営: MuscleLove
- X: @MuscleGirlLove7
- Patreon: https://www.patreon.com/MuscleLove

## 掲載対象（ロスター）
記事対象の選手リストは必ず `references/roster.md` を読んで参照すること。リストの追加・更新もそのファイルに対して行う。

## 記事生成ルール
1. **言語**: 日本語
2. **文字数**: 200〜400文字（本文のみ）
3. **トーン**: キャッチーでファン目線。熱量高め。選手への敬意を忘れずに
4. **内容**: 以下のいずれか
   - 選手の最新ニュース・試合結果
   - 選手の魅力・強さの分析
   - 女子格闘技界のトレンド
   - 試合プレビュー・展望
   - 団体（RIZIN, DEEP JEWELS, ONE等）の最新動向
5. **毎回3本生成**: 異なる選手・テーマで3本
6. **Web検索必須**: 最新情報を検索してから記事を書く
7. **ヒーロー画像**: 各記事にUnsplashの画像を1枚使用する
   - WebSearchで記事テーマに合うUnsplashの画像を探す（検索: "site:unsplash.com [テーマ英語]"）
   - URL形式: `https://images.unsplash.com/photo-XXXXX?w=800&h=400&fit=crop&q=80`
   - テーマ例: MMA → "MMA octagon cage", 打撃 → "boxing fight", トレーニング → "martial arts gym"
   - 必ず実在するUnsplash画像URLを確認してから使うこと
8. **広告カード**: 全記事とindex.htmlのフッター直前に MuscleLove広告カード（ML_PROMO_CARDマーカー）を必ず含める。広告カードにはX / Patreon / ゲームポータルの3導線を必ず入れる

## ファイル構成
```
/
├── index.html          # メインページ
├── CLAUDE.md           # このファイル（エージェント用ガイド）
├── sitemap.xml         # SEO用サイトマップ
├── robots.txt          # クローラー設定
└── articles/           # ブログ記事ディレクトリ
    ├── 2026-04-04-izawa-queen.html
    ├── 2026-04-04-rena-comeback.html
    ├── 2026-04-04-deep-jewels-rising.html
    └── ...（日付-スラッグ.html）
```

## 記事HTMLテンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>【記事タイトル】 | 格闘女子ナビ</title>
    <meta name="description" content="【記事の要約を50-80文字で】">
    <meta property="og:image" content="【Unsplash画像URL】">
    <style>
        :root {
            --bg-primary: #0d1117;
            --bg-card: #1c2333;
            --accent: #e63946;
            --text-primary: #e6edf3;
            --text-secondary: #8b949e;
            --border: #30363d;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans JP', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.8;
        }
        .article { max-width: 720px; margin: 0 auto; padding: 40px 20px; }
        .back { color: var(--accent); text-decoration: none; font-size: 0.9rem; }
        .back:hover { text-decoration: underline; }
        .date { color: var(--text-secondary); font-size: 0.85rem; margin: 20px 0 8px; }
        h1 { font-size: 1.6rem; line-height: 1.4; margin-bottom: 20px; }
        .hero-img {
            width: 100%;
            height: 250px;
            background-size: cover;
            background-position: center;
            border-radius: 8px;
            margin: 0 0 24px 0;
            position: relative;
        }
        .hero-img::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 80px;
            background: linear-gradient(transparent, var(--bg-primary));
        }
        .content { font-size: 1rem; color: var(--text-secondary); }
        .content p { margin-bottom: 16px; }
        .tags { margin-top: 24px; display: flex; gap: 8px; flex-wrap: wrap; }
        .tag { background: rgba(230,57,70,0.15); color: #ff6b7a; padding: 2px 12px; border-radius: 12px; font-size: 0.8rem; }
        footer { text-align: center; margin-top: 60px; padding: 20px; border-top: 1px solid var(--border); }
        footer a { color: var(--accent); text-decoration: none; }
    </style>
</head>
<body>
    <div class="article">
        <a href="../index.html" class="back">&larr; 格闘女子ナビに戻る</a>
        <div class="date">【YYYY-MM-DD】</div>
        <h1>【記事タイトル】</h1>
        <div class="hero-img" style="background-image: url('【Unsplash画像URL?w=800&h=400&fit=crop&q=80】')"></div>
        <div class="content">
            <p>【本文1段落目】</p>
            <p>【本文2段落目】</p>
        </div>
        <div class="tags">
            <span class="tag">【タグ1】</span>
            <span class="tag">【タグ2】</span>
        </div>
    </div>
    <!-- ML_PROMO_CARD_START -->
    <section style="max-width:800px;margin:32px auto;padding:0 20px;">
      <div style="background:#111827;border:1px solid rgba(255,255,255,0.14);border-radius:10px;padding:24px;text-align:center;">
        <p style="margin:0 0 6px;color:#f0f0f5;font-weight:800;">MuscleLove 公式</p>
        <p style="margin:0 0 14px;color:#9ca3af;font-size:0.9rem;">最新情報・限定コンテンツはこちら</p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;">
          <a href="https://x.com/MuscleGirlLove7" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#1d9bf0;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">X @MuscleGirlLove7</a>
          <a href="https://www.patreon.com/MuscleLove" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#ff424d;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">Patreon 限定コンテンツ</a>
          <a href="https://musclelove-games.vercel.app/?utm_source=blog&amp;utm_medium=promo_card&amp;utm_campaign=fighting-girls-blog" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#22c55e;color:#0b1220;border-radius:6px;font-weight:800;text-decoration:none;">🎮 無料ゲーム95本</a>
        </div>
      </div>
    </section>
    <!-- ML_PROMO_CARD_END -->
    <footer>
        <a href="../index.html">格闘女子ナビ</a> | <a href="https://x.com/MuscleGirlLove7">X @MuscleGirlLove7</a>
    </footer>
</body>
</html>
```

## index.html 更新方法

記事を追加したら、`index.html` の `<div class="blog-grid" id="blog-grid">` 内に以下の形式で記事カードを**先頭に**追加する。
最大6件を維持し、古い記事は削除する。

```html
<article class="blog-card">
    <div class="blog-thumb" style="background-image: url('【Unsplash画像URL?w=800&h=300&fit=crop&q=80】')"></div>
    <div class="blog-date">YYYY-MM-DD</div>
    <h3><a href="articles/YYYY-MM-DD-slug.html">記事タイトル</a></h3>
    <p>記事の要約（80-120文字）</p>
    <div class="blog-tags">
        <span class="tag">タグ1</span>
        <span class="tag">タグ2</span>
    </div>
</article>
```

## コミットメッセージ形式
```
[auto] Add daily articles YYYY-MM-DD
```

## 注意事項
- Instagramリンクは実在確認済みのアカウントのみ掲載すること
- 選手への誹謗中傷は絶対にNG。リスペクトを持って書くこと
- 試合結果は正確に。不確かな場合はWeb検索で確認すること
- 画像はUnsplashの無料ライセンス画像のみ使用（著作権フリー）
- 選手の写真は使用しない（肖像権の問題）
- 各記事で異なる画像を使い、バリエーションを出すこと

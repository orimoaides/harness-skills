# 日本語Webタイポグラフィ リファレンス

英語タイポグラフィのルールをそのまま日本語に適用すると破綻する。このリファレンスは日本語固有のルールを体系化したもの。

## 0. 設計思想 — ハーモニー・リズム・メロディ

タイポグラフィは音楽に似ている。恣意的な値の集合ではなく、数学的な法則に従った体系として設計する。

### ハーモニー（調和）= 文字サイズの比率

文字サイズをバラバラに決めない。モジュラースケール（調和数列）を使う。音楽の周波数比（オクターブ=2:1、完全五度=3:2、完全四度=4:3）がギターの弦の長さから導かれるように、文字サイズの比率にも自然な調和がある。

```
base = 1rem (16px)
ratio = 1.25 (Major Third)

scale: base/ratio², base/ratio, base, base×ratio, base×ratio², base×ratio³
  →    0.64rem,     0.8rem,   1rem, 1.25rem,     1.5625rem,   1.953rem
```

このスケールから外れた値（例: 17px、22px）は使わない。スケールに乗っている値だけで構成する。階層が明快になり、「なぜこのサイズなのか」に常に答えられる。

### リズム（律動）= 行送りと余白の規則性

行送り（line-height × font-size）をベースユニットとし、すべての余白をその倍数で統制する。これが Vertical Rhythm。

```scss
$base-font-size: 1rem;
$base-line-height: 1.8;
$rhythm-unit: $base-line-height * $base-font-size; // = 1.8rem

// すべての余白を rhythm-unit の倍数に
h2 { margin-top: $rhythm-unit * 2; margin-bottom: $rhythm-unit; }
p  { margin-bottom: $rhythm-unit; }
```

ページ全体のテキストが見えないグリッド線に揃う。見出し前の大きな余白も、段落間の小さな余白も、同じリズムの上に乗っている。この一貫性が「整っている」という印象を生む。

### メロディ（旋律）= コンテンツそのもの

タイポグラフィの仕事は、コンテンツ（言葉）を最も読みやすく届けること。フォント選び・サイズ・余白は伴奏であり、主役ではない。装飾的なタイポグラフィが目的化すると本末転倒になる。

### 余白の4つのパターン

余白に恣意性を入れない方法は複数ある。プロジェクトに合うものを選ぶ:

1. **フォントサイズベース**: `$spacing: 1rem` を基準に倍数で構成。最もシンプル
2. **Vertical Rhythm**: 行送りを基準単位とし、全余白をその倍数に。テキスト中心のサイトに最適
3. **Modular Scale**: タイプスケールと同じ比率で余白も段階化。`$spacing-small: $spacing / $ratio`。数学的に美しい
4. **8の倍数**: `$spacing: 8px` の倍数。Material Design準拠。チーム開発・ツール連携に強い

どれを選んでもよいが、**何も選ばないこと（場当たり的な値）が最悪**。一つの体系に乗せることで、デザインの判断が減り、一貫性が生まれる。

### 日本語における注意

- 英語のスケールは `65-75ch` や `line-height: 1.5` を前提にしている。日本語にそのまま当てはめると行長が長すぎ、行間が詰まりすぎる
- 日本語の全角文字は英語の小文字より字面が大きく、視覚的密度が高い。同じ数値でも印象が異なる
- **まず日本語本文の行送り（line-height × font-size）を決め、それを起点にスケール全体を組む**のが正しい順序

## 1. 行長（Measure）

英語は `65-75ch`（半角基準）が定番だが、日本語には当てはまらない。

- `ch` 単位は半角文字 "0" の幅基準。日本語全角文字はその約2倍
- `ch` で指定すると、フォント・ウェイト・環境で幅がばらつく
- **日本語本文の推奨行長: `max-width: 45em`**（全角約45文字相当）
- `em` はフォントサイズ連動なので、レスポンシブでも比率が崩れない

### 行長の目安

| 用途 | 行長 | 根拠 |
|---|---|---|
| 本文（長文） | 35-45em | 一行40文字前後が日本語の可読性研究で最適とされる |
| カード・サマリ | 制限なし | レイアウトのコンテナ幅に従う |
| キャプション | 制限なし | 短文は行長制限不要 |

### 適用範囲 — 重要

行長制限（`max-width: 45em`）は**長文コンテンツ**にのみ適用する:

- ✅ 記事本文、ブログ、ドキュメント、利用規約 — 数段落以上のテキストが続くもの
- ✅ 導入事例の引用文 — 読み物として長い
- ❌ LPのヒーローテキスト、カード内テキスト — 短文であり、レイアウトが優先
- ❌ UIコンポーネント（ボタン、ラベル、リスト項目） — コンテナの幅に従う
- ❌ 料金プラン、機能グリッド — カードのレイアウト構造が優先

行長制限をレイアウトコンポーネントに適用すると、カード内のテキストが折り返しすぎてレイアウトが壊れる。短文やUI要素は、親コンテナの幅に自然に従わせるのが正しい。

### 実装

```css
/* 長文コンテンツにのみ適用 */
.article-body,
.prose {
  max-width: 45em; /* Tailwind: max-w-[45em] */
}

/* LP・アプリUIには適用しない */
```

`max-width` で指定し、`width` は `100%` のまま。狭い画面では自然に縮む。

## 2. 行間（Line Height）

日本語は英語より行間を広く取る必要がある。理由:

- 全角文字は字面が大きく、行間が狭いと文字が密着して見える
- 漢字・ひらがな・カタカナの混在で視覚的密度が高い
- 英語の小文字は x-height が小さく、行間が自然に生まれる

### 推奨値

| 要素 | line-height | 備考 |
|---|---|---|
| 本文 | 1.8-2.0 | 英語の 1.5-1.6 より広め |
| 見出し（大） | 1.2-1.4 | 大きい文字は狭めでよい |
| 見出し（中） | 1.4-1.6 | |
| キャプション | 1.6-1.8 | 小さい文字は広めに |
| UI要素（ボタン等） | 1.0-1.4 | 一行なので狭くてよい |

### ダークモードでの補正

暗い背景に明るい文字は、同じサイズでも軽く・細く見える。行間を +0.1 程度広げると可読性が上がる。

## 3. 和欧混植（Mixed Script）

日本語テキストに英数字やアルファベットが混在するケース。処理を怠ると読みにくくなる。

### スペーシング

日本語と英数字の間にはわずかな空白（四分アキ = 0.25em 程度）があると読みやすい。

- **CSS**: `text-spacing-trim` + `text-autospace`（CSS Text Level 4）がブラウザ対応すれば最適解
- **現実解**: フォント側の OpenType feature `chws`（Contextual Half-width Spacing）を有効にする

```css
body {
  font-feature-settings: "chws" 1, "vchw" 1;
}
```

### フォントサイズの調整

英語フォントと日本語フォントを組み合わせる場合、x-height の違いで英語が小さく見えることがある。`size-adjust` で微調整:

```css
@font-face {
  font-family: 'EnglishFont';
  src: url(...);
  size-adjust: 105%; /* 日本語フォントに合わせて微調整 */
}
```

### ベースライン

日本語フォントは仮想ボディの中央寄りにデザインされている。英語フォントのベースライン基準とズレることがある。`font-family` の指定順で日本語フォントを後に置くと、英語フォント優先でベースラインが安定する:

```css
font-family: "Inter", "Noto Sans JP", sans-serif;
```

## 4. 約物（Punctuation）

日本語の句読点・括弧は全角幅を持つため、連続すると間延びする。

### 約物の詰め（ツメ）

```css
body {
  font-feature-settings: "palt" 1; /* プロポーショナルメトリクス */
}
```

- `palt`: 約物や仮名の字幅をプロポーショナルに調整
- `halt`: 約物のみ半角幅に詰める（より控えめ）

### 使い分け

| feature | 効果 | 使いどころ |
|---|---|---|
| `palt` | 約物+仮名をプロポーショナル化 | 見出し、短いテキスト |
| `halt` | 約物のみ半角化 | 本文（仮名幅は変えたくない場合） |
| なし | 全角等幅のまま | 縦書き、フォーマルな組版 |

**注意**: `palt` を本文に適用すると、仮名の字幅が変わりリフローが起きる。本文には `halt` か未適用が安全。

## 5. フォント選定

### 日本語Webフォントの現実

- 日本語フォントは文字数が多くファイルサイズが大きい（数MB〜数十MB）
- Google Fonts はサブセット配信で実用的（Noto Sans JP 等）
- 有料フォントは TypeSquare、FONTPLUS、Adobe Fonts が主要サービス
- システムフォント（ヒラギノ、游ゴシック、Noto Sans CJK）でも十分なケースは多い

### ゴシック体 vs 明朝体

| | ゴシック体 | 明朝体 |
|---|---|---|
| 用途 | UI、見出し、短文 | 長文、記事、書籍的 |
| 可読性 | 画面上で高い | 小サイズで潰れやすい |
| 印象 | モダン、カジュアル | フォーマル、知的、文学的 |

### 人気のある日本語Webフォント

**ゴシック体（sans-serif）**:
- **Noto Sans JP**: Google Fonts。ニュートラル。迷ったらこれ。ウェイト豊富
- **BIZ UDPGothic**: ユニバーサルデザイン。可読性が高い。Google Fonts
- **M PLUS 1p / 2p**: 丸みがありソフトな印象。Google Fonts
- **IBM Plex Sans JP**: テック感があり、IBM Plexファミリーと統一可能

**明朝体（serif）**:
- **Noto Serif JP**: Google Fonts。ニュートラルな明朝
- **Shippori Mincho**: 少しクラシカルで上品。Google Fonts
- **BIZ UDPMincho**: UD明朝。可読性重視。Google Fonts

**ディスプレイ・特殊**:
- **Zen Kaku Gothic New**: ややモダンなゴシック
- **Zen Maru Gothic**: 丸ゴシック。親しみやすい
- **Sawarabi Mincho / Gothic**: 軽量

### フォントペアリングの型

1. **ゴシック見出し × ゴシック本文**: 統一感。ウェイト差で階層を作る
2. **明朝見出し × ゴシック本文**: コントラスト。メディア・マガジン系に
3. **ディスプレイ見出し × ゴシック本文**: 個性的。ブランド感
4. **英語ディスプレイ × 日本語ゴシック**: 洗練された印象

### システムフォントスタック

Webフォントを使わない場合:

```css
font-family:
  "Hiragino Kaku Gothic ProN",  /* macOS */
  "Hiragino Sans",               /* macOS (新) */
  "Noto Sans CJK JP",           /* Linux */
  "Yu Gothic Medium",            /* Windows */
  "Yu Gothic",                   /* Windows fallback */
  "Meiryo",                     /* Windows 旧 */
  sans-serif;
```

**游ゴシックの注意**: Windows の游ゴシック Regular (400) は細すぎて可読性が低い。`font-weight: 500`（Medium）以上を指定するか、`"Yu Gothic Medium"` を先に書く。

## 6. 文字サイズ

### 最小サイズ

- **本文**: 16px (1rem) 以上が基本。日本語は画数が多く、小さいと潰れる。saas / dashboard プロファイルでは 14px まで許容するが、コントラスト比に注意
- **キャプション・補足**: 13-14px まで。12px 未満は避ける
- **法的テキスト等**: 12px 最小。それ未満は読めない

### rem vs px

`rem` を使う。ユーザーのブラウザ設定（デフォルトフォントサイズ）を尊重するため。

```css
html { font-size: 100%; } /* = 16px */
body { font-size: 1rem; }
h1 { font-size: 2rem; }   /* 32px */
```

### タイプスケール

文字サイズは場当たり的に決めない。モジュラースケール（セクション0「ハーモニー」参照）を使い、一つの比率から全サイズを導出する。

日本語では英語より控えめなスケール比が合いやすい。漢字の画数が多いため、サイズ差が小さくても視認性の違いが出る。

| 比率 | 音楽的対応 | 印象 | 適するUI |
|---|---|---|---|
| 1.2 | Minor Third | 控えめ、落ち着き | 管理画面、ダッシュボード |
| 1.25 | Major Third | バランス良い | SaaS、メディア |
| 1.333 | Perfect Fourth | やや大胆 | LP、マーケティング |
| 1.5 | Perfect Fifth | ダイナミック | ヒーロー、ポートフォリオ |

#### スケールの実装例（ratio = 1.25）

```css
:root {
  --text-xs:    0.64rem;   /* 10.24px — base ÷ ratio³ */
  --text-sm:    0.8rem;    /* 12.8px  — base ÷ ratio² */
  --text-base:  1rem;      /* 16px    — base */
  --text-lg:    1.25rem;   /* 20px    — base × ratio */
  --text-xl:    1.5625rem; /* 25px    — base × ratio² */
  --text-2xl:   1.953rem;  /* 31.25px — base × ratio³ */
  --text-3xl:   2.441rem;  /* 39.06px — base × ratio⁴ */
}
```

スケールの外にある値（17px, 22px 等）は使わない。5段階あれば大半のUIは組める。段階を増やしたくなったら、比率を下げるか見直す。

#### アプリUI vs マーケティングページ

- **アプリUI / ダッシュボード**: 固定 `rem` スケール。空間の予測可能性がUIの使いやすさに直結する
- **マーケティング / コンテンツ**: 見出しに `clamp()` で流体サイズを使ってもよい。ただし本文は固定

## 7. ウェイト（太さ）

### 日本語フォントのウェイト感

日本語フォントは画数が多い分、同じウェイト値でも英語フォントより太く・重く見える。

- Regular (400): 日本語では十分な存在感がある
- Medium (500): 見出しに使える太さ
- Bold (700): 日本語ではかなり強い。多用すると重たくなる

### 推奨ウェイト構成

- 本文: Regular (400)
- ラベル・強調: Medium (500)
- 見出し: Medium (500) or SemiBold (600)
- 最大見出し: Bold (700)

**注意**: 日本語フォントの Bold は英語の Bold より視覚的インパクトが大きい。英語サイトの感覚で Bold を多用すると「くどい」印象になる。

## 8. letter-spacing（字間）

### 日本語の字間

日本語のデフォルト字間（0）はほとんどのケースで適切。

- **本文**: `letter-spacing: 0` or `0.02em`（ごくわずかに開ける程度）
- **見出し**: `0` or `-0.02em`（大きい文字は詰め気味が締まる）
- **英数字混在**: フォントの `chws` feature に任せるのがベスト

**やってはいけないこと**:
- 日本語本文に `letter-spacing: 0.1em` 以上 → 間延びして読みにくい
- 日本語で英語のように大きく tracking を開ける → 一文字ずつバラバラに見える

## 9. 禁則処理

ブラウザのデフォルト禁則処理を有効にする:

```css
body {
  word-break: normal;          /* デフォルトでOK */
  overflow-wrap: anywhere;     /* 長い英単語・URLの折り返し */
  line-break: strict;          /* 厳密な禁則処理 */
}
```

### 禁則のルール

- **行頭禁則**: 句読点（。、）、閉じ括弧（）」』）は行頭に来てはいけない
- **行末禁則**: 開き括弧（（「『）は行末に来てはいけない
- `line-break: strict` でブラウザが処理してくれる

## 10. Webフォントの読み込み

### パフォーマンス戦略

日本語フォントはファイルサイズが大きいため、読み込み戦略が重要。

```css
@font-face {
  font-family: "Noto Sans JP";
  font-display: swap;     /* テキストを先に表示 */
  unicode-range: U+3000-9FFF, U+F900-FAFF; /* CJK範囲のみ */
}
```

### Google Fonts の場合

Google Fonts は自動でサブセット化・最適化してくれるので、`<link>` タグで読み込むのが最もシンプル。`&display=swap` を付ける:

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
```

Next.js では `next/font/google` を使う:

```tsx
import { Noto_Sans_JP } from "next/font/google";
const notoSansJP = Noto_Sans_JP({
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  display: "swap",
});
```

### 読み込むウェイトを絞る

日本語フォントは1ウェイトあたり数百KB〜数MB。必要なウェイトだけ読み込む。3ウェイト以内が理想。

## 11. プロファイル別推奨値

日本語UIは一枚岩ではない。記事メディアと業務UIでは、正解の密度が違う。技術文書とダッシュボードでは、見出しの役割も表の扱いも違う。用途に応じたプロファイルで評価する。

### プロファイル一覧

**media** — 長文読解向け。本文の呼吸を優先し、行間を広めに取る。note、ブログ、オウンドメディア、インタビュー記事、長文読み物。

**saas** — 業務UI向け。可読性を落とさず、密度と安定性を優先する。管理画面、設定画面、社内業務ツール、B2B SaaS。

**docs** — 技術文書向け。本文、コード、見出し、表、注釈の切り分けを重視する。開発者向け文書、ナレッジベース、ヘルプセンター。

**dashboard** — 高密度情報向け。表、数値、ラベル、カードの詰まりすぎを避けつつ、視線移動を短く保つ。BI画面、KPI画面、運用監視画面。

### 推奨値テーブル

| 項目 | media | saas | docs | dashboard |
|------|-------|------|------|-----------|
| 本文 font-size | 18px (1.125rem) | 14px (0.875rem) | 16px (1rem) | 14px (0.875rem) |
| 本文 line-height | 1.8-2.0 | 1.5-1.65 | 1.7-1.8 | 1.4-1.55 |
| 本文 letter-spacing | normal-0.02em | 0 | normal | 0 |
| 見出し line-height | 1.25-1.4 | 1.3-1.45 | 1.35-1.45 | 1.2-1.35 |
| 見出し font-weight | 700 | 500-600 | 500-600 | 500-600 |
| 行長（本文） | 38-44em | — | 40-45em | — |
| スケール比 | 1.25-1.333 | 1.2 | 1.25 | 1.2 |
| 密度方針 | airy | compact | balanced | compact |
| キャプション font-size | 14px | 12px | 13px | 12px |
| キャプション line-height | 1.7 | 1.45 | 1.6 | 1.4 |

### プロファイルの選び方

- 対象サイトの主要な用途で判定する。複数の性格を持つ場合は主要な画面の用途で選ぶ
- 行長制限（`max-width`）は media と docs にのみ適用。saas と dashboard はレイアウトのコンテナ幅に従う
- saas / dashboard では本文の font-size が小さくなるため、コントラスト比と可読性に特に注意
- プロファイルの値は出発点。プロダクト固有の調整は必要に応じて行う

## 12. Reject / Warn 条件

タイポグラフィ評価で、重大度を明確に分ける。Reject は即修正が必要な問題。Warn は改善を推奨する問題。

### Reject（差し戻し）

以下のいずれかに当てはまる場合、❌ として優先的に報告する。

**R1. `word-break: break-all` がテキスト要素全体に適用されている**
日本語本文、見出し、フォームの可読性を壊す。URL対策と日本語の禁則寄りの扱いと mixed-script の見出し調整は、本来は別々に考えるべき。

**R2. 本文に `letter-spacing: 0.05em` 以上が適用されている**
本文の苦しさは字間不足ではなく、行間不足や折り返し設計の粗さから来ていることが多い。本文の不快感を tracking でごまかすと別の場所が崩れる。

**R3. 日本語本文の `line-height` が 1.5 未満（media / docs プロファイル）**
日本語は全角文字の密度が高く、英語より広い行間が必要。長文が主体のプロファイルでは 1.5 未満は読みにくい。saas / dashboard プロファイルでは 1.4 まで許容するが、実画面での確認が必要。

**R4. 日本語フォントが一切指定されていない**
和文フォントの描画責任をブラウザ既定に丸投げしない。font-family に日本語フォントを明示する。

**R5. `palt` が本文全体に適用されている（実読確認なし）**
`palt` は仮名の字幅も変える。本文への一括適用は副作用が出やすい。見出し・ナビゲーション等の短いテキストに限定する。

**R6. 表やフォームが本文のルールをそのまま継承している**
記事本文で気持ちよく読める line-height は、表やフォームにはそのまま使えない。逆に、表に合わせた詰め方を本文へ持ち込むと長文が読みにくくなる。役割ごとに分離する。
判定基準: `table` / `th` / `td` / `input` / `textarea` / `select` に対して `line-height` が独自に指定されていれば非該当。body や親から継承したままの状態を該当とする（値が偶然一致するだけの上書きは非該当扱い）。

### Warn（改善推奨）

以下に当てはまる場合は ⚠️ として報告し、理由と確認結果を添える。

**W1. `ch` 単位で行長を指定している**
`ch` は半角文字 "0" の幅基準。日本語全角文字はその約2倍で、環境差も大きい。`em` を使う。

**W2. 4ウェイト以上のフォントを読み込んでいる**
日本語フォントは1ウェイトあたり数百KB〜数MB。パフォーマンスへの影響が大きい。
判定基準: ファミリー横断の合計ウェイト数で判定する（例: Inter 400/500/600 ＋ Noto Sans JP 400/500/700 = 計 6 ウェイトで該当）。日本語ファミリー単体と英字ファミリー単体を別枠で数えない。

**W3. 見出しのモバイル折り返しを確認していない**
PC表示だけで判断しない。日本語の見出しは意味の途中で改行されやすい。

**W4. mixed-script を含む見出しを確認していない**
日本語 + 英語サービス名、英単語、略称が入る場合は見た目のバランスを確認する。

**W5. Windows 描画を考慮していない**
macOS だけで見て終わると、游ゴシック問題をはじめ日本語描画の印象差が大きく出る。

**W6. `text-autospace` にフォールバック方針がない**
新しい機能なので、段階適用か、未対応環境での方針を書く。

## 13. 責務分離

日本語UIの品質は「文字を大きくする」「余白を増やす」ではなく、**役割ごとのルール分離**で決まる。

### 本文

本文は読むための器。呼吸が必要。

- line-height: 広め（1.4-2.0、プロファイルによる。compact プロファイルでは 1.4 まで許容）
- letter-spacing: 控えめ（0 or normal）
- overflow-wrap: `anywhere`
- line-break: `strict`
- 字間を足しても読みやすくはならない。苦しさは行間や折り返しで解消する

### 見出し

見出しは導線。強さとまとまりが必要。

- line-height: 狭め（1.2-1.45、プロファイルによる）
- letter-spacing: 0 or わずかにマイナス（-0.02em まで）
- `palt` の適用可（短いテキストなので副作用が出にくい）
- `word-break: auto-phrase` を検討（意味のまとまりで改行）
- 本文と同じ spacing logic で設計すると、見出しが間延びするか本文が詰まる

### 表

表は走査性が命。本文ルールをそのまま使うと密度が合わない。

- line-height: 本文より詰める（1.3-1.5）
- font-size: 本文より小さくてよい（12-14px）
- letter-spacing: 0
- 数値は等幅フォント or `font-variant-numeric: tabular-nums`
- カラムヘッダーのウェイトは 500-600
- 本文に合わせた行間を表に持ち込むと、行が間延びして走査しにくくなる

### フォーム

フォームはラベルの可読性とタップ領域の確保が優先。

- line-height: 1.4-1.5（本文より詰め）
- ラベルの font-size: 本文と同等以上
- エラーメッセージ: overflow-wrap: `anywhere`（URL等の長い文字列対策）
- inputmode の適切な設定（tel, email, numeric）
- 本文のルールを引きずると、フォーム全体が窮屈になるか間延びする

### 分離の実装パターン

具体的なCSSはセクション14のレシピ（ja-text / headings / forms）を参照。各レシピが本文・見出し・フォームの分離を実装している。

## 14. CSSレシピ

修正提案時に使える再利用可能なCSS断片。プロジェクトのCSS手法（Tailwind / CSS Modules 等）に合わせて翻訳する。

### ja-text — 日本語本文の基本

```css
html:lang(ja) {
  line-break: strict;
  word-break: normal;
  overflow-wrap: anywhere;
  font-kerning: auto;
  font-feature-settings: "chws" 1, "vchw" 1;
}

body {
  text-rendering: optimizeLegibility;
}

/* 長文コンテンツの行長制限 */
:where(article, .prose, .content) p {
  max-width: 45em;
}
```

### mixed-script — 和欧混植

```css
/* Progressive Enhancement: 対応ブラウザのみ */
html:lang(ja) {
  text-autospace: normal;
}

/* 見出しの意味単位改行 */
:lang(ja) h1,
:lang(ja) h2,
:lang(ja) h3 {
  word-break: auto-phrase;
}

/* mixed-script 要素の安全策 */
:lang(ja) .product-name,
:lang(ja) em,
:lang(ja) strong {
  word-break: normal;
  overflow-wrap: anywhere;
}
```

### headings — 見出し体系

```css
:lang(ja) h1,
:lang(ja) h2,
:lang(ja) h3,
:lang(ja) h4 {
  line-break: strict;
  word-break: normal;
  overflow-wrap: anywhere;
  font-kerning: auto;
  font-feature-settings: "palt" 1;
}

:lang(ja) h1 { line-height: 1.3; }
:lang(ja) h2 { line-height: 1.35; }
:lang(ja) h3 { line-height: 1.4; }
```

### forms — フォーム

```css
:lang(ja) label,
:lang(ja) input,
:lang(ja) textarea,
:lang(ja) select,
:lang(ja) button {
  line-break: strict;
  word-break: normal;
}

:lang(ja) input,
:lang(ja) textarea,
:lang(ja) select {
  line-height: 1.5;
}

:lang(ja) .form-help,
:lang(ja) .form-error {
  line-height: 1.5;
  overflow-wrap: anywhere;
}
```

### dark-mode — ダークモード補正

```css
@media (prefers-color-scheme: dark) {
  :lang(ja) body {
    -webkit-font-smoothing: auto; /* antialiased を外して太さを保つ */
    color: #E5E7EB;              /* 純白ではなくやや灰色に */
  }

  :lang(ja) p,
  :lang(ja) li,
  :lang(ja) dd {
    line-height: 1.9; /* ライトモードの 1.8 より +0.1 */
  }
}

# ハーネス取り込み管理表

> 折茂が投げたリンク・資料を「スキル化できるもの／知見として保持するもの」に振り分けて管理する台帳。
> **運用ルール:** リンクが来るたび1行追加。判定=「スキル化」はスキルとして実装する（予定含む）、「知見」は設計に反映して保持。参考元は必ずリンクで残す。
> 最終的にこのシステムは「評価データが入るたびに改善される」自己改善ループになる前提で、各行がどの層（①文脈②制約③検証④FB／メタ）に効くかも記録する。

## 判定基準（スキル化 or 知見）
- **スキル化**: 繰り返し実行する手順であり、入力と出力が定義でき、検証可能なもの（Anthropic 9分類のどれかに素直に収まるか）
- **知見**: 考え方・原則・実証データ。スキルの中身（SKILL.mdの書き方・Gotchas・判定基準文）に反映して保持

## 台帳

| No | 取込日 | 参考元 | 判定 | 対象・成果物 | 要点 | 効く層 |
|---|---|---|---|---|---|---|
| 1 | 07-21 | [kgsi: デザインハーネスとは何か](https://note.com/kgsi/n/n707d989e1a44) | 知見 | 素材/2026-07-21-デザインハーネス-スキル化整理.md | 4層構造の原典。検証は多段（ルール→スクショ→エージェント→人間） | 全層 |
| 2 | 07-21 | [kgsi: 現在地とこれから](https://note.com/kgsi/n/n64123e4e2aa6)（[Xポスト](https://x.com/kgsi/status/2076813829112307941)経由で再読・深掘り済み） | 知見(重要) | 同上 | **収束のハーネス**（正解に合わせる=今の主流・4段階）と**探索のハーネス**（正解自体を見つける・「ありきたりでは?」「なぜこの案か」を問い判断理由を蓄積）の区別。グラフィック領域は「らしさ」の非言語判断が支配的でlint不能=検査ツール開発段階→**バナー評価ハーネスは業界的に先行領域**。クラシル実例: 5画面でlint検証→ズレ8件検出→一発動作率20→100%。将来の競争優位は「作る速さ」でなく「正解探し（判断の蓄積）」 | ③＋探索 |
| 3 | 07-21 | [kgsi: デザインにおけるSkillsの今](https://note.com/kgsi/n/n1e398fc94652) | スキル化(導入) | Impeccable / Taste Skill / ui-skills / ux-ui-agent-skills（候補）、frontend-design(導入済) | 2026年の効果検証研究3本: 8割のスキルは効かない・入れすぎ逆効果→絞り込みとdescription精度が命 | ③ |
| 4 | 07-21 | [kgsi: Complete Guide to Building Skills](https://note.com/kgsi/n/nf30a88b5dd2d) | 知見 | スキル作成手順に反映 | description3要素（何を/いつ/何ができる）。テスト3レベル（起動/機能/性能比較）。トリガー率90%目標 | メタ |
| 5 | 07-21 | [skill-evaluator (AIDB)](https://ai-data-base.com/skill/skill-evaluator/) | スキル化(導入) | ~/.claude/skills/skill-evaluator/（未導入） | スキルを13項目39点で採点。会社版skill-accessibility-evalの個人版対応物 | メタ |
| 6 | 07-21 | [PKSHA: ヒューリスティック評価のスキル化](https://zenn.dev/pksha/articles/8f4d45b913ed50) | 知見→設計反映 | バナー評価スキルの設計に4点反映 | AI評価精度30-40%前提のガードレール位置づけ／universal-contextual分離／**未確認項目の可視化**／**一度失敗させて回収するループバック** | ③④ |
| 7 | 07-21 | [classmethod: MUST vs 理由](https://dev.classmethod.jp/articles/claude-skill-must-vs-reason/) | 知見(重要) | 全スキルの書き方原則 | **命令型(MUST/NEVER)は捏造率51%、理由型は0%**。理由を書くとAIが目的の別解を自力発見。既存の「❌→✅→理由」形式の理由行が実は本体 | ②③ |
| 8 | 07-21 | [Anthropic: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（36kr邦訳も確認） | 知見(重要) | スキル分類・作成原則に反映 | 9分類（説明/検証/データ接続/自動化/scaffold/品質レビュー/異常調査/ガードレール/反復）。**Gotchasが最高情報密度**。**検証型スキルが品質への定量効果最大＝1週間かける価値**。段階的提示。フックで使用計測。柔軟性を残す | 全層＋メタ |
| 9 | 07-21 | 折茂スクショ: 会社版harness-map.md | 思想原本 | 素材/2026-07-21-会社版banner-harness思想整理.md | class A/B/C設計・21スキル・較正ループ（見落とし2回→追加/誤指摘2回→絞る） | 全層 |
| 10 | 07-21 | 折茂スクショ: メタスキルループ＋A制約ボード | 思想原本 | 同上（追記） | 選択→検証→評価データ→更新のメタ4スキル構想。A制約の具体票（納品形式/画像比率/文字正確性/改行禁則/必須要素/自社ロゴ/素材品質） | メタ・② |
| 11 | 07-20 | [NN/G: 生成AI時代のUIUX論点](https://www.nngroup.com/)※qiita経由 | 知見 | 素材/2026-07-21-NNG生成AI時代のUIUX論点_取り込み.md | 「良い状態の定義」への転換。エージェント向けUI二層化 | ①② |

| 12 | 07-21 | [Layers — Jamie Mill](https://parascope.design/resources/layers) | スキル化(導入候補)＋知見(重要) | `npx skills add jamiemill/layers-skills`（未導入） | プロダクトデザインを7層（問題空間3: 観察された行動/ドメイン/ユーザーニーズ＋解決空間4: 戦略/概念モデル/インタラクション構造/サーフェス）に分け、9スキルが各層に対応。**まず/layers-orientで全層を監査してボトルネック層を診断→該当スキルへ進む「orient-first」設計**。1スキル=1層の純度設計。出力はMarkdown+Mermaid | メタ(選択)・① |

| 13 | 07-21 | [坪田朋: melta-ui](https://github.com/tsubotax/melta-ui)（[note①](https://blog.tsubotax.com/n/n53863aa059ff) / [Zenn](https://zenn.dev/tsubotax/articles/7f0d3693f70e2f)） | スキル化(導入候補・本命) | design-review / ban-pattern スキル同梱。MIT・185★・v1.2.0(2026-04) | `/design-review`=HTML解析でDS禁止パターン違反・未使用トークンを重大度別検出＋ビフォーアフターHTMLレポート。`ban-pattern`=「AIっぽい」実装を1コマンドでJSON禁止ルール登録(105ルール規模)→ハーネスが育つ。クラシル一発動作率20→100%のOSS版 | ②③④ |
| 14 | 07-21 | mukai（Findy）[note](https://note.com/aki_yan/n/nae75bd4e46a8) | 知見 | 公開スキルなし（社内製PRDスキル・全社Plugin配布） | PRD→プルリク30分の協業事例。「Skillを全社に配る・リポジトリにlintを置く」運用。X上のみの推薦は未取得の可能性あり | メタ |

| 15 | 07-21 | [kgsi: Parascope-skills /zen](https://github.com/lumilinks-hq/Parascope-skills) | スキル化(導入候補) | `npx skills add lumilinks-hq/Parascope-skills`（未導入） | **日本語デザイン品質特化**（英語圏デフォルトのline-height 1.5・65ch行長が日本語で崩れる問題に対処）。タイポ＋UIコピー＋統合クリティーク。2026-04公開・05更新＝「5月あたり」該当。日本語バナーの組版評価に直結 | ③ |
| 16 | 07-21 | [parascope.design](https://parascope.design/)（kgsiキュレーション） | 知見(一次ソース) | RSS購読候補 | kgsiの「良い」が集約されるデザイン×AIスキル収集サイト（205件）。今後の定点観測先。design-harness.comは2026-07-03更新 | メタ |
| 17 | 07-21 | [r.kagaya: ハーネスエンジニアリング論](https://zenn.dev/r_kaga/articles/329afdc151899f)（[deck](https://speakerdeck.com/rkaga/how-to-approach-harness-engineering)） | 知見(重要) | 評価運用の設計に反映 | スキル推薦はせず「**Skill評価は定量で**: タスク種別ごとの成功率・人間介入なしマージ率をダッシュボード化」。自作harness-entropy(ルール陳腐化検出→修正PR、マージ率68.4%)/harness-feedback(失敗→ルール還流PR、58.3%)は未OSS。7/9デッキは rules.json/patterns.json/DESIGN.md の機械可読制約ファイル方式。[kauchi記事](https://zenn.dev/kauchi/articles/learning-harness-engineering-by-skill-review)のSkill評価3軸（いつ/誰が/頻度×コスト）も併読価値 | ③④メタ |

| 18 | 07-21 | 清水はるか(PKSHA): [DSスキル精度8つの方法](https://zenn.dev/pksha/articles/7a7db5c105f396) / [1000人規模導入デッキ](https://speakerdeck.com/pkshadeck/1000ren-gui-mo-nozu-zhi-dedezainhanesuwodao-ru-surutamenodi-bu) | 知見(重要・スキル本体は非公開) | banner-eval等の基準文に反映 | 精度向上8策: トークンをCSSで渡す・**「など」→「のみ」表現**・Primitives全面禁止・人間と同じ3ステップ検証等。**社内に「スキル評価用スキル」あり（8観点: トリガー精度/構造健全性/出力一貫性/トークン効率/安全性/堅牢性/評価可能性/記述スタイル）**＝会社版skill-accessibility-evalと同8観点系。スキル出力にGoogleフォームを仕込みFB回収する運用 | ③④メタ |
| 19 | 07-21 | にしゃみー(Rimo): [少人数チームのデザインハーネス](https://speakerdeck.com/nishame/shao-ren-shu-timute-shi-wareruhurotakutonitatorizhao-kutameno-tesainhanesu) | 知見 | 制約設計に反映 | 1人デザイナー体制の実装: トークン外使用禁止・新規Variant作成禁止・制約違反チェック＋**スクショチェック**・プロジェクトごとのFBログ。課題はAI-Slop（凡庸再現）と明言 | ②③④ |

## 未処理キュー
- （なし。リンクが来たらここに一旦入れて、処理後に台帳へ移す）

## 予定されているテスト
- **バナー評価ドライラン**: 折茂から案件データ送付待ち。届いたら討論モデル（計画承認後）で実走し、評価データの初回蓄積を開始する。

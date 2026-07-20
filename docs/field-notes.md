# field-notes — 実践者6人からの抽出知見（2026-07時点）

このパックの設計判断の裏付け。全員2026-07-09「デザインハーネス」イベント（PKSHA本郷）周辺の発信者。

## 坪田朋（クラシルCPO）— 検証のコード化
- [melta-ui](https://github.com/tsubotax/melta-ui)（MIT）: `/design-review` がDS禁止パターン違反・未使用トークンを重大度別検出しビフォーアフターHTMLレポート。`ban-pattern` は「AIっぽい」実装を1コマンドでJSON禁止ルール登録（105ルール規模）。
- 社内では5画面の実験でlint検証がズレ8件を検出し一発動作率20%→100%。
- 本パックへの反映: 「人間の修正を1コマンドでルール化する」動線は eval-calibrate の提案フローの理想形。
- 出典: [note](https://blog.tsubotax.com/n/n53863aa059ff) / [Zenn](https://zenn.dev/tsubotax/articles/7f0d3693f70e2f)

## 清水はるか（PKSHAリードデザイナー）— 評価スキルの運用設計
- [ヒューリスティック評価のスキル化](https://zenn.dev/pksha/articles/8f4d45b913ed50): AI評価精度30〜40%前提の「最低限のガードレール」位置づけ／universal・contextual分離／未確認項目の可視化／一度失敗させて回収するループバック。
- [DSスキル精度向上8策](https://zenn.dev/pksha/articles/7a7db5c105f396): トークンはCSSファイルで渡す／**「など」と書かず「のみ」と書く**（例示は抜け道になる）／人間と同じ手順の3ステップ検証。
- [1000人規模導入](https://speakerdeck.com/pkshadeck/1000ren-gui-mo-nozu-zhi-dedezainhanesuwodao-ru-surutamenodi-bu): 得意領域ごとに担当を割ってスキル化→テストデータで達成度検証→リポジトリ配布→**スキル出力にフォームを仕込んでFB回収**。社内に「スキル評価用スキル」（トリガー精度・構造健全性・出力一貫性・トークン効率・安全性・堅牢性・評価可能性・記述スタイルの8観点）。
- 本パックへの反映: 未確認テーブル（output-format.md）、「のみ」型の基準文表現、配布後FB回収の発想。

## にしゃみー（Rimo Head of Design）— 少人数での制約設計
- [登壇資料](https://speakerdeck.com/nishame/shao-ren-shu-timute-shi-wareruhurotakutonitatorizhao-kutameno-tesainhanesu): トークンに存在しないものは使わない／新規コンポーネントVariant作成禁止／制約違反チェック＋**スクショチェック**の二段検証／プロジェクトごとのFBログ。課題はAI-Slop（凡庸の再現）。
- 本パックへの反映: 画像実寸確認のGotcha、FBログの案件個別分離。

## r.kagaya — スキルではなく検証ループを測る
- [ハーネスエンジニアリング論](https://zenn.dev/r_kaga/articles/329afdc151899f) / [deck](https://speakerdeck.com/rkaga/how-to-approach-harness-engineering): Skillは「使う側のハーネス」の一部にすぎない。**Skill評価は定量で**（タスク種別ごとの成功率・人間介入なしマージ率のダッシュボード化）。自作harness-entropy（ルール陳腐化検出→修正PR、マージ率68.4%）・harness-feedback（失敗→ルール還流PR、58.3%）。
- 本パックへの反映: eval-calibrate の精度カウンタは氏の定量主義の縮小版。KPI候補: 「人間の指摘のうちAIが先に拾えた率」。
- 併読: [kauchi: Skillのレビューを通じて学ぶハーネスエンジニアリング](https://zenn.dev/kauchi/articles/learning-harness-engineering-by-skill-review)（Skill評価3軸: いつ起動/誰が起動/頻度×コンテキストコスト）。

## mukai（Findyデザインマネージャー）— 全社配布の運用
- 公開スキルなし。[note](https://note.com/aki_yan/n/nae75bd4e46a8): 社内PRDスキル＋ガードレールでPRD→プルリク30分。「Skillを全社に配る・リポジトリにlintを置く」運用。

## こぎそ / kgsi — 概念と日本語品質
- [デザインハーネスとは何か](https://note.com/kgsi/n/n707d989e1a44)（4層モデル）/ [現在地とこれから](https://note.com/kgsi/n/n64123e4e2aa6)（収束と探索）。
- [Parascope-skills /zen](https://github.com/lumilinks-hq/Parascope-skills): **日本語デザイン品質特化**（英語圏デフォルトのline-height・行長が日本語で崩れる問題）。タイポ＋UIコピー＋統合クリティーク。
- 定点観測先: [parascope.design](https://parascope.design/)（キュレーション205件・RSSあり）。

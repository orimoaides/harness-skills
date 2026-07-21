# デザインハーネスのスキル化 — 整理メモ（2026-07-21）

> 目的: デザインハーネスを本格的にスキル化する。中心イメージは **「バナー画像を渡すと評価が返ってくるスキル」**。
> あわせて、こぎそ（kgsi）さんがピックアップしている系統のスキル（スキルを評価するスキル等）を全部取り込みたい。

---

## 1. いま手元にある資産（過去セッションの棚卸し）

### Duolingo検証セッション（7/9「デザインシステム」/ `~/visual system`）
GitHub private repo **`orimoaides/visual-design-harness`** にテンプレートとして永続化済み。

**ブランド非依存＝そのまま再利用できる骨格:**
- スキル7種の構成・`validate.py`（自動検証30項目/全66項目）の仕組み
- **AI検品員の手順書**（申告を信用しない／迷ったらfail／unverified明記／検品員は直さない）
- **3観点スコアリング100点の配点**: ブランド適合30 / 視覚階層20 / レイアウト適合15 / ブリーフ適合15 / 構図10 / 技術品質10 ＋即fail条件
- 文字入り完成物は「文字組みに40点振る」3層評価
- **絶対ルール2つ**: 測定手段の明記（〔実測〕〔目視〕〔読解〕）と **craft／compliance の二重判定**
- 評価DB＋集計、4層構成（文脈・制約・検証・フィードバック）、承認ゲート運用
- 実績: 欠陥検出8/8、外部AI生成物を73→86点に改善、レイアウト適合97.8%

**Duolingo固有＝作り直す部品:** 正本（解剖書）/ tokens.json / promptbookのブランドDNA / checksのブランド由来項目 / ロゴ資産

### 折茂カンパニー側にすでにあるもの
- **`orimo-design` スキル**（デザインハーネス本体）: 4層構造、生成前セルフチェック、`references/design-rules.md`（❌→✅→理由の追記式）、承認ゲート＝折茂
- **`orimo-judge` のデザイン品質ゲート**: 「AIっぽさ」（紫グラデ・絵文字乱用・意図なき余白）を世界観チェックの手前で弾く。合格ライン「折茂のポートフォリオに載せて恥ずかしくないか」
- **orimo-qa**: 実環境再現の機械検証（Retina/DPR2・リサイズ・実データ）

### 7/9セッション終了時の申し送り
「Duolingoではなく自分のやつ（おりもラボ版）と会社専用版を、ファイルを分けて作る」。会社版は初稿×FBログの資産を「まず薄くても正本を書く→FBログを検証項目とexceptionsに振り分ける」順で。

---

## 2. 新スキル案: バナー画像評価スキル（仮: `banner-eval` / `orimo-design-eval`）

**イメージ:** バナー等の画像データ＋ブリーフを渡す → ハーネスの評価系だけを単体スキルとして起動 → スコア・根拠・改善指示が返る。

### 設計たたき台
- **入力**: 画像ファイル（PNG/JPG）＋任意でブリーフ（媒体・サイズ・訴求・ターゲット）＋対象ブランド（おりもラボ / 会社 / 汎用）
- **評価は3段階**（Duolingo検証で確立した形をそのまま移植）
  1. **auto検証**: 定規で測れるもの（サイズ・色hex・コントラスト比・セーフエリア・語数・禁止語）→ failは即差し戻し
  2. **AI検品員**: 目視でしか分からないもの（にじみ・崩れ・違和感）。検品員は直さない・迷ったらfail
  3. **ルーブリック採点**: 100点配点（上記30/20/15/15/10/10ベース、ブランドごとに正本から再調整）
- **出力**: 観点別スコア＋根拠（測定手段明記）＋改善指示＋craft/compliance二重判定。評価レポートHTML化は既存テンプレ（`repo/eval-report-R005.html`）が流用可
- **フィードバック層**: 折茂の採点との差分が出たら、採点基準そのものを直すメタループ（承認ゲート＝折茂）
- **ブランド差し替え**: 正本＋tokens＋禁止パターン集をブランドフォルダで切り替える構造にする（おりもラボ版／会社版／クライアント版）

### 分担（重複させない）
- `orimo-design` = 手綱を渡す側（文脈・制約・ルール育成）
- **新スキル = 評価の実行体**（画像を受けて採点する部分の単体化）
- `orimo-judge` = 最終合否ゲート（新スキルのスコアを入力にできる）

---

## 3. こぎそ（kgsi）ピックアップ系スキル — 導入候補リスト

kgsi = デザインエンジニア。デザインハーネス提唱者（[design-harness.com](https://design-harness.com/)、note連載、7/9イベント主催）。

### デザイン生成・品質系（記事「[AIエージェントにおけるSkillと、デザインにおけるSkillsの今](https://note.com/kgsi/n/n1e398fc94652)」で紹介）
| スキル | 作者 | 役割 | 入手先 |
|---|---|---|---|
| **frontend-design** | Anthropic公式 | UI設計時の禁則ルール化（27万+インストール） | GitHub anthropics/skills ※本環境に導入済み |
| **Impeccable** | v3.1.0 (2026/5) | 23コマンド＋29アンチパターン検出 | impeccable.style |
| **Taste Skill** | Leonxlnx | 「AIに良い趣味を与える」。デザイン分散度・モーション強度・視覚密度の3ダイヤルで凡庸回避。画像生成（参照ボード/モックアップ/ブランドキット）も | `npx skills add https://github.com/Leonxlnx/taste-skill`（65k★） |
| **ui-skills** | ibelick | 領域別スキル集約（インターフェース・a11y等） | ui-skills.com |
| **ux-ui-agent-skills** | plugin87 | トークン・コンポーネント・a11y対応 | GitHub plugin87 |

### スキルを作る・評価する系（←「スキルを評価するスキル」はここ）
| スキル | 役割 | 入手先 |
|---|---|---|
| **skill-evaluator** | Agent Skillsの品質を**13項目39点満点**で採点し改善提案を出す。「正しいか・発見されるか・価値があるか」を診断 | [AIDB](https://ai-data-base.com/skill/skill-evaluator/)（スキルライブラリ）。`~/.claude/skills/skill-evaluator/` に配置 |
| **skill-creator** | スキル作成＋**テスト（eval）機能**つき。「勘で直す」の終わり | Anthropic公式 ※本環境に導入済み |
| **find-skills** | スキル探索（41.8万インストール） | GitHub |

### kgsi自作・関連
- **gogcli Skills**（kgsi自作、[X](https://x.com/kgsi/status/2017041029942440400)）
- URL→デザインコンテキスト変換スキル（任意URLを解析し「なぜこの色か・何を捨てたか」まで文書化。※Taste Skillと同系統、kgsiが紹介）
- **Nothingのデザイン言語でUIを生成するスキル**（[X](https://x.com/kgsi/status/2042066672455184398)）— 「特定ブランドのデザイン言語をスキル化する」実例＝おりもラボ版の参考構造（デザイン哲学＋コンポーネント参照＋プラットフォーム別出力マッピング）

### kgsiの知見で新スキルに直接効くもの
- **検証層の多段構成**（[デザインハーネスとは何か](https://note.com/kgsi/n/n707d989e1a44)）: ルール検証→スクリーンショット検証（密度・階層）→エージェントレビュー（原則整合）→人間の最終判断。うちの3段階とほぼ同型、「スクリーンショット検証」の明示は取り込む価値あり
- **グラフィック・ブランド領域はまだ検査ツール開発段階**（[現在地とこれから](https://note.com/kgsi/n/n64123e4e2aa6)）＝バナー評価スキルは先行領域。クラシル事例: lint検証で一発動作率20%→100%
- **Skills効果検証研究3本（2026）の教訓**: スキルは入れれば効くものではない（8割のスキルが性能を動かさない/2割のタスクでは逆効果/自動選別だと効果減衰）→ **descriptionの起動精度とスキル数の絞り込みが命**。skill-evaluatorでの事前診断を運用に組み込む理由になる
- **Anthropic公式ガイドのテスト3レベル**（[Complete Guide要約](https://note.com/kgsi/n/nf30a88b5dd2d)）: 起動テスト（起動すべきでない場面で起動しないか）/ 機能テスト / 性能比較（スキルなしとの定量差）。成功基準: トリガー率90%・ユーザー補正なしで完了

---

## 4. 進め方（案）

1. **skill-evaluator と Taste Skill を導入**して手触りを確認（skill-evaluatorは既存の orimo-design / orimo-judge の診断にもすぐ使える）
2. **バナー評価スキルの骨格を作る**: visual-design-harness repo から評価系（validate.py・検品手順書・ルーブリック）を抜き出し、ブランド差し替え可能な形に
3. **おりもラボ版の正本**（薄くてよい）→ 会社版はFBログから
4. 完成したスキル自体を **skill-evaluator で採点** → skill-creator の eval でテスト（起動テスト含む）
5. Impeccable / ui-skills 等は生成側の強化として orimo-appdev / orimo-build に紐づけ検討

## Sources
- [デザインハーネスとは何か｜こぎそ](https://note.com/kgsi/n/n707d989e1a44)
- [デザインハーネスの現在地とこれから｜こぎそ](https://note.com/kgsi/n/n64123e4e2aa6)
- [AIエージェントにおけるSkillと、デザインにおけるSkillsの今｜こぎそ](https://note.com/kgsi/n/n1e398fc94652)
- [The Complete Guide to Building Skills for Claude｜こぎそ](https://note.com/kgsi/n/nf30a88b5dd2d)
- [Design Harness 公式サイト](https://design-harness.com/)
- [skill-evaluator（AIDB）](https://ai-data-base.com/skill/skill-evaluator/)
- [taste-skill（SkillsLLM）](https://skillsllm.com/skill/taste-skill) / [GitHub](https://github.com/Leonxlnx/taste-skill)
- [skill-creatorにテストが来た話](https://note.com/renkon40/n/n2b3dc4740430)
- kgsi X: [Nothing UIスキル](https://x.com/kgsi/status/2042066672455184398) / [gogcli Skills](https://x.com/kgsi/status/2017041029942440400)

# harness-skills — デザイン評価ハーネスのスキルパック

グラフィック/バナーの評価を AI に任せるための Claude Code スキル群。

> **中心思想:** AIが作ったものを人だけで見るのではなく、「何を良しとするか」「どう検証するか」をSkillsに残す。作るAIだけでなく、評価するAIまで含めて設計する。

## 構成（4スキル＝評価の1周）

| スキル | 役割 | いつ使う |
|---|---|---|
| [eval-orient](skills/eval-orient/SKILL.md) | 診断・評価セット選択 | 評価を始める前に必ず |
| [banner-eval](skills/banner-eval/SKILL.md) | 評価の実行体（A照合→B定性→採点） | 画像＋ブリーフが揃ったら |
| [design-review-panel](skills/design-review-panel/SKILL.md) | 専門家5役の討論（class B用） | 定性観点を深く見たい時・乖離が大きい時 |
| [eval-calibrate](skills/eval-calibrate/SKILL.md) | 人間FBとの突き合わせ・較正 | 人間のレビュー結果が出るたび |

```
eval-orient → banner-eval →（必要なら design-review-panel）→ 人間レビュー → eval-calibrate
     ↑                                                                        │
     └────────────── 較正結果がスキル棚・配点・プリセットを更新 ←──────────────┘
```

## 設計原則（このパックの前提）

1. **class A/B/C の三分類。** 機械照合できるもの（A）だけがブロック権限を持つ。程度問題は定性判定（B）で減点。AIが信頼できない観点は人間領域（C）としてAIは観察の列挙まで。**重要度と測定可能性は別の軸** — AIが苦手だから配点を下げる、はやらない（Cに送る）。
2. **点数はAIに発明させない。** AIは観点ごとの3段階判定まで。合計点は配点表からの機械集計。
3. **評価の一次出力はJSON**（calibration/ に蓄積）、人間向けのペラいちHTMLはそこから生成する。較正ループを回すため。
4. **理由型で書く。** 命令型（MUST/NEVER）は捏造率51%、理由型は0%という実証がある。このパックのルールはすべて「なぜ」つき。
5. **評価は較正されて初めて信用できる。** AI評価の精度はガードレール水準（30〜40%）から始まる前提。人間FBとの突き合わせ（eval-calibrate）が本体で、評価スキルはその入力を作る装置。

## インストール

```bash
git clone https://github.com/orimoaides/harness-skills.git
cp -r harness-skills/skills/* ~/.claude/skills/
```

ブランド固有の規定（ロゴレギュレーション・入稿規定・トークン）は含まれていない。各自 `skills/banner-eval/references/brand-profile.md` の雛形に自分のブランドの値を書き込んで使う。

## 併用を推奨する外部スキル

（調査中 — 各分野の実践者が推すスキルを選定して追記する）

## 参考元

- kgsi: [デザインハーネスとは何か](https://note.com/kgsi/n/n707d989e1a44) / [現在地とこれから](https://note.com/kgsi/n/n64123e4e2aa6)（収束と探索）
- PKSHA 清水はるか: [ヒューリスティック評価のスキル化](https://zenn.dev/pksha/articles/8f4d45b913ed50)（未確認テーブル・ループバック）
- classmethod: [MUST vs 理由の実証](https://dev.classmethod.jp/articles/claude-skill-must-vs-reason/)
- Anthropic: [How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（9分類・Gotchas・検証スキルの価値）
- Jamie Mill: [Layers](https://parascope.design/resources/layers)（orient-first設計）

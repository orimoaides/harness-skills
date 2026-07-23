# output-format — 評価データのスキーマとレポート仕様

## JSON（正本）— calibration/ に1評価1ファイル
ファイル名: `calibration/YYYY-MM-DD_<案件ID>_<稿番号>.json`

```json
{
  "meta": { "case_id": "", "draft": "FB-2", "date": "", "eval_set": "入稿前・正確性重視", "brand_profile": "" },
  "class_a": [
    { "id": "req-mandatory", "result": "true|false|unverified", "note": "" }
  ],
  "class_b": [
    { "id": "hierarchy-priority", "evaluator": "typo|graphic|appeal|brand|solo", "score": 7, "band": "fail|rework|polish|pass", "reason": "", "method": "実測|目視|読解", "confidence": "high|mid|low", "intent_declared": false, "intent_approved_by": null }
  ],
  "class_c": [
    { "id": "kerning-fine", "shadow_score": 6, "band": "polish", "observations": ["見出しの字間が広く見える"], "method": "目視", "confidence": "low", "note": "影スコア=集計外。人間の判定材料" }
  ],
  "unverified": [
    { "id": "", "why": "規定文書未提供 / 画像解像度不足 / ブリーフ欠落" }
  ],
  "score": { "craft": 0, "breakdown": {}, "compliance": "pass|blocked", "instant_fail": null },
  "summary": {
    "verdict": "このまま出せる｜直せば出せる｜方向から再考",
    "one_liner": "総評1〜2文。判定の要約であって新しい評価を書かない",
    "strengths": [ "効いている点・次稿でも維持すべき点（keep）を2つまで" ],
    "fix_first": [ "fix_order の上位3つをそのまま写す（独自ロジック禁止 — 直す順の定義は scoring.md の fix_order 一箇所のみ）" ],
    "handoff_to_human": [ "人間に見てほしい点: C観察・確信度low・panel乖離・未確認" ]
  },
  "delta": { "prev_draft": null, "craft_change": null, "resolved": [], "regressed": [] },
  "reliability": "較正前（ガードレール精度）｜較正n件済み",
  "fix_order": [ "scoring.mdの定義で並べた改善指示（層優先則→配点×(10−score)）" ],
  "panel": { "used": false, "divergence": [] }
}
```

総評の縛り: `summary` に観点判定に無い新しい指摘を書かない。書きたくなったらそれは観点の漏れ → eval-calibrate で新観点起票。`delta` は同一案件の2稿目以降のみ（前稿JSONと比較して改善/後退を機械的に列挙）。

要点:
- `unverified` は必須。「見ていない」を「問題なし」から分離しないと較正が壊れる。
- `intent_declared` は B観点の意図宣言記録。不問にした場合も判定自体は残す（較正の材料になる）。
- `panel.divergence` は討論モデル使用時の専門家間乖離。乖離は隠さず記録する — そこが較正の種。

## HTML（人間向け・ペラいち）
JSONから生成する自己完結HTML（外部依存ゼロ、画像はdata URI埋め込み、ダブルクリックで開ける）:
1. ヘッダ: 案件ID・稿番号・評価セット名・日付・信頼度表示（較正前/較正n件済み）
2. **総評**: 結論（出せる/直せば出せる/再考）＋1〜2文＋維持すべき点（keep）
3. 判定サマリー: 対象画像・craft点・compliance・即failの有無・（2稿目以降）前稿との差分
4. 観点テーブル: **評価項目と判定を同じ行に**（解釈ズレを可視化するため）。スコア(帯)・根拠・測定手段・確信度を列で
5. class C観察リスト＋影スコア: 「人間が見るべき箇所」として提示
6. 未確認テーブル: 確認できなかった観点と理由
7. 改善指示: 直す順（配点×帯の低さ）で上から
8. （討論モデル使用時）専門家間の乖離と裁定理由

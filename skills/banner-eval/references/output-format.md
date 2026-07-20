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
    { "id": "hierarchy-priority", "score": 7, "band": "caution", "reason": "", "method": "実測|目視|読解", "confidence": "high|mid|low", "intent_declared": false }
  ],
  "class_c": [
    { "id": "kerning-fine", "shadow_score": 6, "band": "caution", "observations": ["見出しの字間が広く見える"], "method": "目視", "confidence": "low", "note": "影スコア=集計外。人間の判定材料" }
  ],
  "unverified": [
    { "id": "", "why": "規定文書未提供 / 画像解像度不足 / ブリーフ欠落" }
  ],
  "score": { "craft": 0, "breakdown": {}, "compliance": "pass|blocked", "instant_fail": null },
  "fix_order": [ "配点の高いfailから並べた改善指示" ],
  "panel": { "used": false, "divergence": [] }
}
```

要点:
- `unverified` は必須。「見ていない」を「問題なし」から分離しないと較正が壊れる。
- `intent_declared` は B観点の意図宣言記録。不問にした場合も判定自体は残す（較正の材料になる）。
- `panel.divergence` は討論モデル使用時の専門家間乖離。乖離は隠さず記録する — そこが較正の種。

## HTML（人間向け・ペラいち）
JSONから生成する自己完結HTML（外部依存ゼロ、画像はdata URI埋め込み、ダブルクリックで開ける）:
1. 冒頭: 対象画像・総合スコア・compliance判定・即failの有無
2. 観点テーブル: **評価項目と判定を同じ行に**（解釈ズレを可視化するため）。判定・根拠・測定手段・確信度を列で
3. 未確認テーブル: 確認できなかった観点と理由
4. class C観察リスト: 「人間が見るべき箇所」として提示
5. 改善指示: 配点の高いfailから順に
6. （討論モデル使用時）専門家間の乖離と裁定理由

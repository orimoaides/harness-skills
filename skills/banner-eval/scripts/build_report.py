#!/usr/bin/env python3
"""評価JSON → ペラいち自己完結HTMLレポート生成（決定論・stdlibのみ）。

使い方:
  python3 build_report.py 評価.json --image バナー.png [--out レポート.html]

data URI埋め込み・画像なしでも動く。LLMにbase64を書かせないための専用装置。
"""
import argparse
import base64
import html
import json
import mimetypes
import os
import sys

CSS = """html{background:#FFFFFF}body{font-family:'Hiragino Sans','Hiragino Kaku Gothic ProN',sans-serif;max-width:860px;margin:24px auto;padding:0 16px;background:#FFFFFF;color:#292826;line-height:1.7}
table{background:#FFFFFF}
h1{font-size:20px}h2{font-size:16px;border-left:4px solid #5E7E7A;padding-left:8px;margin-top:28px}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid #D3D1C7;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#F1EFE8}img.banner{max-width:100%;border:1px solid #D3D1C7}
.badge{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:600}
.pass{background:#E1F5EE;color:#085041}.polish{background:#FAEEDA;color:#633806}.rework{background:#F5E3D0;color:#712B13}.fail{background:#FCEBEB;color:#791F1F}
.gray{background:#F1EFE8;color:#444441}.legend{font-size:12px;color:#5F5E5A;background:#F7F5EF;padding:10px 12px;border-radius:8px}
.warn{background:#FCEBEB;padding:10px 12px;border-radius:8px;font-weight:600}"""

BAND_JP = {"pass": "合格 8-10", "polish": "表層修正 6-7", "rework": "構造修正 4-5", "fail": "致命 1-3", "caution": "要改善 4-7(旧)"}


def badge(band):
    b = band or "gray"
    return f'<span class="badge {html.escape(b)}">{html.escape(BAND_JP.get(band, band or "—"))}</span>'


def esc(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def rows(items, cols):
    out = []
    for it in items or []:
        tds = []
        for c in cols:
            v = it.get(c)
            if c == "band":
                tds.append(f"<td>{badge(v)}</td>")
            elif isinstance(v, list):
                tds.append(f"<td>{esc('、'.join(map(str, v)))}</td>")
            else:
                tds.append(f"<td>{esc(v)}</td>")
        out.append("<tr>" + "".join(tds) + "</tr>")
    return "\n".join(out) or '<tr><td colspan="9">なし</td></tr>'


def main():
    p = argparse.ArgumentParser()
    p.add_argument("eval_json")
    p.add_argument("--image")
    p.add_argument("--out")
    a = p.parse_args()

    with open(a.eval_json, encoding="utf-8") as f:
        d = json.load(f)
    meta = d.get("meta", {})
    s = d.get("summary", {})
    score = d.get("score", {})

    img_tag = ""
    if a.image and os.path.isfile(a.image):
        mime = mimetypes.guess_type(a.image)[0] or "image/png"
        with open(a.image, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        img_tag = f'<img class="banner" src="data:{mime};base64,{b64}" alt="評価対象バナー">'

    blocked = score.get("compliance") == "blocked" or score.get("instant_fail")
    warn = ""
    if blocked:
        warn = f'<p class="warn">⛔ ブロック: {esc(score.get("instant_fail") or "class A照合にfalseあり — 点数以前に差し戻し")}</p>'
    intents = sum(1 for x in d.get("class_b") or [] if x.get("intent_declared"))
    if intents >= 3:
        warn += f'<p class="warn">⚠ 意図宣言が{intents}件 — コンセプト不在の疑い。不問化には依頼主/レビュアーの承認が必要</p>'
    unverified = d.get("unverified", [])
    if unverified:
        warn += f'<p class="warn" style="background:#FAEEDA">⚠ 未確認 {len(unverified)}件あり — 「見ていない」は「問題なし」ではない</p>'

    delta = d.get("delta") or {}
    delta_txt = ""
    if delta.get("prev_draft"):
        delta_txt = (f"<p>前稿({esc(delta.get('prev_draft'))})比: craft {esc(delta.get('craft_change'))} ／ "
                     f"改善: {esc('、'.join(delta.get('resolved') or []) or 'なし')} ／ "
                     f"後退: {esc('、'.join(delta.get('regressed') or []) or 'なし')}</p>")

    panel = d.get("panel") or {}
    panel_html = ""
    if panel.get("used"):
        pr = "".join(f"<li>{esc(x)}</li>" for x in panel.get("divergence") or []) or "<li>乖離なし（全役合意）</li>"
        panel_html = f"<h2>専門家パネルの乖離と裁定</h2><ul>{pr}</ul>"

    doc = f"""<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">
<meta name="color-scheme" content="light only"><title>評価レポート {esc(meta.get('case_id'))} {esc(meta.get('draft'))}</title><style>{CSS}</style></head><body>
<h1>バナー評価レポート — {esc(meta.get('case_id'))} / {esc(meta.get('draft'))}</h1>
<p class="legend"><b>このレポートの読み方</b>: craft=出来栄えの点（100点満点）／compliance=規定を守れているか（点と別判定）／
帯=致命1-3・構造修正4-5・表層修正6-7・合格8-10／影スコア=AIの参考判定（合計には入っていない。最終判断は人間）／
未確認=見られなかった項目（問題なしという意味ではない）。信頼度: <b>{esc(d.get('reliability') or '較正前（ガードレール精度）')}</b></p>
{warn}
<h2>総評</h2>
<p><b>{esc(s.get('verdict'))}</b> — {esc(s.get('one_liner'))}</p>
<p>👍 維持すべき点（keep）: {esc('、'.join(s.get('strengths') or []) or 'なし')}<br>
🔧 直す順: {esc(' → '.join(s.get('fix_first') or []) or '—')}<br>
👀 人間に見てほしい点: {esc('、'.join(s.get('handoff_to_human') or []) or '—')}</p>
<h2>判定サマリー</h2>
{img_tag}
<p>craft: <b>{esc(score.get('craft'))}</b> / 100 ／ compliance: <b>{esc(score.get('compliance'))}</b> ／ 評価セット: {esc(meta.get('eval_set'))} ／ {esc(meta.get('date'))}</p>
{delta_txt}
<h2>class A — 機械照合</h2>
<table><tr><th>観点</th><th>結果</th><th>備考</th></tr>{rows(d.get('class_a'), ['id','result','note'])}</table>
<h2>class B — 10段階採点</h2>
<table><tr><th>観点</th><th>score</th><th>帯</th><th>根拠</th><th>測定</th><th>確信度</th><th>意図宣言</th></tr>
{rows(d.get('class_b'), ['id','score','band','reason','method','confidence','intent_declared'])}</table>
<h2>class C — 人間が判定する箇所</h2>
<table><tr><th>観点</th><th>観察（先にここを自分の目で）</th><th>測定</th><th>確信度</th></tr>
{rows(d.get('class_c'), ['id','observations','method','confidence'])}</table>
<details><summary>AIの影スコアを開く（自分の判定を決めてから開くこと — 先に見ると引っ張られます）</summary>
<table><tr><th>観点</th><th>影score</th><th>帯</th></tr>{rows(d.get('class_c'), ['id','shadow_score','band'])}</table></details>
<h2>未確認テーブル</h2>
<table><tr><th>観点</th><th>確認できなかった理由</th></tr>{rows(unverified, ['id','why'])}</table>
<h2>改善指示（直す順）</h2>
<ol>{''.join(f'<li>{esc(x)}</li>' for x in d.get('fix_order') or []) or '<li>なし</li>'}</ol>
{panel_html}
</body></html>"""

    out = a.out or os.path.splitext(a.eval_json)[0] + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(json.dumps({"written": out, "bytes": len(doc), "image_embedded": bool(img_tag)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""class A 機械照合スクリプト — 画像のサイズ・比率・容量・形式を true/false で返す。

使い方:
  python3 check_image.py 対象.png --width 1200 --height 630 --max-kb 500 --format png,jpeg
  python3 check_image.py 対象.png --ratio 16:9

出力はJSON。checks の値が1つでも false なら verdict=false（ブロック）。
指定しなかった項目は照合しない（unverified 扱いは呼び出し側で管理する）。
"""
import argparse
import json
import os
import sys


def normalize_format(fmt: str) -> str:
    fmt = fmt.strip().lower().lstrip(".")
    return "jpeg" if fmt == "jpg" else fmt


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--width", type=int, help="期待する横px（完全一致）")
    p.add_argument("--height", type=int, help="期待する縦px（完全一致）")
    p.add_argument("--ratio", help="期待する比率 例 16:9（誤差1%%許容）")
    p.add_argument("--max-kb", type=int, dest="max_kb", help="容量上限KB")
    p.add_argument("--format", dest="fmt", help="許可する形式 例 png,jpeg")
    a = p.parse_args()

    result = {"file": a.image, "checks": {}}
    if not os.path.isfile(a.image):
        print(json.dumps({"error": "ファイルが見つからない", **result}, ensure_ascii=False))
        return 1
    result["file_kb"] = round(os.path.getsize(a.image) / 1024, 1)

    try:
        from PIL import Image
    except ImportError:
        print(json.dumps({"error": "Pillow未導入。`pip3 install Pillow` 後に再実行", **result}, ensure_ascii=False))
        return 2

    with Image.open(a.image) as img:
        w, h = img.size
        fmt = normalize_format(img.format or "")
    result.update({"width": w, "height": h, "format": fmt})

    if a.width is not None:
        result["checks"]["width"] = w == a.width
    if a.height is not None:
        result["checks"]["height"] = h == a.height
    if a.ratio:
        try:
            rw, rh = (int(x) for x in a.ratio.split(":"))
            result["checks"]["ratio"] = abs(w * rh - h * rw) <= max(w * rh, h * rw) * 0.01
        except ValueError:
            result["checks"]["ratio"] = None
            result["ratio_error"] = "比率の書式は 16:9 の形"
    if a.max_kb is not None:
        result["checks"]["capacity"] = result["file_kb"] <= a.max_kb
    if a.fmt:
        allowed = {normalize_format(f) for f in a.fmt.split(",")}
        result["checks"]["format"] = fmt in allowed

    decided = [v for v in result["checks"].values() if v is not None]
    result["verdict"] = all(decided) if decided else None
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

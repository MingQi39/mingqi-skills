#!/usr/bin/env python3
"""生成 #11 手写风格候鸟城市气候表（PNG，小红书配图用）。"""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT_PNG = ROOT / "assets" / "note11-climate-table-handwritten.png"

FONT_CANDIDATES = [
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/a3c69464b629577766c23bcdb12ffbfe3759b923.asset/AssetData/Hanzipen.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/00bfc46ccb002b730e29def5116e0a571fb617d8.asset/AssetData/Hannotate.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/13b8ce423f920875b28b551f9406bf1014e0a656.asset/AssetData/Xingkai.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/88d6cc32a907955efa1d014207889413890573be.asset/AssetData/Kaiti.ttc",
]

COLUMNS = ["城市", "冬体感", "夏体感", "湿度", "我妈一句话", "适合"]

ROWS = [
    ["三亚", "22-26℃\n暖闷潮", "30-33℃\n闷热", "高", "贵，膝盖酸", "冬主力"],
    ["海口", "18-24℃\n阴雨风大", "30-32℃\n闷", "中高", "手指老划这边", "冬★"],
    ["万宁", "17-22℃\n海边风硬", "28-31℃\n潮", "高", "待两天想回酒店", "冬短住"],
    ["北海", "14-18℃\n屋里冷", "28-30℃\n闷", "很高", "第二天流鼻涕", "冬慎用"],
    ["昆明", "8-15℃\n晒干凉", "20-24℃\n舒服", "冬干", "不像海边", "夏★"],
    ["大理", "3-12℃\n早晚冷", "18-26℃\n干爽", "干", "腿疼没多待", "夏短住"],
    ["厦门", "12-18℃\n海风", "28-32℃\n潮热", "中", "看完房价没吭声", "短住"],
    ["威海", "-2-5℃\n风像刀片", "22-28℃\n海风", "冬干夏湿", "当天说不考虑", "夏★"],
]

TITLE = "替我妈跑的 8 个城 · 气候体感"
FOOTER = "★=目前倾向   数字是体感不是气象局"
NOTE = "2026.6  哈尔滨出发"


def load_font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, index=index)


def pick_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if not Path(path).exists():
            continue
        for idx in (1, 0) if bold and "Hanzipen" in path or "Hannotate" in path else (0,):
            try:
                return load_font(path, size, idx)
            except OSError:
                continue
    return ImageFont.load_default()


def paper_background(w: int, h: int, seed: int = 19) -> Image.Image:
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h), "#F4E8D4")
    draw = ImageDraw.Draw(img)

    for y in range(56, h, 46):
        color = "#C9B8A0" if (y // 46) % 5 == 4 else "#D9CCBA"
        draw.line([(40, y), (w - 40, y)], fill=color, width=1)

    draw.line([(118, 0), (118, h)], fill="#E8A0A0", width=2)

    for _ in range(9000):
        x, y = rng.randint(0, w - 1), rng.randint(0, h - 1)
        c = rng.randint(230, 248)
        draw.point((x, y), fill=(c, c - 8, c - 18))

    vignette = Image.new("L", (w, h), 0)
    vd = ImageDraw.Draw(vignette)
    vd.ellipse((-w * 0.15, -h * 0.1, w * 1.15, h * 1.1), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(80))
    dark = Image.new("RGB", (w, h), "#8B7355")
    img = Image.composite(img, dark, Image.eval(vignette, lambda p: 255 - p // 6))
    return img


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=4)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def wavy_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: str, width: int = 2, wobble: float = 1.2) -> None:
    x0, y0, x1, y1 = box
    edges = [
        (x0, y0, x1, y0, True),
        (x1, y0, x1, y1, False),
        (x1, y1, x0, y1, True),
        (x0, y1, x0, y0, False),
    ]
    for ax, ay, bx, by, horizontal in edges:
        length = abs(bx - ax) + abs(by - ay)
        steps = max(int(length / 8), 4)
        pts = []
        for i in range(steps + 1):
            t = i / steps
            x = ax + (bx - ax) * t
            y = ay + (by - ay) * t
            if i not in (0, steps):
                off = wobble * math.sin(i * 1.7)
                if horizontal:
                    y += off
                else:
                    x += off
            pts.append((x, y))
        draw.line(pts, fill=color, width=width, joint="curve")


def draw_table(img: Image.Image) -> None:
    draw = ImageDraw.Draw(img)
    w, h = img.size

    title_font = pick_font(42, bold=True)
    header_font = pick_font(24, bold=True)
    cell_font = pick_font(22)
    small_font = pick_font(20)
    meta_font = pick_font(26)

    draw.text((132, 36), TITLE, fill="#3D2914", font=title_font)
    draw.text((w - 280, 42), NOTE, fill="#8B7355", font=meta_font)

    col_widths = [88, 140, 140, 72, 228, 96]
    table_x = 48
    table_y = 118
    header_h = 52
    row_h = 122

    x = table_x
    for i, (col, cw) in enumerate(zip(COLUMNS, col_widths)):
        box = (x, table_y, x + cw, table_y + header_h)
        wavy_rect(draw, box, "#B8896A", 2)
        tw, th = text_size(draw, col, header_font)
        draw.text((x + (cw - tw) / 2, table_y + (header_h - th) / 2 - 2), col, fill="#5C3D2E", font=header_font)
        x += cw

    accent = "#C45C26"
    for r, row in enumerate(ROWS):
        y = table_y + header_h + r * row_h
        x = table_x
        font = cell_font if r != 0 else cell_font
        for c, (cell, cw) in enumerate(zip(row, col_widths)):
            box = (x, y, x + cw, y + row_h)
            wavy_rect(draw, box, "#C4AD93", 1, wobble=0.8)
            color = accent if c == 0 or "★" in cell else "#2C2418"
            f = header_font if c == 0 else font
            if c in (1, 2):
                f = small_font
            tw, th = text_size(draw, cell, f)
            tx = x + max(6, (cw - tw) / 2)
            ty = y + max(8, (row_h - th) / 2 - 2)
            if c == 4:
                tx = x + 8
            draw.multiline_text((tx, ty), cell, fill=color, font=f, spacing=3, align="center" if c != 4 else "left")
            x += cw

    footer_y = table_y + header_h + len(ROWS) * row_h + 28
    draw.text((table_x + 8, footer_y), FOOTER, fill="#8B7355", font=small_font)

    draw.text((table_x + 8, footer_y + 36), "贴冰箱上了，省得我妈天天问同一个问题。", fill="#6B5344", font=small_font)


def main() -> None:
    random.seed(19)
    w, h = 1242, 1660
    img = paper_background(w, h)
    draw_table(img)
    img = img.rotate(-0.6, expand=False, fillcolor="#E8DDD0", resample=Image.Resampling.BICUBIC)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.3))
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PNG, format="PNG", optimize=True)
    print(OUT_PNG)


if __name__ == "__main__":
    main()

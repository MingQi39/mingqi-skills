#!/usr/bin/env python3
"""
DEPRECATED — 卡通插画风,用户反馈「没人味、蠢」。
请改用: python3 tools/gen_note_assets.py --note <题号>
见 references/image-pipeline.md
"""
import sys

print("已弃用 gen_note_images.py，请运行: python3 tools/gen_note_assets.py --note <题号>", file=sys.stderr)
sys.exit(1)

# --- legacy code below (not executed) ---

from __future__ import annotations

import math
import random
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SIZE = (1242, 1660)

FONT_CANDIDATES = [
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/a3c69464b629577766c23bcdb12ffbfe3759b923.asset/AssetData/Hanzipen.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/00bfc46ccb002b730e29def5116e0a571fb617d8.asset/AssetData/Hannotate.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/13b8ce423f920875b28b551f9406bf1014e0a656.asset/AssetData/Xingkai.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/88d6cc32a907955efa1d014207889413890573be.asset/AssetData/Kaiti.ttc",
]


def pick_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if not Path(path).exists():
            continue
        for idx in (1, 0) if bold else (0, 1):
            try:
                return ImageFont.truetype(path, size=size, index=idx)
            except OSError:
                continue
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=6)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def paper_background(w: int, h: int, seed: int, tone: str = "#F4E8D4") -> Image.Image:
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h), tone)
    draw = ImageDraw.Draw(img)
    for y in range(56, h, 46):
        color = "#C9B8A0" if (y // 46) % 5 == 4 else "#D9CCBA"
        draw.line([(40, y), (w - 40, y)], fill=color, width=1)
    draw.line([(118, 0), (118, h)], fill="#E8A0A0", width=2)
    for _ in range(6000):
        x, y = rng.randint(0, w - 1), rng.randint(0, h - 1)
        c = rng.randint(228, 248)
        draw.point((x, y), fill=(c, c - 8, c - 18))
    return img


def wavy_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: str, width: int = 2) -> None:
    x0, y0, x1, y1 = box
    for ax, ay, bx, by in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
        draw.line([(ax, ay), (bx, by)], fill=color, width=width)


def finish(img: Image.Image, tilt: float = -0.5) -> Image.Image:
    img = img.rotate(tilt, expand=False, fillcolor="#E8DDD0", resample=Image.Resampling.BICUBIC)
    return img.filter(ImageFilter.GaussianBlur(radius=0.25))


def save(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG", optimize=True)
    print(path)


def draw_cover_life(title: str, subtitle: str, seed: int, doodle: str) -> Image.Image:
    """生活感封面：暖纸 + 简笔画 + 底部标题。"""
    w, h = SIZE
    img = paper_background(w, h, seed, "#EDE4D2")
    draw = ImageDraw.Draw(img)

    if doodle == "tea":
        draw.ellipse((420, 380, 720, 520), outline="#8B6914", width=3)
        draw.arc((460, 320, 680, 420), 200, 340, fill="#8B6914", width=3)
        draw.rectangle((520, 520, 620, 680), fill="#D4C4A8", outline="#8B6914", width=2)
        draw.text((280, 720), "窗台 · 没出门的一天", fill="#8B7355", font=pick_font(28))
    elif doodle == "phone":
        draw.rounded_rectangle((380, 340, 620, 720), radius=28, outline="#4A4A4A", width=4)
        draw.rectangle((410, 400, 590, 640), fill="#E8F0F8", outline="#99AABB")
        draw.text((430, 480), "异地就医\n备案", fill="#2C5282", font=pick_font(26))
        draw.text((260, 760), "茶几上折腾了一下午", fill="#8B7355", font=pick_font(28))
    elif doodle == "map":
        draw.ellipse((340, 320, 900, 900), outline="#C45C26", width=3)
        pts = [(520, 520), (720, 480), (640, 680)]
        labels = ["三亚", "海口", "万宁"]
        for (x, y), lb in zip(pts, labels):
            draw.ellipse((x - 18, y - 18, x + 18, y + 18), fill="#C45C26")
            draw.text((x - 36, y + 22), lb, fill="#3D2914", font=pick_font(30, bold=True))
        draw.text((300, 940), "笔记本上画了三圈", fill="#8B7355", font=pick_font(28))
    elif doodle == "contract":
        draw.rectangle((280, 300, 920, 820), outline="#6B5344", width=2)
        for i in range(6):
            y = 380 + i * 58
            draw.line([(320, y), (860, y)], fill="#C4AD93", width=2)
        draw.text((320, 340), "租房合同 · 草稿", fill="#5C3D2E", font=pick_font(32, bold=True))
        draw.text((300, 880), "没签完，先记雷", fill="#8B7355", font=pick_font(28))

    title_font = pick_font(52, bold=True)
    sub_font = pick_font(26)
    tw, th = text_size(draw, title, title_font)
    draw.text(((w - tw) / 2, h - 280), title, fill="#3D2914", font=title_font)
    sw, _ = text_size(draw, subtitle, sub_font)
    draw.text(((w - sw) / 2, h - 200), subtitle, fill="#8B7355", font=sub_font)
    draw.text((132, 48), "我妈的养老地图", fill="#A08060", font=pick_font(24))
    return finish(img, -0.4)


def draw_table(
    title: str,
    columns: list[str],
    rows: list[list[str]],
    footer: str,
    seed: int,
    col_widths: list[int] | None = None,
) -> Image.Image:
    w, h = SIZE
    img = paper_background(w, h, seed)
    draw = ImageDraw.Draw(img)
    title_font = pick_font(38, bold=True)
    header_font = pick_font(24, bold=True)
    cell_font = pick_font(22)
    small_font = pick_font(20)

    draw.text((132, 36), title, fill="#3D2914", font=title_font)

    if col_widths is None:
        usable = w - 96
        col_widths = [usable // len(columns)] * len(columns)
        col_widths[0] = int(col_widths[0] * 0.85)

    table_x, table_y = 48, 110
    header_h, row_h = 50, 0
    row_heights = []
    for row in rows:
        max_lines = 1
        for c, cell in enumerate(row):
            f = small_font if c > 0 else cell_font
            _, th = text_size(draw, cell, f)
            lines = cell.count("\n") + 1
            rh = max(th + 24, 70 if lines == 1 else 90 + lines * 18)
            max_lines = max(max_lines, rh)
        row_heights.append(max_lines)

    avg_h = min(130, max(88, sum(row_heights) // len(row_heights)))
    row_h = avg_h

    x = table_x
    for col, cw in zip(columns, col_widths):
        wavy_rect(draw, (x, table_y, x + cw, table_y + header_h), "#B8896A", 2)
        tw, th = text_size(draw, col, header_font)
        draw.text((x + (cw - tw) / 2, table_y + (header_h - th) / 2), col, fill="#5C3D2E", font=header_font)
        x += cw

    accent = "#C45C26"
    for r, row in enumerate(rows):
        y = table_y + header_h + r * row_h
        x = table_x
        for c, (cell, cw) in enumerate(zip(row, col_widths)):
            wavy_rect(draw, (x, y, x + cw, y + row_h), "#C4AD93", 1)
            f = header_font if c == 0 else (small_font if "\n" in cell or len(cell) > 8 else cell_font)
            color = accent if c == 0 or "★" in cell or "倾向" in cell else "#2C2418"
            tw, th = text_size(draw, cell, f)
            tx = x + 8 if c >= 3 else x + max(6, (cw - tw) / 2)
            ty = y + max(8, (row_h - th) / 2)
            draw.multiline_text((tx, ty), cell, fill=color, font=f, spacing=4, align="left" if c >= 3 else "center")
            x += cw

    fy = table_y + header_h + len(rows) * row_h + 24
    draw.text((table_x + 8, fy), footer, fill="#8B7355", font=small_font)
    return finish(img)


def draw_checklist_note10() -> Image.Image:
    w, h = SIZE
    img = paper_background(w, h, 10)
    draw = ImageDraw.Draw(img)
    title_font = pick_font(40, bold=True)
    body_font = pick_font(30)
    note_font = pick_font(24)

    draw.text((120, 48), "我妈医保异地 · 我记的 steps", fill="#3D2914", font=title_font)
    draw.text((120, 108), "（以国家医保服务平台 App + 12333 为准，各地不同）", fill="#8B7355", font=note_font)

    steps = [
        ("① 先搞清楚", "不是转走，是「备案」\n参保地还在老家"),
        ("② App 办", "异地就医备案 → 选类型\n填海南实际住址（租房可）"),
        ("③ 留底", "截屏成功页 + 打 12333 问\n要不要每年确认"),
    ]
    y = 200
    for head, body in steps:
        wavy_rect(draw, (80, y, w - 80, y + 200), "#B8896A", 2)
        draw.text((110, y + 20), head, fill="#C45C26", font=pick_font(32, bold=True))
        draw.multiline_text((110, y + 68), body, fill="#2C2418", font=body_font, spacing=8)
        y += 220

    draw.text((100, y + 40), "我踩的坑：跑去窗口排队，大姐说 App 就行。", fill="#6B5344", font=note_font)
    draw.text((100, y + 90), "吉林口头说每年 3 月确认 — 你必须自己核实。", fill="#A0522D", font=note_font)
    return finish(img, -0.5)


def draw_nav_sketch() -> Image.Image:
    """万宁 5 分钟 vs 23 分钟示意（手绘风，非真实地图）。"""
    w, h = SIZE
    img = paper_background(w, h, 11, "#F2EADC")
    draw = ImageDraw.Draw(img)
    f_title = pick_font(36, bold=True)
    f = pick_font(26)
    draw.text((100, 40), "万宁 · 中介说 5 分钟到沙滩", fill="#3D2914", font=f_title)
    draw.text((100, 100), "我步行导航量的（同一条路）", fill="#8B7355", font=f)

    draw.ellipse((120, 200, 280, 320), outline="#4A7C59", width=3)
    draw.text((140, 250), "住处", fill="#2C2418", font=f)
    draw.ellipse((900, 180, 1080, 340), outline="#1E6BA8", width=3)
    draw.text((920, 240), "沙滩", fill="#2C2418", font=f)

    draw.line([(280, 260), (520, 400), (700, 480), (900, 260)], fill="#C45C26", width=4)
    draw.text((480, 420), "实际约 23 分钟\n2 个红绿灯", fill="#C45C26", font=pick_font(28, bold=True))

    draw.line([(280, 300), (900, 300)], fill="#9AB", width=2)
    draw.text((400, 310), "中介标的 5 分钟（按车程？）", fill="#6B5344", font=f)

    draw.text((100, h - 200), "建议：自己走一遍再签租约", fill="#5C3D2E", font=pick_font(30))
    return finish(img, 0.3)


def draw_three_pitfalls() -> Image.Image:
    w, h = SIZE
    img = paper_background(w, h, 15)
    draw = ImageDraw.Draw(img)
    draw.text((120, 44), "候鸟租房 · 我家踩过的 3 个雷", fill="#3D2914", font=pick_font(42, bold=True))
    items = [
        ("雷 1 · 望海", "隔条马路 + 楼后面\n侧脖子才能看见海，月租还按海景算"),
        ("雷 2 · 距离", "步行 5 分钟 → 实测 23 分钟\n中介说按车程算"),
        ("雷 3 · 租期", "11 月前订价、季租再续\n合同看清短租证 / 押金 / 维修"),
    ]
    y = 140
    for head, body in items:
        wavy_rect(draw, (70, y, w - 70, y + 240), "#C45C26" if "1" in head else "#B8896A", 2)
        draw.text((100, y + 16), head, fill="#C45C26", font=pick_font(34, bold=True))
        draw.multiline_text((100, y + 72), body, fill="#2C2418", font=pick_font(28), spacing=6)
        y += 270
    draw.text((90, y + 20), "我妈原话：能买菜、能去医院，比望海重要。", fill="#6B5344", font=pick_font(26))
    return finish(img)


def main() -> None:
    random.seed(20260605)
    climate_script = ROOT / "tools" / "gen_climate_table_handwritten.py"
    if climate_script.exists():
        subprocess.run([sys.executable, str(climate_script)], check=True)

    specs = [
        (draw_cover_life("候鸟冬天去哪", "8 城气候 · 手写表", 11, "tea"), ASSETS / "note11-cover.png"),
        (draw_checklist_note10(), ASSETS / "note10-checklist-handwritten.png"),
        (draw_cover_life("我妈医保异地", "备案 · 别白跑窗口", 10, "phone"), ASSETS / "note10-cover.png"),
        (
            draw_table(
                "海南三城 · 替我妈跑了一遍",
                ["城市", "月租体感", "医院", "沙滩距离", "我家"],
                [
                    ["三亚", "淡季 3.5k+", "2 家三甲远", "舒服", "太贵"],
                    ["海口", "2k 左右两居", "多，西海岸", "阴风大", "倾向 ★"],
                    ["万宁", "中介 2k 海景", "1 家三甲小", "5→23 分", "度假行"],
                ],
                "不是越贵越好 · 数字自己再核实",
                1,
                [100, 200, 180, 200, 160],
            ),
            ASSETS / "note01-compare-three-cities.png",
        ),
        (draw_cover_life("三亚海口万宁", "三城怎么选", 1, "map"), ASSETS / "note01-cover.png"),
        (draw_nav_sketch(), ASSETS / "note01-walk-5-vs-23.png"),
        (draw_cover_life("候鸟租房", "3 个雷别踩", 15, "contract"), ASSETS / "note15-cover.png"),
        (draw_three_pitfalls(), ASSETS / "note15-three-pitfalls.png"),
    ]
    for img, path in specs:
        save(img, path)

    print("\n配图清单见 assets/README-note-images.md")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""生成 #11 候鸟城市气候对比表（第 2 张配图用 PNG + CSV）。"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
OUT_PNG = OUT_DIR / "note11-climate-table.png"
OUT_CSV = OUT_DIR / "note11-climate-table.csv"

COLUMNS = [
    "城市",
    "冬均温体感",
    "夏均温体感",
    "湿度",
    "我妈一句话",
    "适合季节",
]

ROWS = [
    [
        "三亚",
        "22–26℃\n暖、闷潮",
        "30–33℃\n闷热",
        "高",
        "贵，膝盖会酸",
        "冬主力",
    ],
    [
        "海口",
        "18–24℃\n阴雨、风大",
        "30–32℃\n闷",
        "中高",
        "手指老划这边",
        "冬主力 ★",
    ],
    [
        "万宁",
        "17–22℃\n海边风硬",
        "28–31℃\n潮",
        "高",
        "待两天想回酒店",
        "冬短住",
    ],
    [
        "北海",
        "14–18℃\n屋里冷",
        "28–30℃\n闷",
        "很高",
        "第二天就流鼻涕",
        "冬慎用",
    ],
    [
        "昆明",
        "8–15℃\n晒干凉",
        "20–24℃\n舒服",
        "冬干",
        "不像海边，要防晒",
        "夏避暑 ★",
    ],
    [
        "大理",
        "3–12℃\n早晚冷",
        "18–26℃\n干爽",
        "干",
        "腿疼，没多待",
        "夏短住",
    ],
    [
        "厦门",
        "12–18℃\n海风",
        "28–32℃\n潮热",
        "中",
        "看完房价没吭声",
        "短住均可",
    ],
    [
        "威海",
        "−2–5℃\n风像刀片",
        "22–28℃\n海风",
        "冬干夏湿",
        "当天说不考虑",
        "夏 ★",
    ],
]

FOOTER = "体感为主，数字请发前对照当地气象 / 自家感受核对"


def pick_chinese_font() -> str:
    candidates = [
        "PingFang SC",
        "Heiti SC",
        "STHeiti",
        "Arial Unicode MS",
        "Noto Sans CJK SC",
        "SimHei",
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    return "sans-serif"


def write_csv() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for row in ROWS:
            writer.writerow([c.replace("\n", " ") for c in row])


def write_png(font_name: str) -> None:
    plt.rcParams["font.sans-serif"] = [font_name]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(11.5, 7.2), dpi=200)
    fig.patch.set_facecolor("#FFF6ED")
    ax.set_axis_off()

    table = ax.table(
        cellText=ROWS,
        colLabels=COLUMNS,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    table.scale(1.0, 2.15)

    header_color = "#E8A87C"
    row_colors = ["#FFFCF7", "#FFF0E0"]
    accent = "#C45C26"

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#D4B896")
        cell.set_linewidth(0.8)
        if row == 0:
            cell.set_facecolor(header_color)
            cell.set_text_props(weight="bold", color="#3D2914", fontsize=10)
            cell.set_height(0.09)
        else:
            cell.set_facecolor(row_colors[(row - 1) % 2])
            if col == 0:
                cell.set_text_props(weight="bold", color=accent)
            if col == 5 and "★" in str(cell.get_text().get_text()):
                cell.set_text_props(weight="bold", color=accent)

    ax.set_title(
        "我妈考察过的 8 个候鸟城市 · 气候体感表",
        fontsize=14,
        fontweight="bold",
        color="#3D2914",
        pad=18,
    )
    fig.text(
        0.5,
        0.02,
        FOOTER,
        ha="center",
        fontsize=8,
        color="#8B7355",
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(
        OUT_PNG,
        bbox_inches="tight",
        pad_inches=0.35,
        facecolor=fig.get_facecolor(),
    )
    plt.close()


def main() -> None:
    font = pick_chinese_font()
    write_csv()
    write_png(font)
    print(f"PNG: {OUT_PNG}")
    print(f"CSV: {OUT_CSV}")
    print(f"Font: {font}")


if __name__ == "__main__":
    main()

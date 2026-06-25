#!/usr/bin/env python3
"""生成纯文本配图 PNG（1242×1660）— 定稿标准 2026-06，勿改回假 iOS 头。

规格锁定：灰底 #EBEBEB、白卡片、TEXT_PAD=120、TOP_INSET=96、字号 38 起、无状态栏。
改规格前先读 references/image-pipeline.md §定稿视觉规格。
"""

from __future__ import annotations

import random
from datetime import date, datetime
from pathlib import Path

from memo_presets import FOOTER_DATE

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "usable"
SIZE = (1242, 1660)

MARGIN_X = 48
TEXT_PAD = 120
CARD_TOP = 56
CARD_BOTTOM = 56
TOP_INSET = 96


def _text_x() -> int:
    return MARGIN_X + TEXT_PAD


def _text_right() -> int:
    return SIZE[0] - MARGIN_X - TEXT_PAD


def _max_text_w() -> int:
    return _text_right() - _text_x() - 8


def _card_box() -> tuple[int, int, int, int]:
    w, h = SIZE
    return MARGIN_X, CARD_TOP, w - MARGIN_X, h - CARD_BOTTOM


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/00bfc46ccb002b730e29def5116e0a571fb617d8.asset/AssetData/Hannotate.ttc",
    ]
    for path in paths:
        if not Path(path).exists():
            continue
        try:
            return ImageFont.truetype(path, size=size, index=index)
        except OSError:
            continue
    return ImageFont.load_default()


def _text_width(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont) -> float:
    if hasattr(draw, "textlength"):
        return draw.textlength(text, font=f)
    bbox = draw.textbbox((0, 0), text, font=f)
    return bbox[2] - bbox[0]


def wrap_line(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, max_w: float) -> list[str]:
    if not text.strip():
        return [""]
    max_w = max_w if max_w > 0 else _max_text_w()
    if _text_width(draw, text, f) <= max_w:
        return [text]
    parts: list[str] = []
    buf = ""
    for ch in text:
        trial = buf + ch
        if _text_width(draw, trial, f) <= max_w:
            buf = trial
        else:
            if buf:
                parts.append(buf)
            buf = ch
    if buf:
        parts.append(buf)
    return parts or [text]


def _block_height(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, spacing: int) -> int:
    if not text.strip():
        return 16
    bbox = draw.multiline_textbbox((0, 0), text, font=f, spacing=spacing)
    return bbox[3] - bbox[1] + 12


def _expand_lines(draw: ImageDraw.ImageDraw, raw_lines: list[str], body_f, section_f, meta_f) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for line in raw_lines:
        if not line.strip():
            out.append(("blank", ""))
            continue
        if line.startswith("【"):
            style, f = "section", section_f
        elif line.startswith("—"):
            style, f = "meta", meta_f
        else:
            style, f = "body", body_f
        for wrapped in wrap_line(draw, line, f, _max_text_w()):
            out.append((style, wrapped))
    return out


def _content_height(
    draw: ImageDraw.ImageDraw,
    title: str,
    expanded: list[tuple[str, str]],
    title_f,
    body_f,
    section_f,
    meta_f,
) -> int:
    h = TOP_INSET + _block_height(draw, title, title_f, 6) + 36
    for style, text in expanded:
        if style == "blank":
            h += 14
        elif style == "section":
            h += _block_height(draw, text, section_f, 6)
        elif style == "meta":
            h += _block_height(draw, text, meta_f, 6)
        else:
            h += _block_height(draw, text, body_f, 8)
    return h + 48


def _pick_sizes(title: str, lines: list[str], card_h: int) -> tuple[int, int]:
    probe = ImageDraw.Draw(Image.new("RGB", SIZE))
    budget = card_h - 24
    for body_size in range(38, 22, -1):
        title_size = min(body_size + 8, 46)
        title_f = font(title_size, 1)
        body_f = font(body_size)
        section_f = font(body_size, 1)
        meta_f = font(max(body_size - 2, 20))
        expanded = _expand_lines(probe, lines, body_f, section_f, meta_f)
        if _content_height(probe, title, expanded, title_f, body_f, section_f, meta_f) <= budget:
            return title_size, body_size
    return 24, 22


def format_publish_date(d: date) -> str:
    """页脚日期：发笔记当天，格式 M.D（例 6.5）。"""
    return f"{d.month}.{d.day}"


def resolve_footer(footer: str, publish_date: date | None = None) -> str:
    if footer == FOOTER_DATE:
        d = publish_date or date.today()
        return format_publish_date(d)
    return footer


def add_grain(img: Image.Image, seed: int = 7) -> Image.Image:
    rng = random.Random(seed)
    w, h = img.size
    noise = Image.new("RGB", (w, h))
    nd = ImageDraw.Draw(noise)
    for _ in range(w * h // 5):
        x, y = rng.randint(0, w - 1), rng.randint(0, h - 1)
        g = rng.randint(238, 252)
        nd.point((x, y), fill=(g, g, g))
    return Image.blend(img, noise, 0.025)


def render_memo(
    title: str,
    lines: list[str],
    footer: str,
    filename: str,
    seed: int = 7,
    out_dir: Path | None = None,
    publish_date: date | None = None,
) -> Path:
    w, h = SIZE
    img = Image.new("RGB", (w, h), "#EBEBEB")
    draw = ImageDraw.Draw(img)

    x0, y0, x1, y1 = _card_box()
    card_h = y1 - y0
    draw.rounded_rectangle((x0, y0, x1, y1), radius=16, fill="#FFFFFF")

    title_size, body_size = _pick_sizes(title, lines, card_h)
    title_f = font(title_size, 1)
    body_f = font(body_size)
    section_f = font(body_size, 1)
    meta_f = font(max(body_size - 2, 20))
    footer_f = font(max(body_size - 2, 20))

    expanded = _expand_lines(draw, lines, body_f, section_f, meta_f)
    tx = _text_x()
    y = y0 + TOP_INSET

    draw.text((tx, y), title, fill="#111111", font=title_f)
    y += _block_height(draw, title, title_f, 6) + 32

    footer_y = y1 - 52
    for style, text in expanded:
        if style == "blank":
            y += 14
            continue
        if style == "section":
            f, color, spacing = section_f, "#C45C26", 6
        elif style == "meta":
            f, color, spacing = meta_f, "#8E8E93", 6
        else:
            f, color, spacing = body_f, "#1C1C1E", 8
        draw.text((tx, y), text, fill=color, font=f)
        y += _block_height(draw, text, f, spacing)

    resolved_footer = resolve_footer(footer, publish_date)
    if resolved_footer.strip():
        draw.text((tx, footer_y), resolved_footer, fill="#AEAEB2", font=footer_f)

    img = add_grain(img, seed)
    dest = (out_dir or OUT) / filename
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, format="PNG", optimize=True)
    return dest


def main() -> None:
    from memo_presets import NOTE_ASSETS

    for assets in NOTE_ASSETS.values():
        for fname, title, lines, footer, seed in assets:
            p = render_memo(title, lines, footer, fname, seed)
            print(p)


if __name__ == "__main__":
    main()

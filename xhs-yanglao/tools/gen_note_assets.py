#!/usr/bin/env python3
"""
按题号或草稿 YAML 生成笔记配图。

用法:
  python3 tools/gen_note_assets.py --note 11
  python3 tools/gen_note_assets.py --note 10 --date 2026-06-05
  python3 tools/gen_note_assets.py --draft drafts/note11-候鸟冬天去哪.md
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gen_memo_screenshots import render_memo  # noqa: E402
from memo_presets import FOOTER_DATE, NOTE_ASSETS  # noqa: E402


def parse_publish_date(s: str | None) -> date:
    if not s:
        return date.today()
    return datetime.strptime(s, "%Y-%m-%d").date()


def parse_draft_yaml(path: Path) -> tuple[int | None, dict | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end < 0:
        return None, None
    block = text[3:end]
    note = None
    memo = None
    m = re.search(r"^note:\s*(\d+)\s*$", block, re.M)
    if m:
        note = int(m.group(1))
    if "memo:" in block:
        memo = {}
        title_m = re.search(r"title:\s*(.+)", block)
        if title_m:
            memo["title"] = title_m.group(1).strip()
        footer_m = re.search(r"footer:\s*(.+)", block)
        if footer_m:
            raw = footer_m.group(1).strip()
            memo["footer"] = FOOTER_DATE if raw in ("__DATE__", "today", "当天") else raw
        lines_m = re.search(r"lines:\s*\n((?:\s+-\s+.+\n)+)", block)
        if lines_m:
            memo["lines"] = [
                ln.strip()[2:].strip().strip('"')
                for ln in lines_m.group(1).strip().splitlines()
                if ln.strip().startswith("-")
            ]
    return note, memo


def render_note(note: int, publish_date: date, memo_override: dict | None = None) -> list[Path]:
    out: list[Path] = []
    assets = list(NOTE_ASSETS.get(note, []))
    if memo_override and assets:
        fname, _, _, _, seed = assets[0]
        out.append(
            render_memo(
                memo_override.get("title", ""),
                memo_override.get("lines", []),
                memo_override.get("footer", FOOTER_DATE),
                fname,
                seed,
                publish_date=publish_date,
            )
        )
        assets = assets[1:]
    for fname, title, lines, footer, seed in assets:
        out.append(
            render_memo(title, lines, footer, fname, seed, publish_date=publish_date)
        )
    if memo_override and not NOTE_ASSETS.get(note):
        out.append(
            render_memo(
                memo_override["title"],
                memo_override["lines"],
                memo_override.get("footer", FOOTER_DATE),
                f"note{note:02d}-memo-custom.png",
                note,
                publish_date=publish_date,
            )
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="生成笔记纯文本配图")
    ap.add_argument("--note", type=int, action="append")
    ap.add_argument("--draft", type=Path)
    ap.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="发笔记日期（页脚显示为 M.D）；默认今天",
    )
    args = ap.parse_args()

    publish_date = parse_publish_date(args.date)
    paths: list[Path] = []
    if args.draft:
        note, memo = parse_draft_yaml(args.draft)
        if note is None:
            print("草稿无 note: 字段", file=sys.stderr)
            sys.exit(1)
        paths.extend(render_note(note, publish_date, memo))
    if args.note:
        for n in args.note:
            paths.extend(render_note(n, publish_date))

    if not paths:
        ap.print_help()
        sys.exit(1)

    print(f"\n发布日期页脚: {publish_date.month}.{publish_date.day}")
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()

"""备忘录配图文案预设（用户按题号扩展）。

规则：
- 标题：短、像随手记的；不要序号（①②、1 2）、不要「替我整理」
- 正文：禁止内部题号（如 #19）
- 页脚日期：写 FOOTER_DATE，出图时由 gen_note_assets.py 填入发布日
- 出图：python3 tools/gen_note_assets.py --note N [--date YYYY-MM-DD]
"""

FOOTER_DATE = "__DATE__"

# (filename, title, lines, footer, seed)
# 示例结构 — 用户为自己的笔记添加条目：
#
# NOTE_SAMPLE = (
#     "note01-memo-sample.png",
#     "短标题",
#     ["第一行正文", "第二行", ""],
#     FOOTER_DATE,
#     1,
# )

NOTE_ASSETS: dict[int, list[tuple]] = {
    # 1: [NOTE_SAMPLE],
}


def assert_no_internal_refs() -> None:
    import re

    bad_hash = re.compile(r"#\d+")
    bad_title_num = re.compile(r"[①②③]|\s[12]$")
    for assets in NOTE_ASSETS.values():
        for _fn, title, lines, footer, _seed in assets:
            if bad_title_num.search(title):
                raise ValueError(f"标题含序号: {title!r}")
            for text in [title, footer, *lines]:
                if bad_hash.search(text):
                    raise ValueError(f"配图文案含内部题号: {text!r}")


assert_no_internal_refs()

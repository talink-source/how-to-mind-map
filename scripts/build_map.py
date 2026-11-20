#!/usr/bin/env python3
"""Build an interactive "how?" mind map (HTML) and a Markdown copy from an outline file.

Outline format (2 spaces per level):
  - Node title            <- a node: a job someone decides to do
    : Note text           <- a note attached to the node above (not a node)
    : ? Question          <- an open question for the owner, shown as "needs input" in the map
    - Child node          <- answers "how?" for its parent

Usage:
  python3 build_map.py outline.txt --title "How to drive growth for a company" \
      --out-html mind-map.html --out-md mind-map.md [--ratings ratings.json] [--eyebrow "Sam's mind map"]
"""
import argparse, json, html, os, sys

def parse(path):
    root, stack = None, []
    for i, raw in enumerate(open(path, encoding="utf-8"), 1):
        if not raw.strip():
            continue
        ind = len(raw) - len(raw.lstrip(" "))
        s = raw.strip()
        if ind % 2:
            sys.exit(f"Line {i}: indentation must be a multiple of 2 spaces")
        if s.startswith("- "):
            lvl = ind // 2
            node = {"t": s[2:].strip(), "n": [], "c": []}
            while stack and stack[-1][0] >= lvl:
                stack.pop()
            if stack:
                if lvl != stack[-1][0] + 1:
                    sys.exit(f"Line {i}: '{node['t']}' skips a level")
                stack[-1][1]["c"].append(node)
            elif root is None:
                root = node
            else:
                sys.exit(f"Line {i}: only one top node is allowed")
            stack.append((lvl, node))
        elif s.startswith(": "):
            if not stack:
                sys.exit(f"Line {i}: a note must follow a node")
            stack[-1][1]["n"].append(s[2:].strip())
        else:
            sys.exit(f"Line {i}: lines must start with '- ' (node) or ': ' (note)")
    if root is None:
        sys.exit("The outline is empty")
    return root

def stats(root):
    levels, leaves = {}, []
    stats.questions = 0
    def walk(n, d):
        levels[d] = levels.get(d, 0) + 1
        stats.questions += sum(1 for x in n["n"] if x.startswith("? "))
        if not n["c"]:
            leaves.append(d)
        for c in n["c"]:
            walk(c, d + 1)
    walk(root, 1)
    return levels, leaves

def to_md(root, title):
    out = [f"# {title}", "",
           "Each bullet is a node. Each child answers \"how?\" for its parent. Italic lines are notes on that node, not nodes.", ""]
    def walk(n, d):
        ind = "    " * d
        out.append(f"{ind}- **{n['t']}**" if d < 3 else f"{ind}- {n['t']}")
        for x in n["n"]:
            out.append(f"{ind}  **Open question:** {x[2:]}" if x.startswith("? ") else f"{ind}  *{x}*")
        for c in n["c"]:
            walk(c, d + 1)
    walk(root, 0)
    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outline")
    ap.add_argument("--title", required=True)
    ap.add_argument("--out-html", default="mind-map.html")
    ap.add_argument("--out-md", default="mind-map.md")
    ap.add_argument("--split", action="append", default=[], help=argparse.SUPPRESS)  # kept so older commands still run
    ap.add_argument("--eyebrow", default="", help="Small label shown above the title, such as the owner's name")
    ap.add_argument("--ratings", help="Ratings JSON copied or saved from the map, to build them into the HTML")
    ap.add_argument("--template", default=os.path.join(os.path.dirname(__file__), "..", "assets", "template.html"))
    a = ap.parse_args()
    root = parse(a.outline)
    split = [root["t"]] + a.split
    tpl = open(a.template, encoding="utf-8").read()
    ratings = {}
    if a.ratings:
        raw = json.load(open(a.ratings, encoding="utf-8"))
        raw = raw.get("ratings", raw)
        ratings = {k: int(v) for k, v in raw.items() if str(v).isdigit() and 0 < int(v) <= 4}
    data = json.dumps(root, ensure_ascii=False).replace("</", "<\\/")
    page = (tpl.replace("__TITLE__", html.escape(a.title))
               .replace("__EYEBROW__", html.escape(a.eyebrow))
               .replace("__DATA__", data)
               .replace("__RATINGS__", json.dumps({"savedAt": (int(__import__("time").time()*1000) if ratings else 0), "ratings": ratings}, ensure_ascii=False).replace("</", "<\\/"))
               .replace("__SPLIT__", json.dumps(split, ensure_ascii=False).replace("</", "<\\/")))
    open(a.out_html, "w", encoding="utf-8").write(page)
    open(a.out_md, "w", encoding="utf-8").write(to_md(root, a.title))
    levels, leaves = stats(root)
    print(f"Nodes: {sum(levels.values())}  Deepest level: {max(levels)}  Bottom-of-branch tasks: {len(leaves)}")
    print("Nodes per level: " + ", ".join(f"L{k}={v}" for k, v in sorted(levels.items())))
    print(f"Open questions for the owner: {stats.questions}")
    if a.ratings:
        print(f"Ratings built in: {len(ratings)}")
    shallow = sorted(set(d for d in leaves if d <= 6))
    if shallow:
        print(f"Branches ending at level 6 or above: {sum(1 for d in leaves if d <= 6)} (check these are truly calendar-level tasks)")

if __name__ == "__main__":
    main()

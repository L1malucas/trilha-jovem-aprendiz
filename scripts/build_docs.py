#!/usr/bin/env python3
"""Copia trila-jovens-aprendiz/*.md para docs/ adicionando frontmatter Docusaurus."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "trila-jovens-aprendiz"
DST = ROOT / "docs"
DST.mkdir(parents=True, exist_ok=True)

TITLES = {
    1: "Git",
    2: "Padrões de Projeto",
    3: "Sistemas de Numeração",
    4: "Circuitos Digitais",
    5: "Arquitetura de Computadores",
    6: "Sistemas Operacionais",
    7: "Redes de Computadores e Web",
    8: "Linguagens de Programação",
    9: "Algoritmos e Lógica de Programação",
    10: "HTML & CSS",
    11: "MongoDB",
    12: "SQL Server",
    13: "JavaScript / Node.js",
}

def frontmatter(id_, title, position, extra=""):
    return f"---\nid: {id_}\ntitle: \"{title}\"\nsidebar_position: {position}\n{extra}---\n\n"

count = 0
for path in sorted(SRC.glob("*.md")):
    name = path.stem
    text = path.read_text(encoding="utf-8")

    if name == "00_indice":
        fm = frontmatter("00_indice", "Trilha Jovem Aprendiz — Índice", 0, extra="slug: /\nsidebar_label: \"Índice\"\n")
        (DST / "00_indice.md").write_text(fm + text, encoding="utf-8")
        count += 1
        continue

    m = re.match(r"^(\d+)_([a-z0-9-]+)-(teoria|pratica)$", name)
    if not m:
        print(f"SKIP (no match): {name}")
        continue
    num, slug, kind = int(m.group(1)), m.group(2), m.group(3)
    if num not in TITLES:
        print(f"SKIP (unknown module number {num}): {name}")
        continue

    base_title = f"Módulo {num:02d} — {TITLES[num]}"
    if kind == "teoria":
        title = base_title
        position = num * 10
    else:
        title = f"{base_title} — Prática"
        position = num * 10 + 1

    fm = frontmatter(name, title, position)
    (DST / f"{name}.md").write_text(fm + text, encoding="utf-8")
    count += 1

print(f"Wrote {count} files to {DST}")

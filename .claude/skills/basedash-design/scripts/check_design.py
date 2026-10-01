#!/usr/bin/env python3
"""Verifica violações das regras do Basedash Design System em .html/.css/.jinja."""
import re, sys, pathlib

PALETTE = {"#000000","#050607","#ffffff","#e8eaee","#b3b3b3","#808080","#333333","#9984d8","#3fcb7f"}
ALLOWED_RADIUS = {"0","6px","16px","999px","50%","inherit","none"}

def norm(h):
    h = h.lower()
    return "#"+"".join(c*2 for c in h[1:]) if len(h) == 4 else h

def check(path):
    txt = pathlib.Path(path).read_text(errors="ignore")
    errs = []
    for m in re.finditer(r"box-shadow\s*:\s*([^;}\n]+)", txt):
        if m.group(1).strip() not in ("none", "0"):
            errs.append(f"box-shadow proibido: {m.group(0).strip()}")
    for m in re.finditer(r"border-radius\s*:\s*([^;}\n]+)", txt):
        v = m.group(1).strip().replace("var(--radius-buttons)","6px").replace("var(--radius-cards)","16px").replace("var(--radius-badges)","999px")
        if v not in ALLOWED_RADIUS and not v.startswith("var("):
            errs.append(f"raio fora de 6/16/999px: {m.group(0).strip()}")
    for m in re.finditer(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", txt):
        if norm(m.group(0)) not in PALETTE:
            errs.append(f"cor fora da paleta: {m.group(0)}")
    if re.search(r"prefers-color-scheme\s*:\s*light|data-theme=.?light", txt):
        errs.append("modo claro não é permitido (tema somente escuro)")
    if re.search(r"(h1|h2)[^{]*\{[^}]*font-family\s*:\s*[^;]*inter", txt, re.I):
        errs.append("Inter em h1/h2 proibido (usar serifa de display)")
    return errs

if __name__ == "__main__":
    bad = 0
    for f in sys.argv[1:]:
        e = check(f)
        for x in e: print(f"{f}: {x}")
        bad += len(e)
    print("OK — nenhuma violação" if not bad else f"{bad} violação(ões)")
    sys.exit(1 if bad else 0)

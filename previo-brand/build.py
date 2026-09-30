#!/usr/bin/env python3
"""Sestaví samostatné šablony: src/*.html -> templates/*.html.

Do každé šablony vloží font Inter (base64) a logo (inline SVG), takže výsledný
HTML soubor funguje kdekoli bez složek fonts/ a logo/. Spuštění: python3 build.py
"""
import base64, re, pathlib

root = pathlib.Path(__file__).parent

def font_css():
    out = []
    for family, weight, fname in [("Inter", 400, "Inter-Regular.ttf"), ("Inter Medium", 500, "Inter-Medium.ttf")]:
        b64 = base64.b64encode((root / "fonts" / fname).read_bytes()).decode()
        out.append(f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-style: normal; '
                   f'src: url("data:font/ttf;base64,{b64}") format("truetype"); }}')
    return "\n".join(out)

def logo_svg(variant):
    svg = (root / "logo" / f"previo-logo-{variant}.svg").read_text().strip()
    return f'<span class="logo" role="img" aria-label="Previo">{svg}</span>'

fonts = font_css()
(root / "templates").mkdir(exist_ok=True)
for src in sorted((root / "src").glob("*.html")):
    html = src.read_text()
    html = html.replace("/*%%FONTS%%*/", fonts)
    html = re.sub(r"%%LOGO:(color|black|white)%%", lambda m: logo_svg(m.group(1)), html)
    assert "%%" not in html, f"nevyřešený marker v {src.name}"
    (root / "templates" / src.name).write_text(html)
    print(f"{src.name}: {len(html)//1024} KB")

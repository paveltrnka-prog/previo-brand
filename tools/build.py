#!/usr/bin/env python3
"""Builds the self-contained templates: tools/src/*.html -> previo-brand/templates/*.html.

Embeds the Inter font (base64) and the logo (inline SVG) into every template, so the
resulting HTML file works anywhere without the fonts/ and logo/ folders.
Run from anywhere: python3 tools/build.py
"""
import base64, re, pathlib

here = pathlib.Path(__file__).parent
skill = here.parent / "previo-brand"

def font_css():
    out = []
    for family, weight, fname in [("Inter", 400, "Inter-Regular.ttf"), ("Inter Medium", 500, "Inter-Medium.ttf")]:
        b64 = base64.b64encode((skill / "fonts" / fname).read_bytes()).decode()
        out.append(f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-style: normal; '
                   f'src: url("data:font/ttf;base64,{b64}") format("truetype"); }}')
    return "\n".join(out)

def logo_svg(variant):
    svg = (skill / "logo" / f"previo-logo-{variant}.svg").read_text().strip()
    return f'<span class="logo" role="img" aria-label="Previo">{svg}</span>'

fonts = font_css()
(skill / "templates").mkdir(exist_ok=True)
for src in sorted((here / "src").glob("*.html")):
    html = src.read_text()
    html = html.replace("/*%%FONTS%%*/", fonts)
    html = re.sub(r"%%LOGO:(color|black|white)%%", lambda m: logo_svg(m.group(1)), html)
    assert "%%" not in html, f"unresolved marker in {src.name}"
    (skill / "templates" / src.name).write_text(html)
    print(f"{src.name}: {len(html)//1024} KB")

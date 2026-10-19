#!/usr/bin/env python3
"""Renders the icon set: previo-brand/icons/*.svg -> previo-brand/icons/png/<name>-<color>.png.

PowerPoint libraries (python-pptx) cannot insert SVG, so every icon also ships as a transparent
256 px PNG in the three allowed colors. Run after adding or changing an icon: python3 tools/icons.py
"""
import pathlib, subprocess, tempfile  # macOS: uses Chrome + sips

here = pathlib.Path(__file__).parent
icons = here.parent / "previo-brand" / "icons"
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
colors = {"red": "#b50000", "ink": "#202124", "white": "#ffffff"}
size = 256

(icons / "png").mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for svg in sorted(icons.glob("*.svg")):
        for cname, hexv in colors.items():
            page = pathlib.Path(tmp) / f"{svg.stem}-{cname}.html"
            page.write_text(f'<html><body style="margin:0;height:100vh;display:grid;place-items:center;background:transparent;color:{hexv}">'
                            f'<div style="width:{size}px;height:{size}px">'
                            + svg.read_text().replace('width="24" height="24"', 'width="{size}" height="{size}" style="display:block"'.format(size=size))
                            + "</div></body></html>")
            png = icons / "png" / f"{svg.stem}-{cname}.png"
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={tmp}/profile",
                            "--default-background-color=00000000", "--window-size=800,800", "--force-device-scale-factor=1",
                            f"--screenshot={png}", page.as_uri()], check=True, capture_output=True, timeout=60)
            # headless Chrome has a minimum window size; render large with the icon centred, then crop the centre
            subprocess.run(["sips", "-c", str(size), str(size), str(png)],
                           check=True, capture_output=True)
    print(len(list((icons / "png").glob("*.png"))), "PNG files")

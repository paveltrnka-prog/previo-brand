#!/usr/bin/env python3
"""Checks a Previo .pptx deck against the grid, and optionally renders it to PNG.

    python3 scripts/check_deck.py deck.pptx [--render out_dir]

Works on any .pptx, built by scripts/build_deck.py or by hand. Needs python-pptx.

Grid check (no rendering needed): on every white content slide it finds the section label, the
headline and the top of the content block and compares them with the grid in
templates/deck-structure.md; it also reports icon tiles smaller than 0.44 in, icons of different
sizes on one slide, a footer logo under 24 px, shapes over the slide edge, text boxes that let PowerPoint shrink or grow text,
and fonts other than Inter / Inter Medium.

--render converts the deck with LibreOffice (soffice) to PDF and PNG (one per slide plus
contact-sheet.png) so you can look at every slide. It loads the bundled Inter into a private
LibreOffice profile, because headless LibreOffice does not see the system fonts, and stops if the
PDF still uses another font: a render with a substitute font would show wrong line breaks.
Needs soffice and pdftoppm (Mac: brew install --cask libreoffice; brew install poppler).
Exit code 1 when the check finds an error.
"""
import argparse, pathlib, shutil, subprocess, sys, tempfile

SKILL = pathlib.Path(__file__).resolve().parent.parent
PX = 914400 / 128  # EMU per px of the 1280 px wide deck.html grid
GRID = {"label": 64, "headline": 100, "content": 268}
TOL = 6           # px tolerance
MIN_TILE = 56     # px = 0.44 in
MIN_LOGO = 24     # px = 0.19 in, footer logo height
FONTS = {"Inter", "Inter Medium"}


def px(v):
    return round(v / PX)


def check(path):
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    from pptx.oxml.ns import qn

    prs = Presentation(path)
    W, H = px(prs.slide_width), px(prs.slide_height)
    errors, warnings, rows = [], [], []
    for n, slide in enumerate(prs.slides, 1):
        shapes = list(slide.shapes)
        fill = slide.background.fill
        try:
            bg = str(fill.fore_color.rgb).lower()
        except (AttributeError, TypeError):
            bg = "ffffff"
        red = bg in ("b50000", "910000")
        for s in shapes:
            if s.left is None:
                continue
            x, y, w, h = px(s.left), px(s.top), px(s.width), px(s.height)
            bleed = s.shape_type == MSO_SHAPE_TYPE.PICTURE and w > W / 3  # photos may go edge to edge
            if not bleed and (x < 0 or y < 0 or x + w > W + 1 or y + h > H + 1):
                errors.append(f"slide {n}: {s.name} reaches over the slide edge")
            if s.has_text_frame and s.text_frame.text.strip():
                body = s.text_frame._txBody.find(qn("a:bodyPr"))
                if body is not None and (body.find(qn("a:normAutofit")) is not None or body.find(qn("a:spAutoFit")) is not None):
                    warnings.append(f"slide {n}: {s.name!r} lets PowerPoint resize text; set auto_size = NONE")
                for p in s.text_frame.paragraphs:
                    for r in p.runs:
                        if r.text.strip() and r.font.name not in FONTS:
                            errors.append(f"slide {n}: font {r.font.name or 'theme default'!r} in {r.text[:30]!r}; use Inter / Inter Medium")
                            break
        if red:
            rows.append((n, "red", "", "", ""))
            continue
        texts = sorted([s for s in shapes if s.has_text_frame and s.text_frame.text.strip() and px(s.top) < 600],
                       key=lambda s: (px(s.top), px(s.left)))
        label = next((s for s in texts if px(s.top) < 90), None)
        head = next((s for s in texts if 90 <= px(s.top) < 200 and px(s.height) >= 50), None)
        body = [s for s in shapes if s.left is not None and px(s.top) >= 230 and px(s.top) < 640
                and not (s.shape_type == MSO_SHAPE_TYPE.PICTURE and px(s.width) > W / 3)]
        top = min((px(s.top) for s in body), default=None)
        rows.append((n, "content", label and px(label.top), head and px(head.top), top))
        for name, got in (("label", label and px(label.top)), ("headline", head and px(head.top)), ("content", top)):
            if got is None:
                warnings.append(f"slide {n}: no {name} found")
            elif abs(got - GRID[name]) > TOL:
                errors.append(f"slide {n}: {name} starts at {got} px, grid says {GRID[name]} px")
        if head is not None and px(head.height) < 110:
            warnings.append(f"slide {n}: headline box is {px(head.height)} px high; reserve two lines (120 px) so content does not move")
        # icon tiles: small squares with a picture centred inside
        pics = [s for s in shapes if s.shape_type == MSO_SHAPE_TYPE.PICTURE and abs(s.width - s.height) < PX and px(s.width) < 60]
        sizes = set()
        for p in pics:
            cx, cy = p.left + p.width / 2, p.top + p.height / 2
            tile = next((s for s in shapes if s.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE and abs(s.width - s.height) < PX
                         and s.left < cx < s.left + s.width and s.top < cy < s.top + s.height and s.width > p.width), None)
            if tile is None:
                continue
            sizes.add(px(tile.width))
            if px(tile.width) < MIN_TILE:
                errors.append(f"slide {n}: icon tile {px(tile.width)} px, min. {MIN_TILE} px (0.44 in)")
            if abs(px(p.width) * 2 - px(tile.width)) > 4:
                warnings.append(f"slide {n}: icon is {px(p.width)} px in a {px(tile.width)} px tile; make it half the tile")
        logos = [s for s in shapes if s.shape_type == MSO_SHAPE_TYPE.PICTURE and px(s.top) >= 656 and s.width > s.height * 1.4]
        for lg in logos:
            if px(lg.height) < MIN_LOGO:
                warnings.append(f"slide {n}: footer logo {px(lg.height)} px high, min. {MIN_LOGO} px (0.19 in); smaller reads as a dash")
        if len(sizes) > 1:
            warnings.append(f"slide {n}: icon tiles of different sizes {sorted(sizes)} px")
    return rows, errors, warnings


def render(path, out):
    soffice, pdftoppm = shutil.which("soffice"), shutil.which("pdftoppm")
    mac = pathlib.Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
    soffice = soffice or (str(mac) if mac.exists() else None)
    if not soffice or not pdftoppm:
        sys.exit("render needs LibreOffice (soffice) and poppler (pdftoppm); Mac: brew install --cask libreoffice; brew install poppler")
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        fonts = pathlib.Path(tmp, "user", "fonts")
        fonts.mkdir(parents=True)
        for f in (SKILL / "fonts").glob("*.ttf"):
            shutil.copy(f, fonts)
        subprocess.run([soffice, f"-env:UserInstallation={pathlib.Path(tmp).as_uri()}", "--headless",
                        "--convert-to", "pdf", "--outdir", str(out), str(path)], check=True, capture_output=True, timeout=300)
    pdf = out / (path.stem + ".pdf")
    used = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout.splitlines()[2:]
    other = sorted({l.split()[0].split("+")[-1] for l in used} - {"Inter-Regular", "Inter-Medium"})
    if other:
        print(f"warning: the render uses {', '.join(other)} instead of Inter; line breaks may differ from PowerPoint", file=sys.stderr)
    for old in out.glob("slide-*.png"):
        old.unlink()
    subprocess.run([pdftoppm, "-png", "-r", "96", str(pdf), str(out / "slide")], check=True)
    pngs = sorted(out.glob("slide-*.png"))
    sheet = out / "contact-sheet.html"
    sheet.write_text("<body style='margin:0;padding:16px;background:#d9d9d9;display:grid;grid-template-columns:repeat(2,640px);gap:16px'>"
                     + "".join(f"<img src='{p.name}' style='width:640px;display:block'>" for p in pngs) + "</body>")
    chrome = pathlib.Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    if chrome.exists():
        rows = (len(pngs) + 1) // 2
        with tempfile.TemporaryDirectory() as prof:
            subprocess.run([str(chrome), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
                            f"--window-size=1328,{16 + rows * 376}", f"--screenshot={out / 'contact-sheet.png'}", sheet.as_uri()],
                           capture_output=True, timeout=60)
    print(f"rendered {len(pngs)} slides to {out}" + (" (contact-sheet.png)" if (out / "contact-sheet.png").exists() else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("deck", type=pathlib.Path)
    ap.add_argument("--render", type=pathlib.Path, metavar="DIR", help="also render PDF + PNG into DIR")
    a = ap.parse_args()
    rows, errors, warnings = check(a.deck)
    print("slide  type     label  headline  content   (grid: 64 / 100 / 268 px)")
    for n, kind, l, h, c in rows:
        print(f"{n:>5}  {kind:<7}  {l if l is not None else '–':>5}  {h if h is not None else '–':>8}  {c if c is not None else '–':>7}")
    for w in dict.fromkeys(warnings):
        print("warning:", w)
    for e in dict.fromkeys(errors):
        print("ERROR:", e)
    print("grid OK" if not errors else f"{len(set(errors))} error(s)")
    if a.render:
        render(a.deck, a.render)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

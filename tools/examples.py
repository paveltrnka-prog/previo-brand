#!/usr/bin/env python3
"""Renders the README examples: fills the built templates with sample content and
screenshots them with headless Chrome into docs/examples/*.png.

Run after tools/build.py: python3 tools/examples.py
Sample content only; the numbers are illustrative, not real Previo data.
"""
import pathlib, re, subprocess, tempfile

here = pathlib.Path(__file__).parent
templates = here.parent / "previo-brand" / "templates"
out = here.parent / "docs" / "examples"
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# (template, viewport width, height, {placeholder: text})
examples = [
    ("onepager", 794, 1123, {
        "{{One-pager title}}": "Alfred online check-in",
        "42 %": "62 %",
        "{{Topic / segment, e.g. Hotels}}": "Alfred · Hotels",
        "{{A concrete claim, not a slogan. What changes and by how much.}}": "Guests check in on their phone before they reach the desk",
        "{{One or two sentences: what the product does differently. Numbers, steps, mechanics; no \"seamless\".}}": "Alfred sends every guest a link 48 hours before arrival. ID scan, registration form and payment happen there; reception only hands over the key.",
        "{{What the number means and where it comes from (source, period).}}": "of guests finish check-in before arrival (sample data, 3-month pilot).",
        "{{Step 1}}": "Guest gets a link by e-mail or SMS",
        "{{Step 2}}": "Scans ID, fills in the form, pays",
        "{{Step 3}}": "Picks up the key or opens the door with the phone",
        "{{Who it is for}}": "Who it is for",
        "{{What is included / what you need}}": "What you need",
        "{{Reference}}": "Reference",
        "{{Hotel name and result.}}": "City hotel, 80 rooms: queue at the desk down from 12 to 3 minutes.",
        "{{Name Surname, role}}": "Previo Sales",
        "{{e-mail}}": "sales@previo.cz",
        "{{phone}}": "+420 000 000 000",
        "{{https://www.previo.cz}}": "https://www.previo.cz",
        "{{previo.cz}}": "previo.cz",
    }, ["{{One sentence.}}", "Hotels and apartments with Previo PMS.", "Previo PMS 2 and a payment gateway."]),
    ("report", 794, 1123, {
        "{{Report title}}": "Q3 2026 bookings",
        "{{Period, e.g. Q3 2026}}": "Q3 2026",
        "{{Report title: what happened, not \"Overview\"}}": "Direct bookings grew faster than OTAs",
        "{{Author}}": "Revenue team",
        "{{date}}": "10/2026",
        "+18 %": "+18 %",
        "{{Key metric and comparison (against what, for which period).}}": "direct bookings, Q3 2026 vs. Q3 2025 (sample data).",
        "{{Chart title}}": "Direct bookings per quarter",
        "{{Chart description for screen readers}}": "Direct bookings per quarter, rising, last quarter highlighted",
        "{{Q2}}": "Q4 25", "{{Q3}}": "Q1 26", "{{Q4}}": "Q2 26",
        "{{Breakdown by …}}": "Breakdown by channel",
        "{{Item}}": "Channel", "{{Value}}": "Bookings", "{{Change}}": "Change",
        "{{Row 1}}": "Direct web", "{{1 240}}": "1 240", "{{+12 %}}": "+18 %",
        "{{Row 2}}": "Booking.com", "{{980}}": "980", "{{−4 %}}": "−4 %",
        "{{Row 3}}": "Phone and e-mail", "{{610}}": "610", "{{0 %}}": "0 %",
        "{{What to do:}}": "What to do:",
        "{{One or two sentences: the recommendation or decision that follows from the data.}}": "Move part of the OTA commission budget into the direct booking engine promo for Q4.",
        "{{Data source, metric definitions, export date.}}": "Source: Previo PMS, confirmed reservations, exported 1 October 2026. Sample data.",
    }, ["{{Q1}}", "Q3 25", "Q3 26"]),
    ("social-feed", 1080, 1350, {
        "{{Topic}}": "Alfred",
        "{{What the figure means, in one sentence}}": "fewer guest questions at reception after Alfred launch",
        "{{Source or detail: period, sample.}}": "Sample data, 3-month pilot in a city hotel.",
        "{{Call to action, e.g. Learn more}}": "See how Alfred works",
        "{{previo.cz}}": "previo.cz",
    }, None),
    ("social-story", 1080, 1920, {
        "{{Topic}}": "New in Plachta",
        "{{A strong claim, max. 8 words}}": "Fill empty nights in one click",
        "{{One sentence with a concrete detail.}}": "AI suggests prices for gaps in the calendar.",
        "{{Call to action}}": "Try it",
    }, None),
    ("social-linkedin", 1200, 627, {
        "{{Topic}}": "Online check-in",
        "{{A claim, not a topic name}}": "Most guests skip the desk queue",
        "{{One sentence with a concrete detail.}}": "ID scan and payment before arrival, key at the desk.",
        "42 %": "62 %",
        "{{What the number means, source and period.}}": "check in before arrival (sample data, 3-month pilot).",
    }, None),
]

out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for name, w, h, fills, seq in examples:
        html = (templates / f"{name}.html").read_text()
        head, body = html.split("<body>", 1)
        for k, v in fills.items():
            body = body.replace(k, v)
        if seq:  # placeholders that repeat with different values, filled in order
            key, *values = seq
            for v in values:
                body = body.replace(key, v, 1)
        left = re.findall(r"\{\{[^}]*\}\}", body)
        assert not left, f"{name}: unfilled {left}"
        page = pathlib.Path(tmp) / f"{name}.html"
        page.write_text(head + "<body>" + body)
        png = out / f"{name}.png"
        subprocess.run([chrome, "--headless", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{h}", f"--screenshot={png}", page.as_uri()],
                       check=True, capture_output=True)
        print(png.relative_to(here.parent))

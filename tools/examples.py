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
    ("deck", 1312, 1896, {
        "{{Deck type, e.g. Offer}}": "Offer",
        "{{Title: what the client gets}}": "Marketing+ for Hotel Example",
        "{{Subtitle: client name, place or one concrete promise}}": "Website, campaigns and pricing from one partner, measured on revenue.",
        "{{Name Surname, role}}": "Previo Sales",
        "{{date}}": "October 2026",
        "{{Headline as a claim}}": "Marketing+ links promotion with sales",
        "{{Two or three sentences of context: why this matters to the client.}}": "Campaigns, website and prices run on data from Previo and follow one goal: higher hotel revenue.",
        "{{Item 1}}": "More direct bookings", "{{Item 2}}": "Better yield per room", "{{Item 3}}": "Ongoing support",
        "{{Headline as a claim about the process}}": "From data audit to a monthly review in five steps",
        "{{Headline as a claim about both groups}}": "Numbers first, then agreed priorities",
        "{{Short claim the photo proves}}": "Mountains and a lake within reach",
        "{{Headline as a claim about the photos}}": "One photo set for website and campaigns",
        "{{A}}": "01", "{{B}}": "02", "{{Column 1}}": "Data audit", "{{Column 2}}": "Kick-off meeting",
        "{{Optional note, e.g. what is not included.}}": "Meta campaigns are part of the basic Marketing+ activities.",
        "{{02}}": "02",
        "{{One strong claim or section title}}": "Phase 1 builds the base for direct bookings",
        "{{Headline as a claim about the number}}": "Commission only grows when your revenue grows",
        "42 %": "15 %",
        "{{What the number means}}": "commission for the first 18 months, then 13 %",
        "{{Source, period or condition.}}": "Plus 6 % of the year-on-year revenue increase, excl. VAT. Sample terms.",
        "{{Closing line, e.g. a next step}}": "Let us start with an audit of your data",
        "{{Name Surname}}": "Previo Sales", "{{e-mail}}": "sales@previo.cz", "{{phone}}": "+420 000 000 000",
    }, [("{{Section}}", "Why Marketing+", "Process", "Steps 01–02", "Terms", "Location", "Results"),
        ("{{Footer: deck title}}",) + ("Marketing+ · Hotel Example",) * 5,
        ("{{One concrete sentence.}}", "New website, campaigns and your own guest database.", "Prices follow demand, season and occupancy.", "One plan for marketing, distribution and operations.",
         "Occupancy, ADR and RevPAR.", "Traffic and booking sources.", "Website, prices, OTA dependence.", "Timeline for both phases."),
        ("{{Item}}", "Previo", "Google Analytics", "Current state", "Schedule"),
        ("{{Step}}", "Audit", "Kick-off", "Phase 1", "Phase 2", "Reporting"),
        ("{{What happens.}}", "Data from Previo, Analytics and campaigns.", "Priorities and who does what.", "Website, campaigns, prices, photos.", "OTA, mailing, restrictions, Hotel Ads.", "Every month, year on year."),
        ("{{Optional single sentence.}}", "Website, campaigns, pricing and photos first.", "Two hours from Prague, open all year."),
        ("{{Caption}}", "Winter: skiing and wellness", "Summer: river and cycle paths", "Trips nearby"),
        ("{{Fact}}", "2 years", "Monthly report", "No setup fee"),
        ("{{Detail.}}", "Contract length, can be extended.", "Year-on-year, with next steps.", "Website and hosting included in the commission."),
    ], "body{background:#d9d9d9;zoom:.5;display:grid;grid-template-columns:1280px 1280px;gap:32px;padding:32px}.slide{margin:0}"),
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
    for name, w, h, fills, seq, *css in examples:
        html = (templates / f"{name}.html").read_text()
        head, body = html.split("<body>", 1)
        for k, v in fills.items():
            body = body.replace(k, v)
        if seq and isinstance(seq[0], str):
            seq = [seq]
        for key, *values in seq or []:  # placeholders that repeat with different values, filled in order
            for v in values:
                body = body.replace(key, v, 1)
        if css:
            head = head.replace("</style>", css[0] + "</style>", 1)
        left = re.findall(r"\{\{[^}]*\}\}", body)
        assert not left, f"{name}: unfilled {left}"
        page = pathlib.Path(tmp) / f"{name}.html"
        page.write_text(head + "<body>" + body)
        png = out / f"{name}.png"
        subprocess.run([chrome, "--headless", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{h}", f"--screenshot={png}", page.as_uri()],
                       check=True, capture_output=True)
        print(png.relative_to(here.parent))

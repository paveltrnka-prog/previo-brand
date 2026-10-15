# previo-brand

A Claude skill that applies the official Previo brand (colors, typography, logo, composition rules)
to visual outputs: decks, PDFs, HTML reports and dashboards, one-pagers, social graphics. The values
come from the Previo design system in Figma (**P – design system**). The skill ships ready-made
templates, so most outputs start from a proven Previo layout.

**Download:** [previo-brand-v4.skill](https://github.com/paveltrnka-prog/previo-brand/releases/download/v4/previo-brand-v4.skill) (v4) · all versions in [Releases](https://github.com/paveltrnka-prog/previo-brand/releases)

## Install

- **Claude Desktop / claude.ai:** Settings → Capabilities → Skills → **Upload skill**, pick the
  `.skill` file, turn on **previo-brand**.
- **Claude Code:** unzip the package so that the folder `previo-brand/` (with `SKILL.md` inside)
  ends up in your Claude Code skills folder, then start a new session.

**Font for PowerPoint/Word:** HTML and PDF outputs carry Inter inside. To open `.pptx`/`.docx` with
the exact look, install `Inter-Regular.ttf` and `Inter-Medium.ttf` from the package's `fonts/`
folder once (Mac: double-click → Install Font; Windows: right-click → Install for all users).
Otherwise share PDFs.

## Use

Just ask; branding happens automatically:

| Ask | What you get |
|---|---|
| "One-pager about Alfred for hoteliers." | `templates/onepager.html`, fixed A4, one big number, facts beside it. |
| "Q3 report from these numbers." | `templates/report.html`: one main chart, table, recommendation. |
| "Instagram post with 42 %." | `social-feed.html`, 4:5, exported to PNG. |
| "Story for the campaign." | `social-story.html`, 9:16, full red, safe zones. |
| "LinkedIn image for an article." | `social-linkedin.html`, 1200 × 627 px. |
| "Client deck, 8 slides." | `.pptx` following `templates/deck-structure.md`. |
| "Show Alfred presenting a new feature." | The mascot `alfred/alfred.svg` next to the content, on a light background. |
| "Plachta mockup with reservation states." | State colors from `tokens.md`. |

Fine-tune in plain words: "less busy", "highlight just one number", "no purple".

## Examples

What the templates look like once Claude fills them in. Sample content, the numbers are
illustrative, not real Previo data.

<table>
  <tr>
    <td width="50%"><img src="docs/examples/onepager.png" alt="One-pager, A4"><br><b>One-pager</b> · A4, one red number as the hero, facts beside it, steps only when sequential.</td>
    <td width="50%"><img src="docs/examples/report.png" alt="Report, A4"><br><b>Report</b> · A4, one key number + one chart with the highlighted bar, table with signed changes, recommendation.</td>
  </tr>
</table>

<table>
  <tr>
    <td width="36%"><img src="docs/examples/social-feed.png" alt="Social feed 4:5"><br><b>Feed 4:5</b> · 1080 × 1350 px.</td>
    <td width="28%"><img src="docs/examples/social-story.png" alt="Story 9:16"><br><b>Story 9:16</b> · 1080 × 1920 px, full red, app UI safe zones.</td>
    <td width="36%"><img src="docs/examples/social-linkedin.png" alt="LinkedIn / OG image"><br><b>LinkedIn / OG</b> · 1200 × 627 px, claim + number.</td>
  </tr>
</table>

## Color roles at a glance

| Color | Role |
|---|---|
| Red `#b50000` | The brand. One hero per page/slide (red area or biggest number) + small signals (section label, CTA, highlighted chart item). |
| Grays `#fafafa → #202124` | Everything else: text, surfaces, dividers, non-highlighted chart items. |
| AI purple `#673AB7` → `#4E2C8B` | AI features in the Previo product UI only. |
| Alfred plum `#6F2F6A` | The Alfred mascot and materials about the Alfred guest app only. |
| Semantic (positive/negative/warning) | State only, always with an icon. |

Full values in [`previo-brand/tokens.md`](previo-brand/tokens.md), rules in
[`previo-brand/SKILL.md`](previo-brand/SKILL.md).

## Feedback

Missing something? Claude writes a short feedback note when a request goes beyond the skill; send it
to the author. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Structure

```
previo-brand/          the skill (this folder is what gets packaged)
├── SKILL.md           rules: when and how to apply the brand
├── tokens.md          values: colors, typography, radius, spacing, CSS variables
├── fonts/             Inter 400 + 500 (SIL OFL 1.1)
├── logo/              color / black / white SVG
├── alfred/            mascot + AI icon
└── templates/         self-contained HTML templates + deck-structure.md (generated, do not edit HTML)
tools/                 maintenance only, not part of the skill
├── src/               template sources (edit here)
├── build.py           builds templates/ from src/ (embeds font + logo)
└── examples.py        renders the README examples into docs/examples/
docs/examples/         README example images
```

## Maintenance (author)

1. Edit `tools/src/*.html`, then run `python3 tools/build.py` and `python3 tools/examples.py`
   (refreshes the example images; needs Google Chrome).
2. Package: `zip -r -X previo-brand-v4.skill previo-brand -x '.*'`.
3. Publish the `.skill` file as a GitHub Release with tag `vN` and update the download link at the
   top of this README. The package is a build artifact and is not committed (`.gitignore`).
   ```bash
   gh release create v4 previo-brand-v4.skill --title "previo-brand v4" --notes "…"
   ```

When the design system changes, update `tokens.md`; `SKILL.md` usually stays as is.

## Changelog

**v4**
- Skill translated to English; description says in three sentences what the skill is for.
- Environment-independent: no machine paths; fonts and logos are embedded into outputs (base64 /
  inline SVG) instead of linked relatively.
- Clear red rule: one hero per page/slide + small signals; decks gray the label when a red number is
  the hero.
- AI purple `#673AB7` (Previo product UI) vs. Alfred plum `#6F2F6A` (mascot, Alfred guest app),
  same values on screen and in print.
- One-pager is fixed A4; overflow is fixed by shortening content, never by stretching the page.
- `INSTALACE.md` removed (install notes are here); template sources and `build.py` moved out of the
  skill to `tools/`.
- New "feedback for the skill author" section instead of a GitHub contribution workflow.

**v3**
- AI purple, Alfred mascot and AI icon, Plachta state colors, HTML templates (one-pager, report,
  social feed/story/LinkedIn), deck structure.

**v2**
- Bundled Inter TTF, three logo variants, semantic colors, `.docx` boundary, anti-"AI slop"
  composition rules.

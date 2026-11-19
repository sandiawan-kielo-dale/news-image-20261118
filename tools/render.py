"""Dev tool (NOT run by the grader): render design/news.html -> entry.png.

Run with the venv that has Playwright + Chromium:
    ~/workspace/custom-skills/airdrop-agent/.venv/bin/python tools/render.py
Also writes /tmp/news-preview-300.png (300 px wide) for legibility review.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "design" / "news.html"
OUT = ROOT / "entry.png"
LIMIT = 1048576


def main() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
        page.goto(HTML.as_uri())
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": 1024, "height": 1024})
        # small preview: same page scaled to 300 px wide
        small = browser.new_page(viewport={"width": 300, "height": 300}, device_scale_factor=1)
        small.goto(HTML.as_uri())
        small.evaluate("document.documentElement.style.zoom = String(300/1024)")
        small.wait_for_timeout(300)
        small.screenshot(path="/tmp/news-preview-300.png")
        browser.close()
    size = OUT.stat().st_size
    print(f"wrote {OUT} ({size} bytes)")
    if size > LIMIT:
        print("ERROR: entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

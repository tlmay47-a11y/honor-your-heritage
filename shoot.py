from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    for c in ["france","england"]:
        url=f"file:///workspace/heritage/{c}/index.html"
        pg=b.new_page(viewport={"width":1200,"height":675},device_scale_factor=1)
        pg.goto(url,wait_until="networkidle"); pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(500)
        pg.screenshot(path=f"/workspace/heritage/{c}/x-post.png")
        pg=b.new_page(viewport={"width":1440,"height":900})
        pg.goto(url,wait_until="networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"/workspace/heritage/{c}/full.png",full_page=True)
    b.close()

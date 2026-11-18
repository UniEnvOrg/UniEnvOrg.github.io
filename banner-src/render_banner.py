"""Render banner.html (light and #dark) to 2x PNGs. usage: render_banner.py HTML OUTDIR"""
import sys, time, pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
html, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2])
o = webdriver.ChromeOptions()
for a in ["--headless=new", "--hide-scrollbars", "--force-device-scale-factor=2"]: o.add_argument(a)
d = webdriver.Chrome(options=o)
try:
    for theme in ("light", "dark"):
        d.set_window_size(1280, 640)
        d.get(html.as_uri() + ("#dark" if theme == "dark" else "")); d.refresh()
        for _ in range(100):
            if d.execute_script("return document.body.dataset.ready"): break
            time.sleep(0.1)
        w, h = d.execute_script("return [innerWidth, innerHeight]")
        if (w, h) != (1280, 640):
            d.set_window_size(1280 + 1280 - w, 640 + 640 - h); time.sleep(.3)
        time.sleep(.5)
        d.find_element(By.TAG_NAME, "body").screenshot(str(out / f"banner-{theme}.png"))
        print(theme, d.execute_script("return [innerWidth, innerHeight]"))
finally: d.quit()

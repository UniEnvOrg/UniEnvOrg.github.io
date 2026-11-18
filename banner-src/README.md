# README / social banner

`banner.html` is the source of `site/img/unienv-banner-{light,dark}.png` (1280x640 at 2x, also GitHub's
social-preview size). Open it in a browser (`#dark` for the dark variant) to edit; regenerate with

```bash
python render_banner.py banner.html out/   # needs selenium + Chrome; writes banner-light.png / banner-dark.png
```

then reduce to a 256-colour palette (Pillow `quantize(colors=256, dither=NONE)`, ~85 KB each) and copy them
to `site/img/` as `unienv-banner-light.png` / `unienv-banner-dark.png`.

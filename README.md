# unienvorg.github.io

The UniEnv project site and the shared docs theme.

| Path | What it is | Published at |
| --- | --- | --- |
| `site/` | Landing page (static HTML, no build step) | <https://unienvorg.github.io/> |
| `docs-theme/` | Material for MkDocs `custom_dir` used by every project's docs | each project's docs, e.g. `/UniEnv/`, `/XBArray/` |

Project docs are separate GitHub Pages sites of their own repos (`UniEnvOrg/UniEnv` →
`/UniEnv/`), so they live in those repos and are versioned there with mike.

## Landing page

Edit `site/index.html` and push to `main`; `.github/workflows/pages.yml` deploys `site/`.
The release chip reads the latest `unienv` version from PyPI in the browser.
Preview locally with any static server, e.g. `python -m http.server -d site`.

## Docs theme

`docs-theme/` holds:

- `main.html`: the cross-project bar above Material's header. The project list is defined
  here; a project only sets `extra.unienv.current` to its own name.
- `unienv/unienv.css`, `unienv/logo.svg`, `unienv/favicon.svg`: palette, typography and
  mkdocstrings styling, copied into every docs build as theme static files.
- `unversioned-404.html`: copied to the root of each project's `gh-pages` by its docs
  workflow; it redirects links from before versioning to the same page under `latest/`.

A project uses it with:

```yaml
theme:
  name: material
  custom_dir: .org-site/docs-theme
  logo: unienv/logo.svg
  favicon: unienv/favicon.svg
extra_css:
  - unienv/unienv.css
extra:
  unienv:
    current: UniEnv
  version:
    provider: mike
```

Its docs workflow checks this repo out into `.org-site/` (sparse, `docs-theme` only), and
`scripts/fetch_docs_theme.sh` in the project does the same for local builds. Theme changes
reach a project's docs on its next docs deploy; already published versions keep the theme
they were built with.

Brand colours (from the logo): blue `#1b5e93`, navy wordmark `#154b7d`, teal `#38ab8c`
(text-safe `#2a8f75`).

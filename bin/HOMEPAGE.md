# Homepage maintenance

The compact English and Chinese homepages are generated from `_pages/about.md`,
`_pages/about_zh.md`, and `_bibliography/papers.bib`. Styles, theme switching, and
fonts live in `assets/homepage/`; publication figures live in
`assets/img/publication_preview/`.

For a homepage-only preview:

```sh
python3 -m pip install pyyaml
python3 bin/build_homepage.py --output _site
python3 -m http.server 8765 --directory _site
```

For a full production build, use the repository's Ruby and Python dependencies:

```sh
JEKYLL_ENV=production sh bin/cibuild
npm exec --yes --package purgecss -- purgecss -c purgecss.config.js
```

The homepage generator runs after Jekyll and replaces only `/index.html` and
`/zh/index.html`, adding their dedicated assets. Other Jekyll pages are preserved.
Run it again after a Jekyll rebuild; a plain `jekyll serve` rebuild restores the
original theme's homepages until the generator runs.

The deployment workflow performs these steps automatically on pushes to `master`
or `main`, then publishes `_site` to `gh-pages`. Keep `CNAME` set to
`sitongfang.com`. A pull request runs the build without publishing.

In `papers.bib`, `selected=true` places a paper in the main list and
`selected=false` places it under the disclosure. Add a `preview` filename to use
a paper figure. Author asterisks are displayed on the page and removed from
exported BibTeX, along with the configured website-only fields.

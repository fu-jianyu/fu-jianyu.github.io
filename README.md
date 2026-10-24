# Jianyu Fu — academic website

Personal academic website of Jianyu Fu (付舰于), a Ph.D. student at The University of Tokyo.

- Live site: <https://fu-jianyu.github.io>
- Framework: Jekyll + al-folio v1 (`al_folio_core 1.0.11`)
- Source: `main`; generated deployment: `gh-pages`
- Maintenance and content update guide: [docs/SITE_MAINTENANCE.md](docs/SITE_MAINTENANCE.md)

## Local development

Use Ruby 3.3, Bundler, Node.js, and ImageMagick.

```sh
bundle install
npm ci
bundle exec jekyll serve
```

Before deployment:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 bin/check_site.py _site
npm run lint:style-contract
npm run test:visual
```

GitHub Actions validates and deploys the site. Keep personal content in `_pages`, `_posts`, `_projects`, `_news`, `_data`, and `_bibliography`; keep theme runtime behavior in the pinned al-folio gems. Template examples are archived under `docs/template-examples` and excluded from publication.

The downloadable CV is exported from `docs/cv/Jianyu_Fu_CV.docx`. Its public path remains `assets/pdf/Jianyu_Fu_CV.pdf`.

## Theme attribution

Built with [al-folio](https://github.com/alshedivat/al-folio), licensed under MIT. The original starter documentation and license remain in this repository.

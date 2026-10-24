# Maintaining Jianyu Fu's academic website

The site uses Jekyll with the existing al-folio v1 plugin architecture. The core runtime remains pinned to `al_folio_core 1.0.11`. Runtime layouts and styles belong to the pinned gems; this update adds no local theme overrides.

## Content sources

| Content                            | File or directory             |
| ---------------------------------- | ----------------------------- |
| Biography and research interests   | `_pages/about.md`             |
| Publication records                | `_bibliography/papers.bib`    |
| Online CV                          | `_data/cv.yml`                |
| Downloadable CV                    | `assets/pdf/Jianyu_Fu_CV.pdf` |
| Corrected Word source              | `docs/cv/Jianyu_Fu_CV.docx`   |
| Research summaries                 | `_projects/`                  |
| Full updates                       | `_posts/`                     |
| Short homepage announcements       | `_news/`                      |
| Contact and academic profile links | `_data/socials.yml`           |

The Word document is the source for the downloadable PDF. After changing it, export to PDF, inspect every page, and replace the file at the same path. Update `_data/cv.yml` separately when dates or content change. The optional RenderCV workflow is manual and only produces an artifact; it does not commit over the Word-derived CV.

## Accepted paper and journal metrics

The R-ECoT paper is accepted on 23 October 2026, awaiting online publication. The acceptance date and corresponding-author status come from the supplied publisher screenshot; author order and initials come from the CV. Do not invent a DOI, volume, issue, pages, or online date.

JCR Q1 and Impact Factor 11.5 are author-supplied journal metrics. No JCR year was supplied, so no year is asserted. JCR Q1 is not the Chinese Academy of Sciences partition system; do not relabel it CAS Q1 or invent an official JCR “Top” designation. Reconfirm the metrics when the article appears online.

When the article is online:

1. Add the verified DOI, URL, publication date, and bibliographic details to `fu2026recot` in `_bibliography/papers.bib`.
2. Update the online CV and the Word/PDF CV.
3. Write a new post introducing the research and add a short `_news` entry. Keep the acceptance post as a dated record, with a link to the new introduction.

## Research visit

The HKU visit ran from 5 August to 10 October 2026, hosted by Prof. Bo Huang in the Department of Geography. The group photo is the lead image and social preview. The four supplied photos are in `assets/img/hku-2026/`; the figure component supplies responsive images and zoom. Photo captions do not infer the identities of other people in the photographs.

## Publication evidence

The public ORCID record at <https://orcid.org/0009-0006-1279-9675> was reviewed on 24 October 2026. Its four historical records are included. Crossref metadata for the three DOI records confirms author order and publication dates. The rooftop paper is dated 2 February 2026 and lists Jianyu Fu second. The two 2022 conference contributions come from the supplied CV and have no invented DOI or full-text links.

LinkedIn: <https://www.linkedin.com/in/jianyu-fu-24507838b/>. This is the author-provided public profile URL; automated fetching did not independently verify its profile content. Teaching and academic service remain hidden until real details are supplied.

## Build and deployment

```sh
bundle install
npm ci
JEKYLL_ENV=production bundle exec jekyll build
python3 bin/check_site.py _site
npm run lint:style-contract
npm run test:visual
bundle exec al-folio upgrade audit
bundle exec al-folio upgrade overrides audit
```

GitHub Actions builds `main` and deploys the generated `_site` to `gh-pages`. Pull requests build without deploying and upload `site-preview`. Keep GitHub Pages configured to serve the `gh-pages` branch root. Concurrency prevents older deployments from racing newer builds.

The visual workflow tests the academic site's real pages at desktop and phone widths. Upstream template parity tests remain available with `npm run test:theme-visual`, but require their original template fixture/baseline environment. The integration workflow restores archived posts only inside its test checkout for the existing comments/distill tests; they never return to the published build.

## Template archive and SEO

Starter example pages, posts, projects, news, and the Einstein JSON CV are retained in `docs/template-examples/`, excluded by Jekyll. Do not move them into public content directories. Search, feed, sitemap, and navigation should include only genuine personal content.

Descriptions, canonical URLs, Open Graph, schema metadata, UTF-8, a favicon, and `robots.txt` use the existing theme features. The build check validates internal links, metadata, JSON-LD and accidental template publication. It does not guarantee search indexing or ranking. Search Console/Bing verification can be enabled after the owner provides a verification token; analytics remain unconfigured.

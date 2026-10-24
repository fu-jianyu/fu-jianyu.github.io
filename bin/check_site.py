"""Check the built personal site, including local links and public demo leakage."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.canonical = []
        self.description = []
        self.jsonld = []
        self.in_json = False
        self.json_text = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('a', 'img', 'script', 'link', 'source'):
            for key in ('href', 'src'):
                if a.get(key): self.links.append(a[key])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a.get('href', ''))
        if tag == 'meta' and a.get('name') == 'description': self.description.append(a.get('content', ''))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_json = True
            self.json_text = ''
    def handle_data(self, text):
        if self.in_json: self.json_text += text
    def handle_endtag(self, tag):
        if tag == 'script' and self.in_json:
            self.jsonld.append(self.json_text)
            self.in_json = False

required = ['index.html', 'publications/index.html', 'projects/index.html', 'blog/index.html', 'cv/index.html', 'news/index.html', 'sitemap.xml', 'robots.txt', 'assets/pdf/Jianyu_Fu_CV.pdf']
for name in required:
    if not (root / name).is_file(): errors.append(f'Missing required output: {name}')
for name in ['docs', 'test', 'teaching', 'books', 'repositories', 'assets/json/resume.json']:
    if (root / name).exists(): errors.append(f'Template/internal output leaked: {name}')
for file in root.rglob('*.html'):
    if 'assets' in file.relative_to(root).parts: continue
    text = file.read_text(encoding='utf-8')
    page = Page()
    page.feed(text)
    rel = file.relative_to(root)
    for marker in ['Albert Einstein', 'REPLACE_WITH_', 'A simple inline announcement', 'A growing collection of your cool projects', 'test@gmail.com']:
        if marker in text: errors.append(f'{rel}: template text {marker}')
    if len(page.canonical) != 1 or not page.canonical[0].startswith('https://fu-jianyu.github.io/'):
        errors.append(f'{rel}: canonical URL missing or incorrect')
    if not page.description or not page.description[0].strip(): errors.append(f'{rel}: missing description')
    for value in page.jsonld:
        try: json.loads(value)
        except ValueError: errors.append(f'{rel}: invalid JSON-LD')
    for value in page.links:
        url = urlsplit(value)
        if url.scheme and url.scheme not in ('http', 'https'): continue
        if url.netloc and url.netloc != 'fu-jianyu.github.io': continue
        if not url.path: continue
        path = unquote(url.path)
        target = root / path.lstrip('/') if path.startswith('/') else file.parent / path
        if not target.is_file() and not (target / 'index.html').is_file():
            errors.append(f'{rel}: broken local link {value}')
if errors:
    print('\n'.join(sorted(set(errors))))
    raise SystemExit(1)
print('Site checks passed: required pages, local links, canonical metadata, JSON-LD, and template exclusion.')

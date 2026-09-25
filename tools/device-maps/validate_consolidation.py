"""Validate every rendered page and every exact migration destination."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

BASE = 'https://docs.quantumbitsolutions.com/'
ROOT = Path(__file__).resolve().parents[2]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.canonicals, self.refresh, self.robots = [], [], [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script', 'iframe') and 'src' in attrs:
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.refresh.append(attrs.get('content'))
        if tag == 'meta' and attrs.get('name', '').lower() == 'robots':
            self.robots.append(attrs.get('content', ''))


def scan(site):
    pages = {p.relative_to(site).as_posix(): Page(p.read_text(encoding='utf-8')) for p in site.rglob('*.html')}
    missing, fragments, duplicates = set(), set(), {}
    for path, page in pages.items():
        duplicates_here = [key for key, count in Counter(page.ids).items() if count > 1]
        if duplicates_here:
            duplicates[path] = duplicates_here
        url = BASE + (path[:-10] if path.endswith('index.html') else path)
        for link in set(page.links):
            if not link or link.startswith(('mailto:', 'tel:', 'javascript:', 'data:')):
                continue
            target = urlsplit(urljoin(url, link))
            if target.netloc != urlsplit(BASE).netloc:
                continue
            relative = unquote(target.path).lstrip('/')
            candidate = site / relative
            if target.path.endswith('/') or candidate.is_dir():
                candidate /= 'index.html'
            if not candidate.exists():
                missing.add((path, target.path))
                continue
            dest = candidate.relative_to(site).as_posix()
            if target.fragment and dest in pages and unquote(target.fragment) not in pages[dest].ids:
                fragments.add((path, dest, unquote(target.fragment)))
    urls = {node.text for node in ET.parse(site / 'sitemap.xml').findall('.//{*}loc')}
    return pages, missing, fragments, duplicates, urls


def validate(site, baseline=None):
    pages, missing, fragments, duplicates, urls = scan(site)
    manifest = json.loads((ROOT / 'tools/device-maps/consolidation-manifest.json').read_text(encoding='utf-8'))
    errors = []
    for mapping in manifest['redirects']:
        relative = mapping['target'].removeprefix(BASE) + 'index.html'
        page = pages.get(relative)
        if not page or page.canonicals != [mapping['target']] or page.refresh or any('noindex' in s for s in page.robots):
            errors.append(f'Invalid target: {mapping["target"]}')
        if mapping['target'] not in urls:
            errors.append(f'Target absent from sitemap: {mapping["target"]}')
    old = pages['products/xpf/device-maps/index.html']
    hub = BASE + 'modbus-device-maps/'
    if [urljoin(BASE + 'products/xpf/device-maps/', c) for c in old.canonicals] != [hub]:
        errors.append('Old hub canonical does not resolve directly to new hub')
    if not old.refresh or not old.refresh[0].startswith('0;'):
        errors.append('Old hub needs an instant meta refresh')
    if BASE + 'products/xpf/device-maps/' in urls:
        errors.append('Retired hub remains in sitemap')
    lost_paths, lost_ids = [], {}
    if baseline:
        before, _, _, _, _ = scan(baseline)
        lost_paths = sorted(before.keys() - pages.keys())
        for path in before.keys() & pages.keys():
            if path in ('products/xpf/device-maps/index.html', 'modbus-device-maps/index.html'):
                continue
            lost = sorted(set(before[path].ids) - set(pages[path].ids))
            if lost:
                lost_ids[path] = lost
    result = dict(html_pages=len(pages), sitemap_urls=len(urls), redirect_targets=len(manifest['redirects']),
                  missing_files=sorted(missing), missing_fragments=sorted(fragments), duplicate_ids=duplicates,
                  lost_paths=lost_paths, lost_ids=lost_ids, errors=errors)
    print(json.dumps(result, indent=2))
    if missing or fragments or duplicates or lost_paths or lost_ids or errors:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, required=True)
    parser.add_argument('--baseline', type=Path)
    args = parser.parse_args()
    validate(args.site_dir, args.baseline)

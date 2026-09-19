import glob
import os

base_url = 'https://1bun-quiz.kr/'

urls = [
    ('/', 'daily', '1.0'),
    ('/category-spelling.html', 'weekly', '0.9'),
    ('/category-economy.html', 'weekly', '0.9'),
    ('/category-history.html', 'weekly', '0.9'),
    ('/category-science.html', 'weekly', '0.9'),
    ('/category-life.html', 'weekly', '0.9'),
    ('/about.html', 'monthly', '0.7'),
    ('/privacy.html', 'yearly', '0.5'),
    ('/terms.html', 'yearly', '0.5'),
    ('/contact.html', 'monthly', '0.6'),
]

guide_files = sorted(glob.glob('guide/*.html'))
for gf in guide_files:
    rel_path = gf.replace('\\', '/')
    urls.append(('/' + rel_path, 'weekly', '0.8'))

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for path, freq, prio in urls:
    loc = base_url if path == '/' else base_url.rstrip('/') + path
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{loc}</loc>')
    xml_lines.append('    <lastmod>2026-09-19</lastmod>')
    xml_lines.append(f'    <changefreq>{freq}</changefreq>')
    xml_lines.append(f'    <priority>{prio}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')
xml_content = '\n'.join(xml_lines) + '\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f'sitemap.xml successfully generated with {len(urls)} URLs!')

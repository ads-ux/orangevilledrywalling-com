#!/usr/bin/env python3
DOMAIN = "https://orangevilledrywalling.com"
LASTMOD = "2026-08-15"

urls = [
    ("/", "1.0"),
    ("/services", "0.9"),
    ("/services/drywall-installation", "0.8"),
    ("/services/drywall-repair-patching", "0.8"),
    ("/services/taping-mudding", "0.8"),
    ("/services/popcorn-ceiling-removal", "0.8"),
    ("/services/basement-drywalling", "0.8"),
    ("/services/commercial-drywall", "0.8"),
    ("/shelburne", "0.7"),
    ("/grandvalley", "0.7"),
    ("/erin", "0.7"),
    ("/mono", "0.7"),
    ("/caledon-village", "0.7"),
    ("/privacy", "0.3"),
    ("/blog/how-much-does-drywall-installation-cost-in-orangeville", "0.6"),
    ("/blog/popcorn-ceiling-removal-in-orangeville", "0.6"),
]

entries = "\n".join(
    f'  <url><loc>{DOMAIN}{path}</loc><lastmod>{LASTMOD}</lastmod><priority>{prio}</priority></url>'
    for path, prio in urls
)
xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>'''
with open("/tmp/od-deploy/sitemap.xml", "w") as f:
    f.write(xml)
print(f"wrote sitemap.xml with {len(urls)} URLs")

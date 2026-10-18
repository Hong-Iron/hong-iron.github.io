# Writes site/sitemap.xml: this front page, the SMASH hub and every SMASH game.
# usage: python3 tools/build_sitemap.py <path to SMASH hub schools.json>
#   (the hub repo is https://github.com/Hong-Iron/SMASH; the blog keeps its own sitemap, listed in robots.txt)
import datetime, json, pathlib, sys
from xml.sax.saxutils import escape
root = pathlib.Path(__file__).resolve().parent.parent
schools = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
today = datetime.date.today().isoformat()
urls = ["https://hong-iron.github.io/", "https://hong-iron.github.io/SMASH/"] + [s["url"] for s in sorted(schools, key=lambda s: s["code"])]
body = "".join(f"  <url><loc>{escape(u)}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'
(root / "site" / "sitemap.xml").write_text(xml, encoding="utf-8")
print("site/sitemap.xml", len(urls), "urls")

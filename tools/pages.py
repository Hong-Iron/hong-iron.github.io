# 안내 글 페이지: src/pages/<이름>.html(본문 조각)을 같은 머리말·메뉴·꼬리말로 감싸 site/<이름>.html로 쓴다.
# 조각 맨 위 두 줄: <!-- title: … --> 와 <!-- description: … -->. tools/build.py가 마지막에 부르고, 사이트맵에 PAGES를 싣는다.
import html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://smash-univ.app/"
PAGES = [("about", "소개"), ("guide", "하는 법과 점수"), ("making", "만드는 법"), ("updates", "업데이트 기록")]   # 메뉴 순서

STYLE = """:root { --bg: #0b0d12; --panel: #151922; --line: #2a3140; --fg: #eef1f6; --muted: #9aa4b2; --gold: #ffd23f; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg); font: 400 15.5px/1.8 "IBM Plex Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif; }
main { max-width: 760px; margin: 0 auto; padding: calc(24px + env(safe-area-inset-top, 0px)) 16px 48px; }
nav.top { display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: center; margin-bottom: 26px; font-size: 14px; }
nav.top a { color: var(--muted); text-decoration: none; }
nav.top a:hover, nav.top a[aria-current] { color: var(--fg); }
nav.top a.home { margin-right: auto; color: var(--fg); font-weight: 700; }
h1 { margin: 0 0 6px; font-size: 27px; line-height: 1.35; }
h2 { margin: 34px 0 8px; font-size: 19px; color: var(--gold); }
h3 { margin: 22px 0 6px; font-size: 16px; }
p, li { color: var(--fg); }
ul, ol { padding-left: 22px; }
li { margin: 3px 0; }
a { color: var(--gold); }
.lead { color: var(--muted); margin-top: 0; }
table { width: 100%; border-collapse: collapse; margin: 8px 0 4px; font-size: 14.5px; }
th, td { padding: 7px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { color: var(--muted); font-weight: 600; }
td:first-child { white-space: nowrap; }
.note { padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; background: var(--panel); }
.log { list-style: none; padding: 0; }
.log li { padding: 12px 0; border-bottom: 1px solid var(--line); }
.log time { display: block; color: var(--muted); font-size: 13.5px; }
.cta { display: inline-block; margin-top: 10px; padding: 10px 16px; border-radius: 10px; background: var(--gold); color: #111; font-weight: 700; text-decoration: none; }
footer { margin-top: 44px; padding-top: 18px; border-top: 1px solid var(--line); color: var(--muted); font-size: 13.5px; }
footer a { color: var(--muted); }
footer p { color: var(--muted); margin: 4px 0; }"""

def build():
    out = []
    for name, label in PAGES:
        src = (ROOT / "src" / "pages" / f"{name}.html").read_text(encoding="utf-8")
        title = re.search(r"<!-- title: (.*?) -->", src).group(1).strip()
        desc = re.search(r"<!-- description: (.*?) -->", src).group(1).strip()
        body = re.sub(r"<!-- (title|description): .*? -->\n?", "", src).strip()
        e = lambda v: html.escape(v, quote=True)
        nav = "".join(f'<a href="{n}.html"{" aria-current=\"page\"" if n == name else ""}>{l}</a>' for n, l in PAGES)
        ld = ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
              f'{{"@type":"ListItem","position":1,"name":"SMASH 대학교","item":"{SITE}"}},'
              f'{{"@type":"ListItem","position":2,"name":"{label}","item":"{SITE}{name}.html"}}]}}')
        page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)} | SMASH 대학교</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{name}.html">
<meta property="og:site_name" content="SMASH 대학교">
<meta property="og:locale" content="ko_KR">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}{name}.html">
<meta property="og:image" content="{SITE}og.png">
<link rel="icon" href="icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="icon-180.png">
<script type="application/ld+json">{ld}</script>
<style>
{STYLE}
</style>
</head>
<body>
<main>
<nav class="top" aria-label="SMASH 대학교 안내"><a class="home" href="./">SMASH 대학교</a>{nav}</nav>
{body}
<footer>
<p><a href="./">학교 고르러 가기</a> · <a href="privacy.html">개인정보처리방침</a> · 문의 <a href="mailto:hongcheolmin004@gmail.com">hongcheolmin004@gmail.com</a></p>
<p>학교와 관계없는 비공식 팬 게임입니다. 학교 로고와 교표는 쓰지 않습니다. 건물·도로 © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap 기여자</a></p>
</footer>
</main>
</body>
</html>
"""
        (ROOT / "site" / f"{name}.html").write_text(page, encoding="utf-8")
        out.append(f"{SITE}{name}.html")
    return out

if __name__ == "__main__":
    for u in build(): print(u)

#!/usr/bin/env python3
"""
Generate translated SEO landing pages + sitemap for ScreenWakeUp.

Writes <lang>/<slug>/index.html for the 6 non-English languages and rewrites
sitemap.xml with hreflang alternates for every page. The English landing pages
(/<slug>/index.html) are hand-maintained; this script only adds their hreflang
block (idempotent) and references them as x-default.

Run from repo root:  python3 scripts/generate_landing_pages.py
"""
import json
import os
import re

GA4 = "G-WKJ8R82KQZ"
BASE = "https://screenwakeup.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["prevent-teams-away", "caffeine-alternative", "keep-screen-awake-iphone", "prevent-zoom-idle"]
ALL_LANGS = ["en", "es", "pt", "fr", "de", "ja", "ru"]
GEN_LANGS = ["es", "pt", "fr", "de", "ja", "ru"]

STYLE = """    *{box-sizing:border-box;margin:0;padding:0}
    :root{--bg:#0c0e18;--bg2:#11141f;--surface:#181b2a;--accent:#5ee0c0;--text:#eef0f6;--muted:#8892a4;--border:rgba(255,255,255,0.06)}
    body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.7}
    header{background:var(--bg2);border-bottom:1px solid var(--border);padding:16px 24px;display:flex;align-items:center;justify-content:space-between}
    .logo{text-decoration:none;color:var(--text);font-weight:800;font-size:17px}
    .logo em{color:var(--accent);font-style:normal;font-size:11px;font-weight:600;margin-left:6px}
    nav a{color:var(--muted);text-decoration:none;margin-left:20px;font-size:14px}
    nav a:hover{color:var(--accent)}
    main{max-width:760px;margin:0 auto;padding:60px 24px}
    h1{font-size:clamp(28px,5vw,42px);font-weight:800;margin-bottom:16px;letter-spacing:-.5px}
    h1 span{color:var(--accent)}
    h2{font-size:22px;font-weight:700;margin:40px 0 12px;color:var(--text)}
    h3{font-size:17px;font-weight:700;margin:24px 0 8px;color:var(--text)}
    p{color:var(--muted);margin-bottom:16px;font-size:15px}
    ol,ul{color:var(--muted);margin:0 0 16px 22px;font-size:15px}
    li{margin-bottom:8px}
    strong{color:var(--text)}
    .tag{font-size:11px;font-weight:700;letter-spacing:1.5px;color:var(--accent);text-transform:uppercase;margin-bottom:16px}
    .lead{font-size:18px;color:var(--text);margin-bottom:24px}
    .cta{display:inline-block;margin-top:24px;padding:14px 28px;background:var(--accent);color:#0c0e18;border-radius:12px;font-weight:700;text-decoration:none;font-size:15px}
    .box{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:20px 24px;margin:24px 0}
    table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}
    th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--border);color:var(--muted)}
    th{color:var(--text);font-weight:700}
    td strong{color:var(--accent)}
    .related{display:flex;flex-wrap:wrap;gap:12px;margin-top:16px}
    .related a{display:inline-block;padding:10px 16px;background:var(--surface);border:1px solid var(--border);border-radius:10px;color:var(--accent);text-decoration:none;font-size:14px;font-weight:600}
    .related a:hover{border-color:var(--accent)}
    a.inline{color:var(--accent)}
    footer{text-align:center;padding:40px 24px;color:var(--muted);font-size:13px;border-top:1px solid var(--border)}
    footer a{color:var(--muted);text-decoration:none;margin:0 8px}
    footer a:hover{color:var(--accent)}"""

# Donation buttons (B header + C floating) injected into every landing page
DONATE_CSS = """    .nav-kofi{display:inline-flex;align-items:center;gap:6px;background:#FF5E5B;color:#fff;font-size:13px;font-weight:700;padding:7px 14px;border-radius:18px;text-decoration:none;margin-left:0;margin-right:6px}
    .nav-kofi:hover{opacity:.88}
    .float-kofi-wrap{position:fixed;right:18px;bottom:18px;z-index:9998}
    .float-kofi{display:flex;align-items:center;justify-content:center;width:54px;height:54px;border-radius:50%;background:#FF5E5B;color:#fff;font-size:24px;text-decoration:none;box-shadow:0 10px 28px rgba(0,0,0,.4);transition:transform .15s,opacity .2s}
    .float-kofi:hover{transform:scale(1.07)}
    .fk-close{position:absolute;top:-6px;right:-6px;width:20px;height:20px;border-radius:50%;border:none;background:var(--surface2,#1f2338);color:var(--muted,#8892a4);font-size:13px;line-height:1;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.4)}
    .fk-close:hover{color:var(--text,#eef0f6)}
    @media (max-width:560px){.float-kofi-wrap{right:14px;bottom:14px}.float-kofi{width:48px;height:48px;font-size:21px}}"""

# Floating support button block (literal braces — kept out of the f-string template)
FLOAT_TEMPLATE = '''<div class="float-kofi-wrap" id="floatKofi">
  <a class="float-kofi" href="https://ko-fi.com/screenwakeup" target="_blank" rel="noopener" aria-label="{SUP}">☕</a>
  <button class="fk-close" id="floatKofiClose" aria-label="Hide">&times;</button>
</div>
<script>(function(){var w=document.getElementById("floatKofi");if(!w)return;if(+(localStorage.getItem("ka-float-hide")||0)>Date.now()){w.style.display="none";return;}var c=document.getElementById("floatKofiClose");if(c)c.addEventListener("click",function(e){e.preventDefault();w.style.display="none";localStorage.setItem("ka-float-hide",String(Date.now()+7*864e5));});})();</script>'''

UI = {
 "es": {"free":"herramienta gratis","tool":"Herramienta","home":"Inicio","about":"Acerca de","privacy":"Privacidad","terms":"Términos","support":"Apoyar","tagline":"Gratis para siempre · Sin rastreo","related":"Guías relacionadas","allfeatures":"Todas las funciones →","faqh":"Preguntas frecuentes"},
 "pt": {"free":"ferramenta grátis","tool":"Ferramenta","home":"Início","about":"Sobre","privacy":"Privacidade","terms":"Termos","support":"Apoiar","tagline":"Grátis para sempre · Sem rastreamento","related":"Guias relacionados","allfeatures":"Todos os recursos →","faqh":"Perguntas frequentes"},
 "fr": {"free":"outil gratuit","tool":"Outil","home":"Accueil","about":"À propos","privacy":"Confidentialité","terms":"Conditions","support":"Soutenir","tagline":"Gratuit pour toujours · Sans suivi","related":"Guides associés","allfeatures":"Toutes les fonctions →","faqh":"Questions fréquentes"},
 "de": {"free":"kostenloses Tool","tool":"Tool","home":"Startseite","about":"Über uns","privacy":"Datenschutz","terms":"AGB","support":"Unterstützen","tagline":"Für immer kostenlos · Kein Tracking","related":"Verwandte Anleitungen","allfeatures":"Alle Funktionen →","faqh":"Häufige Fragen"},
 "ja": {"free":"無料ツール","tool":"ツール","home":"ホーム","about":"概要","privacy":"プライバシー","terms":"利用規約","support":"支援する","tagline":"ずっと無料 · トラッキングなし","related":"関連ガイド","allfeatures":"すべての機能 →","faqh":"よくある質問"},
 "ru": {"free":"бесплатный инструмент","tool":"Инструмент","home":"Главная","about":"О нас","privacy":"Конфиденциальность","terms":"Условия","support":"Поддержать","tagline":"Бесплатно навсегда · Без отслеживания","related":"Похожие руководства","allfeatures":"Все функции →","faqh":"Частые вопросы"},
}

# Localized nav label for each slug (used to build the header nav linking sibling guides)
NAVLABEL = {
 "prevent-teams-away":      {"es":"Teams Ausente","pt":"Teams Ausente","fr":"Teams Absent","de":"Teams Abwesend","ja":"Teams 退席中","ru":"Teams «Нет на месте»"},
 "caffeine-alternative":    {"es":"Alternativa a Caffeine","pt":"Alternativa ao Caffeine","fr":"Alternative à Caffeine","de":"Caffeine-Alternative","ja":"Caffeine 代替","ru":"Замена Caffeine"},
 "keep-screen-awake-iphone":{"es":"iPhone","pt":"iPhone","fr":"iPhone","de":"iPhone","ja":"iPhone","ru":"iPhone"},
 "prevent-zoom-idle":       {"es":"Zoom Activo","pt":"Zoom Ativo","fr":"Zoom Actif","de":"Zoom Aktiv","ja":"Zoom アクティブ","ru":"Активность в Zoom"},
}

CONTENT = {s: {} for s in SLUGS}

# Content blocks are defined in a companion data module for readability.
from landing_content import CONTENT as _C  # noqa: E402
CONTENT = _C


def url_for(slug, lang):
    return f"{BASE}/{slug}/" if lang == "en" else f"{BASE}/{lang}/{slug}/"


def home_for(lang):
    return f"{BASE}/" if lang == "en" else f"{BASE}/{lang}/"


def hreflang_head(slug):
    lines = []
    for l in ALL_LANGS:
        lines.append(f'  <link rel="alternate" hreflang="{l}" href="{url_for(slug, l)}">')
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{url_for(slug, "en")}">')
    return "\n".join(lines)


def render(slug, lang):
    c = CONTENT[slug][lang]
    ui = UI[lang]
    home = home_for(lang)
    body = c["body"].replace("{HOME}", home)

    # JSON-LD: optional HowTo + FAQ + Breadcrumb
    blocks = []
    if c.get("howto"):
        blocks.append({
            "@context": "https://schema.org", "@type": "HowTo",
            "name": c["howto"]["name"], "description": c["howto"]["desc"],
            "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t}
                     for i, (n, t) in enumerate(c["howto"]["steps"])],
        })
    blocks.append({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]],
    })
    blocks.append({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home"], "item": home},
            {"@type": "ListItem", "position": 2, "name": c["bc_self"], "item": url_for(slug, lang)},
        ],
    })
    schema = json.dumps(blocks, ensure_ascii=False, indent=2)

    # nav: link the two sibling guides + tool
    siblings = [s for s in SLUGS if s != slug]
    nav = f'    <a href="{home}">{ui["tool"]}</a>\n'
    for s in siblings:
        nav += f'    <a href="/{lang}/{s}/">{NAVLABEL[s][lang]}</a>\n'

    related = "".join(f'    <a href="/{lang}/{rs}/">{rl}</a>\n' for rl, rs in c["related"])
    related += f'    <a href="{home}">{ui["allfeatures"]}</a>'

    float_html = FLOAT_TEMPLATE.replace("{SUP}", ui["support"])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']}</title>
  <meta name="description" content="{c['desc']}">
  <meta name="keywords" content="{c['keywords']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{url_for(slug, lang)}">
{hreflang_head(slug)}
  <link rel="icon" href="https://screenwakeup.com/favicon.ico" type="image/x-icon">
  <meta name="theme-color" content="#5ee0c0">

  <meta property="og:type" content="article">
  <meta property="og:url" content="{url_for(slug, lang)}">
  <meta property="og:title" content="{c['ogtitle']}">
  <meta property="og:description" content="{c['ogdesc']}">
  <meta property="og:image" content="https://screenwakeup.com/og-image.png">
  <meta property="og:site_name" content="ScreenWakeUp">

  <script type="application/ld+json">
{schema}
  </script>

  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4}');</script>

  <style>
{STYLE}
{DONATE_CSS}
  </style>
</head>
<body>
<header>
  <a href="{home}" class="logo">ScreenWakeUp <em>{ui['free']}</em></a>
  <nav>
    <a class="nav-kofi" href="https://ko-fi.com/screenwakeup" target="_blank" rel="noopener">☕ {ui['support']}</a>
{nav}  </nav>
</header>

<main>
  <p class="tag">{c['tag']}</p>
  <h1>{c['h1']}</h1>
  <p class="lead">{c['lead']}</p>

  {body}

  <a href="{home}" class="cta">{c['cta']}</a>

  <h2>{ui['related']}</h2>
  <div class="related">
{related}
  </div>
</main>

<footer>
  <p>
    <a href="{home}">{ui['home']}</a>
    <a href="/about/">{ui['about']}</a>
    <a href="/privacy/">{ui['privacy']}</a>
    <a href="/terms/">{ui['terms']}</a>
    <a href="https://ko-fi.com/screenwakeup" target="_blank" rel="noopener">{ui['support']}</a>
  </p>
  <p style="margin-top:12px">© 2026 ScreenWakeUp.com · {ui['tagline']}</p>
</footer>

{float_html}
</body>
</html>
"""


def write_pages():
    n = 0
    for slug in SLUGS:
        for lang in GEN_LANGS:
            d = os.path.join(ROOT, lang, slug)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(render(slug, lang))
            n += 1
    return n


def ensure_english_hreflang():
    """Idempotently insert the hreflang block into the hand-written English pages."""
    for slug in SLUGS:
        path = os.path.join(ROOT, slug, "index.html")
        html = open(path, encoding="utf-8").read()
        if 'hreflang="es"' in html:
            continue
        canonical = f'  <link rel="canonical" href="{url_for(slug, "en")}">'
        html = html.replace(canonical, canonical + "\n" + hreflang_head(slug), 1)
        open(path, "w", encoding="utf-8").write(html)


def build_sitemap():
    lastmod_home = "2026-06-23"
    lastmod_land = "2026-06-25"
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">', '']

    def alts_home():
        a = [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{home_for(l)}"/>' for l in ALL_LANGS]
        a.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{home_for("en")}"/>')
        return "\n".join(a)

    def alts_land(slug):
        a = [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{url_for(slug, l)}"/>' for l in ALL_LANGS]
        a.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for(slug, "en")}"/>')
        return "\n".join(a)

    # Home + language homes
    for lang in ALL_LANGS:
        out += ['  <url>', f'    <loc>{home_for(lang)}</loc>', f'    <lastmod>{lastmod_home}</lastmod>',
                '    <changefreq>monthly</changefreq>',
                f'    <priority>{"1.0" if lang == "en" else "0.9"}</priority>', alts_home(), '  </url>', '']
    # Landing pages (all langs)
    for slug in SLUGS:
        for lang in ALL_LANGS:
            out += ['  <url>', f'    <loc>{url_for(slug, lang)}</loc>', f'    <lastmod>{lastmod_land}</lastmod>',
                    '    <changefreq>monthly</changefreq>',
                    f'    <priority>{"0.8" if lang == "en" else "0.7"}</priority>', alts_land(slug), '  </url>', '']
    # Legal / about (no alternates)
    for slug, prio, freq in [("about", "0.5", "yearly"), ("privacy", "0.4", "yearly"), ("terms", "0.4", "yearly")]:
        out += ['  <url>', f'    <loc>{BASE}/{slug}/</loc>', '    <lastmod>2026-06-23</lastmod>',
                f'    <changefreq>{freq}</changefreq>', f'    <priority>{prio}</priority>', '  </url>', '']
    out += ['</urlset>', '']
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    pages = write_pages()
    ensure_english_hreflang()
    build_sitemap()
    print(f"Generated {pages} translated pages, added hreflang to {len(SLUGS)} English pages, rebuilt sitemap.xml")

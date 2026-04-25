from __future__ import annotations

import argparse
import html
import re
import textwrap
import urllib.parse
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT.parent / "mohammad-site-raw"


NAVIGATION = (
    ("Home", "home", ()),
    (
        "Learn Organic Chemistry",
        "learn-organic-chemistry",
        (
            ("Speaking the Language of Molecules", "learn-organic-chemistry/basics-of-organic-chemistry"),
            ("Exploring Organic Chemistry Fundamentals", "learn-organic-chemistry/organic-i"),
            ("Different Classes of Organic Compounds", "learn-organic-chemistry/organic-ii"),
            ("Exploring Heterocycles and Spectroscopic Techniques", "learn-organic-chemistry/organic-iii"),
        ),
    ),
    (
        "Apps for Academics",
        "apps-for-academics",
        (
            ("Mark List Maker", "apps-for-academics/mark-list-maker"),
            ("Grades & Attendance Sync", "apps-for-academics/attendane-export"),
            ("Sample Key Generator", "apps-for-academics/sample-key-generator"),
            ("My Apps for Academics", "apps-for-academics/my-apps-for-academics"),
        ),
    ),
    (
        "Apps for Students",
        "apps-for-students",
        (
            ("WoodWard-Fieser λmax Calculator", "apps-for-students/woodward-fieser-lmax-calculator"),
            ("Nomenclature", "apps-for-students/nomenclature"),
            ("Elemental Analysis", "apps-for-students/elemental-analysis"),
        ),
    ),
    ("Publications", "publications", ()),
    (
        "Scientific Research Workshop",
        "scientific-research-workshop",
        (
            ("Session 1", "scientific-research-workshop/session-1"),
            ("Session 2", "scientific-research-workshop/session-2"),
            ("Session 3", "scientific-research-workshop/session-3"),
        ),
    ),
    ("AI index", "ai-index", ()),
    ("Highlights", "highlights", ()),
)


PAGE_SPECS = {
    "home": {
        "source": "home.html",
        "title": "Home",
        "description": "Personal website for A. Prof. Mohammad Abdulwahhab.",
        "kind": "home",
    },
    "learn-organic-chemistry": {
        "source": "learn-organic-chemistry.html",
        "title": "Learn Organic Chemistry",
        "description": "A structured learning hub for Basics, Organic-I, Organic-II, and Organic-III.",
        "kind": "learn-overview",
    },
    "learn-organic-chemistry/basics-of-organic-chemistry": {
        "source": "learn-organic-chemistry_basics-of-organic-chemistry.html",
        "title": "Speaking the Language of Molecules",
        "description": "Recorded videos exploring bonding, structure, hybridization, resonance, and the visual language of molecules.",
        "kind": "course-videos",
    },
    "learn-organic-chemistry/organic-i": {
        "source": "learn-organic-chemistry_organic-i.html",
        "title": "Exploring Organic Chemistry Fundamentals",
        "description": "Recorded videos exploring hydrocarbon families, aromaticity, and stereochemical thinking.",
        "kind": "course-videos",
    },
    "learn-organic-chemistry/organic-ii": {
        "source": "learn-organic-chemistry_organic-ii.html",
        "title": "Different Classes of Organic Compounds",
        "description": "Recorded videos exploring major functional groups, their preparation, and their transformations.",
        "kind": "course-videos",
    },
    "learn-organic-chemistry/organic-iii": {
        "source": "learn-organic-chemistry_organic-iii.html",
        "title": "Exploring Heterocycles and Spectroscopic Techniques",
        "description": "Recorded videos exploring heterocyclic chemistry, spectroscopy, and problem solving.",
        "kind": "course-videos",
    },
    "apps-for-academics/my-apps-for-academics": {
        "source": "apps-for-academics_my-apps-for-academics.html",
        "title": "My Apps for Academics",
        "description": "Custom academic and research tools.",
        "kind": "apps-overview",
    },
    "apps-for-academics": {
        "source": "apps-for-academics_my-apps-for-academics.html",
        "title": "Apps for Academics",
        "description": "Useful tools that will help you in your daily academic work",
        "kind": "apps-academics-hub",
    },
    "apps-for-students": {
        "source": "apps-for-students_nomenclature.html",
        "title": "Apps for Students",
        "description": "Student tools for quick calculations and interactive chemistry practice.",
        "kind": "apps-students-hub",
    },
    "apps-for-academics/mark-list-maker": {
        "source": "apps-for-academics_mark-list-maker.html",
        "title": "Mark List Maker",
        "description": "Mark list creation app for academics, rebuilt as a standalone route.",
        "kind": "academic-app-leaf",
        "app_key": "Mark List Maker",
        "shell_class": "live-app-shell--mark-list-maker",
    },
    "apps-for-academics/attendane-export": {
        "source": "apps-for-academics_attendane-export.html",
        "title": "Grades & Attendance Sync",
        "description": "Attendance export and organization tool for academics.",
        "kind": "academic-app-leaf",
        "app_key": "Grades & Attendance Sync",
        "shell_class": "live-app-shell--attendance-export",
    },
    "apps-for-academics/sample-key-generator": {
        "source": "apps-for-academics_sample-key-generator.html",
        "title": "Sample Key Generator",
        "description": "Practical sample key generator rebuilt as a standalone route.",
        "kind": "academic-app-leaf",
        "app_key": "Sample Key Generator",
        "shell_class": "live-app-shell--sample-key-generator",
    },
    "apps-for-students/woodward-fieser-lmax-calculator": {
        "source": "apps-for-students_woodward-fieser-%CE%BBmax-calculator.html",
        "title": "WoodWard-Fieser λmax Calculator",
        "description": "Student-facing calculator preserved from the original site.",
        "kind": "external-app",
    },
    "apps-for-students/nomenclature": {
        "source": "apps-for-students_nomenclature.html",
        "title": "Nomenclature",
        "description": "Interactive nomenclature tools and quizzes from the original site.",
        "kind": "embedded-tools",
    },
    "apps-for-students/elemental-analysis": {
        "source": "apps-for-students_elemental-analysis.html",
        "title": "Elemental Analysis",
        "description": "Interactive elemental analysis tools and calculators.",
        "kind": "embedded-tools",
    },
    "publications": {
        "source": "publications.html",
        "title": "Publications",
        "description": "Research portfolio and publication list.",
        "kind": "publications",
    },
    "scientific-research-workshop": {
        "source": "scientific-research-workshop.html",
        "title": "Scientific Research Workshop",
        "description": "Workshop overview and session navigation.",
        "kind": "workshop-overview",
    },
    "scientific-research-workshop/session-1": {
        "source": "scientific-research-workshop_session-1.html",
        "title": "Session 1",
        "description": "The Everyday Researcher: From Digital Noise to Trusted Source.",
        "kind": "workshop-session",
    },
    "scientific-research-workshop/session-2": {
        "source": "scientific-research-workshop_session-2.html",
        "title": "Session 2",
        "description": "Decoding Research: From Question to Publication.",
        "kind": "workshop-session",
    },
    "scientific-research-workshop/session-3": {
        "source": "scientific-research-workshop_session-3.html",
        "title": "Session 3",
        "description": "Making an Impact: How to Share Your Science.",
        "kind": "workshop-session",
    },
    "ai-index": {
        "source": "ai-index.html",
        "title": "AI index",
        "description": "A curated AI services directory preserved from the original site.",
        "kind": "embedded-tools",
    },
    "highlights": {
        "source": "highlights.html",
        "title": "Highlights",
        "description": "Selected milestones, workshops, recognitions, and certifications.",
        "kind": "highlights",
    },
}


HIGHLIGHT_IMAGE_MAP = {
    "Served as a tutor for the workshop on 'In Silico Structure-Based Drug Design and Docking' at the 2nd International Conference of the Faculty of Pharmacy, Delta University (2023)": [
        {"src": "assets/highlights/highlight-01.jpg", "variant": "landscape"},
    ],
    "Delivered a workshop on 'Molecular Docking in Drug Discovery' at the 1st International Conference of the Faculty of Pharmacy, Delta University, in November 2021": [
        {"src": "assets/highlights/highlight-02.jpg", "variant": "landscape"},
    ],
    "Served as a speaker at the 2nd International Conference of Pharmaceutical Sciences at Mansoura University, held in April 2019": [
        {"src": "assets/highlights/highlight-03.jpg", "variant": "landscape"},
    ],
    "Participated as a workshop tutor at the 1st International Conference of Pharmaceutical Sciences, MU-PHARM 2017": [
        {"src": "assets/highlights/highlight-04.jpg", "variant": "portrait"},
    ],
    "Named a JSPS HOPE Fellow, recognizing my successful participation in The Fifth HOPE Meeting, held in Tokyo, Japan (2013)": [
        {"src": "assets/highlights/highlight-05.jpg", "variant": "portrait"},
    ],
    "Member of the organizing committee for the \"International Workshop on Computational Molecular Modeling & Drug Discovery\" at Mansoura University (2012)": [
        {"src": "assets/highlights/highlight-06.jpg", "variant": "landscape"},
    ],
    "My contributions to the \"Computer-Based Drug Design\" workshop held at Mansoura University in February 2010": [
        {"src": "assets/highlights/highlight-07.jpg", "variant": "landscape"},
    ],
    "Presented a workshop titled 'Discover How AI Can Transform Your Academic Journey' at the Faculty of Pharmacy, Mansoura University, in February-March 2025": [
        {"src": "assets/highlights/highlight-08.jpg", "variant": "landscape"},
    ],
    "Presented a workshop titled \"The Synergy of AI and NMR: Revolutionizing Drug Discovery\" in collaboration with the Pharmacy Center of Scientific Excellence (PCSE) - Faculty of Pharmacy, Mansoura University (2025)": [
        {"src": "assets/highlights/highlight-09.jpg", "variant": "landscape"},
    ],
    "Completed the \"Introduction to programming using Python\" training program, certified by Microsoft (2022)": [
        {"src": "assets/highlights/highlight-10.jpg", "variant": "landscape"},
    ],
    "Completed the Microsoft-certified 'Python programming language - Intermediate level' training (2022)": [
        {"src": "assets/highlights/highlight-11.jpg", "variant": "landscape"},
    ],
    "Recognized as a Microsoft Office Specialist for Word 2016, having successfully completed the requirements on December 19, 2021": [
        {"src": "assets/highlights/highlight-12.jpg", "variant": "landscape"},
    ],
    "Achieved Microsoft Office Specialist certification for PowerPoint 2016 on December 28, 2021": [
        {"src": "assets/highlights/highlight-13.jpg", "variant": "landscape"},
    ],
    "Part of my contribution as a peer reviewer for some reputable Q1 &Q2 scientific journals": [
        {"src": "assets/highlights/highlight-14a.jpg", "variant": "landscape"},
        {"src": "assets/highlights/highlight-14b.jpg", "variant": "landscape"},
        {"src": "assets/highlights/highlight-14c.jpg", "variant": "landscape"},
    ],
    "Flashback to 1995 : Certificate of Appreciation from the Ministry of Education acknowledging my achievement as the 4th-ranked student in the General Secondary Certificate for the 1994/1995 academic year": [
        {"src": "assets/highlights/highlight-15.jpg", "variant": "landscape"},
    ],
}


def sanitize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def unwrap_google_url(url: str) -> str:
    if not url:
        return url
    if "google.com/url?" in url:
        query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        return query.get("q", [url])[0]
    return url


def clean_youtube_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    keep = {}
    for key in ("start", "si"):
        if key in query:
            keep[key] = query[key][0]
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", urllib.parse.urlencode(keep), ""))


def route_to_path(route: str) -> str:
    if route == "home":
        return "home/index.html"
    return f"{route}/index.html"


def route_depth(route: str) -> int:
    return len(("home" if route == "home" else route).split("/"))


def prefix_for_route(route: str) -> str:
    return "../" * route_depth(route)


def route_to_href(route: str, prefix: str = "") -> str:
    slug = "home" if route == "home" else route
    return f"{prefix}{slug}/"


def extract_youtube_urls(raw_html: str) -> list[str]:
    hits = re.findall(r"https://www\.youtube\.com/embed/[^\"'& ]+(?:\?[^\"']*)?", raw_html)
    results = []
    for hit in hits:
        clean = clean_youtube_url(hit)
        if clean not in results:
            results.append(clean)
    return results


def normalize_embed_document(code: str) -> str:
    cleaned = html.unescape(code).strip()
    if cleaned.lower().startswith("<!doctype html") or "<html" in cleaned.lower():
        return cleaned
    return textwrap.dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZJFG15M00T"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){{dataLayer.push(arguments);}}
              gtag('js', new Date());

              gtag('config', 'G-ZJFG15M00T');
            </script>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Embedded Resource</title>
            <style>
              html, body {{
                margin: 0;
                min-height: 100%;
                background: #ffffff;
              }}
              iframe {{
                width: 100%;
                min-height: 100vh;
                border: 0;
              }}
            </style>
          </head>
          <body>
            {cleaned}
          </body>
        </html>
        """
    )


def write_embed_file(route: str, index: int, code: str) -> str:
    embeds_dir = ROOT / "embeds"
    embeds_dir.mkdir(exist_ok=True)
    filename = f"{route.replace('/', '-')}-{index + 1}.html"
    output = embeds_dir / filename
    output.write_text(normalize_embed_document(code), encoding="utf-8")
    return f"embeds/{filename}"


def parse_source_page(source_path: Path) -> dict:
    raw_html = source_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw_html, "html.parser")
    meta_desc = ""
    desc_tag = soup.find("meta", attrs={"property": "og:description"})
    if desc_tag and desc_tag.get("content"):
        meta_desc = sanitize_text(desc_tag["content"])

    sections = []
    for section in soup.select("section.yaqOZd"):
        texts = []
        for paragraph in section.select("p"):
            value = sanitize_text(" ".join(paragraph.stripped_strings))
            if value and value not in texts:
                texts.append(value)
        links = []
        for anchor in section.select("a[href]"):
            href = unwrap_google_url(anchor.get("href", ""))
            label = sanitize_text(" ".join(anchor.stripped_strings))
            if href and href not in {item["href"] for item in links}:
                links.append({"label": label, "href": href})
        embeds = []
        for holder in section.select("[data-code]"):
            code = holder.get("data-code", "").strip()
            if code:
                embeds.append(code)
        sections.append({"texts": texts, "links": links, "embeds": embeds})

    data_urls = []
    for node in soup.find_all(attrs={"data-url": True}):
        url = unwrap_google_url(node.get("data-url", ""))
        if url and url not in data_urls:
            data_urls.append(url)

    return {
        "title": sanitize_text(soup.title.get_text(" ", strip=True)) if soup.title else source_path.stem,
        "description": meta_desc,
        "sections": sections,
        "youtube_urls": extract_youtube_urls(raw_html),
        "data_urls": data_urls,
    }


def render_navigation(prefix: str, current_route: str) -> str:
    parts = []
    for label, route, children in NAVIGATION:
        in_group = current_route == route or any(child_route == current_route for _, child_route in children)
        if children:
            summary = (
                f'<div class="nav-summary"><a href="{route_to_href(route, prefix)}" class="nav-parent-link">{html.escape(label)}</a></div>'
                if route
                else f'<div class="nav-summary"><span class="nav-parent-link nav-parent-text">{html.escape(label)}</span></div>'
            )
            submenu = "".join(
                f'<a class="submenu-link{" is-current" if child_route == current_route else ""}" href="{route_to_href(child_route, prefix)}">{html.escape(child_label)}</a>'
                for child_label, child_route in children
            )
            parts.append(f'<details class="nav-group{" is-current" if in_group else ""}"><summary>{summary}</summary><div class="submenu">{submenu}</div></details>')
        else:
            parts.append(f'<a class="nav-link{" is-current" if current_route == route else ""}" href="{route_to_href(route, prefix)}">{html.escape(label)}</a>')
    return "".join(parts)


def render_breadcrumbs(route: str, prefix: str) -> str:
    if route == "home":
        return ""
    group_labels = {
        "apps-for-academics": "Apps for Academics",
        "apps-for-students": "Apps for Students",
        "learn-organic-chemistry": "Learn Organic Chemistry",
        "scientific-research-workshop": "Scientific Research Workshop",
    }
    crumbs = ['<a href="' + route_to_href("home", prefix) + '">Home</a>']
    partial = []
    for part in route.split("/"):
        partial.append(part)
        current = "/".join(partial)
        label = PAGE_SPECS[current]["title"] if current in PAGE_SPECS else group_labels.get(current, part.replace("-", " ").title())
        if current == route:
            crumbs.append(f"<span>{html.escape(label)}</span>")
        else:
            crumbs.append(f'<a href="{route_to_href(current, prefix)}">{html.escape(label)}</a>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumbs">' + "<span>/</span>".join(crumbs) + "</nav>"


def icon_for_url(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.lower()
    if "linkedin.com" in host:
        return "LinkedIn"
    if "youtube.com" in host:
        return "YouTube"
    if "t.me" in host:
        return "Telegram"
    if "orcid.org" in host:
        return "ORCID"
    if "scholar.google.com" in host:
        return "Google Scholar"
    if "researchgate.net" in host:
        return "ResearchGate"
    if "box.com" in host:
        return "Box"
    if "doi.org" in host:
        return "DOI"
    return host.replace("www.", "") or "Link"


def render_social_links(links: list[dict]) -> str:
    return '<div class="pill-row">' + "".join(
        f'<a class="pill-link" href="{html.escape(item["href"])}" target="_blank" rel="noreferrer">{html.escape(icon_for_url(item["href"]))}</a>'
        for item in links
    ) + "</div>"


def render_topic_cards(items: list[str]) -> str:
    return '<section class="card-grid topics-grid">' + "".join(
        f'<article class="topic-card"><span class="eyebrow-card">Topic {index}</span><h3>{html.escape(item)}</h3></article>'
        for index, item in enumerate(items, 1)
    ) + "</section>"


def render_video_gallery(items: list[tuple[str, str]]) -> str:
    cards = []
    for index, (title, url) in enumerate(items, 1):
        cards.append(
            f"""
            <article class="video-card">
              <div class="card-head">
                <span class="eyebrow-card">Lesson {index}</span>
                <h3>{html.escape(title)}</h3>
              </div>
              <div class="embed-shell video-shell">
                <iframe loading="lazy" src="{html.escape(url)}" title="{html.escape(title)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
              </div>
            </article>
            """
        )
    return '<section class="card-grid videos-grid">' + "".join(cards) + "</section>"


def render_publication_cards(entries: list[tuple[str, str]]) -> str:
    return '<section class="stack-grid">' + "".join(
        f"""
        <article class="publication-card">
          <div class="card-head">
            <span class="eyebrow-card">Publication {index}</span>
            <p>{html.escape(citation)}</p>
          </div>
          <a class="button button-secondary" href="{html.escape(doi)}" target="_blank" rel="noreferrer">Open DOI</a>
        </article>
        """
        for index, (citation, doi) in enumerate(entries, 1)
    ) + "</section>"


def render_embed_cards(items: list[tuple[str, str, str]], prefix: str) -> str:
    cards = []
    for index, (title, embed_path, label) in enumerate(items, 1):
        cards.append(
            f"""
            <article class="tool-card">
              <div class="card-head">
                <h3>{html.escape(title)}</h3>
              </div>
              <div class="embed-shell app-shell">
                <iframe loading="lazy" src="{prefix}{html.escape(embed_path)}" title="{html.escape(title)}"></iframe>
              </div>
              <div class="card-actions">
                <a class="button button-secondary" href="{prefix}{html.escape(embed_path)}" target="_blank" rel="noreferrer">{html.escape(label)}</a>
              </div>
            </article>
            """
        )
    return '<section class="stack-grid">' + "".join(cards) + "</section>"


def render_live_app(title: str, app_url: str, shell_class: str = "") -> str:
    safe_url = html.escape(app_url)
    classes = "embed-shell live-app-shell"
    if shell_class:
        classes += f" {shell_class}"
    return f"""
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">Live Tool</span>
          <h2>{html.escape(title)}</h2>
          <p>This page preserves the original live tool.</p>
        </div>
        <a class="button button-primary" href="{safe_url}" target="_blank" rel="noreferrer">Open in new tab</a>
      </div>
      <div class="{classes}">
        <iframe loading="lazy" src="{safe_url}" title="{html.escape(title)}" sandbox="allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-same-origin"></iframe>
      </div>
    </section>
    """


def render_home(parsed: dict, prefix: str) -> str:
    about_section = next((section for section in parsed["sections"] if section["texts"] and section["texts"][0] == "About Me"), None)
    social_section = next((section for section in parsed["sections"] if len(section["links"]) >= 5), None)
    arabic_section = next((section for section in parsed["sections"] if section["texts"] and "أسألكم" in section["texts"][0]), None)
    video_url = parsed["youtube_urls"][0] if parsed["youtube_urls"] else ""
    about_paragraphs = about_section["texts"][1:] if about_section else []
    return f"""
    <section class="hero">
      <div class="hero-copy">
        <span class="hero-kicker">Academic Profile</span>
        <h1>Mohammad Abdulwahhab</h1>
        <p>Pharmaceutical sciences educator, organic chemistry mentor, research contributor, and builder of practical academic tools.</p>
        <div class="hero-actions">
          <a class="button button-primary" href="{route_to_href('publications', prefix)}">View publications</a>
          <a class="button button-secondary" href="{route_to_href('apps-for-academics/my-apps-for-academics', prefix)}">Explore academic apps</a>
        </div>
      </div>
      <div class="hero-card">
        <span class="eyebrow-card">Focus Areas</span>
        <ul class="clean-list">
          <li>Organic Chemistry education</li>
          <li>Molecular modeling and drug design</li>
          <li>Academic workflow tooling</li>
          <li>Bilingual teaching resources</li>
        </ul>
      </div>
    </section>
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">About Me</span>
          <h2>Academic identity preserved from the original site</h2>
        </div>
      </div>
      <div class="two-column-copy">
        <div>{''.join(f'<p>{html.escape(text)}</p>' for text in about_paragraphs[:2])}</div>
        <div>{''.join(f'<p>{html.escape(text)}</p>' for text in about_paragraphs[2:])}</div>
      </div>
      {render_social_links(social_section["links"]) if social_section else ""}
    </section>
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">Featured Video</span>
          <h2>وصايا لطلبة صيدلة الجدد</h2>
        </div>
      </div>
      <div class="embed-shell video-shell">
        <iframe loading="lazy" src="{html.escape(video_url)}" title="وصايا لطلبة صيدلة الجدد" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </section>
    <section class="panel rtl-panel">
      {''.join(f'<p>{html.escape(text)}</p>' for text in (arabic_section["texts"] if arabic_section else []))}
    </section>
    <!-- Visitor-counter embed omitted intentionally. -->
    """


def render_learn_overview(prefix: str) -> str:
    stages = [
        {
            "route": "learn-organic-chemistry/basics-of-organic-chemistry",
            "label": "Basics",
            "tag": "Structures and concepts",
            "title": "Speaking the Language of Molecules",
            "summary": "Build the foundation of organic chemistry through bonding, structure, hybridization, resonance, and the visual language of molecules.",
        },
        {
            "route": "learn-organic-chemistry/organic-i",
            "label": "Organic-I",
            "tag": "Families and patterns",
            "title": "Exploring Organic Chemistry Fundamentals",
            "summary": "Move through essential ideas including hydrocarbon families, aromaticity, and the stereochemical patterns that shape organic thinking.",
        },
        {
            "route": "learn-organic-chemistry/organic-ii",
            "label": "Organic-II",
            "tag": "Reactivity and transformations",
            "title": "Different Classes of Organic Compounds",
            "summary": "Discover how major functional groups are organized, how they are prepared, and how their reactions drive organic transformations.",
        },
        {
            "route": "learn-organic-chemistry/organic-iii",
            "label": "Organic-III",
            "tag": "Interpretation and analysis",
            "title": "Exploring Heterocycles and Spectroscopic Techniques",
            "summary": "Explore heterocyclic chemistry while developing the tools needed to interpret structures through spectroscopy and problem solving.",
        },
    ]
    cards = "".join(
        f"""
          <article class="learn-journey-card">
            <div class="learn-journey-topline">
              <span class="learn-journey-number">{index:02d}</span>
              <span class="learn-journey-tag">{html.escape(stage['tag'])}</span>
            </div>
            <div class="learn-journey-body">
              <h3>{html.escape(stage['title'])}</h3>
              <p>{html.escape(stage['summary'])}</p>
            </div>
            <div class="learn-journey-footer">
              <a class="button button-primary" href="{route_to_href(stage['route'], prefix)}">Explore this stage</a>
            </div>
          </article>
        """
        for index, stage in enumerate(stages, 1)
    )
    return f"""
    <section class="learn-journey" aria-labelledby="learn-journey-title">
      <div class="learn-journey-hero">
        <div class="learn-journey-copy">
          <span class="learn-journey-kicker">Organic Chemistry Journey</span>
          <h1 id="learn-journey-title">A Journey Through Organic Chemistry</h1>
          <p class="learn-journey-lead">Explore how molecules are built, how organic structures behave, and how we learn to interpret transformations across the rich landscape of organic chemistry.</p>
        </div>
        <div class="learn-journey-summary" aria-label="Journey highlights">
          <div class="learn-journey-stat">
            <strong>4</strong>
            <span>connected stages</span>
          </div>
          <div class="learn-journey-stat">
            <strong>Recorded videos</strong>
            <span>organized by organic themes</span>
          </div>
          <div class="learn-journey-stat">
            <strong>Spectroscopy</strong>
            <span>and heterocyclic exploration</span>
          </div>
        </div>
      </div>

      <div class="learn-journey-heading">
        <div>
          <span class="learn-journey-section-kicker">Journey map</span>
          <h2>Four stages through organic chemistry</h2>
        </div>
        <p>Each stage opens a page with recorded video topics, arranged as a guided exploration rather than a formal course list.</p>
      </div>

      <section class="learn-journey-grid" aria-label="Organic chemistry stages">
        {cards}
      </section>
    </section>
    """


def render_apps_academics_hub(prefix: str) -> str:
    targets = [
        "apps-for-academics/mark-list-maker",
        "apps-for-academics/attendane-export",
        "apps-for-academics/sample-key-generator",
    ]
    return '<section class="card-grid apps-grid">' + "".join(
        f"""
        <article class="tool-card">
          <div class="card-head">
            <h3>{html.escape(PAGE_SPECS[route]['title'])}</h3>
            <p>{html.escape(PAGE_SPECS[route]['description'])}</p>
          </div>
          <div class="card-actions">
            <a class="button button-primary" href="{route_to_href(route, prefix)}">Open page</a>
          </div>
        </article>
        """
        for route in targets
    ) + "</section>"


def render_apps_students_hub(prefix: str) -> str:
    targets = [
        "apps-for-students/woodward-fieser-lmax-calculator",
        "apps-for-students/nomenclature",
        "apps-for-students/elemental-analysis",
    ]
    return '<section class="card-grid apps-grid">' + "".join(
        f"""
        <article class="tool-card">
          <div class="card-head">
            <span class="eyebrow-card">Student Tool</span>
            <h3>{html.escape(PAGE_SPECS[route]['title'])}</h3>
            <p>{html.escape(PAGE_SPECS[route]['description'])}</p>
          </div>
          <div class="card-actions">
            <a class="button button-primary" href="{route_to_href(route, prefix)}">Open page</a>
          </div>
        </article>
        """
        for route in targets
    ) + "</section>"


def render_course_page(parsed: dict) -> str:
    texts = []
    for section in parsed["sections"]:
        texts.extend(section["texts"])
    if texts:
        texts = texts[1:]
    texts = [text for text in texts if text not in {"-", "1", "2", "3"}]
    pairs = []
    for index, video in enumerate(parsed["youtube_urls"]):
        title = texts[index] if index < len(texts) else f"Video {index + 1}"
        pairs.append((title, video))
    return f"""
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">Recorded Topics</span>
          <p>Topic highlights and recorded videos for this stage of the journey.</p>
        </div>
      </div>
    </section>
    {render_topic_cards(texts)}
    {render_video_gallery(pairs) if pairs else ''}
    """


def render_apps_overview(parsed: dict) -> tuple[str, dict]:
    intro = ""
    cards = []
    lookup = {}
    featured_titles = {"Zotero Style Creator", "Paper Marks Calculator", "Excel Dendogram Generator"}
    for section in parsed["sections"]:
        if not intro and section["texts"] and "Blending passion with purpose" in section["texts"][0]:
            intro = section["texts"][0]
        if not any(text.startswith("With ") for text in section["texts"]):
            continue
        descriptor = next(text for text in section["texts"] if text.startswith("With "))
        title = descriptor.replace("With ", "").replace(", you can:", "").replace(" , you can:", "").strip()
        if title == "EduTrack":
            title = "Grades & Attendance Sync"
        if title == "Certificates Maker":
            title = "Sample Key Generator"
        if title not in featured_titles:
            continue
        bullets = [text for text in section["texts"] if text not in {"Download", descriptor}]
        primary = next((link["href"] for link in section["links"] if "box.com" in link["href"] or "doi.org" in link["href"]), "")
        secondary = [link for link in section["links"] if link["href"] != primary]
        actions = []
        if primary:
            actions.append(f'<a class="button button-primary" href="{html.escape(primary)}" target="_blank" rel="noreferrer">Download</a>')
        for item in secondary[:2]:
            label = item["label"] or icon_for_url(item["href"])
            actions.append(f'<a class="button button-secondary" href="{html.escape(item["href"])}" target="_blank" rel="noreferrer">{html.escape(label)}</a>')
        lookup[title] = {"bullets": bullets, "download": primary}
        cards.append(
            f"""
            <article class="tool-card">
              <div class="card-head">
                <span class="eyebrow-card">Academic App</span>
                <h3>{html.escape(title)}</h3>
                <p>{html.escape(descriptor)}</p>
              </div>
              <ul class="clean-list">{''.join(f'<li>{html.escape(item)}</li>' for item in bullets)}</ul>
              <div class="card-actions">{''.join(actions)}</div>
            </article>
            """
        )
    body = f"""
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">Apps for Academics</span>
          <h2>A purposeful toolkit for teaching and research</h2>
          <p>{html.escape(intro)}</p>
        </div>
      </div>
    </section>
    <section class="card-grid apps-grid">{''.join(cards)}</section>
    """
    return body, lookup


def render_leaf_app(spec: dict, parsed: dict, lookup: dict) -> str:
    live_url = next((url for url in parsed["data_urls"] if url.startswith("https://") and "view/mohammad-abdulwahhab" not in url), "")
    details = lookup.get(spec["app_key"], {})
    actions = []
    if live_url:
        actions.append(f'<a class="button button-primary" href="{html.escape(live_url)}" target="_blank" rel="noreferrer">Open live tool</a>')
    if details.get("download"):
        actions.append(f'<a class="button button-secondary" href="{html.escape(details["download"])}" target="_blank" rel="noreferrer">Download package</a>')
    return f"""
    <section class="panel">
      <div class="panel-header">
        <div>
          <span class="eyebrow-card">Standalone Route</span>
          <h2>{html.escape(spec['title'])}</h2>
          <p>This dedicated route mirrors the original leaf page while surfacing the live tool and download entry points more clearly.</p>
        </div>
        <div class="card-actions">{''.join(actions)}</div>
      </div>
      {'<ul class="clean-list">' + ''.join(f'<li>{html.escape(item)}</li>' for item in details.get("bullets", [])) + '</ul>' if details.get("bullets") else ''}
    </section>
    {render_live_app(spec['title'], live_url, spec.get('shell_class', '')) if live_url else ''}
    """


def render_embedded_tools(route: str, parsed: dict, prefix: str) -> str:
    embeds = []
    for section in parsed["sections"]:
        embeds.extend(section["embeds"])
    embed_items = []
    for index, code in enumerate(embeds):
        match = re.search(r"<title>(.*?)</title>", html.unescape(code), re.IGNORECASE | re.DOTALL)
        title = sanitize_text(match.group(1)) if match else f"Embedded tool {index + 1}"
        embed_items.append((title, write_embed_file(route, index, code), "Open full screen"))
    grid_class = "stack-grid stack-grid-two" if route == "apps-for-students/elemental-analysis" else "stack-grid"
    specific_class = " app-shell--nomenclature" if route == "apps-for-students/nomenclature" else ""
    cards = []
    for title, embed_path, label in embed_items:
        cards.append(
            f"""
            <article class="tool-card">
              <div class="card-head">
                <h3>{html.escape(title)}</h3>
              </div>
              <div class="embed-shell app-shell{specific_class}">
                <iframe loading="lazy" src="{prefix}{html.escape(embed_path)}" title="{html.escape(title)}"></iframe>
              </div>
              <div class="card-actions">
                <a class="button button-secondary" href="{prefix}{html.escape(embed_path)}" target="_blank" rel="noreferrer">{html.escape(label)}</a>
              </div>
            </article>
            """
        )
    return f'<section class="{grid_class}">' + "".join(cards) + "</section>"


def render_external_app(spec: dict, parsed: dict) -> str:
    live_url = next((url for url in parsed["data_urls"] if url.startswith("https://") and "view/mohammad-abdulwahhab" not in url), "")
    if not live_url:
        return """
        <section class="panel">
          <div class="panel-header">
            <div>
              <span class="eyebrow-card">Placeholder</span>
              <h2>Embed source was not directly reusable</h2>
              <p>The original wrapper did not expose a reusable public embed here. This route remains in place so the site structure is complete.</p>
            </div>
          </div>
        </section>
        """
    return render_live_app(spec["title"], live_url)


def render_publications(parsed: dict) -> str:
    citations = []
    dois = []
    for section in parsed["sections"]:
        if len(section["texts"]) > 5:
            citations = section["texts"]
            dois = [link["href"] for link in section["links"] if "doi.org" in link["href"]]
            break
    return render_publication_cards([(citation, dois[index]) for index, citation in enumerate(citations) if index < len(dois)])


def render_workshop_overview(prefix: str) -> str:
    session_routes = [
        "scientific-research-workshop/session-1",
        "scientific-research-workshop/session-2",
        "scientific-research-workshop/session-3",
    ]
    session_details = {
        "scientific-research-workshop/session-1": {
            "label": "Session 1",
            "title": "The Everyday Researcher: From Digital Noise to Trusted Source",
            "summary": "Build a practical foundation for finding reliable information and separating strong evidence from distraction and weak sourcing.",
        },
        "scientific-research-workshop/session-2": {
            "label": "Session 2",
            "title": "Decoding Research: From Question to Publication",
            "summary": "Follow the research journey from forming a strong question to understanding the steps that shape a publishable scientific study.",
        },
        "scientific-research-workshop/session-3": {
            "label": "Session 3",
            "title": "Making an Impact: How to Share Your Science",
            "summary": "Explore practical strategies for presenting, communicating, and amplifying research so that good science reaches the right audience.",
        },
    }
    cards = "".join(
        f"""
          <article class="workshop-session-card">
            <div class="workshop-session-topline">
              <span class="workshop-session-number">{index:02d}</span>
              <span class="workshop-session-format">Interactive material + video</span>
            </div>
            <div class="workshop-session-body">
              <span class="workshop-session-label">{html.escape(session_details[route]['label'])}</span>
              <h3>{html.escape(session_details[route]['title'])}</h3>
              <p>{html.escape(session_details[route]['summary'])}</p>
            </div>
            <div class="workshop-session-footer">
              <a class="button button-primary" href="{route_to_href(route, prefix)}">Open session</a>
            </div>
          </article>
        """
        for index, route in enumerate(session_routes, 1)
    )
    return f"""
    <section class="workshop-overview" aria-labelledby="workshop-title">
      <div class="workshop-hero">
        <div class="workshop-hero-copy">
          <span class="workshop-kicker">Research Workshop</span>
          <h1 id="workshop-title">Introduction to Scientific Research</h1>
          <p class="workshop-lead">A focused three-session learning path covering trusted sources, research design, and practical ways to share scientific work with clarity and impact.</p>
        </div>
        <div class="workshop-summary" aria-label="Workshop highlights">
          <div class="workshop-stat">
            <strong>3</strong>
            <span>guided sessions</span>
          </div>
          <div class="workshop-stat">
            <strong>Interactive</strong>
            <span>embedded materials</span>
          </div>
          <div class="workshop-stat">
            <strong>Recorded</strong>
            <span>session videos</span>
          </div>
        </div>
      </div>

      <div class="workshop-section-heading">
        <div>
          <span class="workshop-section-kicker">Workshop roadmap</span>
          <h2>Move through the sessions in order</h2>
        </div>
        <p>Each session has its own materials page with the embedded content and recording ready to open.</p>
      </div>

      <section class="workshop-session-grid" aria-label="Workshop sessions">
        {cards}
      </section>
    </section>
    """


def render_workshop_session(route: str, parsed: dict, prefix: str) -> str:
    embeds = [code for section in parsed["sections"] for code in section["embeds"]]
    embed_items = [(f"Embedded workshop material {index}", write_embed_file(route, index - 1, code), "Open full material") for index, code in enumerate(embeds, 1)]
    workshop_html = ""
    if embed_items:
        workshop_html = '<section class="stack-grid">' + "".join(
            f"""
            <article class="tool-card">
              <div class="card-head">
                <h3>{html.escape(title)}</h3>
              </div>
              <div class="embed-shell app-shell app-shell--workshop">
                <iframe loading="lazy" src="{prefix}{html.escape(embed_path)}" title="{html.escape(title)}"></iframe>
              </div>
              <div class="card-actions">
                <a class="button button-secondary" href="{prefix}{html.escape(embed_path)}" target="_blank" rel="noreferrer">{html.escape(label)}</a>
              </div>
            </article>
            """
            for title, embed_path, label in embed_items
        ) + "</section>"
    video_html = ""
    if parsed["youtube_urls"]:
        video_html = f"""
        <section class="panel">
          <div class="panel-header">
            <div>
              <span class="eyebrow-card">Recording</span>
              <h2>Session Video</h2>
            </div>
          </div>
          <div class="embed-shell video-shell">
            <iframe loading="lazy" src="{html.escape(parsed['youtube_urls'][0])}" title="{html.escape(PAGE_SPECS[route]['title'])}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          </div>
        </section>
        """
    return workshop_html + video_html


def render_highlights(parsed: dict, prefix: str) -> str:
    items = []
    for section in parsed["sections"]:
        if section["texts"] and section["texts"][0] != "Highlights from My Journey":
            items.extend(section["texts"])
    cards = []
    for index, raw_item in enumerate(items, 1):
        item = raw_item.replace("som e", "some")
        media = HIGHLIGHT_IMAGE_MAP.get(item, [])
        media_html = ""
        if media:
            figures = "".join(
                f'<figure class="highlight-figure highlight-figure--{entry["variant"]}"><img src="{prefix}{html.escape(entry["src"])}" alt="{html.escape(item)}" loading="lazy" /></figure>'
                for entry in media
            )
            media_html = f'<div class="highlight-media{" highlight-media--gallery" if len(media) > 1 else ""}">{figures}</div>'
        cards.append(
            f"""
            <article class="highlight-card">
              {media_html}
              <div class="card-head">
                <span class="eyebrow-card">Highlight {index}</span>
                <p>{html.escape(item)}</p>
              </div>
            </article>
            """
        )
    return '<section class="stack-grid">' + "".join(cards) + "</section>"


def render_body(route: str, spec: dict, parsed: dict, prefix: str, app_lookup: dict) -> tuple[str, dict]:
    if spec["kind"] == "home":
        return render_home(parsed, prefix), app_lookup
    if spec["kind"] == "learn-overview":
        return render_learn_overview(prefix), app_lookup
    if spec["kind"] == "apps-academics-hub":
        return render_apps_academics_hub(prefix), app_lookup
    if spec["kind"] == "apps-students-hub":
        return render_apps_students_hub(prefix), app_lookup
    if spec["kind"] == "course-videos":
        return render_course_page(parsed), app_lookup
    if spec["kind"] == "apps-overview":
        body, lookup = render_apps_overview(parsed)
        app_lookup.update(lookup)
        return body, app_lookup
    if spec["kind"] == "academic-app-leaf":
        return render_leaf_app(spec, parsed, app_lookup), app_lookup
    if spec["kind"] == "embedded-tools":
        return render_embedded_tools(route, parsed, prefix), app_lookup
    if spec["kind"] == "external-app":
        return render_external_app(spec, parsed), app_lookup
    if spec["kind"] == "publications":
        return render_publications(parsed), app_lookup
    if spec["kind"] == "workshop-overview":
        return render_workshop_overview(prefix), app_lookup
    if spec["kind"] == "workshop-session":
        return render_workshop_session(route, parsed, prefix), app_lookup
    if spec["kind"] == "highlights":
        return render_highlights(parsed, prefix), app_lookup
    return "", app_lookup


def render_page(route: str, spec: dict, parsed: dict, prefix: str, body_html: str) -> str:
    description = spec["description"] or parsed["description"]
    return textwrap.dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZJFG15M00T"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){{dataLayer.push(arguments);}}
              gtag('js', new Date());

              gtag('config', 'G-ZJFG15M00T');
            </script>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>{html.escape(spec['title'])} | Mohammad Abdulwahhab</title>
            <meta name="description" content="{html.escape(description)}" />
            <meta property="og:title" content="{html.escape(spec['title'])} | Mohammad Abdulwahhab" />
            <meta property="og:description" content="{html.escape(description)}" />
            <meta property="og:type" content="website" />
            <meta name="theme-color" content="#123342" />
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
            <link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
            <link rel="stylesheet" href="{prefix}assets/site.css" />
            <script type="module" src="{prefix}assets/site.js"></script>
          </head>
          <body>
            <a class="skip-link" href="#main-content">Skip to content</a>
            <header class="site-header">
              <div class="top-shell">
                <a class="brand" href="{route_to_href('home', prefix)}">
                  <span class="brand-mark">MA</span>
                  <span class="brand-copy">
                    <strong>Mohammad Abdulwahhab</strong>
                    <small>Academic website</small>
                  </span>
                </a>
                <div class="header-actions">
                  <button class="icon-button" type="button" data-theme-toggle aria-label="Toggle dark mode">Theme</button>
                  <button class="icon-button mobile-nav-toggle" type="button" data-mobile-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
                </div>
              </div>
              <nav id="site-nav" class="site-nav" aria-label="Primary navigation">
                <div class="nav-inner">{render_navigation(prefix, route)}</div>
              </nav>
            </header>
            <main id="main-content" class="page-shell">
              {render_breadcrumbs(route, prefix)}
              <section class="page-intro">
                <h1>{html.escape(spec['title'])}</h1>
                <p>{html.escape(description)}</p>
              </section>
              {body_html}
            </main>
            <footer class="site-footer">
              <div>
                <strong>Mohammad Abdulwahhab</strong>
                <p>Academic, research, and teaching website.</p>
              </div>
              <div class="footer-links">
                <a href="mailto:mwahhab@mans.edu.eg">mwahhab@mans.edu.eg</a>
                <a href="https://www.linkedin.com/in/mwahhab95" target="_blank" rel="noreferrer">LinkedIn</a>
                <a href="https://www.youtube.com/@mwahhab95" target="_blank" rel="noreferrer">YouTube</a>
              </div>
            </footer>
          </body>
        </html>
        """
    )


def clear_generated_output() -> None:
    for name in ["home", "learn-organic-chemistry", "apps-for-academics", "apps-for-students", "publications", "scientific-research-workshop", "ai-index", "highlights", "embeds"]:
        target = ROOT / name
        if not target.exists():
            continue
        for child in sorted(target.rglob("*"), reverse=True):
            try:
                if child.is_file():
                    child.unlink()
                elif child.is_dir():
                    child.rmdir()
            except PermissionError:
                pass
        try:
            target.rmdir()
        except PermissionError:
            pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the rebuilt academic website.")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="Directory containing the raw HTML dump.")
    args = parser.parse_args()

    source_dir = Path(args.source).resolve()
    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")

    clear_generated_output()
    parsed_pages = {route: parse_source_page(source_dir / spec["source"]) for route, spec in PAGE_SPECS.items()}
    app_lookup = {}
    for route, spec in PAGE_SPECS.items():
        prefix = prefix_for_route(route)
        body, app_lookup = render_body(route, spec, parsed_pages[route], prefix, app_lookup)
        output = ROOT / route_to_path(route)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_page(route, spec, parsed_pages[route], prefix, body), encoding="utf-8")


if __name__ == "__main__":
    main()

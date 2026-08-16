#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, json, re
sys.path.insert(0, os.path.dirname(__file__))
from build import (page, crumbs_html, breadcrumb_schema, local_business_schema,
                    faq_schema, faq_html, quote_form, DOMAIN, PHONE_TEL, PHONE_DISPLAY, EMAIL, TRACKING_HEAD, CSS, NAV, FOOTER)
from generate_pages import hero, SERVICES

OUT = os.path.dirname(__file__)

# ---------------------------------------------------------------------------
# PRIVACY POLICY
# ---------------------------------------------------------------------------
def privacy_page():
    body = f"""{crumbs_html([("Home","/"),("Privacy Policy",None)])}
<section><div class="container narrow prose">
<p>Last updated: August 2026.</p>
<p>Orangeville Drywalling ("we") operates orangevilledrywalling.com. This page explains what we collect and how we use it.</p>
<h2>What we collect</h2>
<p>When you submit our quote form we collect the details you provide: name, email, phone, property address, service needed, and any project details you add. Our hosting provider also logs standard technical data (IP address, browser type) for security purposes. We use Google Analytics, Microsoft Clarity, and the Meta Pixel to understand how visitors use this site.</p>
<h2>How we use it</h2>
<p>Quote requests are used for one purpose: connecting you with our exclusive local drywall contracting partner who can complete your job. We share your request details with that partner so they can contact you with a quote. We do not sell your information to third parties or use it for unrelated marketing.</p>
<h2>How this site works</h2>
<p>orangevilledrywalling.com is a lead-generation and referral site based in Orangeville, Ontario — not a contracting company itself. When you request a quote, your inquiry is routed to a single vetted, exclusive local drywall contractor serving Orangeville and Dufferin County.</p>
<h2>Cookies</h2>
<p>This site uses essential cookies plus analytics and advertising cookies (Google Analytics, Microsoft Clarity, Meta Pixel) to measure site performance and ad effectiveness. You can control cookies through your browser settings.</p>
<h2>Contact / removal requests</h2>
<p>To ask what information we hold about you, or to have it deleted, email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
</div></section>"""
    schemas = [
        local_business_schema(),
        breadcrumb_schema([("Home", DOMAIN + "/"), ("Privacy Policy", DOMAIN + "/privacy")]),
    ]
    html = page(
        "Privacy Policy | Orangeville Drywalling",
        "Privacy policy for Orangeville Drywalling, explaining what information we collect, how we use it, and how we protect your data when you request a quote.",
        "/privacy", schemas, body,
        hero("Privacy Policy", "What we collect, how we use it, and how to reach us about your data.")
    )
    with open(os.path.join(OUT, "privacy.html"), "w") as f:
        f.write(html)
    print("wrote privacy.html")

privacy_page()

# ---------------------------------------------------------------------------
# HOMEPAGE UPDATE (edit the live homepage: fix breadcrumb schema, add
# real internal links from service cards to their new dedicated pages)
# ---------------------------------------------------------------------------
def update_homepage():
    html = open("/tmp/od_home.html").read()

    # 1) Remove the BreadcrumbList schema that pointed at a non-crawlable
    #    "#services" anchor. A breadcrumb trail doesn't belong on the
    #    homepage itself (nothing sits "above" it) -- the hub/service/area
    #    pages now carry correct BreadcrumbList schema instead.
    bad_breadcrumb = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://orangevilledrywalling.com/"}, {"@type": "ListItem", "position": 2, "name": "Drywall Services", "item": "https://orangevilledrywalling.com/#services"}]}</script>\n'
    assert bad_breadcrumb.strip() in html, "breadcrumb block not found verbatim"
    html = html.replace(bad_breadcrumb, "")

    # 2) Replace the services grid-3 block with one that links each card to
    #    its new dedicated /services/{slug} page, plus a link to the hub.
    old_services_block = '''<section id="services"><div class="container">
  <h2>Drywall Services</h2>
  <p class="section-intro">Clean lines, smooth finishes, and no dust everywhere it shouldn't be — that's the standard we hold every job to.</p>
  <div class="grid-3"><div class="card"><span class="card-icon">🧱</span><h3>Drywall Installation</h3><p>New-construction and renovation drywall hung, taped, and finished to a smooth, paint-ready surface.</p></div><div class="card"><span class="card-icon">🩹</span><h3>Drywall Repair &amp; Patching</h3><p>Holes, cracks, water damage, and dents patched invisibly — no mismatched texture.</p></div><div class="card"><span class="card-icon">🖌️</span><h3>Taping &amp; Mudding</h3><p>Level 4 and Level 5 finishes for a flawless wall, ready for paint or wallpaper.</p></div><div class="card"><span class="card-icon">🧹</span><h3>Popcorn Ceiling Removal</h3><p>Scrape, re-mud, and re-texture for a clean, modern ceiling.</p></div><div class="card"><span class="card-icon">🏚️</span><h3>Basement Drywalling</h3><p>Full basement drywall packages, including moisture-resistant board where needed.</p></div><div class="card"><span class="card-icon">🏢</span><h3>Commercial Drywall</h3><p>Office, retail, and light-commercial drywall and partition work.</p></div></div>
</div></section>'''
    assert old_services_block in html, "services block not found verbatim"

    cards = "".join(
        f'<div class="card"><span class="card-icon">{icon}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<p><a class="card-link" href="/services/{slug}">Details &amp; FAQ →</a></p></div>'
        for slug, name, icon, blurb in SERVICES
    )
    new_services_block = f'''<section id="services"><div class="container">
  <h2>Drywall Services</h2>
  <p class="section-intro">Clean lines, smooth finishes, and no dust everywhere it shouldn't be — that's the standard we hold every job to. <a href="/services">Browse full service details →</a></p>
  <div class="grid-3">{cards}</div>
</div></section>'''
    html = html.replace(old_services_block, new_services_block)

    # 3) Add card-link style so the new "Details & FAQ ->" links render
    #    consistently with the rest of the card styling (matches the CSS
    #    already added to build.py's shared stylesheet for new pages).
    style_anchor = ".card a { color: var(--accent-dark); font-weight: 700; text-decoration: none; }"
    # homepage doesn't have that exact rule (it styles cards without a
    # pre-existing card link style) -- add one right after .card p rule.
    old_card_p_rule = ".card p { font-size: .95rem; color: var(--text-muted); line-height: 1.6; }"
    assert old_card_p_rule in html
    html = html.replace(
        old_card_p_rule,
        old_card_p_rule + "\n.card a.card-link { color: var(--accent-dark); font-weight: 700; font-size: .92rem; text-decoration: none; }\n.card a.card-link:hover { text-decoration: underline; }"
    )

    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(html)
    print("wrote index.html (homepage, updated)")

update_homepage()

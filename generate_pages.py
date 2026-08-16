#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import (page, crumbs_html, breadcrumb_schema, local_business_schema,
                    faq_schema, faq_html, quote_form, DOMAIN, PHONE_TEL, PHONE_DISPLAY, EMAIL)

OUT = os.path.dirname(__file__)

def hero(title, sub, cta_label="Get a Free Quote"):
    return f"""<div class="hero">
<div class="hero-bg"></div>
<div class="hero-content">
<h1>{title}</h1>
<p>{sub}</p>
<a class="btn btn-primary" href="#contact">{cta_label}</a>
<a href="tel:{PHONE_TEL}" class="btn btn-secondary">📞 Call Now</a>
</div></div>"""

# ---------------------------------------------------------------------------
# SERVICES HUB
# ---------------------------------------------------------------------------
SERVICES = [
    ("drywall-installation", "Drywall Installation", "🧱",
     "New-construction and renovation drywall hung, taped, and finished to a smooth, paint-ready surface."),
    ("drywall-repair-patching", "Drywall Repair &amp; Patching", "🩹",
     "Holes, cracks, water damage, and dents patched invisibly — no mismatched texture."),
    ("taping-mudding", "Taping &amp; Mudding", "🖌️",
     "Level 4 and Level 5 finishes for a flawless wall, ready for paint or wallpaper."),
    ("popcorn-ceiling-removal", "Popcorn Ceiling Removal", "🧹",
     "Scrape, re-mud, and re-texture for a clean, modern ceiling."),
    ("basement-drywalling", "Basement Drywalling", "🏚️",
     "Full basement drywall packages, including moisture-resistant board where needed."),
    ("commercial-drywall", "Commercial Drywall", "🏢",
     "Office, retail, and light-commercial drywall and partition work."),
]

def services_hub():
    cards = "".join(
        f'<div class="card"><span class="card-icon">{icon}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<p><a class="card-link" href="/services/{slug}">Details &amp; FAQ →</a></p></div>'
        for slug, name, icon, blurb in SERVICES
    )
    body = f"""{crumbs_html([("Home","/"),("Services",None)])}
<section id="services"><div class="container">
<h2>Drywall Services in Orangeville &amp; Dufferin County</h2>
<p class="section-intro">Six services, one exclusive local partner. Pick the one that matches your project for full details, or just send us the basics and we'll figure it out with you.</p>
<div class="grid-3">{cards}</div>
</div></section>
<section class="local-section"><div class="container">
<h2>Proudly Serving Orangeville &amp; Area</h2>
<p class="section-intro">Based in Orangeville, regularly on the road across Dufferin County and the edges of Wellington and Peel.</p>
<p style="margin-top:1rem">Also serving nearby: <a href="/shelburne">Shelburne</a>, <a href="/grandvalley">Grand Valley</a>, <a href="/erin">Erin</a>, <a href="/mono">Mono</a>, and <a href="/caledon-village">Caledon Village</a>.</p>
</div></section>
{quote_form("Drywall Services")}"""
    schemas = [
        local_business_schema(),
        breadcrumb_schema([("Home", DOMAIN + "/"), ("Services", DOMAIN + "/services")]),
    ]
    html = page(
        "Drywall Services in Orangeville, ON | Orangeville Drywalling",
        "Drywall installation, repair, taping and mudding, popcorn ceilings, basements, and commercial work in Orangeville and Dufferin County. Free quotes.",
        "/services", schemas, body,
        hero("Drywall Services", "Installation, repair, taping, ceilings, basements, and commercial — pick your project below.")
    )
    with open(os.path.join(OUT, "services.html"), "w") as f:
        f.write(html)

# ---------------------------------------------------------------------------
# INDIVIDUAL SERVICE PAGES
# ---------------------------------------------------------------------------
def related_services_html(exclude_slug):
    others = [s for s in SERVICES if s[0] != exclude_slug][:3]
    cards = "".join(
        f'<div class="card"><span class="card-icon">{icon}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<p><a class="card-link" href="/services/{slug}">Details →</a></p></div>'
        for slug, name, icon, blurb in others
    )
    return f"""<section class="local-section"><div class="container">
<h2>Other Drywall Services</h2>
<div class="grid-3">{cards}</div>
</div></section>"""

def service_page(slug, name_plain, name_html, title, description, hero_h1, hero_sub,
                  intro_html, faqs, extra_service_type=None):
    body = f"""{crumbs_html([("Home","/"),("Services","/services"),(name_plain,None)])}
<section><div class="container narrow prose">
{intro_html}
</div></section>
{related_services_html(slug)}
<section class="faq-section"><div class="container narrow">
<h2>{name_plain} — Frequently Asked Questions</h2>
{faq_html(faqs)}
</div></section>
{quote_form(extra_service_type or name_html)}"""
    schemas = [
        local_business_schema(),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": name_plain,
            "provider": {"@type": "LocalBusiness", "name": "Orangeville Drywalling", "telephone": PHONE_TEL, "url": DOMAIN},
            "areaServed": ["Orangeville", "Shelburne", "Grand Valley", "Erin", "Mono", "Caledon Village"],
            "description": description,
        },
        breadcrumb_schema([
            ("Home", DOMAIN + "/"),
            ("Services", DOMAIN + "/services"),
            (name_plain, f"{DOMAIN}/services/{slug}"),
        ]),
        faq_schema(faqs),
    ]
    html = page(title, description, f"/services/{slug}", schemas, body, hero(hero_h1, hero_sub))
    with open(os.path.join(OUT, "services", f"{slug}.html"), "w") as f:
        f.write(html)


service_page(
    "drywall-installation", "Drywall Installation", "Drywall Installation",
    "Drywall Installation in Orangeville, ON | Orangeville Drywalling",
    "New-construction and renovation drywall installation in Orangeville and Dufferin County — hung, taped, and finished to a smooth, paint-ready surface.",
    "Drywall Installation in Orangeville",
    "New builds, additions, and renovations — hung and finished to a smooth, paint-ready surface.",
    """<h2>Full-Service Drywall Installation</h2>
<p>Whether it's a new addition, a basement being framed out for the first time, or a full room stripped back to the studs during a renovation, drywall installation is the step that turns framing into finished space. Our exclusive local contracting partner handles the full process for Orangeville and Dufferin County homeowners: measuring and layout, hanging sheets sized to minimize seams, screwing to code spacing, and taping and mudding to your choice of finish level before the room is ready for primer.</p>
<h2>What's Included</h2>
<ul>
<li>Layout and material takeoff so the job is quoted accurately the first time</li>
<li>Board hung on walls and ceilings, including tricky spots like stairwells, bulkheads, and tight closets</li>
<li>Screws set to proper depth and spacing — no popped screws down the road</li>
<li>Taping and mudding to Level 4 (standard, paint-ready) or Level 5 (skim coat, for accent walls or high-gloss paint) — see our <a href="/services/taping-mudding">taping &amp; mudding page</a> for the difference</li>
<li>Sanding and a final walk-through before we call it done</li>
</ul>
<h2>New Construction vs. Renovation Work</h2>
<p>New-construction installation is the simpler case — open framing, easy material access, and a predictable schedule. Renovation installation is where local experience matters more: protecting finished areas of the house, working around existing electrical and plumbing, and matching the new wall's finish to whatever's already up so the seam between old and new disappears. If your project is specifically a basement, our <a href="/services/basement-drywalling">basement drywalling page</a> covers the moisture and code considerations that come with below-grade work.</p>
<p>For a sense of what installation typically runs in this area, see our <a href="/blog/how-much-does-drywall-installation-cost-in-orangeville">2026 drywall installation cost guide for Orangeville</a>.</p>""",
    [
        ("How long does a typical installation take?", "It depends on scope — a single room can often be hung and finished within a week including drying time between coats, while a full basement or addition typically runs one to two weeks. We'll give you a realistic timeline with your quote."),
        ("Do I need to prime and paint separately?", "Yes — we finish the drywall to a paint-ready surface (Level 4 or Level 5), but priming and painting are a separate step. We're happy to recommend painters if you need one."),
        ("Can you match an existing wall's texture where new drywall meets old?", "Yes, texture matching (orange peel, knockdown, or smooth) is standard practice when new drywall ties into an existing wall or ceiling."),
        ("Do you handle the permit if my project needs one?", "Structural and larger renovation permits are typically pulled by the general contractor or homeowner; we're glad to advise on what a project will likely need and coordinate around inspection timing."),
    ],
)

service_page(
    "drywall-repair-patching", "Drywall Repair &amp; Patching", "Drywall Repair & Patching",
    "Drywall Repair &amp; Patching in Orangeville | Orangeville Drywalling",
    "Drywall repair and patching in Orangeville and Dufferin County — holes, cracks, water damage, and dents fixed invisibly with matched texture. Free quotes.",
    "Drywall Repair &amp; Patching",
    "Holes, cracks, water damage, and dents — patched invisibly, no mismatched texture.",
    """<h2>Repairs That Actually Disappear</h2>
<p>A bad patch job is more obvious than the hole it fixed — a flat spot where the texture doesn't match, a slightly different sheen once it's painted, a seam you can see at an angle in low light. The difference between a good repair and an obvious one is almost always in the texture match and the feathering of the joint compound, and that's where experience shows.</p>
<h2>What We Repair</h2>
<ul>
<li><strong>Doorknob holes and impact damage</strong> — the most common call, usually a same-visit fix</li>
<li><strong>Cracks</strong> — settling cracks at corners and above doorways, common in both older farmhouses and newer builds as a house settles through its first few winters</li>
<li><strong>Water damage</strong> — from roof leaks, plumbing failures, or ice damming; we assess whether the affected board needs full replacement or can be patched once the source is fixed</li>
<li><strong>Dents and gouges</strong> from moving furniture or renovations elsewhere in the house</li>
<li><strong>Nail pops and popped screws</strong> on older installations</li>
</ul>
<h2>Texture Matching</h2>
<p>Orange peel, knockdown, and smooth (skim-coated) are the three textures we run into most across Orangeville, Shelburne, and the surrounding towns — older homes tend toward heavier textures, newer builds and renovated spaces increasingly go smooth. We match whatever's already on your wall so the repair blends in rather than standing out once it's painted.</p>
<h2>Small Job? Still Worth a Call</h2>
<p>No repair is too small to quote — from a single hole to patching an entire wall after removing old paneling or wallpaper. If the damage is extensive enough that patching won't hold up, we'll tell you honestly and talk through whether a full-panel replacement makes more sense.</p>""",
    [
        ("Is a small hole worth calling a pro for, or can I DIY it?", "A single small hole is a reasonable DIY project if you're comfortable with it. Where pros earn their keep is texture matching and feathering the edge so the patch is invisible once painted — that's the part that's hard to get right without experience."),
        ("Can you fix a crack without it coming back?", "We address the underlying cause where we can identify it (settling, humidity, structural movement) and use the right repair method for the crack type — but on active settling cracks, some recurrence over years is normal for any repair, patch or professional."),
        ("What if the water damage is still active?", "We'll flag it and recommend fixing the source (roof, plumbing, ice damming) before we patch — repairing over an active leak just means redoing the work later."),
        ("Do you patch and paint, or just patch?", "We patch, tape, and finish the texture. Painting is a separate step, though we can point you to painters we've worked alongside if you need the full job done."),
    ],
)

service_page(
    "taping-mudding", "Taping &amp; Mudding", "Taping & Mudding",
    "Taping &amp; Mudding in Orangeville, ON | Orangeville Drywalling",
    "Level 4 and Level 5 drywall taping and mudding in Orangeville and Dufferin County — flawless walls ready for paint or wallpaper. Free quotes.",
    "Taping &amp; Mudding",
    "Level 4 and Level 5 finishes for a flawless wall, ready for paint or wallpaper.",
    """<h2>Where the Finish Actually Comes From</h2>
<p>Hanging drywall is the easy part to see; the finish quality of a wall almost entirely comes down to the taping and mudding — three to four coats of joint compound over every seam and screw head, sanded smooth between coats, so the wall reads as one continuous surface instead of a grid of panels.</p>
<h2>Level 4 vs. Level 5 Finish</h2>
<p><strong>Level 4</strong> is the standard finish for most rooms: joints and fasteners covered with compound, sanded smooth, ready for a standard paint sheen (flat to satin). It's what the large majority of Orangeville-area homes need and what's typically included when installation is quoted.</p>
<p><strong>Level 5</strong> adds a thin skim coat of compound over the entire wall surface, not just the joints. It's worth the extra step for accent walls, walls that will get raking light from a window or pot lights (which shows every imperfection at Level 4), semi-gloss or gloss paint, and any wall going straight to a very light or dark colour where texture variation would otherwise show.</p>
<h2>The Process</h2>
<ul>
<li>Tape embedded over every seam with the first coat of compound</li>
<li>Two to three additional coats, each wider than the last, feathered to a smooth transition</li>
<li>Sanding between coats and after the final coat</li>
<li>Skim coat across the full surface for Level 5 work</li>
</ul>
<p>Drying time between coats matters more than people expect — rushing it is the most common cause of cracking and visible ridges later. We schedule for proper cure time between coats rather than compressing the timeline.</p>""",
    [
        ("Do I need Level 5 everywhere in my house?", "No — Level 4 is the right, standard finish for most rooms. Level 5 is worth the extra cost specifically where lighting or paint sheen would otherwise show every seam, like an accent wall under pot lights."),
        ("How long does taping and mudding take?", "Each coat needs to dry before the next goes on and before sanding, so a typical room runs three to five days start to finish even though the hands-on work is a fraction of that."),
        ("Will I see the seams after painting?", "Not if the taping and mudding is done properly and given enough dry time between coats — that's the whole point of the process."),
        ("Can this be done over existing painted drywall for a smoother finish?", "Yes, a skim coat can be applied over existing painted drywall to smooth out texture or minor imperfections, which is a common ask before repainting a room a darker or glossier colour."),
    ],
)

service_page(
    "popcorn-ceiling-removal", "Popcorn Ceiling Removal", "Popcorn Ceiling Removal",
    "Popcorn Ceiling Removal in Orangeville | Orangeville Drywalling",
    "Popcorn ceiling removal in Orangeville and Dufferin County — scraped, re-mudded, and re-textured for a clean, modern ceiling. Free quotes.",
    "Popcorn Ceiling Removal",
    "Scrape, re-mud, and re-texture for a clean, modern ceiling.",
    """<h2>Retiring the Popcorn Ceiling</h2>
<p>Textured "popcorn" ceilings were standard through the 1970s–90s and are common across older homes in Orangeville's downtown core and the surrounding villages — Erin, Hillsburgh, Grand Valley, and Caledon Village all have plenty of housing stock from that era. It's one of the most requested updates we get, and it makes a bigger visual difference to a room than almost any other single job.</p>
<h2>A Note on Older Homes and Asbestos</h2>
<p>Popcorn ceiling texture applied before the early-to-mid 1980s can, in some cases, contain asbestos. If your home was built or last had its ceilings finished before roughly 1990, we recommend a texture sample be tested before any scraping begins — it's a standard, inexpensive step and it's the responsible way to handle older ceilings. If a test comes back positive, that work needs to be handled by a licensed abatement contractor before we can do finish work; we're glad to point you toward one if it comes to that.</p>
<h2>The Process (Once Testing Clears)</h2>
<ul>
<li>Room prep and dust containment — plastic sheeting, floor protection, and containing the work area from the rest of the house</li>
<li>Wetting and scraping the texture off</li>
<li>Repairing any damage to the underlying drywall from the original texture application</li>
<li>Re-mudding and finishing to a smooth Level 4/5 ceiling, or a lighter modern texture if you prefer</li>
<li>Thorough cleanup — this is a genuinely messy job and containment matters</li>
</ul>
<p>Most single rooms are a one- to two-day job depending on ceiling condition; whole-house projects are scheduled in sections so you're not living in a construction zone the entire time.</p>""",
    [
        ("Do all popcorn ceilings need asbestos testing?", "Not necessarily, but if your home's ceilings were finished before about 1990, we recommend testing before scraping starts — it's a quick, low-cost step and the safe way to proceed on older homes."),
        ("How messy is this job really?", "It's one of the messier drywall jobs there is. We use dust and debris containment throughout, but plan for us to fully seal off the work area and expect some fine dust regardless — we clean thoroughly at the end of each day."),
        ("Can you leave a light texture instead of going fully smooth?", "Yes — after scraping we can finish the ceiling smooth (Level 4/5) or apply a lighter, more modern texture depending on what you'd prefer."),
        ("Do you also handle repainting the ceiling after?", "We finish the ceiling to a paint-ready surface; painting itself is a separate step, though we can recommend painters if needed."),
    ],
)

service_page(
    "basement-drywalling", "Basement Drywalling", "Basement Drywalling",
    "Basement Drywalling in Orangeville, ON | Orangeville Drywalling",
    "Full basement drywall packages in Orangeville and Dufferin County, including moisture-resistant board where needed. Free quotes on finishing your basement.",
    "Basement Drywalling",
    "Full basement drywall packages, including moisture-resistant board where needed.",
    """<h2>Finishing a Basement the Right Way</h2>
<p>Basements bring a different set of considerations than an above-grade room — moisture, framing over foundation walls, mechanical rooms, and often an irregular layout around ductwork, sump pits, and support columns. It's also one of the highest-demand jobs we get, since a large share of Dufferin County's newer builds — including many of the executive-style homes going up around Mono, Grand Valley, and the newer subdivisions in Shelburne — are sold with an unfinished basement.</p>
<h2>What's Different About Basement Work</h2>
<ul>
<li><strong>Moisture-resistant board</strong> around mechanical rooms, bathrooms, and anywhere near plumbing, so a future small leak doesn't mean replacing a whole wall</li>
<li><strong>Working around what's already there</strong> — support columns, ductwork, electrical panels, and sump pump locations that need to stay accessible</li>
<li><strong>Insulation coordination</strong> — Ontario Building Code sets minimum insulation requirements for basement walls, and drywall goes up after insulation and any required vapour barrier is in place; we'll flag if something upstream needs attention before we hang board</li>
<li><strong>Bulkheads and soffits</strong> to box in ductwork and pipes cleanly rather than leaving them exposed</li>
</ul>
<h2>Full Packages or Just the Drywall</h2>
<p>Some homeowners have framing and electrical already roughed in and just need the drywall phase; others are starting from a bare unfinished basement and want the whole build-out coordinated. Tell us where your project is at when you request a quote and we'll scope accordingly — including moisture-resistant board specifically wherever it's needed, not applied blanket across the whole space, which keeps cost reasonable.</p>""",
    [
        ("Do I need moisture-resistant board throughout the whole basement?", "No — it's used strategically near mechanical rooms, bathrooms, and plumbing, not required for the entire space. We'll spec it where it actually matters."),
        ("Can you work around an unfinished mechanical room or sump pit?", "Yes, and we should — those areas typically need to stay accessible rather than being fully enclosed, which we plan for in the layout."),
        ("Is my basement too irregular in shape to finish?", "Almost never. Support columns, low bulkheads, and odd corners are normal in basement work and something we plan around regularly."),
        ("Does this include the framing and insulation, or just drywall?", "We can quote drywall only if framing and insulation are already in place, or scope the fuller build-out if you're starting from a bare basement — tell us where your project stands when you request a quote."),
    ],
)

service_page(
    "commercial-drywall", "Commercial Drywall", "Commercial Drywall",
    "Commercial Drywall in Orangeville, ON | Orangeville Drywalling",
    "Office, retail, and light-commercial drywall and partition work in Orangeville and Dufferin County. Free quotes, minimal disruption to your business.",
    "Commercial Drywall",
    "Office, retail, and light-commercial drywall and partition work.",
    """<h2>Commercial &amp; Light-Industrial Drywall</h2>
<p>Office build-outs, retail fit-ups, and light-commercial partition work along Orangeville's Broadway core and the surrounding business parks come with different priorities than residential jobs: scheduling around business hours, meeting fire-rating requirements where partitions call for them, and finishing to a consistent commercial standard across larger square footage.</p>
<h2>What We Handle</h2>
<ul>
<li>Office partition walls and interior build-outs</li>
<li>Retail space fit-ups ahead of a new tenant or renovation</li>
<li>Fire-rated assemblies where code requires them between units or occupancies</li>
<li>Light-commercial and small industrial office/mezzanine spaces</li>
</ul>
<h2>Working Around Your Business</h2>
<p>We understand a commercial job usually can't just shut a business down for two weeks. We'll talk through scheduling around your operating hours, phased work if only part of the space needs to stay closed at a time, and containment so drywall dust doesn't reach areas that stay open to staff or customers during the project.</p>
<p>Every commercial quote is scoped to the specific space and code requirements — send us the square footage, current use, and target timeline and we'll put together a proposal.</p>""",
    [
        ("Can you work outside normal business hours?", "Yes, evening and weekend scheduling is common for commercial jobs specifically to minimize disruption — let us know your constraints when requesting a quote."),
        ("Do you handle fire-rated partition assemblies?", "Yes, where code requires a fire-rated assembly between units or occupancies, we build to that specification."),
        ("What size of commercial job do you take on?", "From a single office partition to a full retail fit-up — send us the scope and we'll tell you honestly if it's a fit."),
        ("Can you match an existing commercial space's finish for an addition or renovation?", "Yes, matching existing wall texture and finish level is standard practice when new work ties into an existing commercial space."),
    ],
    extra_service_type="Commercial Drywall",
)

services_hub()
print("Services hub + 6 service pages written.")

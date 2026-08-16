#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import (page, crumbs_html, breadcrumb_schema, local_business_schema,
                    faq_schema, faq_html, quote_form, DOMAIN, PHONE_TEL, PHONE_DISPLAY, EMAIL)
from generate_pages import hero, SERVICES

OUT = os.path.dirname(__file__)

def service_cards_html():
    return "".join(
        f'<div class="card"><span class="card-icon">{icon}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<p><a class="card-link" href="/services/{slug}">Details →</a></p></div>'
        for slug, name, icon, blurb in SERVICES
    )

AREAS = [
    dict(
        slug="shelburne", name="Shelburne", drive="about 20 minutes north of Orangeville via Highway 10",
        lat=44.0787, lng=-80.2088,
        local_html="""<h2>Drywalling for Shelburne Homes</h2>
<p>Shelburne has grown quickly over the past decade, and it shows in the housing stock: newer subdivisions on the north and west sides of town sit alongside an older downtown core along Main Street with its mix of century homes and early-1900s brick storefronts converted to residential use. The two eras call for different approaches — new-build basements in Shelburne are very often sold unfinished, which makes basement drywalling one of our most common calls here, while the older core's homes tend to need texture-matched repair work and, in some cases, a full popcorn ceiling update if they haven't been touched since the 1980s.</p>
<h2>What We See Most in Shelburne</h2>
<p>Unfinished basements in newer subdivisions, drywall repair around older plaster-to-drywall transition points in century homes downtown, and popcorn ceiling removal in homes built through the town's earlier growth periods. We're set up to handle all three without treating Shelburne as an afterthought to Orangeville — it's a regular part of our week.</p>""",
    ),
    dict(
        slug="grandvalley", name="Grand Valley", drive="about 25 minutes west of Orangeville via Highway 25",
        lat=43.9020, lng=-80.3212,
        local_html="""<h2>Drywalling for Grand Valley Homes</h2>
<p>Grand Valley sits along the Grand River and still reads as a small rural town, even with newer executive-style homes built along the river corridor over the last fifteen years. That mix means we regularly work on two very different property types in the same week: older farmhouse-style homes on well and septic systems throughout the surrounding township, and newer larger-format homes that were built with unfinished basements or bonus rooms left as a next-phase project.</p>
<h2>What We See Most in Grand Valley</h2>
<p>Basement drywalling in newer builds along the river, drywall installation in additions and outbuilding conversions on rural properties, and general repair work on older farmhouses where settling and humidity swings are a normal part of owning a rural property. Well/septic properties don't change how we approach the drywall itself, but we're familiar with the access and scheduling realities of working on larger rural lots.</p>""",
    ),
    dict(
        slug="erin", name="Erin", drive="about 20–25 minutes southeast of Orangeville",
        lat=43.7827, lng=-80.0656,
        local_html="""<h2>Drywalling for Erin &amp; Hillsburgh Homes</h2>
<p>Erin and Hillsburgh's mix of rural properties, older village homes, and newer estate builds each come with their own quirks — from well/septic considerations on the outskirts to heritage-character guidelines for homes in the two villages' historic cores. Hillsburgh in particular retains a lot of its old mill-village character, with older homes that often still have some original plaster surfaces meeting more recent drywall additions.</p>
<h2>What We See Most in Erin &amp; Hillsburgh</h2>
<p>Repair and texture-matching where new drywall meets original plaster in older village homes, basement and addition work on the area's larger rural estate properties, and popcorn ceiling removal in homes from Erin's mid-century growth period. We've worked across all three property types and plan accordingly — including being mindful of heritage-character considerations in the village cores when a project is visible from the street.</p>""",
    ),
    dict(
        slug="mono", name="Mono", drive="Orangeville is surrounded by Mono on its north and east sides",
        lat=44.0006, lng=-80.0245,
        local_html="""<h2>Drywalling for Mono Homes</h2>
<p>Mono is mostly large-acreage rural and estate properties rather than dense subdivisions — think Mono Centre, the Mono Cliffs area, and the custom country homes scattered along the township's rural roads. That property type shapes the work: Mono homes tend to be larger-format custom builds with big basements, bonus rooms above garages, and finished lower levels that go well beyond a typical suburban basement package. We also see older stone and brick farmhouses, some dating back well over a century, where a renovation means blending new drywall carefully with original wall surfaces.</p>
<h2>What We See Most in Mono</h2>
<p>Large-scope basement drywalling and finishing in custom estate homes, bonus-room and above-garage installation, and careful repair/matching work in older farmhouses. Given the size of many Mono properties, we plan for longer jobs and coordinate scheduling around a property's specific access and layout.</p>""",
    ),
    dict(
        slug="caledon-village", name="Caledon Village", drive="about 30 minutes south of Orangeville via Highway 10",
        lat=43.8365, lng=-80.0107,
        local_html="""<h2>Drywalling for Caledon Village Homes</h2>
<p>Caledon Village is a small heritage hamlet within the Town of Caledon, with an older core of stone and brick homes near the Bruce Trail and Niagara Escarpment, surrounded by the large-lot executive estate development Caledon has seen over the past couple of decades. Heritage-character considerations sometimes apply to renovation work visible from the street in the village core, which is something we factor into planning and material choices on those jobs.</p>
<h2>What We See Most in Caledon Village</h2>
<p>Careful repair and texture-matching in the older heritage core, and full-scope basement and new-construction drywalling in the newer estate homes surrounding the village. As with Mono, Caledon Village properties skew larger, so we plan job timelines accordingly rather than treating every basement like a standard suburban package.</p>""",
    ),
]

for a in AREAS:
    slug = a["slug"]; name = a["name"]
    title = f"Drywall Services in {name}, ON | Orangeville Drywalling"
    description = f"Drywall installation, repair, taping, and mudding serving {name} and surrounding areas. Licensed, insured, free quotes from Orangeville Drywalling."
    body = f"""{crumbs_html([("Home","/"),(f"Drywall Services in {name}",None)])}
<section><div class="container narrow prose">
<p>{name} homeowners looking for drywall installation and repair will find a trusted partner in <a href="/">Orangeville Drywalling</a>. We're {a['drive']} and regularly serve {name} as part of our normal service area — this isn't a special trip, it's a regular part of our week.</p>
{a['local_html']}
</div></section>
<section id="services" class="local-section"><div class="container">
<h2>Drywall Services We Offer in {name}</h2>
<p class="section-intro">The same six services we offer across Dufferin County, all available in {name}.</p>
<div class="grid-3">{service_cards_html()}</div>
</div></section>
<section class="local-section alt"><div class="container">
<h2>Also Serving Nearby</h2>
<p>We're based in Orangeville and regularly serve {', '.join(x['name'] for x in AREAS if x['slug'] != slug)}, along with Orangeville itself.</p>
</div></section>
{quote_form("Drywall Services", area_hint=name)}"""
    schemas = [
        local_business_schema(area_served=name, extra={"description": f"Drywall installation, repair, taping, and mudding serving {name} and Dufferin County. Licensed, insured, free quotes."}),
        breadcrumb_schema([("Home", DOMAIN + "/"), (f"Drywall Services in {name}", f"{DOMAIN}/{slug}")]),
        faq_schema([
            (f"Do you regularly work in {name}, or is it out of your way?", f"{name} is a regular part of our service area, not a special trip — we're {a['drive']}."),
            ("Do you offer free quotes?", "Yes. Fill out the form on this page or call us directly, and we'll arrange a no-obligation quote for your project."),
            ("Can you match existing wall texture?", "Yes, matching existing texture (orange peel, knockdown, smooth) is standard on every repair."),
        ]),
    ]
    html = page(title, description, f"/{slug}", schemas, body,
                hero(f"Drywall Services in {name}, ON", f"Serving {name} and the surrounding area. Licensed, insured, and locally based in Orangeville."))
    with open(os.path.join(OUT, f"{slug}.html"), "w") as f:
        f.write(html)
    print(f"wrote {slug}.html")

print("Area pages done.")

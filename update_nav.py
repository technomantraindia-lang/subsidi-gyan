import os
import re

files_to_update = [
    "index.html",
    "about.html",
    "services.html",
    "central-subsidies.html",
    "gujarat-subsidies.html",
    "articles.html",
    "contact.html",
    "check-subsidy-eligibility.html",
    "industries.html",
    "article-detail.html",
    "service-detail.html"
]

base_nav = """<nav role="navigation" class="nav-menu-block w-nav-menu"><div class="nav-menu-wrap"><a href="index.html" class="menu-link{home_current}">Home</a><a href="about.html" class="menu-link{about_current}">About</a><div data-delay="200" data-hover="true" data-w-id="services-dropdown" class="dropdown w-dropdown"><div class="dropdown-toggle w-dropdown-toggle"><div class="menu-link dropdown" onclick="window.location.href='services.html';" style="cursor: pointer;">Services</div><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6908348359918a65f7271da8_down-arrow.svg" alt="down-arrow" class="dropdown-arrow-icon"/></div><nav class="dropdown-list w-dropdown-list"><a href="service-detail.html?id=dpr" class="dropdown-link w-dropdown-link">Detailed Project Report (DPR)</a><a href="service-detail.html?id=registration" class="dropdown-link w-dropdown-link">Registration &amp; Certification</a><a href="service-detail.html?id=banking" class="dropdown-link w-dropdown-link">Banking &amp; Financial Liaison</a><a href="service-detail.html?id=liaison" class="dropdown-link w-dropdown-link">Government Liaison</a></nav></div><div data-delay="200" data-hover="true" data-w-id="bbc6562a-bfb3-d8c0-d80e-2bd70185ef66" class="dropdown w-dropdown"><div class="dropdown-toggle w-dropdown-toggle"><div class="menu-link dropdown">Subsidies</div><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6908348359918a65f7271da8_down-arrow.svg" alt="down-arrow" class="dropdown-arrow-icon"/></div><nav class="dropdown-list w-dropdown-list"><a href="central-subsidies.html" class="dropdown-link w-dropdown-link{central_current}">Central Government Subsidies</a><a href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link{gujarat_current}">Gujarat Government Subsidies</a></nav></div><a href="industries.html" class="menu-link{industries_current}">Industries</a><a href="articles.html" class="menu-link{articles_current}">Articles</a><a href="contact.html" class="menu-link{contact_current}">Contact</a><div class="button-block hide"><a href="check-subsidy-eligibility.html" class="button is-primary w-inline-block"><div class="button-text-effect"><div class="button-text is-primary-button">Check Subsidy Eligibility</div><div class="button-text is-primary-button">Check Subsidy Eligibility</div></div></a></div></div></nav>"""

for filename in files_to_update:
    filepath = os.path.join(r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan", filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    home_current = " w--current" if filename == "index.html" else ""
    about_current = " w--current" if filename == "about.html" else ""
    central_current = " w--current" if filename == "central-subsidies.html" else ""
    gujarat_current = " w--current" if filename == "gujarat-subsidies.html" else ""
    industries_current = " w--current" if filename == "industries.html" else ""
    articles_current = " w--current" if filename == "articles.html" else ""
    contact_current = " w--current" if filename == "contact.html" else ""
    
    nav_to_insert = base_nav.format(
        home_current=home_current,
        about_current=about_current,
        central_current=central_current,
        gujarat_current=gujarat_current,
        industries_current=industries_current,
        articles_current=articles_current,
        contact_current=contact_current
    )
    
    # regex to replace <nav role="navigation" class="nav-menu-block w-nav-menu"> ... </nav> 
    # it must match up to the matching </nav> tag
    # The nav block is a bit nested, so we can replace everything between <nav role="navigation" class="nav-menu-block w-nav-menu"> and the *first* <div class="nav-button-block">
    
    pattern = re.compile(r'<nav role="navigation" class="nav-menu-block w-nav-menu">.*?</nav>(?=\s*<div class="nav-button-block">)', re.DOTALL)
    
    new_content = pattern.sub(nav_to_insert, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")

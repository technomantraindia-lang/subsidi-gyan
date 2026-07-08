import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

header_m = re.search(r'<section class="header">.*?</section>', index, re.DOTALL)
footer_m = re.search(r'<section class="footer".*?</section>', index, re.DOTALL)
header = header_m.group(0) if header_m else ""
footer = footer_m.group(0) if footer_m else ""


def fix_header(header, active_page):
    h = header.replace('href="index.html" class="menu-link w--current">Home', 'href="index.html" class="menu-link">Home')
    h = h.replace('href="about.html" class="menu-link">About', 'href="about.html" class="menu-link">About')
    h = h.replace('href="services.html" class="menu-link">Services', 'href="services.html" class="menu-link">Services')
    h = h.replace('href="#services" class="menu-link">Services', 'href="services.html" class="menu-link">Services')
    h = h.replace('href="/" aria-current="page" class="brand-block', 'href="index.html" class="brand-block')
    h = h.replace('class="brand-block w-nav-brand w--current"', 'class="brand-block w-nav-brand"')
    h = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', h)
    h = h.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Central Government Subsidies',
        'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
    )
    h = h.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
        'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
    )
    h = h.replace(
        'href="index.html#schemes" class="dropdown-link w-dropdown-link">Central Government Subsidies',
        'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
    )
    h = h.replace(
        'href="index.html#schemes" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
        'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
    )
    if active_page == "central":
        h = h.replace(
            'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
            'href="central-subsidies.html" class="dropdown-link w-dropdown-link w--current">Central Government Subsidies',
        )
    elif active_page == "gujarat":
        h = h.replace(
            'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
            'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link w--current">Gujarat Government Subsidies',
        )
    return h


def fix_footer(footer, active_page):
    f = footer.replace('href="index.html" class="footer-link w--current">Home', 'href="index.html" class="footer-link">Home')
    f = f.replace('href="about.html" class="footer-link">About', 'href="about.html" class="footer-link">About')
    f = f.replace('href="/" aria-current="page" class="footer-link w--current">Home', 'href="index.html" class="footer-link">Home')
    f = f.replace('href="/about-us" class="footer-link">About Us', 'href="about.html" class="footer-link">About Us')
    f = f.replace('href="#services" class="footer-link">Services', 'href="services.html" class="footer-link">Services')
    f = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', f)
    f = f.replace('href="#schemes" class="footer-link">Central Government', 'href="central-subsidies.html" class="footer-link">Central Government')
    f = f.replace('href="#schemes" class="footer-link">Gujarat Government', 'href="gujarat-subsidies.html" class="footer-link">Gujarat Government')
    f = f.replace('href="index.html#schemes" class="footer-link">Central Government', 'href="central-subsidies.html" class="footer-link">Central Government')
    f = f.replace('href="index.html#schemes" class="footer-link">Gujarat Government', 'href="gujarat-subsidies.html" class="footer-link">Gujarat Government')
    if active_page == "central":
        f = f.replace('href="central-subsidies.html" class="footer-link">Central Government', 'href="central-subsidies.html" class="footer-link w--current">Central Government')
    elif active_page == "gujarat":
        f = f.replace('href="gujarat-subsidies.html" class="footer-link">Gujarat Government', 'href="gujarat-subsidies.html" class="footer-link w--current">Gujarat Government')
    return f


def head(title, description):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title}</title>
  <meta name="description" content="{description}"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="css/style.css" rel="stylesheet"/>
  <link href="css/custom.css" rel="stylesheet"/>
  <link href="css/about.css?v=1.1" rel="stylesheet"/>
  <link href="css/subsidies.css" rel="stylesheet"/>
</head>
<body>
<div class="page-wrapper">
"""


def accordion_item(title, body):
    return f"""
      <div class="accordion-item w-dropdown sub-accordion-item">
        <div class="accordion-toggle w-dropdown-toggle sub-accordion-toggle">
          <div class="accordion-tittle">{title}</div>
          <div class="accordion-icon-block"><div class="horizontal-line"></div><div class="vertical-line"></div></div>
        </div>
        <nav class="accordion-body w-dropdown-list sub-accordion-body"><p class="accordion-text">{body}</p></nav>
      </div>"""


def scheme_card(badge_class, badge_text, name, best_for, desc, card_class=""):
    return f"""
      <div class="sub-scheme-card {card_class} fade-in">
        <span class="sub-scheme-badge {badge_class}">{badge_text}</span>
        <h3>{name}</h3>
        <div class="sub-scheme-best">Best for: {best_for}</div>
        <p>{desc}</p>
        <a href="index.html#contact" class="sub-scheme-cta">Check Eligibility →</a>
      </div>"""


def process_section(steps):
    items = ""
    for num, title, desc in steps:
        items += f'<div class="about-process-step"><div class="about-process-num">{num}</div><h3>{title}</h3><p>{desc}</p></div>'
    return f"""
<section class="sub-process-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block" style="text-align:center">
      <div class="pill-button">[ Process ]</div>
      <h2 class="section-heading">Subsidy Application Support Process</h2>
    </div>
    <div class="about-process-grid fade-in">{items}
    </div>
  </div>
  <div class="empty-space"></div>
</section>"""


def docs_section(docs):
    items = ""
    for title, desc in docs:
        items += f'<div class="sub-doc-item"><strong>{title}</strong><span>{desc}</span></div>'
    return f"""
<section class="sub-docs-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="sub-docs-card fade-in">
      <div class="pill-button">[ Documents ]</div>
      <h2 class="section-heading">Documents &amp; Information Required</h2>
      <p class="section-intro-text">Exact requirements vary by scheme. Contact us for scheme-wise checklists.</p>
      <div class="sub-docs-grid">{items}
      </div>
      <p class="sub-disclaimer">Subsidy eligibility, required documents, benefit amount and approval depend on applicable government policy, project category, location, investment and department verification.</p>
    </div>
  </div>
  <div class="empty-space"></div>
</section>"""


def trust_section(points):
    cards = ""
    for title, desc in points:
        cards += f'<div class="sub-trust-card"><strong>{title}</strong><p>{desc}</p></div>'
    return f"""
<section class="sub-trust-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block" style="text-align:center">
      <div class="pill-button">[ Why Choose Us ]</div>
      <h2 class="section-heading">Why Choose Subsidy Gyaan</h2>
    </div>
    <div class="sub-trust-grid fade-in">{cards}
    </div>
  </div>
</section>"""


def faq_section(faqs, label):
    items = ""
    for q, a in faqs:
        items += accordion_item(q, a)
    return f"""
<section class="sub-faq-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block" style="text-align:center">
      <div class="pill-button">[ FAQ ]</div>
      <h2 class="section-heading">Frequently Asked Questions</h2>
      <p class="section-intro-text">{label}</p>
    </div>
    <div class="sub-accordion-list fade-in">{items}
    </div>
  </div>
</section>"""


def promo_section(tagline_cta, heading, desc, primary, secondary="Call Subsidy Expert"):
    return f"""
<section class="promo-section">
  <div class="promo-main-block">
    <div class="promo-sticky-block">
      <div class="promo-wrapper sg-about-promo">
        <div class="container">
          <div class="promo-content-wrap">
            <p class="about-inner-tagline about-promo-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
            <h2 class="promo-text">{heading}</h2>
            <p class="promo-desc-text">{desc}</p>
            <p class="sub-cta-phone"><a href="tel:+918320542940">+91 8320542940</a> / <a href="tel:+918866248393">+91 8866248393</a></p>
            <div class="button-block is-promo hero-btns">
              <a href="index.html#contact" class="button is-primary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-primary-button">{primary}</div><div class="button-text is-primary-button">{primary}</div></div>
              </a>
              <a href="tel:+918320542940" class="button is-secondary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-secondary">{secondary}</div><div class="button-text is-secondary">{secondary}</div></div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""


# ── CENTRAL GOVERNMENT PAGE ──

CENTRAL_SCHEMES = [
    ("PMFME Scheme", "Micro food processors, gruh udyog, SHGs, FPOs", "Individual units may avail 35% capital subsidy up to Rs. 10 lakh; group/common infrastructure support may also be available as per scheme eligibility."),
    ("NABARD / AMIGS", "Agri-processing, warehouse and commodity infrastructure", "For cleaning, sorting, grading and agricultural commodity infrastructure. Useful for agri-processing and warehouse-related projects."),
    ("AIF Scheme", "Post-harvest infrastructure and community farming assets", "For post-harvest management infrastructure and community farming assets. Interest subvention support may apply on eligible loans."),
    ("EPCG Subsidy", "Export-oriented projects and capital goods procurement", "For eligible industries importing capital goods against export commitments. Useful for export-oriented projects."),
    ("APEDA Scheme", "Agricultural and processed food exporters", "Export promotion support for agricultural and processed food products, including infrastructure, quality development and market development areas."),
    ("Cold Storage Subsidy", "Cold storage investors and agri-infrastructure projects", "Credit-linked support for construction, expansion and modernization of cold storages, subject to scheme conditions."),
    ("Credit Linked Capital Subsidy", "Eligible SC/ST MSEs for plant and machinery", "Support for eligible SC/ST MSEs for procurement of plant, machinery or equipment through institutional credit."),
    ("MOFPI Subsidy Schemes", "Food processing infrastructure and cold chain projects", "Support for food processing infrastructure such as cold chain, value addition, mega food parks and agro-processing clusters."),
    ("Biomass / Renewable Energy Subsidy", "Biomass, briquette, pellet and renewable energy projects", "Support for briquette, pellet and biomass-based renewable energy projects, subject to capacity and scheme rules."),
]

CENTRAL_ACCORDION = [
    ("PMFME Scheme", "The PMFME scheme supports micro food processing units with capital subsidy up to 35% (max Rs. 10 lakh for individual units). Group and common infrastructure support may also be available for FPOs, SHGs and cooperatives, subject to eligibility conditions."),
    ("NABARD / AMIGS", "NABARD / AMIGS provides support for cleaning, sorting, grading and agricultural commodity infrastructure. This is useful for agri-processing units, warehouse projects and commodity handling facilities."),
    ("AIF Scheme", "The Agriculture Infrastructure Fund (AIF) supports post-harvest management infrastructure and community farming assets. Eligible projects may receive interest subvention on loans, subject to scheme guidelines."),
    ("EPCG Subsidy", "EPCG allows eligible industries to import capital goods at concessional customs duty against export commitments. This is beneficial for export-oriented manufacturing and capital goods procurement projects."),
    ("APEDA Scheme", "APEDA provides export promotion support for agricultural and processed food products, covering infrastructure development, quality certification, market development and export facilitation."),
    ("Cold Storage Subsidy", "Credit-linked capital subsidy is available for construction, expansion and modernization of cold storage facilities. Eligibility depends on project location, capacity and scheme-specific conditions."),
    ("MOFPI Subsidy Schemes", "MOFPI schemes support food processing infrastructure including cold chain, value addition units, mega food parks and agro-processing clusters. Capital subsidy and other incentives may apply."),
    ("Biomass / Renewable Energy Subsidy", "Support is available for biomass, briquette, pellet and cogeneration projects. Benefits depend on project capacity, technology and applicable renewable energy scheme rules."),
]

central_schemes_html = ""
for name, best, desc in CENTRAL_SCHEMES:
    central_schemes_html += scheme_card("sub-scheme-badge--central", "Central Scheme", name, best, desc)

central_accordion_html = ""
for title, body in CENTRAL_ACCORDION:
    central_accordion_html += accordion_item(title, body)

central_main = f"""
<section class="page-hero-section about-inner-hero sub-hero">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-inner-hero-grid">
      <div class="about-inner-hero-content fade-in">
        <div class="pill-button">[ Central Government Subsidies ]</div>
        <p class="about-inner-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
        <h1 class="about-inner-title">Central Government Subsidy Advisory for MSMEs &amp; Industrial Projects</h1>
        <p class="about-inner-desc">Guidance for PMFME, NABARD / AMIGS, AIF, EPCG, APEDA, Cold Storage, Credit Linked Capital Subsidy, MOFPI, Biomass and Renewable Energy subsidy schemes.</p>
        <div class="button-block hero-btns">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Check Central Subsidy Eligibility</div><div class="button-text is-primary-button">Check Central Subsidy Eligibility</div></div>
          </a>
          <a href="#schemes" class="button is-secondary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-secondary">Explore Schemes</div><div class="button-text is-secondary">Explore Schemes</div></div>
          </a>
        </div>
        <div class="breadcrumb-nav">
          <a href="index.html" class="breadcrumb-home">Home</a>
          <div class="breadcrumb-divider"><img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690af44dbcda67d4e97f4bc9_breadcrumb-icon.svg" loading="lazy" alt=""/></div>
          <div>Central Government Subsidies</div>
        </div>
      </div>
      <div class="about-inner-hero-visual fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690992115e99223039814b76_contact-image.avif" loading="lazy" alt="Central Government subsidy advisory" class="about-inner-hero-img"/>
        <div class="sub-floating-tags">
          <span>PMFME</span><span>NABARD</span><span>AIF</span><span>APEDA</span><span>EPCG</span><span>MOFPI</span><span>Cold Storage</span><span>Biomass</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sub-strip">
  <div class="w-layout-blockcontainer container w-container">
    <div class="sub-strip-grid fade-in">
      <div class="sub-strip-item"><div class="sub-strip-icon">🏭</div><div><strong>Food Processing Subsidy</strong><span>PMFME, MOFPI and food infrastructure</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">🌾</div><div><strong>Agri Infrastructure Support</strong><span>NABARD, AIF and warehouse projects</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">🌍</div><div><strong>Export Promotion Assistance</strong><span>APEDA and EPCG schemes</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">❄️</div><div><strong>Cold Storage Subsidy</strong><span>Construction and modernization support</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">♻️</div><div><strong>Renewable Energy Assistance</strong><span>Biomass and green energy projects</span></div></div>
    </div>
  </div>
</section>

<section class="sub-intro-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Central Subsidy Guidance ]</div>
      <h2 class="section-heading">Helping Businesses Access Central Government Support with Clarity</h2>
    </div>
    <div class="sub-intro-grid fade-in">
      <div>
        <p class="about-text">Many Central Government schemes support eligible businesses through capital subsidy, interest support, credit-linked assistance, export promotion, infrastructure support and sector-specific incentives.</p>
        <p class="about-text">Subsidy Gyaan helps businesses understand scheme eligibility, prepare proper DPRs, arrange required documents and move through application and follow-up stages with a compliance-first approach.</p>
        <div class="sub-intro-cards">
          <div class="sub-intro-card"><strong>Eligibility Check</strong><span>Scheme mapping for your project</span></div>
          <div class="sub-intro-card"><strong>DPR Support</strong><span>Bank and government-ready reports</span></div>
          <div class="sub-intro-card"><strong>Documentation</strong><span>Registration and compliance files</span></div>
          <div class="sub-intro-card"><strong>Application Follow-Up</strong><span>Department coordination support</span></div>
        </div>
      </div>
      <div class="sub-process-diagram">
        <div class="sub-process-step-item">Understand Project Details</div>
        <div class="sub-process-step-item">Check Scheme Eligibility</div>
        <div class="sub-process-step-item">Prepare DPR &amp; Financials</div>
        <div class="sub-process-step-item">Arrange Documents</div>
        <div class="sub-process-step-item">File Application</div>
        <div class="sub-process-step-item">Follow-Up &amp; Compliance</div>
      </div>
    </div>
  </div>
</section>

<section id="schemes" class="sub-schemes-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Featured Schemes ]</div>
      <h2 class="section-heading">Central Government Subsidy Schemes</h2>
      <p class="section-intro-text">Explore major Central Government subsidy categories. Each scheme has specific eligibility conditions — contact us for a detailed eligibility assessment.</p>
    </div>
    <div class="sub-schemes-grid">{central_schemes_html}
    </div>
  </div>
</section>

<section class="sub-accordion-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Scheme Details ]</div>
      <h2 class="section-heading">Explore Central Scheme Details</h2>
      <p class="section-intro-text">Click each scheme to learn more about eligibility, benefits and application focus areas.</p>
    </div>
    <div class="sub-accordion-list fade-in">{central_accordion_html}
    </div>
  </div>
</section>

<section class="sub-highlight-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="sub-highlight-grid fade-in">
      <div>
        <div class="pill-button">[ Food Processing Support ]</div>
        <h2 class="section-heading">Special Guidance for Micro Food Processing &amp; Agri-Processing Units</h2>
        <p class="about-text">The Central Government offers strong support for micro food processing through PMFME and MOFPI schemes. Subsidy Gyaan provides end-to-end guidance including FSSAI readiness, DPR preparation and subsidy-linked project planning.</p>
        <ul class="sub-highlight-list">
          <li>PMFME capital subsidy for micro food processing units</li>
          <li>MOFPI support for cold chain and food processing infrastructure</li>
          <li>FSSAI registration and compliance readiness</li>
          <li>DPR preparation aligned with scheme requirements</li>
          <li>Machinery supplier networking and food technologist support</li>
        </ul>
        <div class="button-block">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Discuss Food Processing Subsidy</div><div class="button-text is-primary-button">Discuss Food Processing Subsidy</div></div>
          </a>
        </div>
        <div class="sub-good-for"><strong>Good for:</strong> micro food processors, gruh udyog, SHGs, FPOs, FPCs, cooperatives, cold chain and processing units.</div>
      </div>
      <div>
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b0913b14506195ef385b1_about-image-1.avif" loading="lazy" alt="Food processing subsidy guidance" class="about-inner-hero-img"/>
      </div>
    </div>
  </div>
</section>

<section class="sub-audience-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-team">
      <div class="pill-button is-faq">[ Who Can Benefit ]</div>
      <h2 class="section-heading is-team">Who Can Benefit from Central Government Subsidies</h2>
    </div>
    <div class="sub-audience-grid fade-in">
      <div class="sub-audience-card"><h3>Micro Food Industries</h3><p>Home-based or small food processing units looking to formalize and expand with government support.</p></div>
      <div class="sub-audience-card"><h3>FPOs / FPCs / Cooperatives</h3><p>Groups planning common infrastructure, processing units or agri-support facilities.</p></div>
      <div class="sub-audience-card"><h3>MSMEs &amp; Industrial Units</h3><p>Businesses planning capital investment, machinery purchase, expansion or modernization.</p></div>
      <div class="sub-audience-card"><h3>Exporters</h3><p>Agricultural and processed food exporters seeking market and infrastructure assistance.</p></div>
      <div class="sub-audience-card"><h3>Cold Storage Projects</h3><p>Investors planning construction, expansion or modernization of cold storage facilities.</p></div>
      <div class="sub-audience-card"><h3>Renewable Energy Projects</h3><p>Biomass, briquette, pellet and cogeneration project developers.</p></div>
    </div>
  </div>
</section>

{process_section([
    ("01", "Understand Project Details", "Business idea, industry, location, investment, machinery and current status."),
    ("02", "Check Scheme Eligibility", "Identify matching Central Government schemes and basic eligibility conditions."),
    ("03", "Prepare DPR & Financials", "Create scheme-ready DPR, project viability, cost details and projections."),
    ("04", "Arrange Documents", "Collect registrations, quotations, KYC, bank and project documents."),
    ("05", "File Application", "Support application filing through relevant portals and departments."),
    ("06", "Follow-Up & Compliance", "Coordinate, respond to queries and guide until process completion."),
])}

{docs_section([
    ("Business Details", "Business name, promoter details, business type, product/service details"),
    ("Project Details", "Investment plan, machinery, land/building status, production capacity and location"),
    ("Financial Details", "Estimated project cost, loan requirement, bank status and own contribution"),
    ("Registration Details", "Udyam, GST, FSSAI, IEC or other registrations where applicable"),
    ("Supporting Documents", "Quotations, project report, KYC, ownership/rent documents, bank documents"),
])}

{trust_section([
    ("Holistic Approach", "Complete subsidy strategy aligned with project goals, not just form filing."),
    ("Compliance-First Mindset", "Correct documentation and eligibility understanding to reduce rejection risk."),
    ("Knowledge Democratization", "Complex schemes made understandable for micro-enterprises and industries."),
    ("Ecosystem Access", "DPR, registration, banking, machinery and allied support in one advisory network."),
    ("Social Commitment", "Support for micro, rural and underserved entrepreneurs through awareness and guidance."),
])}

{faq_section([
    ("Which Central Government subsidy schemes do you guide for?", "We provide guidance for PMFME, NABARD / AMIGS, AIF, EPCG, APEDA, MOFPI, Cold Storage, Credit Linked Capital Subsidy, Biomass / Renewable Energy and related Central Government schemes."),
    ("Is subsidy approval guaranteed?", "No. Subsidy eligibility and approval depend on scheme rules, documents, project category, location and department verification. We provide advisory and documentation support, not guaranteed approval."),
    ("Do you prepare DPR for subsidy applications?", "Yes, DPR preparation is a core part of Subsidy Gyaan services. We prepare scheme-ready project reports with viability analysis, financial projections and subsidy optimization."),
    ("Can new businesses apply for Central Government subsidy?", "Some schemes support new businesses, but eligibility depends on the specific project, industry and scheme conditions. Contact us for a case-by-case assessment."),
    ("Do you help food processing units?", "Yes, we specialize in PMFME, MOFPI and related food processing support including FSSAI readiness, DPR preparation and machinery guidance."),
    ("Do you support exporters?", "Yes, we provide scheme guidance for APEDA and export-linked support including EPCG for capital goods import against export commitments."),
], "Common questions about Central Government subsidy advisory.")}

{promo_section(
    "Check Subsidy Eligibility",
    "Want to Know Which Central Government Subsidy Fits Your Project?",
    "Share your business idea, investment plan, industry and location. Our team will guide you with suitable Central Government subsidy options and documentation requirements.",
    "Check Subsidy Eligibility",
)}
"""

# ── GUJARAT GOVERNMENT PAGE ──

GUJARAT_SCHEMES = [
    ("MSME Assistance Scheme", "Micro, small and medium enterprises in Gujarat", "Guidance for eligible MSMEs under Gujarat industrial policy incentives, including capital subsidy, interest subsidy and power tariff assistance."),
    ("Large / Mega / Ultra-Mega Units", "Large-scale industrial investment projects", "Advisory for large-scale industrial investment categories where capital subsidy, interest subsidy, power tariff assistance and other benefits may apply."),
    ("Textile Industry Subsidy", "Garments, apparel, technical textiles and processing units", "Support for garments, apparel, made-ups, technical textiles, weaving, knitting, dyeing, processing and certain MMF spinning activities."),
    ("Logistic Park Assistance", "Logistics park and warehousing projects", "Guidance for logistics park projects with capital subsidy, interest subsidy, stamp duty reimbursement and electricity duty exemption, subject to eligibility."),
    ("Electric Duty Waiver", "New industries and expansion projects", "Advisory for new industries and expansion projects where electricity duty exemption may apply under Gujarat policy conditions."),
    ("Marketing Support Schemes", "Exhibition and market development activities", "Guidance for exhibition participation support, stall rent refunds and market development assistance subject to scheme rules."),
    ("IT / Electronics Policies", "IT, ITeS and electronics sector projects", "Case-to-case guidance for IT, ITeS, electronics and related technology sector policies with capital, interest or sector-specific benefits."),
    ("Bio Fuel / Energy / Biotechnology", "Bio fuel, energy and biotech sector projects", "Support direction for eligible bio fuel, energy and biotechnology sector projects under dedicated Gujarat policies."),
]

gujarat_schemes_html = ""
for name, best, desc in GUJARAT_SCHEMES:
    gujarat_schemes_html += scheme_card("sub-scheme-badge--gujarat", "Gujarat Scheme", name, best, desc, "sub-scheme-card--gujarat")

GUJARAT_MSME_ACCORDION = [
    ("Capital Subsidy", "Capital subsidy is provided based on eligible fixed capital investment and Taluka category. The benefit percentage and ceiling vary by location category and enterprise type under the Gujarat MSME Assistance Scheme."),
    ("Interest Subsidy", "Term loan interest subsidy support is available for eligible MSME projects. Duration, percentage and maximum limits apply as per current Gujarat industrial policy guidelines."),
    ("Power Tariff Assistance", "Unit-based power tariff support is available for eligible new MSME projects. This helps reduce operational energy costs during the initial years of operation."),
    ("Additional MSME Support", "Additional support areas include technology & quality upgradation, market & capital access, utility savings and power connection assistance for eligible MSME units."),
    ("SC/ST Entrepreneur Support", "Additional incentive ceiling support is available for eligible SC/ST entrepreneurs as per Gujarat Government policy, providing enhanced subsidy benefits."),
    ("Selected Thrust Sectors", "Special focus sectors include sports goods, toys, footwear, robotics and drones, with additional incentive support for eligible projects in these areas."),
]

gujarat_msme_accordion_html = ""
for title, body in GUJARAT_MSME_ACCORDION:
    gujarat_msme_accordion_html += accordion_item(title, body)

gujarat_main = f"""
<section class="page-hero-section about-inner-hero sub-hero">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-inner-hero-grid">
      <div class="about-inner-hero-content fade-in">
        <div class="pill-button">[ Gujarat Government Subsidies ]</div>
        <p class="about-inner-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
        <h1 class="about-inner-title">Gujarat Government Subsidy Advisory for MSMEs &amp; Industrial Projects</h1>
        <p class="about-inner-desc">Guidance for MSME Assistance, Large / Mega / Ultra-Mega unit incentives, Textile subsidy, Logistic Park assistance, Electric Duty Waiver, Marketing Support and sector-specific Gujarat policies.</p>
        <div class="button-block hero-btns">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Check Gujarat Subsidy Eligibility</div><div class="button-text is-primary-button">Check Gujarat Subsidy Eligibility</div></div>
          </a>
          <a href="#schemes" class="button is-secondary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-secondary">Explore Gujarat Schemes</div><div class="button-text is-secondary">Explore Gujarat Schemes</div></div>
          </a>
        </div>
        <div class="breadcrumb-nav">
          <a href="index.html" class="breadcrumb-home">Home</a>
          <div class="breadcrumb-divider"><img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690af44dbcda67d4e97f4bc9_breadcrumb-icon.svg" loading="lazy" alt=""/></div>
          <div>Gujarat Government Subsidies</div>
        </div>
      </div>
      <div class="about-inner-hero-visual fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b091362f6fe3fff57e63c_about-image-3.avif" loading="lazy" alt="Gujarat Government subsidy advisory" class="about-inner-hero-img"/>
        <div class="sub-floating-tags">
          <span>MSME Assistance</span><span>Textile Subsidy</span><span>Logistic Park</span><span>Electric Duty</span><span>Marketing Support</span><span>IT / Electronics</span><span>Bio Fuel</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sub-strip">
  <div class="w-layout-blockcontainer container w-container">
    <div class="sub-strip-grid fade-in">
      <div class="sub-strip-item"><div class="sub-strip-icon">🏭</div><div><strong>MSME Assistance</strong><span>Capital, interest and power tariff support</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">🏗️</div><div><strong>Large &amp; Mega Units</strong><span>Industrial investment incentives</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">🧵</div><div><strong>Textile Subsidy</strong><span>Garments, apparel and processing units</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">🚛</div><div><strong>Logistic Park Assistance</strong><span>Warehousing and logistics infrastructure</span></div></div>
      <div class="sub-strip-item"><div class="sub-strip-icon">⚡</div><div><strong>Electric Duty &amp; Marketing</strong><span>Duty waiver and exhibition support</span></div></div>
    </div>
  </div>
</section>

<section class="sub-intro-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Gujarat Subsidy Guidance ]</div>
      <h2 class="section-heading">Helping Businesses Access Gujarat Government Support with Confidence</h2>
    </div>
    <div class="sub-intro-grid fade-in">
      <div>
        <p class="about-text">Gujarat Government policies provide incentive support for eligible MSMEs, industrial units, textile businesses, logistics parks and selected sectors through capital subsidy, interest subsidy, power tariff assistance, duty waiver and market support.</p>
        <p class="about-text">Subsidy Gyaan helps businesses understand which Gujarat scheme may apply, prepare DPRs and documentation, and coordinate the application process with compliance-first advisory support.</p>
      </div>
      <div class="sub-process-diagram">
        <div class="sub-process-step-item">Project Assessment</div>
        <div class="sub-process-step-item">Eligibility Check</div>
        <div class="sub-process-step-item">Documents Preparation</div>
        <div class="sub-process-step-item">Application Filing</div>
        <div class="sub-process-step-item">Follow-Up Support</div>
      </div>
    </div>
  </div>
</section>

<section id="schemes" class="sub-schemes-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Gujarat Schemes ]</div>
      <h2 class="section-heading">Gujarat Government Subsidy Scheme Overview</h2>
      <p class="section-intro-text">Major Gujarat Government subsidy categories for eligible businesses and industrial projects. Contact us for Taluka category and sector-specific eligibility assessment.</p>
    </div>
    <div class="sub-schemes-grid">{gujarat_schemes_html}
    </div>
  </div>
</section>

<section class="sub-highlight-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ MSME Assistance Scheme ]</div>
      <h2 class="section-heading">Guidance for Gujarat MSMEs to Access Capital, Interest &amp; Power Tariff Support</h2>
      <p class="section-intro-text">The Gujarat MSME Assistance Scheme provides capital subsidy, interest subsidy and power tariff assistance based on enterprise category and Taluka location. Subsidy Gyaan helps MSMEs understand eligibility and prepare documentation.</p>
    </div>
    <div class="sub-msme-def-grid fade-in">
      <div class="sub-msme-def-card"><h4>Micro Enterprise</h4><p>Investment in plant &amp; machinery/equipment up to &#8377;2.5 Cr as per revised MSME definition.</p></div>
      <div class="sub-msme-def-card"><h4>Small Enterprise</h4><p>Investment above &#8377;2.5 Cr up to &#8377;25 Cr in plant &amp; machinery/equipment.</p></div>
      <div class="sub-msme-def-card"><h4>Medium Enterprise</h4><p>Investment above &#8377;25 Cr up to &#8377;125 Cr in plant &amp; machinery/equipment.</p></div>
    </div>
    <div class="button-block" style="text-align:center;margin-top:32px">
      <a href="index.html#contact" class="button is-primary w-inline-block">
        <div class="button-text-effect"><div class="button-text is-primary-button">Check MSME Subsidy Eligibility</div><div class="button-text is-primary-button">Check MSME Subsidy Eligibility</div></div>
      </a>
    </div>
  </div>
</section>

<section class="sub-accordion-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ MSME Incentives ]</div>
      <h2 class="section-heading">MSME Incentive Components</h2>
      <p class="section-intro-text">Explore the key incentive components under the Gujarat MSME Assistance Scheme.</p>
    </div>
    <div class="sub-accordion-list fade-in">{gujarat_msme_accordion_html}
    </div>
  </div>
</section>

<section class="sub-audience-section" style="background:#f8f9fb">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Large Scale Industrial Support ]</div>
      <h2 class="section-heading">Advisory for Large, Mega &amp; Ultra-Mega Industrial Investments in Gujarat</h2>
      <p class="section-intro-text">Eligible units may combine capital subsidy, interest subsidy and power tariff assistance subject to category, sector and policy conditions.</p>
    </div>
    <div class="sub-large-unit-grid fade-in">
      <div class="sub-large-unit-card"><h4>Large Unit</h4><p>Minimum &#8377;125 Cr investment in plant &amp; machinery. Eligible for capital subsidy, interest subsidy and power tariff assistance as per policy.</p></div>
      <div class="sub-large-unit-card"><h4>Mega Unit</h4><p>Minimum &#8377;1,000 Cr investment + 250 jobs + thrust sector requirement. Premium incentive package for large industrial projects.</p></div>
      <div class="sub-large-unit-card"><h4>Ultra-Mega Unit</h4><p>Minimum &#8377;10,000 Cr investment + 3,000 jobs + thrust sector requirement. Highest tier of Gujarat industrial incentives.</p></div>
    </div>
    <div class="button-block" style="text-align:center;margin-top:32px">
      <a href="index.html#contact" class="button is-primary w-inline-block">
        <div class="button-text-effect"><div class="button-text is-primary-button">Discuss Industrial Project Subsidy</div><div class="button-text is-primary-button">Discuss Industrial Project Subsidy</div></div>
      </a>
    </div>
  </div>
</section>

<section class="sub-highlight-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Textile Subsidy ]</div>
      <h2 class="section-heading">Subsidy Guidance for Garments, Apparel, Technical Textiles &amp; Processing Units</h2>
    </div>
    <div class="sub-textile-grid fade-in">
      <div class="sub-textile-card"><h4>Garments, Apparel, Made-ups &amp; Technical Textiles</h4><p>Capital subsidy, interest subsidy, power tariff subsidy, payroll assistance and additional support measures for garment and apparel manufacturing units.</p></div>
      <div class="sub-textile-card"><h4>Weaving, Knitting, Dyeing, Processing &amp; MMF Spinning</h4><p>Support for weaving, knitting, dyeing, processing and certain MMF spinning activities including technology acquisition and quality certification.</p></div>
    </div>
    <div class="sub-support-icons fade-in">
      <span class="sub-support-icon">Capital Subsidy</span>
      <span class="sub-support-icon">Interest Subsidy</span>
      <span class="sub-support-icon">Power Tariff Subsidy</span>
      <span class="sub-support-icon">Payroll Assistance</span>
      <span class="sub-support-icon">Technology &amp; Quality</span>
      <span class="sub-support-icon">Energy &amp; Water Saving</span>
    </div>
    <div class="button-block" style="text-align:center;margin-top:32px">
      <a href="index.html#contact" class="button is-primary w-inline-block">
        <div class="button-text-effect"><div class="button-text is-primary-button">Check Textile Subsidy Eligibility</div><div class="button-text is-primary-button">Check Textile Subsidy Eligibility</div></div>
      </a>
    </div>
  </div>
</section>

<section class="sub-logistic-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="sub-logistic-grid fade-in">
      <div>
        <div class="pill-button">[ Logistic Park Assistance ]</div>
        <h2 class="section-heading">Guidance for Logistics Park Projects &amp; Infrastructure Investors</h2>
        <p class="about-text">Gujarat offers incentives for building logistics parks, including capital and interest support and duty-related benefits subject to eligibility. Subsidy Gyaan helps investors understand scheme conditions and prepare documentation.</p>
        <div class="sub-benefit-badges">
          <span class="sub-benefit-badge">Capital Subsidy</span>
          <span class="sub-benefit-badge">Interest Subsidy</span>
          <span class="sub-benefit-badge">Stamp Duty Reimbursement</span>
          <span class="sub-benefit-badge">Electricity Duty Exemption</span>
        </div>
        <div class="button-block" style="margin-top:24px">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Discuss Logistic Park Subsidy</div><div class="button-text is-primary-button">Discuss Logistic Park Subsidy</div></div>
          </a>
        </div>
      </div>
      <div>
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b0913ec147be6ab17ca3e_about-image-2.avif" loading="lazy" alt="Logistic park subsidy guidance" class="about-inner-hero-img"/>
      </div>
    </div>
  </div>
</section>

<section class="sub-audience-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Other Gujarat Policies ]</div>
      <h2 class="section-heading">Electric Duty, Marketing &amp; Sector-Specific Policies</h2>
    </div>
    <div class="sub-policy-grid fade-in">
      <div class="sub-policy-card"><h4>Electric Duty Waiver</h4><p>New industries and expansion projects may receive electricity duty exemption subject to applicable policy rules and project conditions.</p></div>
      <div class="sub-policy-card"><h4>Marketing Support Schemes</h4><p>Exhibition and market support may include refunds for stall rent and incidental expenses subject to government conditions.</p></div>
      <div class="sub-policy-card"><h4>IT &amp; Electronics Policies</h4><p>Eligible IT, ITeS and electronics sector projects can be guided on capital, interest and sector-specific policy benefits.</p></div>
      <div class="sub-policy-card"><h4>Bio Fuel / Energy / Biotechnology</h4><p>Dedicated sector policies may provide capital, interest and other benefits; analysis provided case-by-case.</p></div>
    </div>
  </div>
</section>

<section class="sub-audience-section" style="background:#f8f9fb">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-team">
      <div class="pill-button is-faq">[ Who Can Benefit ]</div>
      <h2 class="section-heading is-team">Who Can Benefit from Gujarat Government Subsidies</h2>
    </div>
    <div class="sub-audience-grid fade-in">
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>New MSME Entrepreneurs</h3><p>Businesses planning to start manufacturing or service projects in Gujarat.</p></div>
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>Existing MSME Units</h3><p>Units planning expansion, modernization, additional machinery or compliance improvements.</p></div>
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>Textile &amp; Garment Units</h3><p>Garments, apparel, made-ups, technical textiles, weaving, knitting, processing and dyeing businesses.</p></div>
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>Industrial Investors</h3><p>Large, mega and ultra-mega investors planning eligible industrial projects.</p></div>
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>Logistics &amp; Warehousing</h3><p>Logistic parks, warehousing, storage and industrial infrastructure projects.</p></div>
      <div class="sub-audience-card sub-audience-card--gujarat"><h3>Technology &amp; Sector Units</h3><p>IT, electronics, biofuel, energy, biotechnology and other notified sectors.</p></div>
    </div>
  </div>
</section>

{process_section([
    ("01", "Understand Project & Location", "Business type, Taluka/category, investment, sector, land/building and project status."),
    ("02", "Check Gujarat Policy Fit", "Identify possible Gujarat subsidy policy or sector-specific support area."),
    ("03", "Prepare DPR & Financials", "Create DPR, project viability, cost structure, projections and subsidy planning."),
    ("04", "Collect Documents", "Gather registrations, quotations, investment proofs, financials and compliance records."),
    ("05", "Application & Liaison", "Support application filing and coordination with relevant departments or nodal agencies."),
    ("06", "Follow-Up & Compliance", "Track queries, provide clarifications and support until process completion."),
])}

{docs_section([
    ("Business Details", "Business name, promoter details, type of unit, sector and product/service details"),
    ("Project Location", "District, Taluka, land/building status and eligible area/category"),
    ("Investment Details", "Plant & machinery, equipment, building, utilities, project cost and funding source"),
    ("Financial Details", "Term loan, working capital, bank status, own contribution and projections"),
    ("Supporting Documents", "Quotations, ownership/rent papers, KYC, financials, project report and compliance records"),
])}

{trust_section([
    ("Gujarat-Focused Guidance", "Ahmedabad-based advisory with deep Gujarat Government subsidy expertise."),
    ("Compliance-First Mindset", "Documentation and eligibility handled carefully to reduce rejection risk."),
    ("Process Knowledge", "Experience with government process flow, departments and application stages."),
    ("DPR & Documentation", "Detailed project reports, financial projections and required documents."),
    ("Ecosystem Access", "Machinery suppliers, banking liaison, government liaison and compliance partners."),
])}

{faq_section([
    ("Which Gujarat Government subsidy schemes do you guide for?", "We provide guidance for MSME Assistance, Large/Mega/Ultra-Mega units, Textile subsidy, Logistic Park assistance, Electric Duty waiver, Marketing Support and sector-specific Gujarat policies."),
    ("Is Gujarat subsidy approval guaranteed?", "No. Eligibility and approval depend on policy rules, location, project category, documents and authority verification. We provide advisory support, not guaranteed approval."),
    ("Do Taluka categories matter for subsidy?", "Yes, many Gujarat incentives depend on project location and applicable Taluka category. We help assess your project's location-based eligibility."),
    ("Can an existing business apply for subsidy?", "Expansion and modernization may be eligible in some cases depending on policy conditions. Contact us for a case-by-case assessment."),
    ("Do you help textile units?", "Yes, we provide guidance for garments, apparel, technical textiles, weaving, knitting, processing and related textile activities under Gujarat policies."),
    ("Do you prepare DPR for Gujarat subsidy?", "Yes, DPR preparation for MSME, logistic park and textile subsidy schemes is part of our service profile."),
], "Common questions about Gujarat Government subsidy advisory.")}

{promo_section(
    "Check Gujarat Subsidy Eligibility",
    "Want to Know Which Gujarat Government Subsidy Fits Your Project?",
    "Share your project idea, location, investment plan and industry. Our team will guide you with possible Gujarat Government subsidy options and documentation requirements.",
    "Check Gujarat Subsidy Eligibility",
)}
"""

# Build pages
for filename, active, title, desc, main in [
    ("central-subsidies.html", "central",
     "Central Government Subsidy Consultant in India | Subsidy Gyaan",
     "Get expert guidance for Central Government subsidy schemes including PMFME, NABARD, AIF, EPCG, APEDA, MOFPI, Cold Storage and Renewable Energy support.",
     central_main),
    ("gujarat-subsidies.html", "gujarat",
     "Gujarat Government Subsidy Consultant | MSME, Textile &amp; Industrial Subsidy Guidance",
     "Get expert guidance for Gujarat Government subsidies including MSME assistance, textile subsidy, logistic park support, electric duty waiver, DPR preparation and documentation.",
     gujarat_main),
]:
    out = (
        head(title, desc)
        + fix_header(header, active)
        + '<div class="main">'
        + main
        + '</div>'
        + fix_footer(footer, active)
        + '</div><script src="js/main.js"></script></body></html>'
    )
    with open(f"{base}/{filename}", "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Built {filename}", len(out))

# Update nav links in existing pages
for page in ["index.html", "about.html", "services.html"]:
    path = f"{base}/{page}"
    html = open(path, encoding="utf-8").read()
    html = html.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Central Government Subsidies',
        'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
    )
    html = html.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
        'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
    )
    html = html.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Central Government Subsidies',
        'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
    )
    html = html.replace(
        'href="#schemes" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
        'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
    )
    html = html.replace(
        'href="index.html#schemes" class="dropdown-link w-dropdown-link">Central Government Subsidies',
        'href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies',
    )
    html = html.replace(
        'href="index.html#schemes" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
        'href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies',
    )
    html = html.replace(
        'href="index.html#schemes" class="scheme-cta">View Central Subsidies',
        'href="central-subsidies.html" class="scheme-cta">View Central Subsidies',
    )
    html = html.replace(
        'href="index.html#schemes" class="scheme-cta">View Gujarat Subsidies',
        'href="gujarat-subsidies.html" class="scheme-cta">View Gujarat Subsidies',
    )
    html = html.replace(
        'href="#schemes" class="footer-link">Central Government',
        'href="central-subsidies.html" class="footer-link">Central Government',
    )
    html = html.replace(
        'href="#schemes" class="footer-link">Gujarat Government',
        'href="gujarat-subsidies.html" class="footer-link">Gujarat Government',
    )
    html = html.replace(
        'href="index.html#schemes" class="footer-link">Central Government',
        'href="central-subsidies.html" class="footer-link">Central Government',
    )
    html = html.replace(
        'href="index.html#schemes" class="footer-link">Gujarat Government',
        'href="gujarat-subsidies.html" class="footer-link">Gujarat Government',
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated nav in {page}")

# Update build_services.py links
services_py = open(f"{base}/build_services.py", encoding="utf-8").read()
services_py = services_py.replace('href="index.html#schemes" class="scheme-cta">View Central Subsidies', 'href="central-subsidies.html" class="scheme-cta">View Central Subsidies')
services_py = services_py.replace('href="index.html#schemes" class="scheme-cta">View Gujarat Subsidies', 'href="gujarat-subsidies.html" class="scheme-cta">View Gujarat Subsidies')
with open(f"{base}/build_services.py", "w", encoding="utf-8") as f:
    f.write(services_py)

print("Done.")

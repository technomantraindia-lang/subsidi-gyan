import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

header_m = re.search(r'<section class="header">.*?</section>', index, re.DOTALL)
footer_m = re.search(r'<section class="footer".*?</section>', index, re.DOTALL)
header = header_m.group(0) if header_m else ""
footer = footer_m.group(0) if footer_m else ""

header = header.replace('href="index.html" class="menu-link w--current">Home', 'href="index.html" class="menu-link">Home')
header = header.replace('href="about.html" class="menu-link">About', 'href="about.html" class="menu-link">About')
header = header.replace('href="#services" class="menu-link">Services', 'href="services.html" class="menu-link w--current">Services')
header = header.replace('href="/" aria-current="page" class="brand-block', 'href="index.html" class="brand-block')
header = header.replace('class="brand-block w-nav-brand w--current"', 'class="brand-block w-nav-brand"')
header = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', header)

footer = footer.replace('href="index.html" class="footer-link w--current">Home', 'href="index.html" class="footer-link">Home')
footer = footer.replace('href="about.html" class="footer-link">About', 'href="about.html" class="footer-link">About')
footer = footer.replace('href="/" aria-current="page" class="footer-link w--current">Home', 'href="index.html" class="footer-link">Home')
footer = footer.replace('href="/about-us" class="footer-link">About Us', 'href="about.html" class="footer-link">About Us')
footer = footer.replace('href="#services" class="footer-link">Services', 'href="services.html" class="footer-link w--current">Services')
footer = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', footer)

SERVICES = [
    ("01", "Central Government Subsidy Advisory", "Guidance for schemes such as PMFME, NABARD / AMIGS, AIF, EPCG, APEDA, Cold Storage, MOFPI and Biomass / Renewable Energy subsidy opportunities."),
    ("02", "Gujarat Government Subsidy Advisory", "Support for Gujarat-based units to understand MSME assistance, textile incentives, logistic park assistance, electric duty benefits, marketing support and sector policies."),
    ("03", "Detailed Project Report Preparation", "Preparation of DPRs structured for government requirements, banking standards, viability analysis, financial projections and subsidy optimization."),
    ("04", "Registration & Certification Services", "Facilitation support for Udyam, FSSAI, GST, Import Export License and other industry-specific certificates required for eligibility and compliance."),
    ("05", "Banking & Financial Liaison", "Coordination support with term loan providers, financial institutions and bank documentation for subsidy-linked projects and project finance."),
    ("06", "Government Liaison & Follow-Up", "Application flow support, department coordination, nodal agency follow-up and document readiness to reduce delays and rejection risk."),
    ("07", "Machinery Supplier Networking", "Access to trusted equipment and machinery vendors relevant to food processing, manufacturing and industrial setup needs."),
    ("08", "Food Technologist & Compliance Support", "Expert ecosystem support for food processing units, micro food processors, gruh udyog and businesses needing technical compliance guidance."),
]

cards_html = ""
for num, title, desc in SERVICES:
    cards_html += f'''
      <div class="svc-card fade-in">
        <div class="svc-card-num">{num}</div>
        <div class="svc-card-icon">◆</div>
        <h3 class="svc-card-title">{title}</h3>
        <p class="svc-card-text">{desc}</p>
        <span class="svc-card-arrow">→</span>
      </div>'''

head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Subsidy Consultancy Services in Gujarat &amp; India | Subsidy Gyaan</title>
  <meta name="description" content="Explore Subsidy Gyaan services for Central and Gujarat Government subsidy advisory, DPR preparation, Udyam, FSSAI, GST, IEC, banking liaison and government follow-up support."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="css/style.css" rel="stylesheet"/>
  <link href="css/custom.css" rel="stylesheet"/>
  <link href="css/about.css?v=1.1" rel="stylesheet"/>
  <link href="css/services.css" rel="stylesheet"/>
</head>
<body>
<div class="page-wrapper">
"""

main = f"""
<section class="page-hero-section about-inner-hero svc-hero">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-inner-hero-grid">
      <div class="about-inner-hero-content fade-in">
        <div class="pill-button">[ Services ]</div>
        <p class="about-inner-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
        <h1 class="about-inner-title">Complete Subsidy &amp; Business Advisory Services</h1>
        <p class="about-inner-desc">From subsidy eligibility guidance to DPR preparation, registrations, documentation, banking liaison and government follow-up, Subsidy Gyaan supports entrepreneurs and industries through every important stage of subsidy availment.</p>
        <div class="button-block hero-btns">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Check Subsidy Eligibility</div><div class="button-text is-primary-button">Check Subsidy Eligibility</div></div>
          </a>
          <a href="index.html#contact" class="button is-secondary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-secondary">Talk to Our Expert</div><div class="button-text is-secondary">Talk to Our Expert</div></div>
          </a>
        </div>
        <div class="breadcrumb-nav">
          <a href="index.html" class="breadcrumb-home">Home</a>
          <div class="breadcrumb-divider"><img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690af44dbcda67d4e97f4bc9_breadcrumb-icon.svg" loading="lazy" alt=""/></div>
          <div>Services</div>
        </div>
      </div>
      <div class="about-inner-hero-visual fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690992115e99223039814b76_contact-image.avif" loading="lazy" alt="Subsidy consultancy services" class="about-inner-hero-img"/>
        <div class="svc-floating-tags">
          <span>DPR</span><span>Udyam</span><span>FSSAI</span><span>PMFME</span><span>MSME</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="svc-overview-strip">
  <div class="w-layout-blockcontainer container w-container">
    <div class="svc-strip fade-in">
      <div class="svc-strip-item"><div class="svc-strip-icon">🏛️</div><div><strong>Subsidy Advisory</strong><span>Central &amp; Gujarat Government schemes</span></div></div>
      <div class="svc-strip-item"><div class="svc-strip-icon">📋</div><div><strong>DPR Preparation</strong><span>Bank and government-ready project reports</span></div></div>
      <div class="svc-strip-item"><div class="svc-strip-icon">✅</div><div><strong>Registrations</strong><span>Udyam, FSSAI, GST, IEC and compliance</span></div></div>
      <div class="svc-strip-item"><div class="svc-strip-icon">🏦</div><div><strong>Liaison Support</strong><span>Banking, financial and government coordination</span></div></div>
      <div class="svc-strip-item"><div class="svc-strip-icon">🔗</div><div><strong>Ecosystem Access</strong><span>Machinery, food technology and partner network</span></div></div>
    </div>
  </div>
</section>

<section class="services-section svc-main-grid-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-service">
      <div class="pill-button is-service">[ Our Services ]</div>
      <h2 class="section-heading is-service">All Core Advisory &amp; Support Services</h2>
      <p class="section-intro-text">Subsidy Gyaan by Advait Associates provides end-to-end consultancy for Central and Gujarat Government subsidy schemes, helping businesses understand eligibility, prepare documents and coordinate with the right ecosystem partners.</p>
    </div>
    <div class="svc-cards-grid">{cards_html}
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="svc-advisory-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block">
      <div class="pill-button">[ Subsidy Advisory ]</div>
      <h2 class="section-heading">Central &amp; Gujarat Government Subsidy Advisory</h2>
      <p class="section-intro-text">Subsidy schemes can be complex because eligibility depends on investment, industry, location, documents, policy conditions and department verification. Subsidy Gyaan helps businesses understand which schemes may apply and how to move forward with a structured subsidy strategy.</p>
    </div>
    <div class="schemes-split-grid fade-in">
      <div class="scheme-card scheme-card--central">
        <h3>Central Government Subsidy Advisory</h3>
        <p>Best for national schemes related to food processing, agriculture infrastructure, export promotion, cold storage, capital equipment, renewable energy and MSME-linked benefits.</p>
        <ul><li>PMFME, NABARD / AMIGS, AIF</li><li>EPCG, APEDA, Cold Storage</li><li>MOFPI, Biomass / Renewable Energy</li></ul>
        <a href="central-subsidies.html" class="scheme-cta">View Central Subsidies →</a>
      </div>
      <div class="scheme-card scheme-card--gujarat">
        <h3>Gujarat Government Subsidy Advisory</h3>
        <p>Best for Gujarat-based entrepreneurs, MSMEs, textile units, logistics projects, manufacturing units and sector-specific policy benefits.</p>
        <ul><li>MSME Assistance Scheme</li><li>Textile &amp; Logistic Park incentives</li><li>Electric duty waiver, Marketing support</li></ul>
        <a href="gujarat-subsidies.html" class="scheme-cta">View Gujarat Subsidies →</a>
      </div>
    </div>
  </div>
</section>

<section class="svc-dpr-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="svc-dpr-grid">
      <div class="svc-dpr-image fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b0913b14506195ef385b1_about-image-1.avif" loading="lazy" alt="DPR and documentation" class="about-inner-hero-img"/>
      </div>
      <div class="svc-dpr-content fade-in">
        <div class="pill-button">[ DPR &amp; Documentation ]</div>
        <h2 class="section-heading">DPR, Registration &amp; Documentation Support</h2>
        <p class="about-text">A well-prepared DPR is the foundation of many subsidy applications and project finance proposals. Our support covers project viability, financial projections, technical specifications and documentation readiness.</p>
        <ul class="svc-feature-list">
          <li><strong>Detailed Project Report (DPR)</strong> — viability analysis, financial projections, scheme-wise structuring and subsidy optimization.</li>
          <li><strong>Registration &amp; Certification</strong> — Udyam, FSSAI, GST, IEC and industry-specific certificates.</li>
          <li><strong>Documentation Readiness</strong> — business, project, financial and machinery documents for applications.</li>
          <li><strong>Compliance Guidance</strong> — compliance-first approach to reduce rejection risk before submission.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="svc-network-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="svc-network-grid">
      <div class="svc-network-content fade-in">
        <div class="pill-button">[ Ecosystem Support ]</div>
        <h2 class="section-heading">Networking &amp; Allied Services</h2>
        <p class="about-text">Beyond application support, Subsidy Gyaan acts as a bridge between industries and verified ecosystem partners — helping businesses move closer to practical execution.</p>
        <div class="svc-network-cards">
          <div class="svc-network-card"><strong>Machinery Supplier Networking</strong><p>Trusted equipment vendors for food processing and manufacturing.</p></div>
          <div class="svc-network-card"><strong>Food Technologist Support</strong><p>Technical guidance for micro food processors and gruh udyog.</p></div>
          <div class="svc-network-card"><strong>Compliance Partner Coordination</strong><p>FSSAI, quality and industry-specific compliance support.</p></div>
          <div class="svc-network-card"><strong>Banking &amp; Government Liaison</strong><p>Coordination with banks, financial institutions and departments.</p></div>
        </div>
      </div>
      <div class="svc-network-visual fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b0913ec147be6ab17ca3e_about-image-2.avif" loading="lazy" alt="Ecosystem networking" class="about-inner-hero-img"/>
      </div>
    </div>
  </div>
</section>

<section class="about-approach-section svc-process-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block" style="text-align:center">
      <div class="pill-button">[ Process ]</div>
      <h2 class="section-heading">How Our Service Process Works</h2>
    </div>
    <div class="about-process-grid fade-in">
      <div class="about-process-step"><div class="about-process-num">01</div><h3>Understand Your Business</h3><p>Industry, investment, location and project idea assessment.</p></div>
      <div class="about-process-step"><div class="about-process-num">02</div><h3>Check Eligibility</h3><p>Identify suitable Central or Gujarat Government schemes.</p></div>
      <div class="about-process-step"><div class="about-process-num">03</div><h3>Prepare Documents</h3><p>DPR, registrations, compliance and application files.</p></div>
      <div class="about-process-step"><div class="about-process-num">04</div><h3>File Application</h3><p>Structured submission as per scheme requirements.</p></div>
      <div class="about-process-step"><div class="about-process-num">05</div><h3>Coordinate &amp; Follow Up</h3><p>Banks, departments and nodal agency coordination.</p></div>
      <div class="about-process-step"><div class="about-process-num">06</div><h3>Support Until Execution</h3><p>Handholding until subsidy-ready execution.</p></div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="svc-clients-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-team">
      <div class="pill-button is-faq">[ Who Can Use ]</div>
      <h2 class="section-heading is-team">Who Can Use Our Services</h2>
    </div>
    <div class="svc-clients-grid fade-in">
      <div class="svc-client-card"><h3>New Entrepreneurs</h3><p>Understand business setup, subsidy possibility, documents and project planning before investment.</p></div>
      <div class="svc-client-card"><h3>MSME Industries</h3><p>Plan subsidy strategy, registrations, DPR, loan documentation and application readiness.</p></div>
      <div class="svc-client-card"><h3>Micro Food Processors</h3><p>Guidance for PMFME, FSSAI, DPR, machinery and subsidy-linked compliance.</p></div>
      <div class="svc-client-card"><h3>Gruh Udyog</h3><p>Support to formalize, become subsidy-ready and access government support.</p></div>
      <div class="svc-client-card"><h3>SHGs / FPOs / FPCs</h3><p>Group-based infrastructure, food processing and scheme-oriented applications.</p></div>
      <div class="svc-client-card"><h3>Industrial Units</h3><p>Expansion, modernization, sector policies, government liaison and subsidy planning.</p></div>
    </div>
  </div>
</section>

<section class="svc-docs-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="svc-docs-card fade-in">
      <div class="pill-button">[ Documents Preview ]</div>
      <h2 class="section-heading">Documents &amp; Inputs You May Need</h2>
      <p class="section-intro-text">Exact requirements vary by scheme. Contact us for scheme-wise checklists.</p>
      <div class="svc-docs-grid">
        <div class="svc-doc-item"><strong>Business Details</strong><span>Industry, location, ownership, investment plan</span></div>
        <div class="svc-doc-item"><strong>Project Details</strong><span>Machinery, capacity, process, project cost</span></div>
        <div class="svc-doc-item"><strong>Registration Details</strong><span>Udyam, GST, FSSAI, IEC certificates</span></div>
        <div class="svc-doc-item"><strong>Financial Details</strong><span>Loan requirement, quotations, projections</span></div>
        <div class="svc-doc-item"><strong>Scheme-Specific Documents</strong><span>Vary by scheme, department and policy</span></div>
      </div>
      <p class="svc-disclaimer">Subsidy eligibility, required documents, benefit amount and approval depend on applicable government policy, project category, location, investment and department verification.</p>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="promo-section">
  <div class="promo-main-block">
    <div class="promo-sticky-block">
      <div class="promo-wrapper sg-about-promo">
        <div class="container">
          <div class="promo-content-wrap">
            <p class="about-inner-tagline about-promo-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
            <h2 class="promo-text">Need Help Choosing the Right Service for Your Business?</h2>
            <p class="promo-desc-text">Share your business idea, industry, location and investment plan. Subsidy Gyaan will help you understand whether you need subsidy advisory, DPR preparation, registration support, banking liaison or complete handholding.</p>
            <p class="svc-cta-phone"><a href="tel:+918320542940">+91 8320542940</a> / <a href="tel:+918866248393">+91 8866248393</a></p>
            <div class="button-block is-promo hero-btns">
              <a href="index.html#contact" class="button is-primary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-primary-button">Book Consultation</div><div class="button-text is-primary-button">Book Consultation</div></div>
              </a>
              <a href="tel:+918320542940" class="button is-secondary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-secondary">Call Now</div><div class="button-text is-secondary">Call Now</div></div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

out = head + header + '<div class="main">' + main + '</div>' + footer + '</div><script src="js/main.js"></script></body></html>'

with open(f"{base}/services.html", "w", encoding="utf-8") as f:
    f.write(out)

print("Built services.html", len(out))

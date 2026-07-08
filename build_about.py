import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

with open(f"{base}/about-source.html", encoding="utf-8") as f:
    html = f.read()

with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

# Extract header and footer from index
header_m = re.search(r'<section class="header">.*?</section>', index, re.DOTALL)
footer_m = re.search(r'<section class="footer">.*?</section>', index, re.DOTALL)
header = header_m.group(0) if header_m else ""
footer = footer_m.group(0) if footer_m else ""

# Mark About as active in nav
header = header.replace('href="#" class="menu-link w--current">Home', 'href="index.html" class="menu-link">Home')
header = header.replace('href="#about" class="menu-link">About', 'href="about.html" class="menu-link w--current">About')
header = header.replace('href="#contact"', 'href="about.html#contact"')

# Head
head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>About Subsidy Gyaan | Gujarat &amp; Central Government Subsidy Consultancy</title>
  <meta name="description" content="Learn about Subsidy Gyaan by Advait Associates, Ahmedabad-based subsidy advisory firm helping MSMEs, industries, entrepreneurs, SHGs and FPOs with Central and Gujarat Government subsidy consultancy."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="css/style.css" rel="stylesheet"/>
  <link href="css/custom.css" rel="stylesheet"/>
  <link href="css/about.css?v=1.1" rel="stylesheet"/>
</head>
<body>
<div class="page-wrapper">
"""

main = """
<section class="page-hero-section about-inner-hero">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-inner-hero-grid">
      <div class="about-inner-hero-content fade-in">
        <div class="pill-button">[ About Subsidy Gyaan ]</div>
        <h1 class="about-inner-title">Guiding Businesses from Subsidy Awareness to Successful Availment</h1>
        <p class="about-inner-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
        <p class="about-inner-desc">Subsidy Gyaan by Advait Associates is an Ahmedabad-based advisory platform helping industries, MSMEs, entrepreneurs, micro food processors, SHGs, FPOs and growing enterprises avail eligible Central and Gujarat Government subsidy benefits with clarity and confidence.</p>
        <div class="button-block">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Check Eligibility</div><div class="button-text is-primary-button">Check Eligibility</div></div>
          </a>
        </div>
        <div class="breadcrumb-nav">
          <a href="index.html" class="breadcrumb-home">Home</a>
          <div class="breadcrumb-divider"><img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690af44dbcda67d4e97f4bc9_breadcrumb-icon.svg" loading="lazy" alt=""/></div>
          <div>About Us</div>
        </div>
      </div>
      <div class="about-inner-hero-visual fade-in">
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/690b091362f6fe3fff57e63c_about-image-3.avif" loading="lazy" alt="Subsidy advisory consultation" class="about-inner-hero-img"/>
      </div>
    </div>
  </div>
</section>

<section class="about-section about-intro-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-intro-grid">
      <div class="about-intro-left fade-in">
        <div class="heading-block is-about-page">
          <div class="pill-button">[ Who We Are ]</div>
          <h2 class="section-heading is-about-page">A specialized subsidy advisory firm built to simplify government schemes for businesses.</h2>
        </div>
        <p class="about-text">Subsidy Gyaan is a knowledge-sharing and advisory platform focused on creating awareness about subsidy opportunities available to MSME industries and helping enterprises secure maximum eligible benefits under Central and State Government schemes.</p>
        <p class="about-text">Subsidy Gyaan by Advait Associates offers end-to-end consultancy services across India. The firm assists industries with subsidy availment under Central Government and Government of Gujarat schemes through practical advisory, compliance guidance, project report preparation and ecosystem support.</p>
        <p class="about-text">Since its inception in 2011, Subsidy Gyaan has guided over 3,500 clients in navigating the complexities of subsidy applications, documentation, project reports, compliance requirements and government processes.</p>
        <div class="button-block">
          <a href="services.html" class="button is-secondary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-secondary">Explore Our Services</div><div class="button-text is-secondary">Explore Our Services</div></div>
          </a>
        </div>
      </div>
      <div class="about-brand-card fade-in">
        <div class="about-brand-card-inner">
          <div class="about-brand-name">Subsidy Gyaan</div>
          <div class="about-brand-by">by Advait Associates</div>
          <ul class="about-brand-meta">
            <li><strong>Location</strong> Ahmedabad, Gujarat</li>
            <li><strong>Service Area</strong> Across India</li>
            <li><strong>Established</strong> 2011</li>
            <li><strong>Category</strong> Subsidy Availment Consultancy</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="counter-section about-stats-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="counter-main-block about-stats-grid">
      <div class="counter-single-block fade-in">
        <div class="counter-card about-stat-card">
          <div class="about-stat-num">2011</div>
          <p class="counter-text">Year Established</p>
          <p class="about-stat-sub">Years of subsidy advisory experience and practical government process understanding.</p>
        </div>
      </div>
      <div class="counter-single-block fade-in">
        <div class="counter-card about-stat-card">
          <div class="about-stat-num">3,500+</div>
          <p class="counter-text">Clients Served</p>
          <p class="about-stat-sub">Clients guided across subsidy applications, documentation and business support.</p>
        </div>
      </div>
      <div class="counter-single-block fade-in">
        <div class="counter-card about-stat-card">
          <div class="about-stat-num">Pan-India</div>
          <p class="counter-text">Advisory Reach</p>
          <p class="about-stat-sub">Advisory support for Central and State Government subsidy opportunities.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="about-purpose-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-purpose-grid">
      <div class="about-purpose-left fade-in">
        <div class="pill-button">[ Our Purpose ]</div>
        <h2 class="section-heading">Making subsidy knowledge accessible, practical and useful for every eligible business.</h2>
        <p class="about-text">We help clients understand schemes, become documentation-ready, plan projects, identify eligibility and move from idea to implementation — not just file submission.</p>
      </div>
      <div class="about-purpose-cards fade-in">
        <div class="about-purpose-card"><span>01</span><h3>Create awareness about subsidy opportunities.</h3></div>
        <div class="about-purpose-card"><span>02</span><h3>Guide enterprises to secure maximum eligible benefits.</h3></div>
        <div class="about-purpose-card"><span>03</span><h3>Support compliance, DPR preparation and government process readiness.</h3></div>
      </div>
    </div>
  </div>
</section>

<section class="about-audience-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-team">
      <div class="pill-button is-faq">[ Who We Support ]</div>
      <h2 class="section-heading is-team">Supporting entrepreneurs, industries and grassroots enterprises.</h2>
      <p class="section-intro-text">Subsidy Gyaan works with a wide range of business categories, from industrial units to micro food processors and home-based enterprises.</p>
    </div>
    <div class="about-audience-grid fade-in">
      <div class="about-audience-card">Entrepreneurs</div>
      <div class="about-audience-card">Industrial Units</div>
      <div class="about-audience-card">MSMEs</div>
      <div class="about-audience-card">Micro Food Processors</div>
      <div class="about-audience-card">Gruh Udyog</div>
      <div class="about-audience-card">Self-Help Groups</div>
      <div class="about-audience-card">Farmer Producer Organizations</div>
      <div class="about-audience-card">Cooperatives</div>
      <div class="about-audience-card">Exporters</div>
      <div class="about-audience-card">Growing Businesses</div>
    </div>
    <div class="about-audience-highlight fade-in">
      <strong>Special Focus:</strong> Strengthening the micro food processing sector through awareness, handholding and subsidy-readiness support for underserved entrepreneurs.
    </div>
  </div>
  <div class="empty-space"></div>
</section>
"""

# Extract why-choose section from about-source and customize
why_m = re.search(r'<section class="why-choose-section">.*?</section>', html, re.DOTALL)
why = why_m.group(0) if why_m else ""
why = why.replace('[ Why Choose Us ]', '[ Our USP ]')
why = why.replace('Sustainable Solutions<br/>Proven Results', 'What makes Subsidy Gyaan different?')
why = re.sub(r'style="opacity:0"', '', why)
why = why.replace('Eco-Friendly <br/>Commitment', 'Expertise')
why = why.replace("We’re dedicated to protecting the planet with responsible, sustainable recycling solutions.", "Deep understanding of Central and State Government subsidy schemes with a streamlined application process.")
why = why.replace('Smart Technology<br/>Integration', 'Process Knowledge')
why = why.replace('AI-powered tools make sorting and tracking recyclables easier than ever.', 'Extensive experience with government departments and application flows to reduce delays and confusion.')
why = why.replace('Reward-Based<br/>System', 'Proactive Approach')
why = why.replace('Earn points and incentives for every eco-friendly action you take.', 'Stays updated with amendments and policy changes so clients can make informed decisions.')
why = why.replace('Transparent &amp;<br/>Reliable Service', 'Reliability')
why = why.replace('From pickup to processing, you can track your recycling journey anytime.', 'Transparent and responsive advisory that builds trust with industries across India.')
why = why.replace('Community-Driven<br/>Impact', '')
why = why.replace('Together, we build awareness and drive real change for a cleaner future.', '')
# Remove 5th card block
why = re.sub(r'<div class="why-choose-hide-mobile"></div><div data-w-id="154e3f6a.*?</div></div></div></div>', '</div></div></div>', why, flags=re.DOTALL)

approach = """
<section class="about-approach-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-project">
      <div class="pill-button is-faq">[ Our Approach ]</div>
      <h2 class="section-heading is-faq">A structured advisory process from eligibility to execution.</h2>
    </div>
    <div class="about-process-grid fade-in">
      <div class="about-process-step"><div class="about-process-num">01</div><h3>Understand the business</h3><p>Project idea, industry, investment and location assessment.</p></div>
      <div class="about-process-step"><div class="about-process-num">02</div><h3>Identify suitable schemes</h3><p>Central or Gujarat Government subsidy scheme mapping.</p></div>
      <div class="about-process-step"><div class="about-process-num">03</div><h3>Document readiness</h3><p>Registration, compliance and eligibility preparation.</p></div>
      <div class="about-process-step"><div class="about-process-num">04</div><h3>Prepare DPR &amp; strategy</h3><p>Project report, viability analysis and subsidy strategy.</p></div>
      <div class="about-process-step"><div class="about-process-num">05</div><h3>Application &amp; liaison</h3><p>Filing, banking coordination and government follow-up.</p></div>
      <div class="about-process-step"><div class="about-process-num">06</div><h3>Support until approval</h3><p>Claim processing and benefit realization support.</p></div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>

<section class="about-knowledge-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-knowledge-card fade-in">
      <div class="pill-button">[ Knowledge Platform ]</div>
      <h2 class="section-heading">More than consultancy — a knowledge platform for subsidy awareness.</h2>
      <blockquote class="about-knowledge-quote">Knowledge democratization: from large industries to micro-enterprises, complex schemes are made accessible.</blockquote>
      <p class="about-text">Subsidy Gyaan focuses on making complex schemes accessible to MSMEs, micro-enterprises and industries through articles and practical advisory content.</p>
      <a href="index.html#articles" class="button is-secondary w-inline-block">
        <div class="button-text-effect"><div class="button-text is-secondary">Read Subsidy Articles</div><div class="button-text is-secondary">Read Subsidy Articles</div></div>
      </a>
    </div>
  </div>
</section>

<section class="about-commitment-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-blog">
      <div class="pill-button">[ Our Commitment ]</div>
      <h2 class="section-heading is-testimonial">Committed to transparent, timely and inclusive advisory support.</h2>
    </div>
    <div class="about-commitment-grid fade-in">
      <div class="about-commitment-card"><strong>Transparency</strong><p>In every transaction and advisory interaction.</p></div>
      <div class="about-commitment-card"><strong>Timeliness</strong><p>In application processing and government follow-ups.</p></div>
      <div class="about-commitment-card"><strong>Excellence</strong><p>In documentation quality and compliance management.</p></div>
      <div class="about-commitment-card"><strong>Inclusivity</strong><p>Supporting micro and rural enterprises through accessible guidance.</p></div>
      <div class="about-commitment-card"><strong>Partnership</strong><p>Supporting the client growth journey from idea to implementation.</p></div>
    </div>
    <p class="about-commitment-note fade-in">At Subsidy Gyaan, every eligible industry — whether a large industrial unit or a home-based gruh udyog — deserves expert guidance to access government support.</p>
  </div>
  <div class="empty-space"></div>
</section>

<section class="about-trust-section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="about-trust-grid">
      <div class="about-trust-left fade-in">
        <div class="pill-button">[ Why Choose Us ]</div>
        <h2 class="section-heading">Why Businesses Trust Subsidy Gyaan</h2>
        <p class="about-inner-tagline about-trust-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
        <div class="button-block">
          <a href="index.html#contact" class="button is-primary w-inline-block">
            <div class="button-text-effect"><div class="button-text is-primary-button">Talk to Our Subsidy Expert</div><div class="button-text is-primary-button">Talk to Our Subsidy Expert</div></div>
          </a>
        </div>
      </div>
      <div class="about-trust-points fade-in">
        <div class="about-trust-point"><strong>Holistic Approach</strong><span>End-to-end support from eligibility to approval.</span></div>
        <div class="about-trust-point"><strong>Compliance-First Mindset</strong><span>Documentation handled with precision.</span></div>
        <div class="about-trust-point"><strong>Knowledge Democratization</strong><span>Making subsidy knowledge accessible.</span></div>
        <div class="about-trust-point"><strong>Ecosystem Access</strong><span>Banking, machinery and technologist network.</span></div>
        <div class="about-trust-point"><strong>Social Commitment</strong><span>Empowering MSMEs, SHGs and rural enterprises.</span></div>
      </div>
    </div>
  </div>
</section>
"""

promo = """
<section class="promo-section">
  <div class="promo-main-block">
    <div class="promo-sticky-block">
      <div class="promo-wrapper sg-about-promo">
        <div class="container">
          <div class="promo-content-wrap">
            <p class="about-inner-tagline about-promo-tagline"><span class="tagline-line">Gyaan se Pragati,</span><span class="tagline-line tagline-line--shift">Salah se Samriddhi</span></p>
            <h2 class="promo-text">Ready to understand your subsidy eligibility?</h2>
            <p class="promo-desc-text">Whether you are starting a new business, expanding an industrial unit, setting up a micro food processing project or planning a subsidy-linked investment, Subsidy Gyaan can guide you with eligibility, documents and the right process.</p>
            <div class="button-block is-promo hero-btns">
              <a href="index.html#contact" class="button is-primary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-primary-button">Check Eligibility</div><div class="button-text is-primary-button">Check Eligibility</div></div>
              </a>
              <a href="index.html#contact" class="button is-secondary w-inline-block">
                <div class="button-text-effect"><div class="button-text is-secondary">Contact Us</div><div class="button-text is-secondary">Contact Us</div></div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Fix footer links for about page
footer = footer.replace('href="#" class="footer-link w--current">Home', 'href="index.html" class="footer-link">Home')
footer = footer.replace('href="#about" class="footer-link">About', 'href="about.html" class="footer-link w--current">About')
footer = footer.replace('href="#', 'href="index.html#')
footer = re.sub(r'href="index\.html#"', 'href="index.html"', footer)

out = head + header + '<div class="main">' + main + why + approach + promo + '</div>' + footer + '</div><script src="js/main.js"></script></body></html>'

with open(f"{base}/about.html", "w", encoding="utf-8") as f:
    f.write(out)

print("Built about.html", len(out))

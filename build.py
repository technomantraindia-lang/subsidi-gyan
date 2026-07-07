import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
with open(f"{base}/source.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    (r'<title>[^<]+</title>', '<title>Subsidy Gyaan | Central &amp; Gujarat Government Subsidy Consultancy</title>'),
    (r'name="description" content="[^"]*"', 'name="description" content="Subsidy Gyaan by Advait Associates provides expert guidance for Central and Gujarat Government subsidies, DPR preparation, registrations, compliance and subsidy application support."'),
    (r'<link href="https://cdn\.prod\.website-files\.com/69082f2869747d13e82f1a82/css/[^"]+"[^>]+>', '<link href="css/style.css?v=1.2" rel="stylesheet" type="text/css"/><link href="css/custom.css?v=1.2" rel="stylesheet" type="text/css"/>'),
    (r'<script src="https://d3e54v103j8qbb[^"]*"[^>]*></script>', ''),
    (r'<script src="https://cdn\.prod\.website-files\.com/69082f2869747d13e82f1a82/js/[^"]+"[^>]*></script>', ''),
    (r' style="opacity:0"', ''),
    (
        r'<img loading="lazy" src="https://cdn\.prod\.website-files\.com/69082f2869747d13e82f1a82/690836ed3a8e5318f1adce64_brand-logo\.svg" alt="brand-logo" class="brand-logo-icon"/>',
        '<span class="brand-logo-text">Subsidy Gyaan<span class="brand-byline">by Advait Associates</span></span>'
    ),
    (
        r'<a href="/" aria-current="page" class="menu-link w--current">Home</a><a href="/about-us" class="menu-link">About us</a><a href="/pricing" class="menu-link">Pricing</a>',
        '<a href="#" class="menu-link w--current">Home</a><a href="#about" class="menu-link">About</a><a href="#services" class="menu-link">Services</a>'
    ),
    (r'<div class="menu-link dropdown">Pages</div>', '<div class="menu-link dropdown">Subsidies</div>'),
    (
        r'<nav class="dropdown-list w-dropdown-list"><a href="/" aria-current="page" class="dropdown-link w-dropdown-link w--current">Home</a>.*?</nav>',
        '<nav class="dropdown-list w-dropdown-list"><a href="central-subsidies.html" class="dropdown-link w-dropdown-link">Central Government Subsidies</a><a href="gujarat-subsidies.html" class="dropdown-link w-dropdown-link">Gujarat Government Subsidies</a></nav>',
        re.DOTALL
    ),
    (
        r'<a href="/contact" class="menu-link">Contact</a>',
        '<a href="#industries" class="menu-link">Industries</a><a href="articles.html" class="menu-link">Articles</a><a href="contact.html" class="menu-link">Contact</a>'
    ),
    (r'<div class="button-text is-primary-button">Contact Us</div>', '<div class="button-text is-primary-button">Check Eligibility</div>'),
    (r'href="/contact"', 'href="#contact"'),
    (r'<h1[^>]*class="hero-heading">ENVIRONMENT</h1>', '<h1 class="hero-heading hero-tagline"><span class="tagline-line">ज्ञान से प्रगति,</span><span class="tagline-line">सलाह से समृद्धि</span></h1>'),
    (r'Eco-Friendly Solutions for Smart Recycling', 'Expert Guidance for Central &amp; Gujarat Government Subsidies'),
    (
        r'Providing innovative recycling solutions that reduce waste, save energy, and promote sustainability for a cleaner, greener, and smarter planet\.',
        'Gyaan se Pragati, Salah se Samriddhi — Subsidy Gyaan by Advait Associates helps entrepreneurs, MSMEs, industries, SHGs, FPOs and growing businesses avail maximum eligible subsidy benefits through expert advisory, DPR preparation and government process support.'
    ),
    (r'<div class="satisfied-clients">Customers</div>', '<div class="satisfied-clients">Year Established</div>'),
    (r'<div class="satisfied-clients is-experiance">Years Of Experience</div>', '<div class="satisfied-clients is-experiance">Clients Served</div>'),
    (
        r'We help communities businesses minimize waste recycle efficiently and create a sustainable future for generations ahead\.',
        'We help businesses understand subsidies, prepare documents, and move from idea to implementation with confidence.'
    ),
    (
        r'Empowering communities and businesses to minimize waste, recycle efficiently, and promote sustainable practices for a cleaner, greener, and healthier planet\.',
        'Subsidy Gyaan by Advait Associates is an Ahmedabad-based advisory firm offering end-to-end consultancy for Central and Gujarat Government subsidy schemes. Since 2011, the firm has supported 3,500+ clients with subsidy applications, DPR preparation, compliance guidance and registrations.'
    ),
    (r'More about us', 'Know More About Us'),
    (r'<p class="counter-text">Project Complete</p>', '<p class="counter-text">Subsidy Metric</p>', ),
    (r'Sustainable Waste Management Services', 'Complete Subsidy &amp; Business Advisory Services'),
    (r'<div class="service-title">Electronic Waste</div><p class="service-text">Collecting and processing plastic waste into reusable materials\.</p>', '<div class="service-title">Central Government Subsidy Advisory</div><p class="service-text">Expert guidance on PMFME, NABARD, AIF, EPCG and other Central schemes.</p>'),
    (r'<div class="service-title">Cardboard Recycling</div><p class="service-text">Managing discarded electronics responsibly to reduce pollution\.</p>', '<div class="service-title">Gujarat Government Subsidy Advisory</div><p class="service-text">MSME, textile, logistic park and Gujarat state subsidy scheme support.</p>'),
    (r'<div class="service-title">Plastic Recycling</div><p class="service-text">Collecting and processing plastic waste into reusable materials, reducing environmental\.</p>', '<div class="service-title">Detailed Project Report Preparation</div><p class="service-text">Professional DPR preparation aligned with government requirements.</p>'),
    (r'<div class="service-title">Metal Recycling</div><p class="service-text">Collecting and processing plastic waste into reusable materials, reducing environmental\.</p>', '<div class="service-title">Registration &amp; Certification Services</div><p class="service-text">Udyam, FSSAI, GST and other registrations for subsidy readiness.</p>'),
    (r'<div class="service-title">Glass Recycling</div><p class="service-text">Collecting and processing plastic waste into reusable materials, reducing environmental\.</p>', '<div class="service-title">Banking &amp; Financial Liaison</div><p class="service-text">Coordination with banks for subsidy-linked finance and approvals.</p>'),
    (r'<div class="service-title">Textile Recycling</div><p class="service-text">Collecting and processing plastic waste into reusable materials, reducing environmental\.</p>', '<div class="service-title">Government Liaison &amp; Follow-Up</div><p class="service-text">Department coordination and application tracking until approval.</p>'),
    (r'<div class="service-title">Battery Recycling</div><p class="service-text">Collecting and processing plastic waste into reusable materials, reducing environmental\.</p>', '<div class="service-title">Food Technologist &amp; Compliance Support</div><p class="service-text">Technical and compliance support for food processing units.</p>'),
    (r'\[ Project \]', '[ Subsidy Schemes ]'),
    (r'1\. Smart Waste Sorting System', '1. PMFME Scheme'),
    (r'2\. Industrial Waste Exchange Platform', '2. Gujarat MSME Assistance Scheme'),
    (r'3\. School &amp; Campus Recycling Challenge', '3. NABARD / AMIGS'),
    (r'4\. Reverse Vending Machine Network', '4. AIF Scheme'),
    (r'5\. Recycled Product Marketplace', '5. Textile Industry Subsidy'),
    (r'AI-powered system that detects, sorts, and guides users for proper recycling\.', 'Expert advisory for eligibility, DPR preparation, documentation and government application support.'),
    (r'\[ Testimonials \]', '[ Why Choose Us ]'),
    (r'Recycling Success Stories from Our Users', 'Why Businesses Trust Subsidy Gyaan'),
    (r'\[ FAQ.s \]', '[ FAQ ]'),
    (r'Quick Answers to Your Recycling Concerns', 'Common Questions About Subsidy Guidance'),
    (r'What items can I recycle in my area\?', 'Which businesses can apply for government subsidy?'),
    (r'How do I know which bin to use for different materials\?', 'Do you provide Gujarat Government subsidy guidance?'),
    (r'Can plastic bags and wrappers be recycled\?', 'Do you help with Central Government schemes?'),
    (r'What should I do with electronic waste \(e-waste\)\?', 'Is DPR required for subsidy application?'),
    (r'Do I need to clean or rinse recyclables before disposal\?', 'Can new businesses also contact Subsidy Gyaan?'),
    (r'Your questions answered\.', 'We guide you through every step of your subsidy journey.'),
    (r'Customer Satisfaction rate\.', 'Client Satisfaction Rate.'),
    (r'Get in Touch', 'Book a Consultation'),
    (r'\(24/7 Available\)', '(Ahmedabad, Gujarat | Across India)'),
    (r'<option value="">Select one\.\.\.</option><option value="First">Electronic Waste</option><option value="Second">Cardboard Recycling</option><option value="Third">Plastic Recycling</option>', '<option value="">Select subsidy type...</option><option value="Central">Central Government Subsidy</option><option value="Gujarat">Gujarat Government Subsidy</option><option value="DPR">DPR Preparation</option>'),
    (r'Enter yor name', 'Enter your name'),
    (r'I agree to all terms and conditions\.', 'I agree to be contacted regarding subsidy advisory services.'),
    (r'Thank you! Your submission has been received!', 'Thank you! We will contact you shortly.'),
    (r'\[ Blog Post \]', '[ Articles ]'),
    (r'Recycling News, Guides &amp; Success Stories', 'Subsidy Guides, Updates &amp; Business Growth Articles'),
    (r'\[ Plastic Waste \]', '[ Central Schemes ]'),
    (r'\[ Electric Waste \]', '[ Gujarat Schemes ]'),
    (r'Green Investments Shaping a More Resilient Global Economy', 'What is PMFME Scheme?'),
    (r'Eco-Friendly Technologies Fueling Future Economic Growth Potential', 'Gujarat MSME Subsidy Guide'),
    (r'Green investments drive sustainable economic growth, support environmental initiatives, and create a resilient\.', 'A complete guide to PMFME scheme eligibility, benefits and application process for micro food processors.'),
    (r'Eco-friendly technologies promote sustainable development, reduce environmental impact, and drive long-term economic growth\.', 'Everything MSME owners need to know about Gujarat state subsidy schemes and capital assistance.'),
    (r'Make a positive environmental impact today — <span class="promo-highlight">recycle more, waste less, live better\.</span>', 'Gyaan se Pragati, Salah se Samriddhi — <span class="promo-highlight">Want to know which subsidy your business can get?</span>'),
    (r'<div class="button-text is-primary-button">Get Started</div>', '<div class="button-text is-primary-button">Book Consultation</div>'),
    (r'Main Page', 'Quick Links'),
    (r'Other Page', 'Subsidies'),
    (r'Template', 'Contact Info'),
    (r'<li class="footer-list-item"><a href="/pricing" class="footer-link">Pricing Plan</a></li>', '<li class="footer-list-item"><a href="#services" class="footer-link">Services</a></li>'),
    (r'<li class="footer-list-item"><a href="/blog-post" class="footer-link">Blog</a></li>', '<li class="footer-list-item"><a href="#articles" class="footer-link">Articles</a></li>'),
    (r'Info@enviro\.com', 'oswal2nisarg@gmail.com'),
    (r'Ahmedabad, Gujarat', 'Ahmedabad, Gujarat, India'),
    (r'© 2024 Copyright - Enviro - Design by .Pixelfit.', '© 2026 Subsidy Gyaan by Advait Associates. All rights reserved.'),
    (r'License - Powered by <a href="https://webflow.com" target="_blank" class="highlight">Webflow</a>', 'Subsidy eligibility depends on government policy, project category and verification.'),
    (r'<section class="about-section">', '<section id="about" class="about-section">'),
    (r'<section class="services-section">', '<section id="services" class="services-section">'),
    (r'<section class="project-section">', '<section id="schemes" class="project-section">'),
    (r'<section class="blog-section">', '<section id="articles" class="blog-section">'),
    (r'<section class="contact-section">', '<section id="contact" class="contact-section">'),
    (r'<section class="testimonial-section">', '<section id="why-us" class="testimonial-section">'),
]

# testimonial quotes - use simple string replace
html = html.replace(
    "\u201cThis service helped my caf\u00e9 properly manage plastic waste. Customers love knowing we\u2019re part of a sustainable system\u201d",
    "\u201cSubsidy Gyaan guided us through the PMFME scheme and helped us get our food processing unit approved.\u201d"
)
html = html.replace(
    "\u201cI used to be confused about what goes where \u2014 now the smart sorting guide makes it effortless.\u201d",
    "\u201cTheir DPR preparation and Gujarat MSME subsidy guidance saved us months of effort.\u201d"
)
html = html.replace(
    "\u201cThe industrial waste exchange saved us money and connected us with reliable recycling partners.\u201d",
    "\u201cExcellent liaison with banks and government departments. Smooth subsidy approval.\u201d"
)
html = html.replace(
    "\u201cWe proudly use this recycling service across all our offices. It aligns perfectly with our sustainability goals.\u201d",
    "\u201cA trusted advisory partner since 2011. Holistic approach from eligibility to final approval.\u201d"
)
html = html.replace('Daniel Carter', 'Rajesh Patel')
html = html.replace('Ava Robinson', 'Priya Shah')
html = html.replace('Ethan Johnson', 'Amit Mehta')
html = html.replace('<div class="client-position">CEO</div>', '<div class="client-position">Business Owner</div>')

faq_answer = 'Subsidy Gyaan provides expert guidance for MSMEs, food processing units, SHGs, FPOs and industries on Central and Gujarat Government subsidy schemes.'
html = html.replace(
    'Most recycling programs accept paper, cardboard, glass bottles, plastic containers, and metal cans. Check your local recycling guide for specific accepted materials.',
    faq_answer
)

phone_old = '+123 \xa076599854'
html = html.replace(phone_old, '+91 8320542940')
html = html.replace('+91 8866248393 / +91 6355145558', '+91 8320542940')

for item in replacements:
    if len(item) == 4:
        html = re.sub(item[0], item[1], html, flags=item[3])
    else:
        html = re.sub(item[0], item[1], html)

# Footer links block
html = re.sub(
    r'<li class="footer-list-item"><a href="/service" class="footer-link">Services</a></li><li class="footer-list-item"><a href="/project" class="footer-link">Project</a></li><li class="footer-list-item"><a href="/contact" class="footer-link">Contact us</a></li>',
    '<li class="footer-list-item"><a href="central-subsidies.html" class="footer-link">Central Government</a></li><li class="footer-list-item"><a href="gujarat-subsidies.html" class="footer-link">Gujarat Government</a></li><li class="footer-list-item"><a href="central-subsidies.html" class="footer-link">PMFME</a></li><li class="footer-list-item"><a href="#contact" class="footer-link">Contact</a></li>',
    html
)
html = re.sub(
    r'<li class="footer-list-item"><a href="/404" class="footer-link">404 Page</a></li><li class="footer-list-item"><a href="/style-guide" class="footer-link">Style Guide</a></li><li class="footer-list-item"><a href="/license" class="footer-link">Licenses</a></li><li class="footer-list-item"><a href="/changelog" class="footer-link">Changelog</a></li>',
    '<li class="footer-list-item"><a href="tel:+918320542940" class="footer-link">+91 8320542940</a></li><li class="footer-list-item"><a href="tel:+918866248393" class="footer-link">+91 8866248393</a></li><li class="footer-list-item"><a href="mailto:oswal2nisarg@gmail.com" class="footer-link">Email Us</a></li>',
    html
)

html = html.replace('</body></html>', '<script src="js/main.js?v=1.2"></script></body></html>')

with open(f"{base}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Built index.html", len(html))

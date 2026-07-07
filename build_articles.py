import re
import os

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

# 1. Read index.html to grab the exact Header and Footer
with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

# Extract header and footer from index
header_m = re.search(r'<section class="header">.*?</section>', index, re.DOTALL)
footer_m = re.search(r'<section class="footer">.*?</section>', index, re.DOTALL)
header = header_m.group(0) if header_m else ""
footer = footer_m.group(0) if footer_m else ""

# Mark Articles as active in nav
header = header.replace('href="index.html" class="menu-link w--current">Home', 'href="index.html" class="menu-link">Home')
header = header.replace('href="#articles" class="menu-link">Articles', 'href="articles.html" class="menu-link w--current">Articles')
header = header.replace('href="#contact"', 'href="articles.html#contact"')

# 2. Build the Page structure
head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Subsidy Guides & Articles | Subsidy Gyaan by Advait Associates</title>
  <meta name="description" content="Read practical guides on Central Government subsidies, Gujarat Government schemes, MSME support, DPR preparation, documents, registrations and subsidy eligibility."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="css/style.css" rel="stylesheet"/>
  <link href="css/custom.css" rel="stylesheet"/>
  <style>
    /* Article Page Specific Styles */
    .article-hero { padding: 120px 0 80px; background: linear-gradient(135deg, #f0f7f4 0%, #ffffff 100%); }
    .hero-label { font-size: 14px; font-weight: 600; color: #0a6b57; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; display: inline-block; padding: 6px 12px; background: rgba(10, 107, 87, 0.1); border-radius: 4px; }
    .brand-badge { display: inline-block; font-size: 12px; font-weight: 600; color: #d97706; background: #fef3c7; padding: 4px 10px; border-radius: 20px; margin-bottom: 20px; }
    .hero-title { font-size: 48px; font-weight: 700; color: #0f172a; line-height: 1.2; margin-bottom: 24px; }
    .hero-desc { font-size: 18px; color: #475569; line-height: 1.6; margin-bottom: 32px; max-width: 600px; }
    .btn-group { display: flex; gap: 16px; flex-wrap: wrap; }
    .btn-primary { background: linear-gradient(90deg, #0a6b57, #0d9488); color: white; padding: 14px 28px; border-radius: 6px; text-decoration: none; font-weight: 600; transition: opacity 0.3s; }
    .btn-primary:hover { opacity: 0.9; }
    .btn-outline { border: 2px solid #0a6b57; color: #0a6b57; padding: 12px 28px; border-radius: 6px; text-decoration: none; font-weight: 600; transition: background 0.3s, color 0.3s; }
    .btn-outline:hover { background: #0a6b57; color: white; }
    
    /* Category Strip */
    .category-strip { background: white; padding: 30px 0; border-bottom: 1px solid #e2e8f0; }
    .category-strip-inner { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; }
    .cat-item { display: flex; align-items: center; gap: 10px; font-weight: 500; color: #334155; }
    .cat-icon { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
    
    /* Intro Section */
    .intro-section { padding: 80px 0; background: #fff; }
    .intro-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
    @media (max-width: 768px) { .intro-grid { grid-template-columns: 1fr; } }
    
    /* Featured Article */
    .featured-article { padding: 60px 0; }
    .featured-card { display: flex; background: #f8fafc; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }
    @media (max-width: 768px) { .featured-card { flex-direction: column; } }
    .featured-img { width: 50%; object-fit: cover; }
    @media (max-width: 768px) { .featured-img { width: 100%; height: 250px; } }
    .featured-content { padding: 40px; width: 50%; display: flex; flex-direction: column; justify-content: center; }
    @media (max-width: 768px) { .featured-content { width: 100%; } }
    
    /* Filters & Grid */
    .grid-section { padding: 80px 0; background: #f8fafc; }
    .filter-group { display: flex; gap: 12px; margin-bottom: 40px; flex-wrap: wrap; }
    .filter-btn { padding: 8px 16px; border-radius: 20px; border: 1px solid #cbd5e1; background: white; cursor: pointer; font-weight: 500; transition: 0.3s; }
    .filter-btn.active, .filter-btn:hover { background: #0a6b57; color: white; border-color: #0a6b57; }
    
    .article-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
    @media (max-width: 991px) { .article-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 767px) { .article-grid { grid-template-columns: 1fr; } }
    
    .article-card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: transform 0.3s, box-shadow 0.3s; display: flex; flex-direction: column; height: 100%; }
    .article-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    .card-img { height: 200px; width: 100%; object-fit: cover; }
    .card-body { padding: 24px; flex-grow: 1; display: flex; flex-direction: column; }
    .card-badge { display: inline-block; padding: 4px 10px; font-size: 12px; font-weight: 600; border-radius: 4px; margin-bottom: 12px; }
    .card-title { font-size: 20px; font-weight: 700; color: #0f172a; margin-bottom: 12px; line-height: 1.3; }
    .card-excerpt { font-size: 14px; color: #64748b; margin-bottom: 20px; flex-grow: 1; }
    .read-more { color: #0a6b57; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; }
    
    /* FAQ Section */
    .faq-section { padding: 80px 0; background: white; }
    .faq-item { border-bottom: 1px solid #e2e8f0; padding: 20px 0; cursor: pointer; }
    .faq-q { font-size: 18px; font-weight: 600; color: #0f172a; display: flex; justify-content: space-between; }
    .faq-a { font-size: 16px; color: #475569; margin-top: 16px; display: none; line-height: 1.6; }
    .faq-item.active .faq-a { display: block; }
    
    /* CTA Section */
    .cta-section { padding: 80px 0; background: linear-gradient(135deg, #e0f2fe 0%, #f0fdf4 100%); text-align: center; }
  </style>
</head>
<body>
<div class="page-wrapper">
"""

main = """
<!-- Hero Section -->
<section class="article-hero">
  <div class="container w-container">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 40px;">
      <div style="max-width: 600px;">
        <div class="hero-label">[ Articles & Subsidy Guides ]</div>
        <div><span class="brand-badge">Gyaan se Pragati, Salah se Samriddhi</span></div>
        <h1 class="hero-title">Subsidy Guides, Scheme Updates & Business Growth Articles</h1>
        <p class="hero-desc">Explore practical articles on Central Government subsidies, Gujarat Government schemes, MSME support, DPR preparation, documents, registrations and business setup guidance for entrepreneurs and industries.</p>
        <div class="btn-group">
          <a href="#articles-grid" class="btn-primary">Explore Articles</a>
          <a href="index.html#contact" class="btn-outline">Check Eligibility</a>
        </div>
      </div>
      <div style="flex: 1; min-width: 300px; text-align: right;">
        <img src="https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/690ec8e0fab05726959067e4_service-image.jpg" alt="Knowledge Hub" style="max-width: 100%; border-radius: 12px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);">
      </div>
    </div>
  </div>
</section>

<!-- Category Strip -->
<section class="category-strip">
  <div class="container w-container">
    <div class="category-strip-inner">
      <div class="cat-item"><div class="cat-icon" style="background:#e0f2fe;color:#0284c7;">🏛️</div> Central Subsidies</div>
      <div class="cat-item"><div class="cat-icon" style="background:#dcfce7;color:#16a34a;">📍</div> Gujarat Subsidies</div>
      <div class="cat-item"><div class="cat-icon" style="background:#f1f5f9;color:#475569;">🏭</div> MSME & Startup</div>
      <div class="cat-item"><div class="cat-icon" style="background:#ffedd5;color:#ea580c;">🍎</div> Food Processing</div>
      <div class="cat-item"><div class="cat-icon" style="background:#f1f5f9;color:#334155;">📄</div> DPR & Documents</div>
      <div class="cat-item"><div class="cat-icon" style="background:#fef3c7;color:#d97706;">🛡️</div> Compliance</div>
    </div>
  </div>
</section>

<!-- Intro Section -->
<section class="intro-section">
  <div class="container w-container">
    <div class="intro-grid">
      <div>
        <div class="hero-label" style="background: #e0f2fe; color: #0284c7;">[ Knowledge Hub ]</div>
        <h2 style="font-size: 36px; margin-bottom: 20px; line-height: 1.2;">Understand Subsidies Before You Apply</h2>
        <p style="font-size: 16px; color: #475569; margin-bottom: 20px;">Many businesses miss subsidy opportunities because they are unaware of eligible schemes, required documents, timelines, registrations and compliance conditions.</p>
        <p style="font-size: 16px; color: #475569;">Through Subsidy Gyaan articles, entrepreneurs and industries can understand scheme basics, document readiness, DPR importance and the steps required before starting a subsidy application.</p>
      </div>
      <div>
        <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6909d6031b8fa7452d9f71be_project-image-2.webp" alt="Knowledge Flow" style="width: 100%; border-radius: 12px;">
      </div>
    </div>
  </div>
</section>

<!-- Featured Article -->
<section class="featured-article">
  <div class="container w-container">
    <div class="hero-label">[ Featured Guide ]</div>
    <div class="featured-card">
      <img src="https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d5447179b7888cbab7c1_service-image-2.webp" alt="Featured Article" class="featured-img">
      <div class="featured-content">
        <div style="font-size: 14px; color: #64748b; margin-bottom: 12px;">Category: Subsidy Basics | Read Time: 5 min</div>
        <h3 style="font-size: 28px; margin-bottom: 16px;">How to Check Which Government Subsidy Applies to Your Business</h3>
        <p style="font-size: 16px; color: #475569; margin-bottom: 24px;">A practical guide for entrepreneurs and MSMEs to understand the basic factors that affect subsidy eligibility, including business activity, investment, location, documents and scheme conditions.</p>
        <a href="#" class="read-more">Read Article →</a>
      </div>
    </div>
  </div>
</section>

<!-- Main Grid -->
<section class="grid-section" id="articles-grid">
  <div class="container w-container">
    <div class="hero-label">[ Latest Articles ]</div>
    <h2 style="font-size: 32px; margin-bottom: 30px;">Read Practical Guides on Subsidies, DPRs & Business Support</h2>
    
    <div class="filter-group">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="Central">Central Subsidies</button>
      <button class="filter-btn" data-filter="Gujarat">Gujarat Subsidies</button>
      <button class="filter-btn" data-filter="Food">Food Processing</button>
      <button class="filter-btn" data-filter="DPR">DPR & Documents</button>
    </div>

    <div class="article-grid" id="article-container">
      <!-- Injected via JS -->
    </div>
  </div>
</section>

<!-- FAQ Section -->
<section class="faq-section">
  <div class="container w-container">
    <div class="hero-label">[ FAQ ]</div>
    <h2 style="font-size: 32px; margin-bottom: 40px; text-align: center;">Common Questions About Subsidy Guidance</h2>
    <div style="max-width: 800px; margin: 0 auto;">
      
      <div class="faq-item">
        <div class="faq-q">Are the articles a substitute for professional subsidy consultation? <span>+</span></div>
        <div class="faq-a">No. Articles are for awareness. Final eligibility depends on scheme conditions, documents, project category, location and department verification.</div>
      </div>
      
      <div class="faq-item">
        <div class="faq-q">Can I find out which scheme applies to my business from articles? <span>+</span></div>
        <div class="faq-a">Articles can help you understand scheme direction, but a proper eligibility check is recommended before application.</div>
      </div>
      
      <div class="faq-item">
        <div class="faq-q">Will you publish Gujarat Government subsidy updates? <span>+</span></div>
        <div class="faq-a">Yes, the Articles section can include Gujarat subsidy updates, MSME policy information and sector-specific scheme guidance.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Will articles cover Central Government schemes? <span>+</span></div>
        <div class="faq-a">Yes, the page should include guides for PMFME, NABARD, AIF, EPCG, APEDA, MOFPI and other central schemes.</div>
      </div>

    </div>
  </div>
</section>

<!-- Final CTA -->
<section class="cta-section">
  <div class="container w-container">
    <div class="brand-badge">Gyaan se Pragati, Salah se Samriddhi</div>
    <h2 style="font-size: 40px; margin-bottom: 20px;">Read the Guide, Then Speak to the Expert</h2>
    <p style="font-size: 18px; color: #475569; margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">Articles can help you understand subsidy basics, but your business needs a proper eligibility check based on industry, investment, location, scheme conditions and documents.</p>
    <div class="btn-group" style="justify-content: center;">
      <a href="index.html#contact" class="btn-primary">Check My Subsidy Eligibility</a>
      <a href="tel:+918320542940" class="btn-outline">📞 Call Advisory Team</a>
    </div>
  </div>
</section>
"""

footer_html = """
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
  // Article Data Array
  const articles = [
    { title: "What is PMFME Scheme?", category: "Central", badgeBg: "#e0f2fe", badgeColor: "#0284c7", excerpt: "Explain the PMFME scheme in simple language for micro food processing units, individual entrepreneurs and group-based support.", img: "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/690ec8e0fab05726959067e4_service-image.jpg" },
    { title: "Gujarat MSME Subsidy Guide", category: "Gujarat", badgeBg: "#dcfce7", badgeColor: "#16a34a", excerpt: "Introduce Gujarat MSME subsidy support, capital/interest/power assistance direction and why eligibility checking matters.", img: "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d5447179b7888cbab7c1_service-image-2.webp" },
    { title: "Documents Required for Subsidy Application", category: "DPR", badgeBg: "#f1f5f9", badgeColor: "#334155", excerpt: "List common documents needed before subsidy filing, including registration, project details, finance and compliance records.", img: "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d526de5e411eda8044f1_service-image-4.webp" },
    { title: "Why DPR is Important for Subsidy & Bank Loan", category: "DPR", badgeBg: "#f1f5f9", badgeColor: "#334155", excerpt: "Explain how a detailed project report supports viability, finance planning and subsidy application preparation.", img: "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d62fd1ad54133c680136_service-image-7.webp" },
    { title: "Subsidy Guide for Food Processing Units", category: "Food", badgeBg: "#ffedd5", badgeColor: "#ea580c", excerpt: "Guide food businesses on formalization, FSSAI, DPR, PMFME-style support and common infrastructure direction.", img: "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d6a50f7c67f4d5fa31b9_service-image-6.webp" },
    { title: "NABARD / AMIGS Subsidy Overview", category: "Central", badgeBg: "#e0f2fe", badgeColor: "#0284c7", excerpt: "Explain support for cleaning, sorting, grading and agricultural commodity infrastructure in simple terms.", img: "https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6909d603b5e19398b082d361_project-image-4.webp" }
  ];

  function renderArticles(filterCat) {
    const container = document.getElementById('article-container');
    container.innerHTML = '';
    articles.forEach(art => {
      if(filterCat === 'all' || art.category === filterCat) {
        container.innerHTML += `
          <article class="article-card">
            <img src="${art.img}" class="card-img" alt="${art.title}">
            <div class="card-body">
              <div><span class="card-badge" style="background:${art.badgeBg}; color:${art.badgeColor};">${art.category}</span></div>
              <h3 class="card-title">${art.title}</h3>
              <p class="card-excerpt">${art.excerpt}</p>
              <a href="#" class="read-more">Read Article →</a>
            </div>
          </article>
        `;
      }
    });
  }

  // Init
  renderArticles('all');

  // Filter logic
  $('.filter-btn').click(function(){
    $('.filter-btn').removeClass('active');
    $(this).addClass('active');
    renderArticles($(this).attr('data-filter'));
  });

  // FAQ logic
  $('.faq-item').click(function(){
    $(this).toggleClass('active');
    let sign = $(this).hasClass('active') ? '-' : '+';
    $(this).find('span').text(sign);
  });
</script>
</body>
</html>
"""

# Combine everything
final_html = head + header + main + footer + footer_html

output_path = f"{base}/articles.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated successfully: {output_path}")

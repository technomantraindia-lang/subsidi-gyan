import re
import os
import glob

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

# ---------------------------------------------------------
# Step 1: Update all CTAs across existing HTML and Python files
# ---------------------------------------------------------
files = glob.glob(f"{base}/*.html") + glob.glob(f"{base}/*.py")

for file in files:
    # skip this script itself
    if file.endswith("build_eligibility.py"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the texts
    new_content = content.replace('href="#" class="button is-primary w-inline-block"', 'href="check-subsidy-eligibility.html" class="button is-primary w-inline-block"')
    new_content = new_content.replace('href="#contact" class="button is-primary w-inline-block"', 'href="check-subsidy-eligibility.html" class="button is-primary w-inline-block"')
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated CTAs in {os.path.basename(file)}")


# ---------------------------------------------------------
# Step 2: Build the Check Subsidy Eligibility Page
# ---------------------------------------------------------

# Read index.html to grab the exact Header and Footer
with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

# Extract global Header
header_match = re.search(r'(<section class="header">.*?</section>)', index, re.DOTALL)
header_html = header_match.group(1) if header_match else ""
header_html = header_html.replace('w--current', '')

# Extract global Footer
footer_match = re.search(r'(<section class="footer">.*?</section>)', index, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""
footer_html = footer_html.replace('href="/"', 'href="index.html"')

eligibility_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <link href="https://cdn.prod.website-files.com" rel="preconnect" crossorigin="anonymous"/>
  <title>Check Subsidy Eligibility | Gujarat & Central Government Subsidy Guidance</title>
  <meta content="Submit your business details to check possible subsidy eligibility for Gujarat Government and Central Government schemes. Get guidance on DPR, documentation, registration and subsidy application support." name="description"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link href="css/style.css" rel="stylesheet" type="text/css"/>
  <link href="css/custom.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous"/>
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">WebFont.load({{  google: {{    families: ["Inter:300,400,500,600,700", "Plus Jakarta Sans:400,500,600,700", "Open Sans:400,500,600"]  }}}});</script>
  <script type="text/javascript">!function(o,c){{var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}}(window,document);</script>
  <link href="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6912c4c158c54419a02d608d_favicon_icon.png" rel="shortcut icon" type="image/x-icon"/>
  <style>
    body {{ font-family: 'Inter', sans-serif; background-color: #F4FAFF; color: #14213D; }}
    h1, h2, h3, h4 {{ font-family: 'Plus Jakarta Sans', sans-serif; color: #14213D; }}
    
    .eligibility-hero {{ padding: 80px 5% 60px; background: linear-gradient(135deg, #F4FAFF 0%, #E6F2F5 100%); }}
    .e-hero-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .e-badge {{ display: inline-block; padding: 6px 12px; background: rgba(13, 139, 139, 0.1); color: #0D8B8B; border-radius: 20px; font-size: 14px; font-weight: 600; margin-bottom: 20px; }}
    .e-hero-heading {{ font-size: 42px; line-height: 1.2; margin-bottom: 24px; font-weight: 700; color: #14213D; }}
    .e-brand-line {{ color: #1E73BE; font-weight: 600; margin-bottom: 15px; display: block; }}
    .e-hero-desc {{ font-size: 18px; line-height: 1.6; color: #4A5568; margin-bottom: 30px; }}
    .cta-group {{ display: flex; gap: 15px; }}
    .btn-primary {{ background-color: #F28C28; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: background 0.3s; display: inline-block; text-align: center; }}
    .btn-primary:hover {{ background-color: #1E73BE; color: white; }}
    .btn-outline {{ background-color: transparent; color: #1E73BE; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; border: 2px solid #1E73BE; transition: all 0.3s; display: inline-block; text-align: center; }}
    .btn-outline:hover {{ background-color: #1E73BE; color: white; }}
    
    .e-hero-preview {{ position: relative; background: white; padding: 30px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); }}
    .preview-field {{ height: 40px; background: #F4FAFF; border: 1px solid #E2E8F0; border-radius: 6px; margin-bottom: 15px; }}
    .preview-field.half {{ width: 48%; display: inline-block; }}
    .preview-btn {{ height: 45px; background: #E2E8F0; border-radius: 6px; margin-top: 10px; }}
    .floating-tag {{ position: absolute; background: white; padding: 10px 15px; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); font-weight: 600; color: #0D8B8B; font-size: 14px; }}
    .ft-1 {{ top: 20px; left: -30px; }}
    .ft-2 {{ bottom: 40px; right: -30px; color: #82B440; }}
    .ft-3 {{ top: 50%; left: -40px; transform: translateY(-50%); color: #F28C28; }}

    .trust-strip {{ background: white; padding: 30px 5%; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }}
    .trust-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); text-align: center; }}
    .trust-stat {{ font-size: 28px; font-weight: 700; color: #1E73BE; margin-bottom: 5px; }}
    .trust-label {{ font-size: 14px; color: #4A5568; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }}

    .section-padding {{ padding: 80px 5%; max-width: 1200px; margin: 0 auto; }}
    .section-title {{ font-size: 32px; text-align: center; margin-bottom: 50px; font-weight: 700; }}
    
    .who-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }}
    .who-card {{ background: white; padding: 30px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border-top: 4px solid #1E73BE; }}
    .who-card h3 {{ font-size: 18px; margin-bottom: 12px; color: #14213D; }}
    .who-card p {{ color: #4A5568; line-height: 1.6; font-size: 15px; }}

    .form-wrapper {{ background: white; border-radius: 20px; padding: 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
    .form-step {{ margin-bottom: 40px; }}
    .form-step-title {{ font-size: 20px; color: #0D8B8B; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #F4FAFF; }}
    .form-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    .form-group {{ margin-bottom: 20px; }}
    .form-group.full {{ grid-column: span 2; }}
    label {{ display: block; font-size: 14px; font-weight: 600; color: #14213D; margin-bottom: 8px; }}
    input, select, textarea {{ width: 100%; padding: 14px 16px; border: 1px solid #E2E8F0; border-radius: 8px; font-size: 15px; font-family: inherit; background: #F8FAFC; box-sizing: border-box; transition: border-color 0.3s; }}
    input:focus, select:focus, textarea:focus {{ outline: none; border-color: #1E73BE; background: white; }}
    textarea {{ resize: vertical; min-height: 100px; }}
    .checkbox-group {{ display: flex; align-items: flex-start; gap: 10px; font-size: 14px; color: #4A5568; line-height: 1.5; }}
    .checkbox-group input {{ width: 20px; height: 20px; margin-top: 2px; }}

    .timeline-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    .timeline-card {{ background: white; padding: 30px 20px; border-radius: 16px; text-align: center; border: 1px solid #E2E8F0; }}
    .t-num {{ font-size: 42px; font-weight: 800; color: #F28C28; margin-bottom: 10px; opacity: 0.8; }}
    .timeline-card h3 {{ font-size: 18px; margin-bottom: 10px; }}
    .timeline-card p {{ font-size: 14px; color: #4A5568; line-height: 1.5; }}

    .checklist-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    .checklist-item {{ display: flex; align-items: center; background: white; padding: 20px; border-radius: 12px; border-left: 4px solid #82B440; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }}
    .checklist-icon {{ margin-right: 15px; font-size: 24px; color: #82B440; }}

    .scheme-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }}
    .scheme-card {{ background: #14213D; color: white; padding: 40px; border-radius: 20px; text-align: left; }}
    .scheme-card.alt {{ background: #1E73BE; }}
    .scheme-card h3 {{ color: white; font-size: 24px; margin-bottom: 20px; }}
    .scheme-card p {{ color: #E2E8F0; line-height: 1.6; margin-bottom: 30px; }}

    .faq-item {{ background: white; border-radius: 12px; margin-bottom: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); overflow: hidden; border: 1px solid #E2E8F0; }}
    .faq-q {{ padding: 20px 30px; font-size: 18px; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; color: #14213D; }}
    .faq-q:hover {{ color: #1E73BE; }}
    .faq-a {{ padding: 0 30px 20px; color: #4A5568; line-height: 1.6; display: none; }}

    .final-cta {{ background: linear-gradient(135deg, #0D8B8B 0%, #14213D 100%); padding: 80px 5%; text-align: center; color: white; }}
    .final-cta h2 {{ color: #82B440; margin-bottom: 15px; font-size: 24px; }}
    .final-cta h3 {{ color: white; font-size: 36px; margin-bottom: 40px; }}

    #success-msg {{ display: none; background: #82B440; color: white; padding: 20px; border-radius: 8px; text-align: center; font-weight: 600; margin-top: 20px; }}

    @media (max-width: 991px) {{
      .e-hero-container, .form-grid, .scheme-grid {{ grid-template-columns: 1fr; }}
      .who-grid, .timeline-grid, .trust-container, .checklist-grid {{ grid-template-columns: 1fr 1fr; }}
      .form-group.full {{ grid-column: 1; }}
      .ft-1, .ft-2, .ft-3 {{ display: none; }}
    }}
    @media (max-width: 767px) {{
      .who-grid, .timeline-grid, .trust-container, .checklist-grid {{ grid-template-columns: 1fr; }}
      .trust-stat {{ margin-top: 15px; }}
      .cta-group {{ flex-direction: column; }}
      .btn-primary, .btn-outline {{ width: 100%; box-sizing: border-box; }}
      .mobile-sticky-cta {{ position: fixed; bottom: 0; left: 0; right: 0; background: white; padding: 15px; box-shadow: 0 -5px 20px rgba(0,0,0,0.1); z-index: 1000; display: flex; justify-content: center; }}
    }}
  </style>
</head>
<body>
  <div class="page-wrapper">
    <!-- Header -->
    {header_html}

    <div class="main">
      <!-- Section 1: Eligibility Hero -->
      <section class="eligibility-hero">
        <div class="e-hero-container">
          <div class="hero-content">
            <div class="e-badge">[ Check Subsidy Eligibility ]</div>
            <h1 class="e-hero-heading">Find Out Which Government Subsidy May Apply to Your Business</h1>
            <span class="e-brand-line">Gyaan se Pragati, Salah se Samriddhi</span>
            <p class="e-hero-desc">Share your business idea, industry, location and investment details. Subsidy Gyaan will help you understand possible Central Government and Gujarat Government subsidy options, documentation needs, DPR requirements and next steps.</p>
            <div class="cta-group">
              <a href="#eligibility-form" class="btn-primary">Start Eligibility Check</a>
              <a href="tel:+918320542940" class="btn-outline">Call Our Expert</a>
            </div>
          </div>
          <div class="e-hero-preview">
            <div class="floating-tag ft-1">MSME</div>
            <div class="floating-tag ft-2">Gujarat Subsidy</div>
            <div class="floating-tag ft-3">DPR Preparation</div>
            <h3 style="margin-bottom: 20px; font-size: 18px; color: #A0AABF;">Quick Form Preview</h3>
            <div class="preview-field half"></div>
            <div class="preview-field half" style="float: right;"></div>
            <div class="preview-field"></div>
            <div class="preview-field"></div>
            <div class="preview-btn"></div>
          </div>
        </div>
      </section>

      <!-- Section 2: Trust Strip -->
      <section class="trust-strip">
        <div class="trust-container">
          <div><div class="trust-stat">2011</div><div class="trust-label">Year Established</div></div>
          <div><div class="trust-stat">3,500+</div><div class="trust-label">Clients Served</div></div>
          <div><div class="trust-stat">Pan-India</div><div class="trust-label">Advisory Reach</div></div>
          <div><div class="trust-stat">Ahmedabad</div><div class="trust-label">Gujarat HQ</div></div>
        </div>
      </section>

      <!-- Section 3: Who Should Fill This Form -->
      <section class="section-padding">
        <h2 class="section-title">Who Should Fill This Eligibility Form?</h2>
        <div class="who-grid">
          <div class="who-card">
            <h3>New Entrepreneurs</h3>
            <p>People planning to start a manufacturing, food processing, service, trading, or industrial project.</p>
          </div>
          <div class="who-card">
            <h3>Existing MSME Units</h3>
            <p>Businesses planning expansion, machinery purchase, technology upgrade, or subsidy-linked finance.</p>
          </div>
          <div class="who-card">
            <h3>Food Processing Units</h3>
            <p>Micro food processors, gruh udyog, SHGs, FPOs, FPCs, cooperatives and common infrastructure projects.</p>
          </div>
          <div class="who-card">
            <h3>Textile & Garment Units</h3>
            <p>Garment, apparel, technical textile, weaving, knitting, dyeing or processing units.</p>
          </div>
          <div class="who-card">
            <h3>Logistics & Cold Chain</h3>
            <p>Warehouses, cold storage, logistics parks, storage and post-harvest infrastructure.</p>
          </div>
          <div class="who-card">
            <h3>Export & Manufacturing</h3>
            <p>Units looking for APEDA, EPCG, central schemes, Gujarat schemes, DPR and registration support.</p>
          </div>
        </div>
      </section>

      <!-- Section 4: Eligibility Form -->
      <section class="section-padding" id="eligibility-form">
        <h2 class="section-title">Check Your Subsidy Eligibility</h2>
        <div class="form-wrapper">
          <form id="subsidy-form" onsubmit="event.preventDefault(); document.getElementById('success-msg').style.display='block'; this.reset();">
            
            <!-- Step 1 -->
            <div class="form-step">
              <div class="form-step-title">[ Step 1 - Contact Details ]</div>
              <div class="form-grid">
                <div class="form-group"><label>Full Name *</label><input type="text" required placeholder="Enter your full name"/></div>
                <div class="form-group"><label>Mobile Number *</label><input type="tel" required placeholder="e.g., +91 XXXXX XXXXX"/></div>
                <div class="form-group"><label>Email Address</label><input type="email" placeholder="Enter your email address"/></div>
                <div class="form-group"><label>City</label><input type="text" placeholder="Enter your city"/></div>
                <div class="form-group"><label>State *</label><input type="text" required placeholder="Enter your state"/></div>
                <div class="form-group">
                  <label>Preferred Contact Mode</label>
                  <select>
                    <option>Call</option>
                    <option>WhatsApp</option>
                    <option>Email</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="form-step">
              <div class="form-step-title">[ Step 2 - Business / Project Details ]</div>
              <div class="form-grid">
                <div class="form-group">
                  <label>Are you starting a new business or expanding? *</label>
                  <select required>
                    <option value="">Select option...</option>
                    <option>New Business</option>
                    <option>Existing Unit Expansion</option>
                  </select>
                </div>
                <div class="form-group"><label>Business / Industry Type *</label><input type="text" required placeholder="e.g. Textile, Food Processing, IT"/></div>
                <div class="form-group">
                  <label>Project Category</label>
                  <select>
                    <option>Manufacturing</option>
                    <option>Service</option>
                    <option>Food Processing</option>
                    <option>Textile</option>
                    <option>Logistics</option>
                    <option>Export</option>
                    <option>Other</option>
                  </select>
                </div>
                <div class="form-group"><label>Project Location *</label><input type="text" required placeholder="District, Taluka, City / Village"/></div>
                <div class="form-group"><label>Estimated Total Project Investment</label><input type="text" placeholder="e.g. 2 Cr"/></div>
                <div class="form-group"><label>Plant & Machinery / Equipment Investment</label><input type="text" placeholder="e.g. 1.2 Cr"/></div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="form-step">
              <div class="form-step-title">[ Step 3 - Finance & Subsidy Requirement ]</div>
              <div class="form-grid">
                <div class="form-group"><label>Do you need bank loan support?</label><input type="text" placeholder="Yes / No"/></div>
                <div class="form-group"><label>Loan Amount Required</label><input type="text" placeholder="e.g. 1 Cr"/></div>
                <div class="form-group">
                  <label>Subsidy Interest</label>
                  <select>
                    <option>Gujarat Govt.</option>
                    <option>Central Govt.</option>
                    <option>Both</option>
                    <option>Not Sure</option>
                  </select>
                </div>
                <div class="form-group">
                  <label>Need Help With *</label>
                  <select required>
                    <option>Subsidy Eligibility Check</option>
                    <option>DPR Preparation</option>
                    <option>Registration</option>
                    <option>Loan / Documentation</option>
                    <option>Full Setup Guidance</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="form-step">
              <div class="form-step-title">[ Step 4 - Documents & Message ]</div>
              <div class="form-grid">
                <div class="form-group"><label>Do you have business registration?</label><input type="text" placeholder="Yes / No / In Process"/></div>
                <div class="form-group">
                  <label>Documents Available</label>
                  <select>
                    <option>Udyam</option>
                    <option>GST</option>
                    <option>FSSAI</option>
                    <option>None Yet</option>
                    <option>Multiple Documents Ready</option>
                  </select>
                </div>
                <div class="form-group full"><label>Message / Business Idea Description</label><textarea placeholder="Tell us more about your project and what kind of support you are looking for..."></textarea></div>
                <div class="form-group full">
                  <div class="checkbox-group">
                    <input type="checkbox" required id="consent"/>
                    <label for="consent" style="display:inline; font-weight:normal; color:#4A5568;">I consent to Subsidy Gyaan contacting me regarding my eligibility inquiry and providing advisory follow-up. I understand that submission of this form does not guarantee subsidy approval.</label>
                  </div>
                </div>
              </div>
            </div>

            <button type="submit" class="btn-primary" style="width: 100%; border: none; font-size: 18px; cursor: pointer;">Submit Eligibility Request</button>
            <div id="success-msg">Thank you for sharing your project details. Our team will review your subsidy eligibility information and contact you shortly.</div>

          </form>
        </div>
      </section>

      <!-- Section 5: How Assessment Works -->
      <section class="section-padding" style="background: white;">
        <h2 class="section-title">How the Eligibility Assessment Works</h2>
        <div class="timeline-grid">
          <div class="timeline-card">
            <div class="t-num">01</div>
            <h3>Submit Project Details</h3>
            <p>Visitor shares business idea, industry, investment, location and subsidy requirement.</p>
          </div>
          <div class="timeline-card">
            <div class="t-num">02</div>
            <h3>Basic Review by Team</h3>
            <p>Subsidy Gyaan reviews the details and checks likely Central or Gujarat scheme direction.</p>
          </div>
          <div class="timeline-card">
            <div class="t-num">03</div>
            <h3>Document & DPR Guidance</h3>
            <p>The team explains required registrations, DPR, finance documents and application readiness.</p>
          </div>
          <div class="timeline-card">
            <div class="t-num">04</div>
            <h3>Consultation & Next Steps</h3>
            <p>Visitor receives practical guidance for eligibility, documentation and application support.</p>
          </div>
        </div>
      </section>

      <!-- Section 6: Information Required -->
      <section class="section-padding">
        <h2 class="section-title">Information Users Should Keep Ready</h2>
        <div class="checklist-grid">
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Business idea or existing unit details</div></div>
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Industry type and product/service category</div></div>
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Project location: city, district, taluka, village or industrial area</div></div>
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Estimated total investment and machinery/equipment investment</div></div>
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Loan requirement or finance planning details</div></div>
          <div class="checklist-item"><span class="checklist-icon">✓</span><div>Existing registrations (Udyam, GST, FSSAI) or earlier DPRs</div></div>
        </div>
      </section>

      <!-- Section 7: Scheme Direction Preview -->
      <section class="section-padding" style="background: white;">
        <h2 class="section-title">Scheme Direction Preview</h2>
        <div class="scheme-grid">
          <div class="scheme-card">
            <h3>Central Government Subsidy</h3>
            <p>PMFME, NABARD / AMIGS, AIF, EPCG, APEDA, Cold Storage, Credit Linked Capital Subsidy, MOFPI and Biomass / Renewable Energy subsidy guidance.</p>
            <a href="#eligibility-form" class="btn-primary" style="background: white; color: #14213D;">Submit Details for Review</a>
          </div>
          <div class="scheme-card alt">
            <h3>Gujarat Government Subsidy</h3>
            <p>MSME Assistance, Large / Mega / Ultra-Mega support, Textile subsidy, Logistic Park assistance, Electric Duty Waiver, Marketing Support, and IT / Electronics / Biofuel / Biotechnology policy direction.</p>
            <a href="#eligibility-form" class="btn-primary" style="background: white; color: #1E73BE;">Submit Details for Review</a>
          </div>
        </div>
      </section>

      <!-- Section 8: FAQ -->
      <section class="section-padding">
        <h2 class="section-title">Eligibility Page FAQ</h2>
        <div style="max-width:800px; margin:0 auto;">
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Does filling this form guarantee subsidy approval? <span>+</span></div>
            <div class="faq-a">No. The form helps the team understand your business and guide you about possible subsidy direction. Final eligibility and approval depend on official scheme rules, documents, project location, investment, and authority verification.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Can a new business fill this form? <span>+</span></div>
            <div class="faq-a">Yes. New entrepreneurs can fill the form to understand possible schemes, project report requirements, registration needs and finance planning.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Do you guide for both Gujarat and Central Government schemes? <span>+</span></div>
            <div class="faq-a">Yes. The page should clearly mention both Gujarat Government and Central Government subsidy advisory support.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Do I need a DPR before contacting you? <span>+</span></div>
            <div class="faq-a">No. Users can contact first. Subsidy Gyaan can guide on DPR preparation where required for subsidy, bank finance or project approval.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Can small food processors, SHGs or gruh udyog apply? <span>+</span></div>
            <div class="faq-a">Yes. The business supports micro food processors, gruh udyog, SHGs, FPOs, FPCs and small enterprises where applicable.</div>
          </div>
        </div>
      </section>

      <!-- Section 9: Final CTA -->
      <section class="final-cta">
        <h2>Gyaan se Pragati, Salah se Samriddhi</h2>
        <h3>Ready to Check Which Subsidy May Apply to Your Business?</h3>
        <p style="margin-bottom: 30px; font-size: 16px; color: #E2E8F0;">Submit your project details or speak with our team for practical guidance on subsidy eligibility, DPR, documentation, registration and next steps.</p>
        <div class="cta-group" style="justify-content:center;">
          <a href="#eligibility-form" class="btn-primary">Submit Eligibility Request</a>
          <a href="tel:+918320542940" class="btn-outline" style="color: white; border-color: white;">Call Now</a>
        </div>
      </section>

    </div>

    <!-- Footer -->
    {footer_html}
    
    <!-- Mobile Sticky CTA (Hidden on desktop via CSS, shown via media query if needed) -->
    <div class="mobile-sticky-cta" style="display:none;">
      <a href="#eligibility-form" class="btn-primary" style="width: 100%;">Check Eligibility Now</a>
    </div>

  </div>
  <script>
    if (window.innerWidth <= 767) {{
      document.querySelector('.mobile-sticky-cta').style.display = 'flex';
    }}
  </script>
</body>
</html>
"""

# Write out the final HTML file
with open(f"{base}/check-subsidy-eligibility.html", "w", encoding="utf-8") as out:
    out.write(eligibility_content)

print("check-subsidy-eligibility.html has been successfully generated!")
print("All CTA links have been successfully updated to point to check-subsidy-eligibility.html!")

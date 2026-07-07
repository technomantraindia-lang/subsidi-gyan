import re
import os

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

# 1. Read index.html to grab the exact Header and Footer
with open(f"{base}/index.html", encoding="utf-8") as f:
    index = f.read()

# Extract global Header
header_match = re.search(r'(<section class="header">.*?</section>)', index, re.DOTALL)
header_html = header_match.group(1) if header_match else ""
# Remove the "Current" class from Home or any other page
header_html = header_html.replace('w--current', '')
# Add the "Current" class to the Contact link
header_html = header_html.replace('href="contact.html" class="menu-link"', 'href="contact.html" class="menu-link w--current"')

# Extract global Footer
footer_match = re.search(r'(<section class="footer">.*?</section>)', index, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

# Ensure we use correct path in the footer for Home if needed
footer_html = footer_html.replace('href="/"', 'href="index.html"')

contact_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <link href="https://cdn.prod.website-files.com" rel="preconnect" crossorigin="anonymous"/>
  <title>Contact Subsidy Gyaan | Gujarat & Central Government Subsidy Consultancy</title>
  <meta content="Contact Subsidy Gyaan by Advait Associates for Central and Gujarat Government subsidy guidance, DPR preparation, registrations, documentation, banking liaison and business advisory support." name="description"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link href="css/style.css" rel="stylesheet" type="text/css"/>
  <link href="css/custom.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous"/>
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">WebFont.load({{  google: {{    families: ["Inter:300,400,500,600,700", "Plus Jakarta Sans:400,500,600,700"]  }}}});</script>
  <script type="text/javascript">!function(o,c){{var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}}(window,document);</script>
  <link href="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6912c4c158c54419a02d608d_favicon_icon.png" rel="shortcut icon" type="image/x-icon"/>
  <style>
    /* Contact Page Specific Styles */
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #F8FBFC; /* soft blue-green tint */
    }}
    .contact-hero {{
      padding: 100px 5% 60px;
      background: linear-gradient(135deg, #F8FBFC 0%, #E6F2F5 100%);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .contact-hero-container {{
      max-width: 1200px;
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      align-items: center;
    }}
    .badge {{
      display: inline-block;
      padding: 6px 12px;
      background: rgba(13, 124, 131, 0.1);
      color: #0D7C83;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 600;
      margin-bottom: 20px;
    }}
    h1, h2, h3, h4 {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: #111;
    }}
    .hero-heading {{
      font-size: 42px;
      line-height: 1.2;
      margin-bottom: 24px;
      font-weight: 700;
      color: #0B2C3D;
    }}
    .hero-desc {{
      font-size: 18px;
      line-height: 1.6;
      color: #4A5568;
      margin-bottom: 30px;
    }}
    .cta-group {{
      display: flex;
      gap: 15px;
    }}
    .btn-primary {{
      background-color: #F28C28;
      color: white;
      padding: 14px 28px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
      transition: background 0.3s ease;
    }}
    .btn-primary:hover {{
      background-color: #0D7C83;
    }}
    .btn-outline {{
      background-color: transparent;
      color: #0D7C83;
      padding: 14px 28px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
      border: 2px solid #0D7C83;
      transition: all 0.3s ease;
    }}
    .btn-outline:hover {{
      background-color: #0D7C83;
      color: white;
    }}
    .hero-visual {{
      position: relative;
      height: 400px;
      background: white;
      border-radius: 20px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.08);
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .visual-floating-card {{
      background: #fff;
      padding: 15px 20px;
      border-radius: 12px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.05);
      position: absolute;
      font-weight: 600;
      color: #1E73BE;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .vcard-1 {{ top: 40px; left: -20px; }}
    .vcard-2 {{ bottom: 60px; right: -20px; color: #82B440; }}
    .vcard-3 {{ top: 50%; right: 20px; transform: translateY(-50%); color: #0D7C83; }}
    
    .quick-cards-section {{
      padding: 40px 5%;
      background: white;
    }}
    .cards-grid {{
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }}
    .contact-card {{
      background: #F8FBFC;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      padding: 24px;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .contact-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 12px 24px rgba(0,0,0,0.06);
    }}
    .icon-circle {{
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: #E6F2F5;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
      color: #0D7C83;
      font-size: 20px;
    }}
    .card-label {{
      font-size: 14px;
      color: #718096;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
    }}
    .card-value {{
      font-size: 16px;
      font-weight: 600;
      color: #1A202C;
      margin-bottom: 12px;
      line-height: 1.4;
    }}
    .card-action {{
      font-size: 14px;
      color: #1E73BE;
      text-decoration: none;
      font-weight: 500;
    }}
    
    .enquiry-section {{
      padding: 80px 5%;
    }}
    .enquiry-container {{
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 3fr 2fr;
      gap: 50px;
      background: white;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.04);
      overflow: hidden;
    }}
    .form-block {{
      padding: 50px;
    }}
    .panel-block {{
      background: #0B2C3D;
      color: white;
      padding: 50px;
    }}
    .form-heading {{
      font-size: 32px;
      margin-bottom: 30px;
    }}
    .form-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    .form-group {{
      margin-bottom: 20px;
    }}
    .form-group.full {{
      grid-column: span 2;
    }}
    label {{
      display: block;
      font-size: 14px;
      font-weight: 600;
      color: #4A5568;
      margin-bottom: 8px;
    }}
    input, select, textarea {{
      width: 100%;
      padding: 12px 16px;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      font-size: 15px;
      font-family: inherit;
      background: #F8FAFC;
      transition: border-color 0.3s;
    }}
    input:focus, select:focus, textarea:focus {{
      outline: none;
      border-color: #0D7C83;
      background: white;
    }}
    textarea {{
      resize: vertical;
      min-height: 100px;
    }}
    .submit-btn {{
      background: #F28C28;
      color: white;
      border: none;
      padding: 16px 32px;
      font-size: 16px;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      width: 100%;
      transition: background 0.3s;
    }}
    .submit-btn:hover {{
      background: #0D7C83;
    }}
    
    .panel-heading {{
      color: #4FD1C5;
      font-size: 24px;
      margin-bottom: 30px;
    }}
    .panel-list {{
      list-style: none;
      padding: 0;
    }}
    .panel-list li {{
      margin-bottom: 20px;
      font-size: 16px;
      display: flex;
      align-items: flex-start;
      line-height: 1.5;
    }}
    .panel-list li::before {{
      content: '✓';
      color: #82B440;
      font-weight: bold;
      margin-right: 12px;
      font-size: 18px;
    }}

    .ask-section, .process-section, .location-section, .faq-section {{
      padding: 80px 5%;
      max-width: 1200px;
      margin: 0 auto;
    }}
    .section-title {{
      font-size: 36px;
      text-align: center;
      margin-bottom: 50px;
    }}
    
    .ask-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
    }}
    .ask-card {{
      background: white;
      padding: 30px;
      border-radius: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      border-top: 4px solid #1E73BE;
    }}
    .ask-card h3 {{ font-size: 20px; margin-bottom: 15px; }}
    .ask-card p {{ color: #4A5568; line-height: 1.6; }}

    .process-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }}
    .step-card {{
      background: white;
      padding: 30px 20px;
      border-radius: 16px;
      text-align: center;
      position: relative;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }}
    .step-num {{
      font-size: 48px;
      font-weight: 800;
      color: rgba(13, 124, 131, 0.1);
      margin-bottom: -15px;
    }}
    .step-card h3 {{ font-size: 18px; margin-bottom: 10px; }}
    .step-card p {{ font-size: 14px; color: #4A5568; }}

    .location-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      align-items: center;
      background: white;
      padding: 50px;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.04);
    }}
    .map-placeholder {{
      width: 100%;
      height: 350px;
      background: #E6F2F5;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #0D7C83;
      font-weight: 600;
      font-size: 18px;
    }}

    .faq-item {{
      background: white;
      border-radius: 12px;
      margin-bottom: 15px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
      overflow: hidden;
    }}
    .faq-q {{
      padding: 20px 30px;
      font-size: 18px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      color: #2D3748;
    }}
    .faq-q:hover {{ color: #0D7C83; }}
    .faq-a {{
      padding: 0 30px 20px;
      color: #4A5568;
      line-height: 1.6;
      display: none;
    }}

    .final-cta {{
      background: #0B2C3D;
      padding: 80px 5%;
      text-align: center;
      color: white;
    }}
    .final-cta h2 {{ color: #4FD1C5; margin-bottom: 10px; font-size: 24px; }}
    .final-cta h3 {{ color: white; font-size: 36px; margin-bottom: 40px; }}

    @media (max-width: 991px) {{
      .contact-hero-container, .enquiry-container, .location-container {{
        grid-template-columns: 1fr;
      }}
      .cards-grid, .process-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .ask-grid {{
        grid-template-columns: 1fr;
      }}
      .form-grid {{
        grid-template-columns: 1fr;
      }}
      .form-group.full {{
        grid-column: 1;
      }}
    }}
    @media (max-width: 767px) {{
      .cards-grid, .process-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <div class="page-wrapper">
    <!-- Header -->
    {header_html}

    <div class="main">
      <!-- Section 1: Contact Hero -->
      <section class="contact-hero">
        <div class="contact-hero-container">
          <div class="hero-content">
            <div class="badge">Contact Subsidy Gyaan</div>
            <h1 class="hero-heading">Let us discuss your subsidy eligibility and business growth plan</h1>
            <p class="hero-desc">Share your business idea, investment plan, industry and location. Subsidy Gyaan by Advait Associates will guide you with suitable Central and Gujarat Government subsidy options, DPR preparation, registration support, documentation and government process assistance.</p>
            <div class="cta-group">
              <a href="#enquiry-form" class="btn-primary">Send Enquiry</a>
              <a href="tel:+918320542940" class="btn-outline">Call Now</a>
            </div>
          </div>
          <div class="hero-visual">
            <img src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/69084d23007b33fe89b87108_customer-image.avif" alt="Contact Visual" style="width:100%; border-radius:12px; height: 100%; object-fit: cover; opacity: 0.8;"/>
            <div class="visual-floating-card vcard-1">📄 DPR Preparation</div>
            <div class="visual-floating-card vcard-2">✅ Subsidy Eligibility</div>
            <div class="visual-floating-card vcard-3">📍 Ahmedabad HQ</div>
          </div>
        </div>
      </section>

      <!-- Section 2: Quick Contact Cards -->
      <section class="quick-cards-section">
        <div class="cards-grid">
          <div class="contact-card">
            <div class="icon-circle">📞</div>
            <div class="card-label">Phone</div>
            <div class="card-value">+91 8320542940<br/>+91 8866248393</div>
            <a href="tel:+918320542940" class="card-action">Tap to call</a>
          </div>
          <div class="contact-card">
            <div class="icon-circle">✉️</div>
            <div class="card-label">Email</div>
            <div class="card-value">oswal2nisarg@gmail.com</div>
            <a href="mailto:oswal2nisarg@gmail.com" class="card-action">Send email</a>
          </div>
          <div class="contact-card">
            <div class="icon-circle">🏢</div>
            <div class="card-label">Headquarters</div>
            <div class="card-value">Ahmedabad,<br/>Gujarat</div>
            <a href="#location" class="card-action">View location</a>
          </div>
          <div class="contact-card">
            <div class="icon-circle">🌍</div>
            <div class="card-label">Service Area</div>
            <div class="card-value">Across India</div>
            <a href="#enquiry-form" class="card-action">Start online consultation</a>
          </div>
        </div>
      </section>

      <!-- Section 3: Enquiry Form + Consultation Panel -->
      <section class="enquiry-section" id="enquiry-form">
        <div class="enquiry-container">
          <div class="form-block">
            <h2 class="form-heading">Send Your Subsidy Enquiry</h2>
            <form onsubmit="event.preventDefault(); alert('Thank you for your enquiry! Our team will contact you soon.');">
              <div class="form-grid">
                <div class="form-group"><label>Full Name</label><input type="text" required placeholder="John Doe"/></div>
                <div class="form-group"><label>Mobile Number</label><input type="tel" required placeholder="+91 XXXXX XXXXX"/></div>
                <div class="form-group"><label>Email Address</label><input type="email" required placeholder="email@example.com"/></div>
                <div class="form-group"><label>City / State</label><input type="text" required placeholder="Ahmedabad, Gujarat"/></div>
                <div class="form-group"><label>Business Type / Industry</label><input type="text" required placeholder="e.g. Food Processing, MSME"/></div>
                <div class="form-group">
                  <label>Business Status</label>
                  <select>
                    <option>New Business / Startup</option>
                    <option>Existing Unit (Expansion)</option>
                  </select>
                </div>
                <div class="form-group"><label>Estimated Investment Range</label><input type="text" placeholder="e.g. 50 Lakhs - 2 Cr"/></div>
                <div class="form-group">
                  <label>Need Help With</label>
                  <select>
                    <option>Subsidy Eligibility Check</option>
                    <option>DPR Preparation</option>
                    <option>Registration Support</option>
                    <option>Bank Finance Liaison</option>
                    <option>Full Setup Guidance</option>
                  </select>
                </div>
                <div class="form-group full">
                  <label>Message / Brief Project Details</label>
                  <textarea placeholder="Tell us about your project..."></textarea>
                </div>
                <div class="form-group full">
                  <button type="submit" class="submit-btn">Submit Enquiry</button>
                </div>
              </div>
            </form>
          </div>
          <div class="panel-block">
            <h3 class="panel-heading">What our team can guide you on:</h3>
            <ul class="panel-list">
              <li>Central Government subsidy schemes</li>
              <li>Gujarat Government subsidy schemes</li>
              <li>DPR and project report preparation</li>
              <li>Udyam, FSSAI, GST and IEC registration support</li>
              <li>Banking and financial liaison</li>
              <li>Government liaison and application follow-up</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Section 4: What Can You Ask Us? -->
      <section class="ask-section">
        <h2 class="section-title">What Can You Ask Us?</h2>
        <div class="ask-grid">
          <div class="ask-card">
            <h3>Subsidy Eligibility</h3>
            <p>Ask which Central or Gujarat Government subsidy may apply to your project.</p>
          </div>
          <div class="ask-card">
            <h3>DPR Preparation</h3>
            <p>Ask about project report preparation for subsidy, finance or government applications.</p>
          </div>
          <div class="ask-card">
            <h3>Registration Support</h3>
            <p>Ask about Udyam, FSSAI, GST, IEC and other required registrations.</p>
          </div>
          <div class="ask-card">
            <h3>Food Processing Projects</h3>
            <p>Ask about PMFME, MOFPI, cold storage and food processing support.</p>
          </div>
          <div class="ask-card">
            <h3>Industrial Expansion</h3>
            <p>Ask about MSME, large, mega or ultra-mega unit incentive possibilities.</p>
          </div>
          <div class="ask-card">
            <h3>Liaison & Follow-Up</h3>
            <p>Ask about banking, government department coordination and documentation flow.</p>
          </div>
        </div>
      </section>

      <!-- Section 5: What Happens After You Contact Us? -->
      <section class="process-section">
        <h2 class="section-title">What Happens After You Contact Us?</h2>
        <div class="process-grid">
          <div class="step-card">
            <div class="step-num">01</div>
            <h3>Share Your Requirement</h3>
            <p>User submits business idea, location, investment and required support.</p>
          </div>
          <div class="step-card">
            <div class="step-num">02</div>
            <h3>Initial Review</h3>
            <p>Team checks the basic subsidy, registration and document direction.</p>
          </div>
          <div class="step-card">
            <div class="step-num">03</div>
            <h3>Consultation Discussion</h3>
            <p>User receives guidance on possible next steps, eligibility and required documentation.</p>
          </div>
          <div class="step-card">
            <div class="step-num">04</div>
            <h3>Execution Support</h3>
            <p>DPR, registration, application filing, liaison and follow-up support can begin as applicable.</p>
          </div>
        </div>
      </section>

      <!-- Section 6: Ahmedabad Headquarters + Pan-India Advisory Reach -->
      <section class="location-section" id="location">
        <div class="location-container">
          <div>
            <div class="badge">Connect with Subsidy Gyaan</div>
            <h2 class="hero-heading" style="font-size:32px;">Ahmedabad-based advisory, serving businesses across India</h2>
            <p class="hero-desc">Based in Ahmedabad and serving businesses across India, Subsidy Gyaan supports entrepreneurs, MSMEs, food processors, industrial units, SHGs, FPOs and growing businesses with Central and State Government subsidy advisory.</p>
            <div style="margin-top:20px;">
              <strong>Headquarters:</strong> Ahmedabad, Gujarat<br/><br/>
              <strong>Service Area:</strong> Across India
            </div>
          </div>
          <div class="map-placeholder">
            [ India Map / Ahmedabad Pin Placeholder ]
          </div>
        </div>
      </section>

      <!-- Section 7: Contact FAQ -->
      <section class="faq-section">
        <h2 class="section-title">Frequently Asked Questions</h2>
        <div style="max-width:800px; margin:0 auto;">
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Can I contact Subsidy Gyaan for a new business idea? <span>+</span></div>
            <div class="faq-a">Yes. New entrepreneurs can share their business idea, investment plan and location to understand possible subsidy and setup guidance.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Do you guide for both Central and Gujarat Government subsidies? <span>+</span></div>
            <div class="faq-a">Yes. The website should clearly mention guidance for both Central Government and Gujarat Government subsidy schemes.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Can I ask about DPR preparation? <span>+</span></div>
            <div class="faq-a">Yes. DPR preparation should be one of the main enquiry topics because it supports subsidy and project finance applications.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Do you support registration and certification work? <span>+</span></div>
            <div class="faq-a">Yes. The contact form should allow users to ask about Udyam, FSSAI, GST, IEC and other industry-specific certification support.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';">Is service available outside Ahmedabad? <span>+</span></div>
            <div class="faq-a">Yes. The service area should be shown as Across India.</div>
          </div>
        </div>
      </section>

      <!-- Section 8: Final CTA -->
      <section class="final-cta">
        <h2>Gyaan se Pragati, Salah se Samriddhi</h2>
        <h3>Need guidance for subsidy eligibility, DPR, registration or business setup?</h3>
        <div class="cta-group" style="justify-content:center;">
          <a href="#enquiry-form" class="btn-primary">Book Consultation</a>
          <a href="tel:+918320542940" class="btn-primary" style="background:#0D7C83;">Call Now</a>
        </div>
      </section>

    </div>

    <!-- Footer -->
    {footer_html}
  </div>
</body>
</html>
"""

# 3. Write out the final contact.html file
with open(f"{base}/contact.html", "w", encoding="utf-8") as out:
    out.write(contact_content)

print("contact.html has been successfully generated!")

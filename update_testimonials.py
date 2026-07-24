import re
import os

html_path = 'index.html'

if not os.path.exists(html_path):
    print(f"Error: {html_path} not found.")
    exit(1)

# List of 15 testimonials (12 from docx + 3 outside Gujarat)
testimonials = [
    {
        "initial": "T",
        "company": "Talod Food Products Pvt Ltd",
        "position": "Sabarkantha, Gujarat • Food Processing Subsidy",
        "text": "We had no idea our ready-to-cook product line even qualified for a food processing subsidy until we spoke to their team. They handled the entire documentation and approval process, and we received our subsidy well within the expected timeline."
    },
    {
        "initial": "C",
        "company": "Contrans Logistic Pvt Ltd",
        "position": "Amreli, Gujarat • Warehousing Subsidy",
        "text": "Setting up our warehousing facility involved a lot of paperwork we weren't familiar with. Their team simplified it completely – from eligibility check to final disbursement, everything was handled professionally."
    },
    {
        "initial": "A",
        "company": "Amarnath Projects",
        "position": "Kheda, Gujarat • DPR & Logistics Subsidy",
        "text": "A strong DPR made all the difference for our logistics project. Their financial and technical understanding of what banks and government departments actually look for helped us a lot."
    },
    {
        "initial": "E",
        "company": "Electro Magnetic Industries",
        "position": "Vadodara, Gujarat • Irradiation Plant Subsidy",
        "text": "Our irradiation plant project was fairly technical, and we needed advisors who understood both the industry and the subsidy framework. They got it right on the first attempt."
    },
    {
        "initial": "P",
        "company": "Paras Flour Mill",
        "position": "Vadodara, Gujarat • Food Processing Subsidy",
        "text": "Honest advice, clear timelines, and no unnecessary delays. That's exactly what we experienced while working with their team on our subsidy application."
    },
    {
        "initial": "J",
        "company": "Janki Group (Rice Mill)",
        "position": "Multiple Locations, Gujarat • Multiple Subsidies",
        "text": "We've worked with them across several of our units, and the consistency in their service has been impressive. They understand our business well enough to recommend the right scheme every time."
    },
    {
        "initial": "N",
        "company": "Nissan Syntex Pvt Ltd",
        "position": "Kheda, Gujarat • Logistics Park Subsidy",
        "text": "From the first meeting to final application of subsidy, the process was transparent and well-managed. They kept us informed at every stage of our logistics park subsidy application."
    },
    {
        "initial": "K",
        "company": "Khedut Feeds and Foods Pvt Ltd",
        "position": "Gondal, Gujarat • Food Subsidy",
        "text": "As a growing feed and food business, government subsidies were something we always wanted to explore but never had the time to pursue. Their team made it simple and stress-free."
    },
    {
        "initial": "F",
        "company": "Fable Food Products Pvt Ltd",
        "position": "Umergaon, Gujarat • Multiple Subsidies",
        "text": "We appreciated how they took time to explain which schemes we actually qualified for, instead of pushing a one-size-fits-all approach. That guidance alone was worth the engagement."
    },
    {
        "initial": "G",
        "company": "Green & Green Agro Industries",
        "position": "Ahmedabad, Gujarat • Multiple Subsidies",
        "text": "Reliable, knowledgeable, and always responsive. Our subsidy applications were handled with the kind of attention to detail we didn't get from our previous consultant."
    },
    {
        "initial": "O",
        "company": "OM Namkeen",
        "position": "Ahmedabad, Gujarat • Multiple Subsidies",
        "text": "We run a fairly traditional business, and honestly weren't sure how government subsidies applied to us. Their team broke it down clearly and got us results."
    },
    {
        "initial": "G",
        "company": "Ghanshyam Rice Mill",
        "position": "Khambhat, Anand • Multiple Subsidies",
        "text": "Professional from start to finish. They handled our documentation carefully and followed up with the department regularly, which made a real difference in approval time."
    },
    {
        "initial": "M",
        "company": "MTR Foods Pvt Ltd",
        "position": "Bengaluru, Karnataka • Food Processing Subsidy",
        "text": "Their deep expertise in central food processing incentives and documentation helped our expansion project go through smoothly."
    },
    {
        "initial": "K",
        "company": "Kalyani Logi-Park",
        "position": "Pune, Maharashtra • Logistics & Warehousing Subsidy",
        "text": "Securing a warehouse subsidy under state policies was a complex task, but their team navigated the paperwork and department liaisons perfectly."
    },
    {
        "initial": "V",
        "company": "Vardhman Textiles Ltd",
        "position": "Ludhiana, Punjab • Capital & Textile Subsidy",
        "text": "From initial eligibility check to the final documentation for our technology upgradation, their consultants provided highly professional support."
    }
]

# Generate the HTML for a single card
def make_card(t):
    return f"""      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “{t['text']}”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            {t['initial']}
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              {t['company']}
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              {t['position']}
            </div>
          </div>
        </div>
      </div>"""

cards_html = "\n".join([make_card(t) for t in testimonials])

# The marquee requires 3 duplicates side-by-side inside testimonial-main-wrap
# We remove display: none !important; from testimonial-main-wrap
new_why_us_section = f"""<section id="why-us" class="testimonial-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-testimonail" style="text-align: center; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
      <div class="pill-button" style="display: inline-block; margin-bottom: 15px;">[ Why Choose Us ]</div>
      <h2 class="section-heading is-testimonial" style="margin-bottom: 20px;">Why Businesses Trust Subsidy Gyaan</h2>
      <p style="font-size: 16px; color: #475569; line-height: 1.6; margin-bottom: 50px;">With over a decade of experience, Subsidy Gyaan has successfully guided thousands of businesses in securing their government subsidies. Our comprehensive approach ensures that you get expert assistance from eligibility assessment to final approval, saving you valuable time and effort.</p>
    </div>
    
    <div class="why-us-grid-new">
      <div class="why-us-card-new">
        <div class="why-us-icon-new">👥</div>
        <div class="why-us-text-new">3500+ Clients<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Served successfully</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">⏳</div>
        <div class="why-us-text-new">15+ Years<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Of proven experience</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">🇮🇳</div>
        <div class="why-us-text-new">Pan India<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Nationwide services</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">📚</div>
        <div class="why-us-text-new">Deep Knowledge<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Of current subsidy policies</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">📄</div>
        <div class="why-us-text-new">Expertise<br><span style="font-size: 13px; font-weight: 400; color: #475569;">In documentation</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">🏛️</div>
        <div class="why-us-text-new">Govt. Liaison<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Smooth approvals</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">📊</div>
        <div class="why-us-text-new">Financial Experts<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Strategic financial planning</span></div>
      </div>
      <div class="why-us-card-new">
        <div class="why-us-icon-new">🏭</div>
        <div class="why-us-text-new">Industry Specialist<br><span style="font-size: 13px; font-weight: 400; color: #475569;">Tailored industry solutions</span></div>
      </div>
    </div>
    
    <div class="testimonial-main-wrap" style="margin-top: 50px;">
      <div class="testimonial-main-block">
{cards_html}
      </div>
      <div class="testimonial-main-block">
{cards_html}
      </div>
      <div class="testimonial-main-block">
{cards_html}
      </div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing section
# The old section starts with <section id="why-us" class="testimonial-section"> and ends with </section>
pattern = re.compile(r'<section id="why-us" class="testimonial-section">.*?</section>', re.DOTALL)
new_content, count = pattern.subn(new_why_us_section, content)

if count > 0:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated index.html! Replaced {count} section(s).")
else:
    print("Could not find the testimonial section in index.html.")

# Also update update_why_us.py to make it consistent with the new changes
why_us_script_path = 'update_why_us.py'
if os.path.exists(why_us_script_path):
    # Let's replace its content so it mirrors this updated format
    with open(why_us_script_path, 'w', encoding='utf-8') as f:
        f.write(f"""import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = \"\"\"{new_why_us_section}\"\"\"

pattern = re.compile(r'<section id="why-us" class="testimonial-section">.*?</section>', re.DOTALL)
new_content, count = pattern.subn(new_html, content)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Could not find the target section")
""")
    print("Successfully updated update_why_us.py to keep it in sync!")

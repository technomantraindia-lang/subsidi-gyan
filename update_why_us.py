import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """<section id="why-us" class="testimonial-section">
  <div class="empty-space"></div>
  <div class="w-layout-blockcontainer container w-container">
    <div class="heading-block is-testimonail" style="text-align: center; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
      <div class="pill-button" style="display: inline-block; margin-bottom: 15px;">[ Why Choose Us ]</div>
      <h2 class="section-heading is-testimonial" style="margin-bottom: 20px;">Why Businesses Trust Subsidy Gyaan</h2>
      <p style="font-size: 16px; color: #475569; line-height: 1.6; margin-bottom: 50px;">
        With over a decade of experience, Subsidy Gyaan has successfully guided thousands of businesses in securing their government subsidies. Our comprehensive approach ensures that you get expert assistance from eligibility assessment to final approval, saving you valuable time and effort.
      </p>
    </div>
    
    <div class="custom-testimonial-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
      
      <div class="testimonial-card-block" style="width: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff;">
        <div class="testimonial-text-block">
          <p class="testimonial-text" style="font-size: 15px; line-height: 1.6;">“Subsidy Gyaan guided us through the PMFME scheme and helped us get our food processing unit approved.”</p>
        </div>
        <div class="client-info-text">
          <div class="client-info-wrap"><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/691420825f003f3576b36d2e_testimonial-image-1.avif" alt="testimonial-image-1" class="client-image"/></div>
          <div><div class="client-name">Rajesh Patel</div><div class="client-position">Business Owner</div></div>
        </div>
      </div>

      <div class="testimonial-card-block" style="width: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff;">
        <div class="testimonial-text-block">
          <p class="testimonial-text" style="font-size: 15px; line-height: 1.6;">“Their DPR preparation and Gujarat MSME subsidy guidance saved us months of effort.”</p>
        </div>
        <div class="client-info-text">
          <div class="client-info-wrap"><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/69142082fa5aa58227de1804_testimonial-image-4.avif" alt="Testimonial Image" class="client-image"/></div>
          <div><div class="client-name">Suresh Shah</div><div class="client-position">Business Owner</div></div>
        </div>
      </div>

      <div class="testimonial-card-block" style="width: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff;">
        <div class="testimonial-text-block">
          <p class="testimonial-text" style="font-size: 15px; line-height: 1.6;">“Excellent liaison with banks and government departments. Smooth subsidy approval.”</p>
        </div>
        <div class="client-info-text">
          <div class="client-info-wrap"><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/691420828596354fc0585818_testimonial-image-3.avif" alt="Testimonial Image" class="client-image"/></div>
          <div><div class="client-name">Priya Shah</div><div class="client-position">Business Owner</div></div>
        </div>
      </div>

      <div class="testimonial-card-block" style="width: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff;">
        <div class="testimonial-text-block">
          <p class="testimonial-text" style="font-size: 15px; line-height: 1.6;">“A trusted advisory partner since 2011. Holistic approach from eligibility to final approval.”</p>
        </div>
        <div class="client-info-text">
          <div class="client-info-wrap"><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6914208182271761f038af51_testimonial-image-2.avif" alt="Testimonial Image" class="client-image"/></div>
          <div><div class="client-name">Amit Mehta</div><div class="client-position">Business Owner</div></div>
        </div>
      </div>

    </div>
  </div>
  <div class="empty-space"></div>
</section>"""

pattern = re.compile(r'<section id="why-us" class="testimonial-section">.*?</section><section class="brand-section">.*?</section>(?=\s*<section class="accordion-section">)', re.DOTALL)

new_content, count = pattern.subn(new_html, content)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Could not find the target section")

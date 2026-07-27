import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """<section id="why-us" class="testimonial-section">
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
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We had no idea our ready-to-cook product line even qualified for a food processing subsidy until we spoke to their team. They handled the entire documentation and approval process, and we received our subsidy well within the expected timeline.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            T
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Talod Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Sabarkantha, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Setting up our warehousing facility involved a lot of paperwork we weren't familiar with. Their team simplified it completely – from eligibility check to final disbursement, everything was handled professionally.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            C
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Contrans Logistic Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Amreli, Gujarat • Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “A strong DPR made all the difference for our logistics project. Their financial and technical understanding of what banks and government departments actually look for helped us a lot.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            A
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Amarnath Projects
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • DPR & Logistics Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Our irradiation plant project was fairly technical, and we needed advisors who understood both the industry and the subsidy framework. They got it right on the first attempt.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            E
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Electro Magnetic Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Irradiation Plant Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Honest advice, clear timelines, and no unnecessary delays. That's exactly what we experienced while working with their team on our subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            P
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Paras Flour Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We've worked with them across several of our units, and the consistency in their service has been impressive. They understand our business well enough to recommend the right scheme every time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            J
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Janki Group (Rice Mill)
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Multiple Locations, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From the first meeting to final application of subsidy, the process was transparent and well-managed. They kept us informed at every stage of our logistics park subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            N
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Nissan Syntex Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • Logistics Park Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “As a growing feed and food business, government subsidies were something we always wanted to explore but never had the time to pursue. Their team made it simple and stress-free.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Khedut Feeds and Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Gondal, Gujarat • Food Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We appreciated how they took time to explain which schemes we actually qualified for, instead of pushing a one-size-fits-all approach. That guidance alone was worth the engagement.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            F
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Fable Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Umergaon, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Reliable, knowledgeable, and always responsive. Our subsidy applications were handled with the kind of attention to detail we didn't get from our previous consultant.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Green & Green Agro Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We run a fairly traditional business, and honestly weren't sure how government subsidies applied to us. Their team broke it down clearly and got us results.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            O
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              OM Namkeen
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Professional from start to finish. They handled our documentation carefully and followed up with the department regularly, which made a real difference in approval time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Ghanshyam Rice Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Khambhat, Anand • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Their deep expertise in central food processing incentives and documentation helped our expansion project go through smoothly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            M
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              MTR Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Bengaluru, Karnataka • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Securing a warehouse subsidy under state policies was a complex task, but their team navigated the paperwork and department liaisons perfectly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Kalyani Logi-Park
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Pune, Maharashtra • Logistics & Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From initial eligibility check to the final documentation for our technology upgradation, their consultants provided highly professional support.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            V
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Vardhman Textiles Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ludhiana, Punjab • Capital & Textile Subsidy
            </div>
          </div>
        </div>
      </div>
      </div>
      <div class="testimonial-main-block">
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We had no idea our ready-to-cook product line even qualified for a food processing subsidy until we spoke to their team. They handled the entire documentation and approval process, and we received our subsidy well within the expected timeline.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            T
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Talod Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Sabarkantha, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Setting up our warehousing facility involved a lot of paperwork we weren't familiar with. Their team simplified it completely – from eligibility check to final disbursement, everything was handled professionally.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            C
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Contrans Logistic Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Amreli, Gujarat • Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “A strong DPR made all the difference for our logistics project. Their financial and technical understanding of what banks and government departments actually look for helped us a lot.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            A
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Amarnath Projects
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • DPR & Logistics Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Our irradiation plant project was fairly technical, and we needed advisors who understood both the industry and the subsidy framework. They got it right on the first attempt.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            E
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Electro Magnetic Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Irradiation Plant Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Honest advice, clear timelines, and no unnecessary delays. That's exactly what we experienced while working with their team on our subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            P
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Paras Flour Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We've worked with them across several of our units, and the consistency in their service has been impressive. They understand our business well enough to recommend the right scheme every time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            J
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Janki Group (Rice Mill)
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Multiple Locations, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From the first meeting to final application of subsidy, the process was transparent and well-managed. They kept us informed at every stage of our logistics park subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            N
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Nissan Syntex Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • Logistics Park Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “As a growing feed and food business, government subsidies were something we always wanted to explore but never had the time to pursue. Their team made it simple and stress-free.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Khedut Feeds and Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Gondal, Gujarat • Food Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We appreciated how they took time to explain which schemes we actually qualified for, instead of pushing a one-size-fits-all approach. That guidance alone was worth the engagement.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            F
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Fable Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Umergaon, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Reliable, knowledgeable, and always responsive. Our subsidy applications were handled with the kind of attention to detail we didn't get from our previous consultant.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Green & Green Agro Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We run a fairly traditional business, and honestly weren't sure how government subsidies applied to us. Their team broke it down clearly and got us results.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            O
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              OM Namkeen
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Professional from start to finish. They handled our documentation carefully and followed up with the department regularly, which made a real difference in approval time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Ghanshyam Rice Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Khambhat, Anand • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Their deep expertise in central food processing incentives and documentation helped our expansion project go through smoothly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            M
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              MTR Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Bengaluru, Karnataka • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Securing a warehouse subsidy under state policies was a complex task, but their team navigated the paperwork and department liaisons perfectly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Kalyani Logi-Park
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Pune, Maharashtra • Logistics & Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From initial eligibility check to the final documentation for our technology upgradation, their consultants provided highly professional support.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            V
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Vardhman Textiles Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ludhiana, Punjab • Capital & Textile Subsidy
            </div>
          </div>
        </div>
      </div>
      </div>
      <div class="testimonial-main-block">
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We had no idea our ready-to-cook product line even qualified for a food processing subsidy until we spoke to their team. They handled the entire documentation and approval process, and we received our subsidy well within the expected timeline.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            T
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Talod Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Sabarkantha, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Setting up our warehousing facility involved a lot of paperwork we weren't familiar with. Their team simplified it completely – from eligibility check to final disbursement, everything was handled professionally.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            C
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Contrans Logistic Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Amreli, Gujarat • Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “A strong DPR made all the difference for our logistics project. Their financial and technical understanding of what banks and government departments actually look for helped us a lot.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            A
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Amarnath Projects
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • DPR & Logistics Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Our irradiation plant project was fairly technical, and we needed advisors who understood both the industry and the subsidy framework. They got it right on the first attempt.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            E
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Electro Magnetic Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Irradiation Plant Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Honest advice, clear timelines, and no unnecessary delays. That's exactly what we experienced while working with their team on our subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            P
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Paras Flour Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Vadodara, Gujarat • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We've worked with them across several of our units, and the consistency in their service has been impressive. They understand our business well enough to recommend the right scheme every time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            J
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Janki Group (Rice Mill)
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Multiple Locations, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From the first meeting to final application of subsidy, the process was transparent and well-managed. They kept us informed at every stage of our logistics park subsidy application.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            N
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Nissan Syntex Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Kheda, Gujarat • Logistics Park Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “As a growing feed and food business, government subsidies were something we always wanted to explore but never had the time to pursue. Their team made it simple and stress-free.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Khedut Feeds and Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Gondal, Gujarat • Food Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We appreciated how they took time to explain which schemes we actually qualified for, instead of pushing a one-size-fits-all approach. That guidance alone was worth the engagement.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            F
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Fable Food Products Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Umergaon, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Reliable, knowledgeable, and always responsive. Our subsidy applications were handled with the kind of attention to detail we didn't get from our previous consultant.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Green & Green Agro Industries
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “We run a fairly traditional business, and honestly weren't sure how government subsidies applied to us. Their team broke it down clearly and got us results.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            O
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              OM Namkeen
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ahmedabad, Gujarat • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Professional from start to finish. They handled our documentation carefully and followed up with the department regularly, which made a real difference in approval time.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            G
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Ghanshyam Rice Mill
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Khambhat, Anand • Multiple Subsidies
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Their deep expertise in central food processing incentives and documentation helped our expansion project go through smoothly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            M
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              MTR Foods Pvt Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Bengaluru, Karnataka • Food Processing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “Securing a warehouse subsidy under state policies was a complex task, but their team navigated the paperwork and department liaisons perfectly.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            K
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Kalyani Logi-Park
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Pune, Maharashtra • Logistics & Warehousing Subsidy
            </div>
          </div>
        </div>
      </div>
      <div class="testimonial-card-block" style="width: 380px; min-height: 230px; height: auto; margin: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; border-radius: 16px; background: #fff; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;">
        <div class="testimonial-text-block" style="margin-bottom: 20px;">
          <p class="testimonial-text" style="font-size: 14.5px; line-height: 1.6; color: #334155; font-style: italic; font-weight: 500; font-family: 'Inter', sans-serif; max-width: 100%;">
            “From initial eligibility check to the final documentation for our technology upgradation, their consultants provided highly professional support.”
          </p>
        </div>
        <div class="client-info-text" style="display: flex; align-items: center; gap: 12px;">
          <div class="client-avatar-initials" style="width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(135deg, #0D7C83 0%, #1E73BE 100%); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; flex-shrink: 0; box-shadow: 0 4px 10px rgba(13, 124, 131, 0.15);">
            V
          </div>
          <div>
            <div class="client-name" style="font-size: 14px; font-weight: 700; color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 2px;">
              Vardhman Textiles Ltd
            </div>
            <div class="client-position" style="font-size: 12px; color: #64748b; font-family: 'Inter', sans-serif; font-weight: 500;">
              Ludhiana, Punjab • Capital & Textile Subsidy
            </div>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
  <div class="empty-space"></div>
</section>"""

pattern = re.compile(r'<section id="why-us" class="testimonial-section">.*?</section>', re.DOTALL)
new_content, count = pattern.subn(new_html, content)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Could not find the target section")

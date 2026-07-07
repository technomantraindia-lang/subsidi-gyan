import os
import glob
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html")

new_footer_html = """<section class="footer" style="background-color: #F4FAFF; color: #475569; padding-bottom: 20px; font-family: 'Inter', sans-serif;">
    <style>
        .custom-footer-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 40px;
            padding-top: 50px;
        }
        @media screen and (min-width: 768px) {
            .custom-footer-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
        @media screen and (min-width: 1200px) {
            .custom-footer-grid {
                grid-template-columns: 1.5fr 1fr 1.5fr 1.5fr;
                gap: 50px;
            }
        }
        .custom-footer-col {
            display: flex;
            flex-direction: column;
            gap: 15px;
            text-align: left;
        }
        .footer-cta-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        @media screen and (min-width: 768px) {
            .footer-cta-container {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
        }
        .footer-bottom-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            font-size: 13px; 
            color: #64748B;
        }
        @media screen and (min-width: 768px) {
            .footer-bottom-container {
                flex-direction: row;
                justify-content: space-between;
            }
            .footer-bottom-right {
                text-align: right;
                min-width: 250px;
            }
        }
        .new-footer-link {
            color: #475569;
            text-decoration: none;
            transition: color 0.3s ease;
            font-size: 14px;
            line-height: 2.2;
            display: block;
        }
        .new-footer-link:hover {
            color: #0D8B8B;
        }
        .custom-footer-heading {
            color: #14213D;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 10px;
            text-transform: capitalize;
        }
        .contact-list-item {
            font-size: 14px;
            margin-bottom: 12px;
            line-height: 1.5;
            color: #475569;
        }
    </style>

    <!-- Top CTA Strip -->
    <div class="footer-cta-strip" style="background-color: #e6f4f1; padding: 40px 0;">
        <div class="w-layout-blockcontainer container w-container">
            <div class="footer-cta-container">
                <div style="flex: 1; min-width: 300px; padding-right: 20px;">
                    <div style="font-weight: bold; color: #0D8B8B; margin-bottom: 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Need Subsidy Guidance?</div>
                    <h3 style="color: #14213D; font-size: 24px; margin-top: 0; margin-bottom: 8px; font-weight: 700;">Not sure which subsidy applies to your business?</h3>
                    <p style="margin: 0; font-size: 15px; color: #475569; line-height: 1.5;">Share your business idea, location, investment plan and industry. Our team will guide you with suitable Central and Gujarat Government subsidy options.</p>
                </div>
                <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
                    <a href="check-subsidy-eligibility.html" class="button w-inline-block" style="background-color: #F28C28; color: white; border-radius: 50px; padding: 12px 28px; font-size: 15px; font-weight: 600; text-decoration: none; transition: transform 0.3s ease; box-shadow: 0 4px 10px rgba(242, 140, 40, 0.3);">Check Subsidy Eligibility</a>
                    <a href="contact.html" style="color: #1E73BE; font-size: 15px; font-weight: 600; text-decoration: underline;">Contact Our Expert</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Footer Columns -->
    <div class="w-layout-blockcontainer container w-container">
        <div class="custom-footer-grid">
            
            <!-- Column 1: Brand Info -->
            <div class="custom-footer-col">
                <a href="index.html" class="w-inline-block" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; margin-bottom: 15px; width: max-content;">
                    <img src="subsidy-gyaan logo.png" alt="Subsidy Gyaan Logo" style="height: 80px; width: auto;" />
                    <span style="font-size: 14px; color: #0D8B8B; font-weight: 700; text-align: center;">by Advait Associates</span>
                </a>
                <p style="font-size: 14px; line-height: 1.6; margin: 0; color: #475569;">Subsidy Gyaan is a subsidy advisory and knowledge-sharing platform helping entrepreneurs, MSMEs, industries and growing businesses understand eligible Central and Gujarat Government subsidy schemes, prepare documentation, and move from idea to implementation with confidence.</p>
                <div style="font-weight: 700; font-size: 16px; color: #1E73BE; margin-top: 5px;">ज्ञान से प्रगति, सलाह से समृद्धि</div>
            </div>

            <!-- Column 2: Quick Links -->
            <div class="custom-footer-col">
                <div class="custom-footer-heading">Quick Links</div>
                <div style="display: flex; flex-direction: column; gap: 0px;">
                    <a href="index.html" class="new-footer-link">Home</a>
                    <a href="about.html" class="new-footer-link">About</a>
                    <a href="services.html" class="new-footer-link">Services</a>
                    <a href="central-subsidies.html" class="new-footer-link">Central Government Subsidies</a>
                    <a href="gujarat-subsidies.html" class="new-footer-link">Gujarat Government Subsidies</a>
                    <a href="index.html#industries" class="new-footer-link">Industries</a>
                    <a href="articles.html" class="new-footer-link">Articles</a>
                    <a href="contact.html" class="new-footer-link">Contact</a>
                    <a href="check-subsidy-eligibility.html" class="new-footer-link" style="color: #0D8B8B; font-weight: 600;">Check Subsidy Eligibility</a>
                </div>
            </div>

            <!-- Column 3: Services & Subsidies -->
            <div class="custom-footer-col">
                <div class="custom-footer-heading">Services & Subsidies</div>
                <div style="display: flex; flex-direction: column; gap: 0px;">
                    <a href="central-subsidies.html" class="new-footer-link">Central Government Subsidy Advisory</a>
                    <a href="gujarat-subsidies.html" class="new-footer-link">Gujarat Government Subsidy Advisory</a>
                    <a href="services.html" class="new-footer-link">Detailed Project Report Preparation</a>
                    <a href="services.html" class="new-footer-link">Registration & Certification Services</a>
                    <a href="services.html" class="new-footer-link">Banking & Financial Liaison</a>
                    <a href="services.html" class="new-footer-link">Government Liaison & Follow-Up</a>
                    <a href="services.html" class="new-footer-link">Networking & Allied Services</a>
                </div>
            </div>

            <!-- Column 4: Contact Details -->
            <div class="custom-footer-col">
                <div class="custom-footer-heading">Contact Details</div>
                <div class="contact-list-item">
                    <strong style="color: #14213D; font-weight: 600;">Phone:</strong><br/>
                    <a href="tel:+918320542940" style="color: #475569; text-decoration: none;">+91 8320542940</a> / <a href="tel:+918866248393" style="color: #475569; text-decoration: none;">+91 8866248393</a>
                </div>
                <div class="contact-list-item">
                    <strong style="color: #14213D; font-weight: 600;">Email:</strong><br/>
                    <a href="mailto:oswal2nisarg@gmail.com" style="color: #475569; text-decoration: none;">oswal2nisarg@gmail.com</a>
                </div>
                <div class="contact-list-item">
                    <strong style="color: #14213D; font-weight: 600;">Headquarters:</strong><br/>
                    Ahmedabad, Gujarat
                </div>
                <div class="contact-list-item" style="margin-bottom: 20px;">
                    <strong style="color: #14213D; font-weight: 600;">Service Area:</strong><br/>
                    Across India
                </div>
            </div>
        </div>
    </div>
    
    <!-- Bottom Bar -->
    <div style="border-top: 1px solid #E2E8F0; margin-top: 50px; padding-top: 25px;">
        <div class="w-layout-blockcontainer container w-container">
            <div class="footer-bottom-container">
                <div style="flex: 1;">
                    <p style="margin: 0; line-height: 1.5;"><strong style="color: #14213D;">Disclaimer:</strong> Subsidy eligibility, benefit amount, approval and disbursement depend on applicable government policy, project category, location, investment, documents and department verification. Final approval is subject to official government guidelines and authority decision.</p>
                </div>
                <div class="footer-bottom-right">
                    <div style="margin-bottom: 8px;">Copyright 2026 Subsidy Gyaan by Advait Associates.<br/>All Rights Reserved.</div>
                    <div style="color: #1E73BE; font-weight: 700; font-size: 15px;">ज्ञान से प्रगति, सलाह से समृद्धि</div>
                </div>
            </div>
        </div>
    </div>
</section>"""

for file in files:
    filename = os.path.basename(file)
    if "source.html" in filename or filename == "index.html" or filename == "about.html" or filename == "services.html" or filename == "central-subsidies.html" or filename == "gujarat-subsidies.html" or filename == "articles.html" or filename == "contact.html" or filename == "check-subsidy-eligibility.html":
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # FIXED REGEX: Matches any section tag with class="footer" even if it has style attributes
        new_content = re.sub(r'<section class="footer"[^>]*>.*?</section>', new_footer_html, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated footer in {filename}")

print("Footer update complete! Cleaned up the flexbox interference.")

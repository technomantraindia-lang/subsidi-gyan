import os
import glob
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html")

dropdown_html = """<div data-delay="200" data-hover="true" data-w-id="services-dropdown" class="dropdown w-dropdown"><div class="dropdown-toggle w-dropdown-toggle"><div class="menu-link dropdown">Services</div><img loading="lazy" src="https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6908348359918a65f7271da8_down-arrow.svg" alt="down-arrow" class="dropdown-arrow-icon"/></div><nav class="dropdown-list w-dropdown-list"><a href="services.html" class="dropdown-link w-dropdown-link">Detailed Project Report (DPR)</a><a href="services.html" class="dropdown-link w-dropdown-link">Registration &amp; Certification</a><a href="services.html" class="dropdown-link w-dropdown-link">Banking &amp; Financial Liaison</a><a href="services.html" class="dropdown-link w-dropdown-link">Government Liaison</a></nav></div>"""

for file in files:
    filename = os.path.basename(file)
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # If already injected, skip
    if 'data-w-id="services-dropdown"' in content:
        continue
        
    # Standard replacement
    new_content = re.sub(r'<a href="services.html" class="menu-link">Services</a>', dropdown_html, content)
    new_content = re.sub(r'<a href="services.html" class="menu-link w--current">Services</a>', dropdown_html, new_content)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Injected Services dropdown in {filename}")

print("Services dropdown injection complete!")

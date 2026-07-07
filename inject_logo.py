import os
import glob
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html")

# The regex matches the entire <a ... brand-block ...> ... </a> tag regardless of whether it's the old text version or the recently injected logo version.
brand_block_regex = r'<a[^>]*class="[^"]*brand-block[^"]*"[^>]*>.*?</a>'

# New layout: Column flexbox with Logo on top and "by Advait Associates" directly below
new_brand_block = """<a href="index.html" class="brand-block w-nav-brand w--current" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; padding-top: 5px;">
    <img src="subsidy-gyaan logo.png" alt="Subsidy Gyaan Logo" style="height: 80px; width: auto;" />
    <span class="brand-byline" style="margin-top: 0; text-align: center; font-size: 0.8rem; font-weight: 700;">by Advait Associates</span>
</a>"""
new_brand_block_non_current = new_brand_block.replace('w--current', '')

for file in files:
    filename = os.path.basename(file)
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to replace the first instance of brand-block (the header one)
    # Re.sub with count=1 ensures we only replace the header one if there are others.
    
    if "index.html" in filename:
        new_content = re.sub(brand_block_regex, new_brand_block, content, count=1, flags=re.IGNORECASE | re.DOTALL)
    else:
        new_content = re.sub(brand_block_regex, new_brand_block_non_current, content, count=1, flags=re.IGNORECASE | re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated brand layout in {filename}")

print("Brand layout update complete!")

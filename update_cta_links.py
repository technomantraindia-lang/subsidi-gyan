import os
import glob

workspace_dir = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

html_files = glob.glob(os.path.join(workspace_dir, "*.html"))

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content.replace('href="index.html#contact"', 'href="contact.html"')
    new_content = new_content.replace('href="index.html#articles"', 'href="articles.html"')
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

print("Done updating CTA links.")

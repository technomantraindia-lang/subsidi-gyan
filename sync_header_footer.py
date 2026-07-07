import os
import glob
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html")

# Read index.html to get the master header and footer
with open(os.path.join(base, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract header
header_match = re.search(r'(<section class="header">.*?</section>)<div class="main">', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)
master_header = header_match.group(1)

# Extract footer
footer_match = re.search(r'(<section class="footer">.*?</section>)</div><script', index_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)
master_footer = footer_match.group(1)

# Map pages to their menu link text for setting the w--current class
page_to_link_text = {
    "index.html": "Home",
    "about.html": "About",
    "services.html": "Services",
    "articles.html": "Articles",
    "contact.html": "Contact"
}

for file in files:
    filename = os.path.basename(file)
    if filename == "index.html" or "source" in filename:
        continue

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace header
    content = re.sub(r'<section class="header">.*?</section>', master_header, content, flags=re.DOTALL)

    # Replace footer
    content = re.sub(r'<section class="footer">.*?</section>', master_footer, content, flags=re.DOTALL)

    # Fix w--current class
    # First, remove it from all menu links
    content = content.replace('w--current', '')
    
    # Add it back to the correct link if applicable
    if filename in page_to_link_text:
        link_text = page_to_link_text[filename]
        # Regex to find the link tag for the current page and add w--current
        # e.g. <a href="about.html" class="menu-link">About</a> -> <a href="about.html" class="menu-link w--current">About</a>
        content = re.sub(f'(<a href="[^"]+" class="menu-link[^"]*)(">\\s*{link_text}</a>)', r'\1 w--current\2', content)
        content = re.sub(f'(<a href="[^"]+" aria-current="page" class="menu-link[^"]*)(">\\s*{link_text}</a>)', r'\1 w--current\2', content)

    # If it's a subsidy page, maybe highlight the dropdown
    if "subsidies" in filename:
        content = re.sub(f'(<div class="menu-link dropdown[^"]*)(">)', r'\1 w--current\2', content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Synced header and footer in {filename}")

import os
import re
import json
import zipfile
import xml.etree.ElementTree as ET

articles_dir = r"c:\Users\vivek patel\OneDrive\Desktop\technomantra\subsidi-gyan-main\subsidi-gyan-main\articles"
output_json_path = r"c:\Users\vivek patel\OneDrive\Desktop\technomantra\subsidi-gyan-main\subsidi-gyan-main\articles.json"

# Helper: simple markdown to HTML parser
def md_to_html(md_text):
    # Strip BOM first if any
    md_text = md_text.lstrip('\ufeff').strip()
    
    # Strip front matter
    if md_text.startswith('---'):
        parts = md_text.split('---', 2)
        if len(parts) >= 3:
            md_text = parts[2]
            
    # Replace placeholder company name with Subsidy Gyaan
    md_text = md_text.replace('[Your Company Name]', 'Subsidy Gyaan')
            
    lines = md_text.strip().split('\n')
    html_parts = []
    in_list = False
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            continue
            
        # Ignore horizontal rules / divider lines (e.g., ---, --, etc.)
        if re.match(r'^[-*_]{3,}$', line_str) or line_str == '--':
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            continue
            
        # Bold formatting **text**
        line_str = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line_str)
        # Italic formatting *text*
        line_str = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line_str)
        # Links [text](url)
        line_str = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line_str)
        
        # Headers
        if line_str.startswith('###'):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h3>{line_str[3:].strip()}</h3>")
        elif line_str.startswith('##'):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h2>{line_str[2:].strip()}</h2>")
        elif line_str.startswith('#'):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h1>{line_str[1:].strip()}</h1>")
            
        # Blockquotes
        elif line_str.startswith('>'):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<blockquote>{line_str[1:].strip()}</blockquote>")
            
        # List items
        elif line_str.startswith('-') or line_str.startswith('*'):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"  <li>{line_str[1:].strip()}</li>")
            
        # Paragraphs
        else:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<p>{line_str}</p>")
            
    if in_list:
        html_parts.append("</ul>")
        
    return "\n".join(html_parts)

# Helper: parse YAML front matter metadata
def parse_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip BOM
    content_clean = content.lstrip('\ufeff').strip()
    
    if content_clean.startswith('---'):
        parts = content_clean.split('---', 2)
        if len(parts) >= 3:
            header = parts[1]
            for line in header.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    metadata[key.strip().lower()] = val.strip()
    return metadata, content_clean

# Helper: parse docx and convert paragraphs to HTML
def docx_to_html(docx_path):
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        paragraphs = []
        for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
            if texts:
                paragraphs.append("".join(texts))
                
    # Format the paragraphs as HTML
    html_parts = []
    for i, p in enumerate(paragraphs):
        p_clean = p.strip()
        if not p_clean:
            continue
        
        # Header formatting
        if i == 0:
            html_parts.append(f"<h1>{p_clean}</h1>")
        elif i == 1:
            html_parts.append(f"<blockquote><strong>{p_clean}</strong></blockquote>")
        elif p_clean.endswith('Documents') or p_clean.startswith('Need Help') or p_clean.startswith('A subsidy'):
            html_parts.append(f"<h2>{p_clean}</h2>")
        elif '—' in p_clean:
            # Format list item like: Business Registration Documents -> Udyam Registration...
            title, desc = p_clean.split('—', 1)
            html_parts.append(f"<p><strong>{title.strip()}:</strong> {desc.strip()}</p>")
        else:
            html_parts.append(f"<p>{p_clean}</p>")
            
    return "\n".join(html_parts)

# Target list to hold compiled articles
compiled_articles = []

# Define categories design badges
badges = {
    "Central": {"bg": "#e0f2fe", "color": "#0284c7"},
    "Gujarat": {"bg": "#dcfce7", "color": "#16a34a"},
    "DPR": {"bg": "#f1f5f9", "color": "#334155"},
    "Food": {"bg": "#ffedd5", "color": "#ea580c"}
}

# Image placeholders
images = {
    "PMFME": "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/690ec8e0fab05726959067e4_service-image.jpg",
    "MSME": "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d5447179b7888cbab7c1_service-image-2.webp",
    "Logistics": "https://cdn.prod.website-files.com/69082f2869747d13e82f1a82/6909d603b5e19398b082d361_project-image-4.webp",
    "DPR": "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d62fd1ad54133c680136_service-image-7.webp",
    "Docs": "https://cdn.prod.website-files.com/6908887361c6f5fa611258b3/6912d526de5e411eda8044f1_service-image-4.webp",
    "Advisory": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80"
}

# 1. PMFME Scheme Subsidy Guide
pmfme_path = os.path.join(articles_dir, "PMFME Scheme Subsidy Guide for Food Processing Units.md")
if os.path.exists(pmfme_path):
    meta, raw = parse_metadata(pmfme_path)
    compiled_articles.append({
        "id": 1,
        "title": "PMFME Scheme: Subsidy Guide for Food Processing",
        "category": "Food",
        "badgeBg": badges["Food"]["bg"],
        "badgeColor": badges["Food"]["color"],
        "excerpt": meta.get("meta description", "Comprehensive guide to the PMFME scheme - 35% credit-linked capital subsidy for food processing units."),
        "content": md_to_html(raw),
        "img": images["PMFME"]
    })

# 2. Gujarat MSME Subsidy Guide
msme_path = os.path.join(articles_dir, "gujarat-msme-subsidy-guide_1.md")
if os.path.exists(msme_path):
    meta, raw = parse_metadata(msme_path)
    compiled_articles.append({
        "id": 2,
        "title": "Gujarat MSME Subsidy Guide",
        "category": "Gujarat",
        "badgeBg": badges["Gujarat"]["bg"],
        "badgeColor": badges["Gujarat"]["color"],
        "excerpt": meta.get("meta description", "Simple guide to capital, interest, and power tariff subsidies under Gujarat's industrial policy."),
        "content": md_to_html(raw),
        "img": images["MSME"]
    })

# 3. Documents Required
docs_path = os.path.join(articles_dir, "documents-required-for-subsidy-application.docx")
if os.path.exists(docs_path):
    html_content = docx_to_html(docs_path)
    compiled_articles.append({
        "id": 3,
        "title": "Documents Required for Subsidy Application",
        "category": "DPR",
        "badgeBg": badges["DPR"]["bg"],
        "badgeColor": badges["DPR"]["color"],
        "excerpt": "A checklist of business registration, financial, and compliance documents needed before filing for a government subsidy.",
        "content": html_content,
        "img": images["Docs"]
    })

# 4. Why DPR is Important
dpr_path = os.path.join(articles_dir, "why-dpr-is-important-for-subsidy-and-bank-loan.md")
if os.path.exists(dpr_path):
    meta, raw = parse_metadata(dpr_path)
    compiled_articles.append({
        "id": 4,
        "title": "Why DPR is Important for Subsidy & Bank Loan",
        "category": "DPR",
        "badgeBg": badges["DPR"]["bg"],
        "badgeColor": badges["DPR"]["color"],
        "excerpt": meta.get("meta description", "Explain how a Detailed Project Report (DPR) supports viability and financial evaluation for bank loan and subsidy approval."),
        "content": md_to_html(raw),
        "img": images["DPR"]
    })

# 5. Gujarat Logistics Park Subsidy
logistics_path = os.path.join(articles_dir, "gujarat-logistics-park-subsidy-scheme-v2.md")
if os.path.exists(logistics_path):
    meta, raw = parse_metadata(logistics_path)
    compiled_articles.append({
        "id": 5,
        "title": "Gujarat Logistics Park Subsidy Scheme",
        "category": "Gujarat",
        "badgeBg": badges["Gujarat"]["bg"],
        "badgeColor": badges["Gujarat"]["color"],
        "excerpt": meta.get("meta description", "Guide to Gujarat's subsidy scheme for warehousing, logistics parks, and cold chains."),
        "content": md_to_html(raw),
        "img": images["Logistics"]
    })

# 6. Why Choose Professional Subsidy Advisory
advisory_path = os.path.join(articles_dir, "why-choose-professional-subsidy-advisory_1.md")
if os.path.exists(advisory_path):
    meta, raw = parse_metadata(advisory_path)
    compiled_articles.append({
        "id": 6,
        "title": "Why Choose Professional Subsidy Advisory",
        "category": "Central",
        "badgeBg": badges["Central"]["bg"],
        "badgeColor": badges["Central"]["color"],
        "excerpt": meta.get("meta description", "Learn why businesses prefer professional advisory support for eligibility checking and error-free applications."),
        "content": md_to_html(raw),
        "img": images["Advisory"]
    })

# 7. NABARD / AMIGS Subsidy Overview (Keep this one as it's highly relevant Central scheme)
compiled_articles.append({
    "id": 7,
    "title": "NABARD / AMIGS Subsidy Overview",
    "category": "Central",
    "badgeBg": badges["Central"]["bg"],
    "badgeColor": badges["Central"]["color"],
    "excerpt": "Explain support for cleaning, sorting, grading and agricultural commodity infrastructure in simple terms.",
    "content": """
    <h1>NABARD / AMIGS Subsidy Overview</h1>
    <p>The National Bank for Agriculture and Rural Development (NABARD) implements various schemes to boost agricultural infrastructure. One such prominent scheme is the Agricultural Marketing Infrastructure (AMI), a sub-scheme of ISAM.</p>
    <h2>What Projects Qualify?</h2>
    <ul>
      <li>Godowns and agricultural warehouses</li>
      <li>Cold storage and ripening chambers</li>
      <li>Sorting, grading, cleaning, and packaging units</li>
      <li>Primary processing of agri-commodities (without changing its natural form)</li>
    </ul>
    <h2>Key Benefits</h2>
    <p>This scheme provides back-ended capital subsidy ranging from 25% to 33.33% of the eligible project cost, depending on the applicant category (general, SC/ST, women, or entrepreneurs in hilly/NE states) and project location.</p>
    <p>The subsidy is credit-linked, meaning the applicant must avail a bank loan of at least 50% of the project cost from a cooperative bank, commercial bank, or RRB to qualify for the scheme.</p>
    """,
    "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=400&q=80"
})

# Write the compiled articles list to articles.json
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(compiled_articles, f, indent=2, ensure_ascii=False)

print(f"Successfully compiled {len(compiled_articles)} articles to articles.json!")

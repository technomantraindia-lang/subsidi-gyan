import os
import glob

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html") + glob.glob(f"{base}/*.py")

replacements = {
    # Email replacements
    'href="mailto:Info@enviro.com?subject=Info%40enviro.com"': 'href="mailto:oswal2nisarg@gmail.com"',
    'Info@enviro.com': 'oswal2nisarg@gmail.com',
    
    # Phone replacements
    'href="tel:+12376599854"': 'href="tel:+918866248393"',
    '+123  76599854': '+91 8866248393 / +91 6355145558',
    '+123 \xa076599854': '+91 8866248393 / +91 6355145558', # Handle non-breaking space
    
    # Address replacements
    '45 Eco Ave, New York, NY': 'Ahmedabad, Gujarat',
    
    # Copyright replacements
    '© 2024 Copyright - Enviro - Design by “<a href="https://webflow.com/pixflow" target="_blank" class="highlight">Pixelfit</a>”': '© 2024 Copyright - Subsidy Gyaan',
    '© 2024 Copyright - Enviro - Design by “Pixelfit”': '© 2024 Copyright - Subsidy Gyaan'
}

for file in files:
    if file.endswith("update_contact_info.py") or file.endswith("run.bat") or file.endswith("translate_slogan.py"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for old_text, new_text in replacements.items():
        new_content = new_content.replace(old_text, new_text)
        
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")

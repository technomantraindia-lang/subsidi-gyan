import os
import glob

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
files = glob.glob(f"{base}/*.html") + glob.glob(f"{base}/*.py")

for file in files:
    if file.endswith("translate_slogan.py"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the texts
    new_content = content.replace("Gyaan se Pragati,", "ज्ञान से प्रगति,")
    new_content = new_content.replace("Salah se Samriddhi", "सलाह से समृद्धि")
    new_content = new_content.replace("Gyaan se Pragati", "ज्ञान से प्रगति")
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")

import os
import glob

directory = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"

html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the button texts
    content = content.replace(">Check Eligibility<", ">Check Subsidy Eligibility<")
    content = content.replace(">Check Eligibility →<", ">Check Subsidy Eligibility →<")
    content = content.replace(">Check Eligibility Now<", ">Check Subsidy Eligibility Now<")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Replacement completed for all HTML files.")

import os
from bs4 import BeautifulSoup

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
file_path = os.path.join(base, "index.html")

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
sections = soup.find_all("section")

output = []
for s in sections:
    output.append(f"Section ID: {s.get('id')}, Classes: {s.get('class')}")
    
with open(os.path.join(base, "sections.txt"), "w") as f:
    f.write("\n".join(output))

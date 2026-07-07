import os
from bs4 import BeautifulSoup

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
file_path = os.path.join(base, "index.html")

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
sections = soup.find_all("section")
for s in sections:
    print(f"Section ID: {s.get('id')}, Classes: {s.get('class')}")

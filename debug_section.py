import os
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
file_path = os.path.join(base, "index.html")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the index of "Gyaan se" or "Glass" or "Samrid"
matches = list(re.finditer(r'.{0,200}Salah se.{0,200}', content, flags=re.IGNORECASE))

output = []
for m in matches:
    output.append("MATCH: " + m.group(0))

with open(os.path.join(base, "debug_output.txt"), "w", encoding="utf-8") as f:
    f.write("\n======================\n".join(output))


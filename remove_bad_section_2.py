import os

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
file_path = os.path.join(base, "index.html")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target_text1 = "to know which subsidy"
target_text2 = "Gyaan se Pragati"

idx = content.find(target_text1)
if idx == -1:
    idx = content.find(target_text2)

if idx != -1:
    # Find the start of the section
    start_idx = content.rfind("<section", 0, idx)
    if start_idx == -1:
        # maybe it's a div?
        start_idx = content.rfind('<div class="section', 0, idx)
        
    if start_idx == -1:
        start_idx = content.rfind('<div', 0, idx) # worst case, just find nearest wrapper
        
    end_idx = content.find("</section>", idx)
    if end_idx == -1 or (content.rfind("<section", 0, idx) == -1):
        # if it's a div, finding the matching closing div is hard without parsing, 
        # but let's assume it ends at the next <section
        end_idx = content.find("<section", idx)
        if end_idx == -1:
            end_idx = content.find("<footer", idx)
            
    if start_idx != -1 and end_idx != -1:
        if content[end_idx:end_idx+10] == "</section>":
            end_idx += len("</section>")
            
        new_content = content[:start_idx] + content[end_idx:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Success! Completely removed the broken scroll section!")
    else:
        print("Error: Could not find section boundaries.")
else:
    print("Error: Could not find the specific text in the file. It might have already been removed, or is named differently.")

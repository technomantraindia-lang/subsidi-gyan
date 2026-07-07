import os
import re

base = r"c:\Users\techn\OneDrive\Desktop\vivek projects (1)\vivek projects\subsidygyaan"
file_path = os.path.join(base, "index.html")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Use regex to find and remove the entire section that contains the broken text "to know which subsidy applies"
# The regex matches from <section to </section> non-greedily, ensuring it contains the unique text snippet.
pattern = r'<section[^>]*>(?:(?!</section>).)*?to know which subsidy applies(?:(?!</section>).)*?</section>'

new_content = re.sub(pattern, '', content, flags=re.IGNORECASE | re.DOTALL)

if new_content != content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success! The broken section has been removed.")
else:
    print("Could not find the broken section. It might have already been removed.")

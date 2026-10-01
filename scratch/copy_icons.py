import os
import shutil

src_dir = r"c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io\images"
dest_dir = r"c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus\static\images"
os.makedirs(dest_dir, exist_ok=True)

dest_img_dir = r"c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus\static\img"

files_to_copy = [
    "icon-logo.png",
    "icon-tech-writing.svg",
    "icon-ux-writing.svg",
    "icon-articles.svg",
    "icon-vector1.svg",
    "icon-languages.svg",
    "icon-recordkeeping.svg",
    "logo.png",
]

for f in files_to_copy:
    src_path = os.path.join(src_dir, f)
    if os.path.exists(src_path):
        shutil.copy2(src_path, os.path.join(dest_dir, f))
        shutil.copy2(src_path, os.path.join(dest_img_dir, f))
        print(f"Copied {f}")

# Copy flags folder too
flags_src = os.path.join(src_dir, "flags")
flags_dest = os.path.join(dest_dir, "flags")
if os.path.exists(flags_src):
    shutil.copytree(flags_src, flags_dest, dirs_exist_ok=True)
    print("Copied flags to static/images/flags")

print("Done copying icons.")

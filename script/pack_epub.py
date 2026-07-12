import zipfile
import os
import sys

# Determine paths automatically based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

epub_dir = os.path.join(root_dir, 'orv_sequel')
books_dir = os.path.join(root_dir, 'books')
output_file = os.path.join(books_dir, '全知读者视角-外传.epub')

# Ensure books directory exists
os.makedirs(books_dir, exist_ok=True)

print(f"Packaging {epub_dir} into {output_file}...")

with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    # 1. Add mimetype MUST BE FIRST AND UNCOMPRESSED
    mimetype_path = os.path.join(epub_dir, 'mimetype')
    if os.path.exists(mimetype_path):
        zf.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
        print("Added mimetype (uncompressed)")
    else:
        print("ERROR: mimetype file not found!")
        sys.exit(1)

    # 2. Add META-INF and OEBPS folders with MAX COMPRESSION
    for folder in ['META-INF', 'OEBPS']:
        folder_path = os.path.join(epub_dir, folder)
        if not os.path.exists(folder_path):
            continue
            
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                filepath = os.path.join(root, file)
                # Calculate relative path inside the zip
                rel_path = os.path.relpath(filepath, epub_dir)
                arcname = rel_path.replace('\\\\', '/')
                
                # Add file to zip
                zf.write(filepath, arcname)

print("EPUB packaging complete!")

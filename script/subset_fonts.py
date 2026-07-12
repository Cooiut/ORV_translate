import os
import re
import sys
import glob
import shutil
import subprocess

# Paths based on the new script location in /script
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

epub_dir = os.path.join(root_dir, 'orv_sequel', 'OEBPS')
source_fonts_dir = os.path.join(root_dir, 'fonts')
target_fonts_dir = os.path.join(epub_dir, 'fonts')

# Ensure target directory exists
os.makedirs(target_fonts_dir, exist_ok=True)

print("1. Scanning all XHTML files for unique characters...")
unique_chars = set()

for root_path, _, files in os.walk(epub_dir):
    for file in files:
        if file.endswith('.xhtml'):
            filepath = os.path.join(root_path, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                # Remove HTML tags
                text_no_tags = re.sub(r'<[^>]+>', '', text)
                unique_chars.update(text_no_tags)

# Add common punctuation and ASCII
common_chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~·×—''""【】…、。，：；？！"
unique_chars.update(common_chars)

text_file = os.path.join(script_dir, "unique_chars.txt")
with open(text_file, 'w', encoding='utf-8') as f:
    f.write(''.join(unique_chars))

print(f"Total unique characters found: {len(unique_chars)}")
print("\n2. Subsetting and compressing fonts to WOFF2...")

# Use the current Python interpreter and find pyftsubset on PATH
python_exe = sys.executable
pyftsubset_exe = shutil.which('pyftsubset')
if not pyftsubset_exe:
    # Fallback: look next to the current python executable
    candidate = os.path.join(os.path.dirname(python_exe), 'pyftsubset.exe')
    if os.path.isfile(candidate):
        pyftsubset_exe = candidate
    else:
        print("ERROR: pyftsubset not found. Install fonttools with: pip install fonttools[woff]")
        sys.exit(1)

font_files = glob.glob(os.path.join(source_fonts_dir, '*.ttf')) + glob.glob(os.path.join(source_fonts_dir, '*.otf'))

if not font_files:
    print(f"WARNING: No font files found in {source_fonts_dir}")

has_error = False

for font_path in font_files:
    filename = os.path.basename(font_path)
    
    # Handle the SourceHanSerif name mismatch if needed
    base_name = os.path.splitext(filename)[0]
    if base_name == "SourceHanSerifSC-Regular":
        base_name = "SourceHanSerif-Regular"
        
    output_filename = base_name + ".woff2"
    output_path = os.path.join(target_fonts_dir, output_filename)
    
    print(f"\nProcessing {filename}...")
    orig_size = os.path.getsize(font_path)
    
    # Run pyftsubset with WOFF2 flavor and optimization flags
    cmd = [
        pyftsubset_exe,
        font_path,
        f"--text-file={text_file}",
        f"--output-file={output_path}",
        "--flavor=woff2",
        "--no-hinting",              # Remove hinting (not needed for e-readers)
        "--desubroutinize",          # Flatten CFF subroutines for better Brotli compression
        "--layout-features=*",       # Preserve all OpenType layout features
    ]
    
    try:
        subprocess.run(cmd, check=True)
        new_size = os.path.getsize(output_path)
        print(f"Subsetting + WOFF2 successful!")
        print(f"Original size: {orig_size / 1024 / 1024:.2f} MB")
        print(f"Subset size:   {new_size / 1024 / 1024:.2f} MB")
    except subprocess.CalledProcessError:
        print(f"Subsetting failed for {filename} (possibly a cmap bug). Attempting fallback: WOFF2 compression without subsetting...")
        
        fallback_cmd = [
            python_exe,
            "-m", "fontTools.ttLib.woff2",
            "compress",
            font_path
        ]
        
        # This will output a .woff2 file in the source directory by default, so we move it to the target directory
        try:
            subprocess.run(fallback_cmd, check=True)
            temp_output = os.path.splitext(font_path)[0] + ".woff2"
            
            if os.path.exists(temp_output):
                # Move and rename to target dir
                if os.path.exists(output_path):
                    os.remove(output_path)
                os.rename(temp_output, output_path)
                new_size = os.path.getsize(output_path)
                print(f"Fallback WOFF2 compression successful!")
                print(f"Original size: {orig_size / 1024 / 1024:.2f} MB")
                print(f"Compressed size: {new_size / 1024 / 1024:.2f} MB")
            else:
                print(f"Failed to find the compressed output for {filename}")
                has_error = True
        except subprocess.CalledProcessError as fallback_e:
            print(f"Fallback compression also failed for {filename}: {fallback_e}")
            has_error = True

# Clean up
if os.path.exists(text_file):
    os.remove(text_file)

if has_error:
    print("\nSome fonts failed to process!")
    sys.exit(1)

print("\nAll fonts processed successfully!")

import os
import re
import zipfile
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

epub_path = os.path.join(root_dir, 'books', 'orv_sequel.epub')
orv_sequel_dir = os.path.join(root_dir, 'orv_sequel')
orv_sequel_eng_dir = os.path.join(root_dir, 'orv_sequel_eng')

def get_chapter_info(content):
    # Returns (actual_number, full_title_string)
    # Search for <h2...>1000...</h2>
    match = re.search(r'<h2[^>]*>\s*([0-9]+)([^<]*)</h2>', content)
    if match:
        actual_num = int(match.group(1))
        sub_title = match.group(2).strip()
        title_str = f"{match.group(1)} {sub_title}" if sub_title else str(match.group(1))
        return actual_num, title_str
    return None, None

def process_for_translation(content, title_str):
    # Standardize the head section to match existing files exactly
    standard_head = f'<head>\n    <link rel="stylesheet" href="style.css" type="text/css" /><title>{title_str}</title></head>'
    content = re.sub(r'<head[^>]*>.*?</head>', standard_head, content, flags=re.DOTALL)
    
    # Remove the comment link:
    content = re.sub(r'<hr/>\s*<p[^>]*><a[^>]*>\[CLICK TO READ CHAPTER COMMENTS\]</a></p>', '', content, flags=re.IGNORECASE)
    
    # Remove endnotes section:
    content = re.sub(r'<hr/>\s*<section epub:type=[\'"]endnotes[\'"][^>]*>.*?</section>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    return remove_empty_lines(content)

def remove_empty_lines(content):
    return '\n'.join([line for line in content.splitlines() if line.strip()])

def main():
    if not os.path.exists(epub_path):
        print(f"EPUB file not found: {epub_path}")
        return

    # 1. Get highest existing local chapter
    local_oebps = os.path.join(orv_sequel_dir, 'OEBPS')
    highest_local_actual = 0
    highest_local_ch_num = 0
    
    local_ch_files = [f for f in os.listdir(local_oebps) if f.startswith('ch_') and f.endswith('.xhtml')]
    for f in local_ch_files:
        filepath = os.path.join(local_oebps, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            actual, _ = get_chapter_info(content)
            if actual is not None:
                if actual > highest_local_actual:
                    highest_local_actual = actual
        
        # Extract X from ch_X.xhtml
        try:
            ch_num = int(f.replace('ch_', '').replace('.xhtml', ''))
            if ch_num > highest_local_ch_num:
                highest_local_ch_num = ch_num
        except ValueError:
            pass

    print(f"Highest local actual chapter: {highest_local_actual}")
    print(f"Highest local filename index: ch_{highest_local_ch_num}.xhtml")
    
    # 2. Open EPUB and find new chapters & images
    with zipfile.ZipFile(epub_path, 'r') as zf:
        epub_files = zf.namelist()
        
        # New images
        epub_images = [f for f in epub_files if f.startswith('OEBPS/images/') and not f.endswith('/')]
        for img_path in epub_images:
            img_filename = os.path.basename(img_path)
            for target_dir in [orv_sequel_dir, orv_sequel_eng_dir]:
                target_img_path = os.path.join(target_dir, 'OEBPS', 'images', img_filename)
                if not os.path.exists(target_img_path):
                    os.makedirs(os.path.dirname(target_img_path), exist_ok=True)
                    with open(target_img_path, 'wb') as img_f:
                        img_f.write(zf.read(img_path))
                    print(f"Extracted new image: {img_filename} to {target_dir}")

        # New chapters
        epub_ch_files = [f for f in epub_files if f.startswith('OEBPS/ch_') and f.endswith('.xhtml')]
        new_chapters = [] # tuple: (epub_path, actual_chapter_number, title_str, content)
        
        for f in epub_ch_files:
            content = zf.read(f).decode('utf-8')
            actual, title = get_chapter_info(content)
            if actual is not None and actual > highest_local_actual:
                new_chapters.append((f, actual, title, content))
        
        new_chapters.sort(key=lambda x: x[1]) # Sort by actual chapter number
        
        if not new_chapters:
            print("No new chapters found.")
        else:
            print(f"Found {len(new_chapters)} new chapters.")
            
            # Write new chapters
            current_local_ch = highest_local_ch_num
            added_chapters = [] # list of dicts with info for OPF/NCX
            
            for epub_f, actual, title, content in new_chapters:
                current_local_ch += 1
                new_filename = f"ch_{current_local_ch}.xhtml"
                added_chapters.append({
                    'filename': new_filename,
                    'title': title
                })
                
                # Write to orv_sequel_eng (raw)
                eng_filepath = os.path.join(orv_sequel_eng_dir, 'OEBPS', new_filename)
                cleaned_raw_content = remove_empty_lines(content)
                with open(eng_filepath, 'w', encoding='utf-8') as file:
                    file.write(cleaned_raw_content)
                print(f"Copied {epub_f} -> orv_sequel_eng/OEBPS/{new_filename} (Raw)")
                
                # Write to orv_sequel (processed)
                processed_content = process_for_translation(content, title)
                seq_filepath = os.path.join(orv_sequel_dir, 'OEBPS', new_filename)
                with open(seq_filepath, 'w', encoding='utf-8') as file:
                    file.write(processed_content)
                print(f"Copied {epub_f} -> orv_sequel/OEBPS/{new_filename} (Processed)")
            
            # Update content.opf and toc.ncx
            for target_dir in [orv_sequel_dir, orv_sequel_eng_dir]:
                opf_path = os.path.join(target_dir, 'OEBPS', 'content.opf')
                ncx_path = os.path.join(target_dir, 'OEBPS', 'toc.ncx')
                
                # Update content.opf
                if os.path.exists(opf_path):
                    with open(opf_path, 'r', encoding='utf-8') as f:
                        opf_content = f.read()
                    
                    manifest_items = []
                    spine_items = []
                    for chap in added_chapters:
                        item_id = chap['filename'].replace('.xhtml', '')
                        manifest_items.append(f'    <item id="{item_id}" href="{chap["filename"]}" media-type="application/xhtml+xml"/>')
                        spine_items.append(f'    <itemref idref="{item_id}"/>')
                    
                    opf_content = re.sub(r'(\s*)</manifest>', '\n' + '\n'.join(manifest_items) + r'\1</manifest>', opf_content)
                    opf_content = re.sub(r'(\s*)</spine>', '\n' + '\n'.join(spine_items) + r'\1</spine>', opf_content)
                    
                    with open(opf_path, 'w', encoding='utf-8') as f:
                        f.write(opf_content)
                    print(f"Updated {opf_path}")
                
                # Update toc.ncx
                if os.path.exists(ncx_path):
                    with open(ncx_path, 'r', encoding='utf-8') as f:
                        ncx_content = f.read()
                    
                    play_order_matches = re.findall(r'playOrder="(\d+)"', ncx_content)
                    max_play_order = max([int(x) for x in play_order_matches]) if play_order_matches else 0
                    
                    nav_points = []
                    for i, chap in enumerate(added_chapters):
                        play_order = max_play_order + 1 + i
                        nav_id = f"ncx_{play_order - 1}"
                        title_text = chap['title']
                        # Create the navPoint snippet
                        nav_point_xml = f"""    <navPoint id="{nav_id}" playOrder="{play_order}">
      <navLabel>
        <text>{title_text}</text>
      </navLabel>
      <content src="{chap['filename']}"/>
    </navPoint>"""
                        nav_points.append(nav_point_xml)
                    
                    ncx_content = re.sub(r'(\s*)</navMap>', '\n' + '\n'.join(nav_points) + r'\1</navMap>', ncx_content)
                    
                    with open(ncx_path, 'w', encoding='utf-8') as f:
                        f.write(ncx_content)
                    print(f"Updated {ncx_path}")

if __name__ == '__main__':
    main()

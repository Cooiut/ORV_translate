# -*- coding: utf-8 -*-
import zipfile
import zlib
import os
import sys
import time
import re
import shutil
import subprocess
from datetime import datetime, timezone
import zopfli.zlib

# Determine paths automatically based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

epub_dir = os.path.join(root_dir, 'orv_sequel')
books_dir = os.path.join(root_dir, 'books')
output_file = os.path.join(books_dir, 'orv_sequel_chn.epub')


def get_git_tag():
    """Retrieve Git tag from environment variables or git describe."""
    tag = os.environ.get('GITHUB_REF_NAME') or os.environ.get('EPUB_TAG')
    if tag:
        return tag.strip()

    try:
        res = subprocess.run(
            ['git', 'describe', '--tags', '--exact-match'],
            cwd=root_dir,
            capture_output=True,
            text=True
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass

    return None


def parse_tag_status(tag):
    """Parse tag status segment into reader-friendly Chinese string."""
    pattern = r'^v([0-9]+)-([0-9]+)-([a-zA-Z0-9]+)-([0-9]{8})$'
    match = re.match(pattern, tag)
    if not match:
        return None

    status_raw = match.group(3)
    if status_raw == 'draft':
        # "未精校版本"
        return '\u672a\u7cbe\u6821\u7248\u672c'

    proof_match = re.match(r'^proof(read)?([0-9]+)$', status_raw)
    if proof_match:
        ch_num = proof_match.group(2)
        # "精校至第{ch_num}章"
        return f'\u7cbe\u6821\u81f3\u7b2c{ch_num}\u7ae0'

    return status_raw


# Enforce Git Tag requirement
tag = get_git_tag()
if not tag:
    print("ERROR: Cannot get a valid Git tag!")
    print("Packaging requires a clean git tag (e.g. 'v553-1029-proof7-20260714') or environment variable GITHUB_REF_NAME / EPUB_TAG.")
    sys.exit(1)

status_text = parse_tag_status(tag)
if not status_text:
    print(f"ERROR: Invalid tag format '{tag}'.")
    print("Tag must match format 'v[start]-[end]-[status]-[date]' (e.g. 'v553-1029-proof7-20260714').")
    sys.exit(1)

# File extensions that are already compressed — store without re-compression
STORED_EXTENSIONS = {'.ttf', '.otf', '.woff2', '.woff', '.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp3', '.mp4'}

# Ensure books directory exists
os.makedirs(books_dir, exist_ok=True)

print(f"Detected Git Tag: {tag}")
print(f"Packaging {epub_dir} into {output_file}...")


class _ZopfliCompressor:
    """Drop-in replacement for zlib.compressobj that uses zopfli for better DEFLATE."""

    def __init__(self, *args, **kwargs):
        self._chunks = []

    def compress(self, data):
        self._chunks.append(data)
        return b''

    def flush(self, *args):
        data = b''.join(self._chunks)
        if not data:
            return b''
        compressed = zopfli.zlib.compress(data)
        # Strip 2-byte zlib header and 4-byte adler32 checksum to get raw deflate
        return compressed[2:-4]


# Monkey-patch zlib.compressobj globally for the entire zip writing session
_original_compressobj = zlib.compressobj
zlib.compressobj = lambda *a, **kw: _ZopfliCompressor()

utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

try:
    with zipfile.ZipFile(output_file, 'w') as zf:
        # 1. Add mimetype MUST BE FIRST AND UNCOMPRESSED (EPUB spec requirement)
        mimetype_path = os.path.join(epub_dir, 'mimetype')
        if os.path.exists(mimetype_path):
            zf.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
            print("Added mimetype (uncompressed)")
        else:
            print("ERROR: mimetype file not found!")
            sys.exit(1)

        # 2. Add META-INF and OEBPS folders
        file_count = 0
        stored_count = 0
        compressed_count = 0

        for folder in ['META-INF', 'OEBPS']:
            folder_path = os.path.join(epub_dir, folder)
            if not os.path.exists(folder_path):
                continue

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, epub_dir).replace('\\', '/')

                    ext = os.path.splitext(file)[1].lower()

                    if arcname == 'OEBPS/content.opf':
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Update dcterms:modified timestamp
                        content = re.sub(
                            r'<meta\s+property="dcterms:modified">.*?</meta>',
                            f'<meta property="dcterms:modified">{utc_now}</meta>',
                            content
                        )

                        # Update dc:title with Chinese status: "全知读者视角 [外传]（{status_text}）"
                        new_title = f'\u5168\u77e5\u8bfb\u8005\u89c6\u89d2 [\u5916\u4f20]\uff08{status_text}\uff09'
                        content = re.sub(
                            r'<dc:title\s+id="title">.*?</dc:title>',
                            f'<dc:title id="title">{new_title}</dc:title>',
                            content
                        )

                        zf.writestr(arcname, content.encode('utf-8'), compress_type=zipfile.ZIP_DEFLATED)
                        compressed_count += 1
                        print(f"Dynamically updated metadata in {arcname}: modified={utc_now}")
                    elif ext in STORED_EXTENSIONS:
                        # Pre-compressed formats: store as-is
                        zf.write(filepath, arcname, compress_type=zipfile.ZIP_STORED)
                        stored_count += 1
                    else:
                        # Text / XML / CSS files: compress with zopfli (via monkey-patch)
                        zf.write(filepath, arcname, compress_type=zipfile.ZIP_DEFLATED)
                        compressed_count += 1

                    file_count += 1
finally:
    zlib.compressobj = _original_compressobj

print(f"\nAdded {file_count} files ({compressed_count} zopfli-compressed, {stored_count} stored as-is)")

if os.environ.get('GITHUB_REF_NAME'):
    named_output = os.path.join(books_dir, f'orv_sequel_chn_{tag}.epub')
    shutil.copyfile(output_file, named_output)
    print(f"Created named release copy: {named_output}")

final_size = os.path.getsize(output_file)
print(f"EPUB size: {final_size / 1024 / 1024:.2f} MB")
print("EPUB packaging complete!")



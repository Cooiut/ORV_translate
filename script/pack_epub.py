import zipfile
import zlib
import os
import sys
import time
import zopfli.zlib

# Determine paths automatically based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

epub_dir = os.path.join(root_dir, 'orv_sequel')
books_dir = os.path.join(root_dir, 'books')
output_file = os.path.join(books_dir, 'orv_sequel_chn.epub')

# File extensions that are already compressed — store without re-compression
STORED_EXTENSIONS = {'ttf','otf','.woff2', '.woff', '.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp3', '.mp4'}

# Ensure books directory exists
os.makedirs(books_dir, exist_ok=True)

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
                    if ext in STORED_EXTENSIONS:
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

final_size = os.path.getsize(output_file)
print(f"EPUB size: {final_size / 1024 / 1024:.2f} MB")
print("EPUB packaging complete!")

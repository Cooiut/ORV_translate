import os
import sys
import shutil

# Resolve paths based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
epub_file = os.path.join(root_dir, 'books', 'orv_sequel_chn.epub')

# Check that Java is available
java_exe = shutil.which('java')
if not java_exe:
    print("ERROR: Java not found in PATH.")
    print("EPUBCheck requires Java Runtime Environment (JRE).")
    print("Please install Java or add it to PATH, e.g.:")
    print('  $env:PATH += ";C:\\Program Files\\Java\\jre1.8.0_491\\bin"')
    sys.exit(1)

if not os.path.exists(epub_file):
    print(f"ERROR: EPUB file not found: {epub_file}")
    sys.exit(1)

print(f"Running EPUBCheck on: {os.path.basename(epub_file)}")
print(f"Using Java: {java_exe}\n")

try:
    from epubcheck import EpubCheck
except ImportError:
    print("ERROR: epubcheck package not installed. Install with: pip install epubcheck")
    sys.exit(1)

# Run EPUBCheck (autorun=True by default)
result = EpubCheck(epub_file)

# Categorize messages
errors = [m for m in result.messages if m.level == 'ERROR']
warnings = [m for m in result.messages if m.level == 'WARNING']
fatals = [m for m in result.messages if m.level == 'FATAL']
infos = [m for m in result.messages if m.level not in ('ERROR', 'WARNING', 'FATAL')]

# Print results
if fatals:
    print(f"FATAL ({len(fatals)}):")
    for m in fatals:
        print(f"  {m.message}")

if errors:
    print(f"ERRORS ({len(errors)}):")
    for m in errors:
        print(f"  {m.message}")

if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for m in warnings[:20]:  # Limit output to avoid flood
        print(f"  {m.message}")
    if len(warnings) > 20:
        print(f"  ... and {len(warnings) - 20} more warnings")

if infos:
    print(f"INFO ({len(infos)}):")
    for m in infos[:10]:
        print(f"  {m.message}")
    if len(infos) > 10:
        print(f"  ... and {len(infos) - 10} more info messages")

# Summary
print(f"\n{'='*50}")
if result.valid:
    print("EPUBCheck PASSED - EPUB is valid!")
else:
    print("EPUBCheck FAILED - EPUB has validation errors.")
    print(f"  Fatal: {len(fatals)}, Errors: {len(errors)}, Warnings: {len(warnings)}")
    sys.exit(1)

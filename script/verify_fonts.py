import os
import sys
import glob
from fontTools.ttLib import TTFont

# Resolve paths based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
font_dir = os.path.join(root_dir, 'orv_sequel', 'OEBPS', 'fonts')

# Random sample of core characters from ORV
sample_chars = "金独子刘众赫韩秀英星流系统鬼怪■，。？！『』「」aA1"
sample_codepoints = [ord(c) for c in sample_chars]

print(f"--- 字体子集化严谨验证 ---")
print(f"抽样验证字符: {sample_chars}\n")

# Auto-discover all fonts instead of hardcoding
font_files = sorted(glob.glob(os.path.join(font_dir, '*.ttf')) + glob.glob(os.path.join(font_dir, '*.otf')))

if not font_files:
    print(f"ERROR: No font files found in {font_dir}")
    sys.exit(1)

has_missing = False

for font_path in font_files:
    font_name = os.path.basename(font_path)
    print(f"--> Verifying: {font_name}...")

    # Load the font
    font = TTFont(font_path)

    # Extract all supported unicode codepoints from the cmap tables
    supported_codepoints = set()
    for table in font['cmap'].tables:
        if table.isUnicode():
            supported_codepoints.update(table.cmap.keys())

    print(f"  当前字体内部包含的实际字符总数: {len(supported_codepoints)}")

    # Check for missing characters
    missing = []
    for c, cp in zip(sample_chars, sample_codepoints):
        if cp not in supported_codepoints:
            missing.append(c)

    if missing:
        print(f"  [警告] 缺失以下字符: {''.join(missing)}")
        has_missing = True
    else:
        print("  [成功] 所有抽样测试字符 100% 存在于字库中！")
    print("-" * 40)

    font.close()

if has_missing:
    print("\nWARNING: Some fonts are missing required characters (may be expected for display fonts).")

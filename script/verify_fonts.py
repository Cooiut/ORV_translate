from fontTools.ttLib import TTFont
import os

# Target WOFF2 fonts
font_dir = os.path.join('orv_sequel', 'OEBPS', 'fonts')
fonts = [
    'LXGWWenKai-Regular.woff2', 
    'SmileySans-Oblique.woff2', 
    'SourceHanSerif-Regular.woff2'
]

# Random sample of core characters from ORV
sample_chars = "金独子刘众赫韩秀英星流系统鬼怪■，。？！『』「」aA1"
sample_codepoints = [ord(c) for c in sample_chars]

print(f"--- 字体子集化严谨验证 ---")
print(f"抽样验证字符: {sample_chars}\n")

for font_name in fonts:
    font_path = os.path.join(font_dir, font_name)
    if not os.path.exists(font_path):
        print(f"找不到字体文件: {font_name}")
        continue
        
    print(f"--> Verifying: {font_name}...")
    # Load the woff2 font
    font = TTFont(font_path)
    
    # Extract all supported unicode codepoints from the cmap tables
    supported_codepoints = set()
    for table in font['cmap'].tables:
        if table.isUnicode():
            supported_codepoints.update(table.cmap.keys())
            
    print(f"  当前 WOFF2 字体内部包含的实际字符总数: {len(supported_codepoints)}")
    
    # Check for missing characters
    missing = []
    for c, cp in zip(sample_chars, sample_codepoints):
        if cp not in supported_codepoints:
            missing.append(c)
            
    if missing:
        print(f"  [警告] 缺失以下字符: {''.join(missing)}")
    else:
        print("  [成功] 所有抽样测试字符 100% 存在于字库中！")
    print("-" * 40)

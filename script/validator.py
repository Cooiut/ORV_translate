import os
import sys
import xml.etree.ElementTree as ET
import zipfile

# Resolve paths based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)


def validate_xml_file(filepath):
    try:
        # Some HTML files might have entities that strict XML parser doesn't like.
        # But we'll try strict XML parsing for opf and ncx.
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # quick workaround for html entities if they fail
        try:
            ET.fromstring(content)
        except ET.ParseError as e:
            if "&" in content:
                # very crude entity replacement to allow basic XML validation of tags
                content = content.replace("&nbsp;", "&#160;").replace("&hellip;", "&#8230;")
                ET.fromstring(content)
            else:
                raise e
        return True, "Valid XML"
    except Exception as e:
        return False, str(e)


def check_orv_sequel(directory):
    print("Checking orv_sequel files...")
    files_to_check = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.xml', '.opf', '.ncx', '.xhtml', '.html')):
                files_to_check.append(os.path.join(root, file))

    errors = []
    for f in files_to_check:
        is_valid, msg = validate_xml_file(f)
        if not is_valid:
            errors.append(f"{os.path.basename(f)}: {msg}")

    if not errors:
        print(f"All {len(files_to_check)} XML/OPF/NCX files in {directory} are valid well-formed XML.")
    else:
        print(f"Found {len(errors)} files with issues:")
        for err in errors:
            print("  - " + err)

    return len(errors)


def check_epub_file(filepath):
    print(f"\nChecking EPUB file: {filepath}")
    errors = 0

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return 1

    if not zipfile.is_zipfile(filepath):
        print("Error: The EPUB file is not a valid zip archive.")
        return 1

    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            bad_file = z.testzip()
            if bad_file:
                print(f"Error: Corrupted file inside EPUB: {bad_file}")
                errors += 1
            else:
                print("The EPUB file is a valid zip archive without corruption.")

            # Check mimetype
            try:
                mimetype = z.read('mimetype').decode('utf-8').strip()
                if mimetype == 'application/epub+zip':
                    print("mimetype file is correct ('application/epub+zip').")
                else:
                    print(f"Error: Incorrect mimetype: {mimetype}")
                    errors += 1
            except KeyError:
                print("Error: Missing 'mimetype' file.")
                errors += 1

            # Check META-INF/container.xml
            try:
                container = z.read('META-INF/container.xml')
                print("Found META-INF/container.xml.")
            except KeyError:
                print("Error: Missing 'META-INF/container.xml'.")
                errors += 1

    except Exception as e:
        print(f"Error reading EPUB: {e}")
        errors += 1

    return errors


if __name__ == '__main__':
    orv_sequel_dir = os.path.join(root_dir, "orv_sequel")
    epub_file = os.path.join(root_dir, "books", "全知读者视角-外传.epub")

    xml_errors = check_orv_sequel(orv_sequel_dir)
    epub_errors = check_epub_file(epub_file)

    total_errors = xml_errors + epub_errors
    if total_errors > 0:
        print(f"\nValidation completed with {total_errors} error(s).")
        sys.exit(1)
    else:
        print("\nAll validations passed!")

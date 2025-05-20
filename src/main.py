import sys

from site_functions import copy_contents, generate_pages_recursive

def main():
    if len(sys.argv) > 2:
        print("Usage: python main.py [template_path]")
        sys.exit(1)
    elif len(sys.argv) == 1:
        base_path = "/"
    else:
        base_path = sys.argv[1]
    

    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", base_path)

main()
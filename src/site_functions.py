import os, shutil

from block_functions import *

def copy_contents(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    file_list = (os.listdir(src))
    for entry in file_list:
        path = os.path.join(src, entry)
        # print(os.path.isfile(path))
        if os.path.isfile(path):
           shutil.copy(path, dest)
        else:
            copy_contents(path, os.path.join(dest, entry))

def extract_title(markdown):
    # print("Extracting title from markdown")
    lines = markdown.split("\n")
    for line in lines:
        # print(line)
        if line.startswith("# "):
            # print("Header found")
            return line[2:]
    raise ValueError("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    from_file = open(from_path, "r")
    template_file = open(template_path, "r")
    from_contents = from_file.read()
    template_contents = template_file.read()
    html = template_contents.replace("{{ Title }}", extract_title(from_contents))
    html = html.replace("{{ Content }}", markdown_to_html_node(from_contents).to_html())
    from_file.close()
    template_file.close()
    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(html)
    to_file.close()

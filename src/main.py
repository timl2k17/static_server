from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from inline_functions import *
from block_functions import *
from site_functions import *

def main():
    copy_contents("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()
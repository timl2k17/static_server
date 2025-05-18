from textnode import *
from htmlnode import HTMLNode

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip() != "":
            new_blocks.append(block.strip())
    return new_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    # block_type = []
    for block in blocks:
        # print(block)
        block_type = block_to_block_type(block)
        # print(block_type)
        if block_type == BlockType.P:
            test = HTMLNode("p", block, None)
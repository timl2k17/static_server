import re

from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_functions import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip() != "":
            new_blocks.append(block.strip())
    return new_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_type = []
    parent_node = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.P:
            text = block.replace("\n", " ")
            children = text_to_children(text)
            p_node = ParentNode("p", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H1:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h1", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H2:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h2", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H3:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h3", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H4:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h4", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H5:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h5", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.H6:
            content = block.lstrip('#').strip()  # remove '-' and leading/trailing spaces
            children = text_to_children(content)
            p_node = ParentNode("h6", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.CODE:
            code_node = LeafNode("code", block.strip('```\n') + '\n', None)
            pre_node = ParentNode("pre", [code_node])
            parent_node.children.append(pre_node)
        elif block_type == BlockType.QUOTE:
            blocks = block.split("\n")
            content = []
            for b in blocks:
                content.append(b.lstrip('>').strip())
            content = "\n".join(content)
            children = text_to_children(content)
            p_node = ParentNode("blockquote", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.UL:
            blocks = block.split("\n")
            children = []
            for b in blocks:
                if b.strip():  # skip empty lines
                    content = b.lstrip('-').strip()  # remove '-' and leading/trailing spaces
                    li_children = text_to_children(content)
                    children.append(ParentNode("li", li_children))
            p_node = ParentNode("ul", children)
            parent_node.children.append(p_node)
        elif block_type == BlockType.OL:
            blocks = block.split("\n")
            children = []
            for b in blocks:
                if b.strip():  # skip empty lines
                    content = re.sub(r"^\d+\.\s*", "", b).strip()
                    li_children = text_to_children(content)
                    children.append(ParentNode("li", li_children))
            p_node = ParentNode("ol", children)
            parent_node.children.append(p_node)
    return parent_node    

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children
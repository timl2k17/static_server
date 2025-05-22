import re

from htmlnode import LeafNode
from textnode import TextType, TextNode

# create LeafNodes from markdown textnodes
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})  

 # create a list of textnodes from markdown string
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            text = node.text.split(delimiter)
            for i in range(len(text)):
                if i == 0 or i == len(text) - 1:
                    new_nodes.append(TextNode(text[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(text[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text) # find ![alt text](url) in text

def extract_markdown_links(text):
    return re.findall(r'\[(.*?)\]\((.*?)\)', text) # find [link text](url) in text

def split_nodes_image(old_nodes): #??
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            text = extract_markdown_images(node.text) # list of tuples (alt, url)
            current_text = node.text
            if  text is None:
                return old_nodes
            for item in text:
                alt, url = item
                split_text = current_text.split(f'![{alt}]({url})', 1)  # split on current image
                if split_text[0] != "":    
                    new_nodes.append(TextNode(split_text[0], TextType.NORMAL))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                current_text = split_text[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.NORMAL))
        else:
           new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            text = extract_markdown_links(node.text) # list of tuples (link text, url)
            current_text = node.text
            if text is None:                               
                return old_nodes
            for item in text:
                txt, url = item
                split_text = current_text.split(f'[{txt}]({url})', 1)  # split on current link
                if split_text[0] != "":    
                    new_nodes.append(TextNode(split_text[0], TextType.NORMAL))
                new_nodes.append(TextNode(txt, TextType.LINK, url))
                current_text = split_text[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.NORMAL))
        else:
            new_nodes.append(node)
    return new_nodes

# convert markdown text to textnodes
def text_to_textnodes(text):
    initial_node = [TextNode(text, TextType.NORMAL)]
    first_string = split_nodes_delimiter(initial_node, "**", TextType.BOLD)
    second_string = split_nodes_delimiter(first_string, "_", TextType.ITALIC)
    third_string = split_nodes_delimiter(second_string, "`", TextType.CODE)
    fourth_string = split_nodes_image(third_string)
    fifth_string = split_nodes_link(fourth_string)
    return fifth_string


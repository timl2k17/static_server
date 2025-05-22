from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None): # text = text content of node, text_type = type of text (bold, italic, etc.), url = url of link or image
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type.value}, {self.url})'
    
class BlockType(Enum):
    P = "paragraph"
    H1 = "heading1"
    H2 = "heading2"
    H3 = "heading3"
    H4 = "heading4"
    H5 = "heading5"
    H6 = "heading6"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def block_to_block_type(block):
    if block.startswith("# "):
        return BlockType.H1
    elif block.startswith("## "):
        return BlockType.H2
    elif block.startswith("### "):
        return BlockType.H3
    elif block.startswith("#### "):
        return BlockType.H4
    elif block.startswith("##### "):
        return BlockType.H5
    elif block.startswith("###### "):
        return BlockType.H6
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith("> "):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UL
    elif block[0].isdigit() and block[1] == ".":  # replace with regex
        return BlockType.OL
    else:
        return BlockType.P
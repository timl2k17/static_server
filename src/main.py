from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from functions import *

def main():
    test = TextNode("Test", TextType.NORMAL)
    # print(test)
    test = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(test)
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    # print(parent_node.to_html())
    node = TextNode("This is text with a `code block`", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes)
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extract_markdown_images(text)
    node = TextNode(
        "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
        TextType.NORMAL,
    )
    # print("split_nodes_link below")
    # print(split_nodes_link([node]))
    text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    
    
main()
from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

def main():
    test = TextNode("Test", TextType.NORMAL)
    print(test)
    test = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test)
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

main()
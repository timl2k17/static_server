from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    test = TextNode("Test", TextType.NORMAL)
    print(test)
    test = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test)
main()
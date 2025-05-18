import unittest

from textnode import TextNode, TextType
from functions import *

class TestFunctions(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "This is a text node"})
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})
    def test_snd(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
        TextNode("This is text with a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)
    def test_snd2(self):
        node = TextNode("This is text with a `code block`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
        TextNode("This is text with a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode("", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with an [link](https://www.example.com)"
    )
        self.assertListEqual([("link", "https://www.example.com")], matches)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        ) 
    def test_split_images2(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )    
    def test_split_links(self):
        node = TextNode(
            "This is a [link](https://www.example.com) and another [second link](https://www.google.com)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second link", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )
    def test_split_images3(self):
            node = TextNode(
                "![image1](https://i.imgur.com/zjjcJKZ.png)![image2](https://i.imgur.com/3elNhQu.png)",
                TextType.NORMAL,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],
                new_nodes,
            )
    def test_split_images_no_images(self):
            node = TextNode("This is just text", TextType.NORMAL)
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is just text", TextType.NORMAL),
                ],
                new_nodes,
            )

    def test_text_to_textnodes(self):
        text = "This is text with a ![image](https://i.imgur.com/zjjcJKZ.png)."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(".", TextType.NORMAL),
            ],
            nodes,
        )
       
if __name__ == "__main__":
    unittest.main()
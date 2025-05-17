import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        hnode = HTMLNode("div", "This is a div", None, {"class": "test"})
        self.assertEqual(hnode.props_to_html(), ' class="test"')
    def test_prop2(self):
        hnode = HTMLNode("div", "This is a div", None, {"class": "test", "id": "test"})
        self.assertEqual(hnode.props_to_html(), ' class="test" id="test"')
    def test_prop3(self):
        hnode = HTMLNode("div", "This is a div", None, None)
        self.assertEqual(hnode.props_to_html(), "")
    def test_to_html(self):
        hnode = HTMLNode("div", "This is a div", None, {"class": "test"})
        with self.assertRaises(NotImplementedError):
            test = hnode.to_html()
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a text node")
        self.assertEqual(node.to_html(), "This is a text node")
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
if __name__ == "__main__":
    unittest.main()
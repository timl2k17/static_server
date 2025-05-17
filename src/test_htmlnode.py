import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        hnode = HTMLNode("div", "This is a div", None, {"class": "test"})
        test = hnode.props_to_html()
        expected = ' class="test"'
        self.assertEqual(test, expected)
    def test_prop2(self):
        hnode = HTMLNode("div", "This is a div", None, {"class": "test", "id": "test"})
        test = hnode.props_to_html()
        expected = ' class="test" id="test"'
        self.assertEqual(test, expected)
    def test_prop3(self):
        hnode = HTMLNode("div", "This is a div", None, None)
        test = hnode.props_to_html()
        expected = ""
        self.assertEqual(test, expected)
if __name__ == "__main__":
    unittest.main()
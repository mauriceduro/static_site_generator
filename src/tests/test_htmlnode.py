import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_equal(self):
        node = HTMLNode("p", "This is the value.", [], {"href":"https//youtube.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https//youtube.com\" target=\"_blank\"")

    def test_props_to_html_not_equal(self):
        node = HTMLNode("p", "This is the value.", [], {"href":"https//youtube.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), " href=\"https//google.com\" target=\"_blank\"")

    def test_props_to_html_is_none(self):
        node = HTMLNode("p", "This is the value.")
        self.assertEqual(node.props_to_html(), "") 

if __name__ == "__main__":
    unittest.main()
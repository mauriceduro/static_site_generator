import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        result = "<p>Hello, World!</p>"
        self.assertEqual(node.to_html(), result)
     
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, World!", {"href":"https//youtube.com", "target": "_blank"})
        result = "<a href=\"https//youtube.com\" target=\"_blank\">Hello, World!</a>"
        self.assertEqual(node.to_html(), result)
        
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, World!")
        result = "<b>Hello, World!</b>"
        self.assertEqual(node.to_html(), result)

if __name__ == "__main__":
    unittest.main()
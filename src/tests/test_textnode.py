import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("This is a test node", TextType.TEXT)
        node2 = TextNode("This is a test node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = TextNode("This is a test node", TextType.TEXT)
        node2 = TextNode("This is a different node", TextType.TEXT)
        self.assertNotEqual(node, node2)
 
    def test_url_different(self):
        node = TextNode("This is a link node", TextType.LINK, "http://myfakeurl.com/testImage")
        node2 = TextNode("This is a link node", TextType.LINK, None)
        self.assertNotEqual(node, node2)

    def test_text_type_different(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a link node", TextType.IMAGE)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
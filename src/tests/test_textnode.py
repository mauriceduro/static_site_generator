import unittest
from textnode import *
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

class TestTextToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node.", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node.")

    def test_bold(self):
        node = TextNode("This is a bold node.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node.")
        
    def test_italic(self):
        node = TextNode("This is a italic node.", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a italic node.")
        
    def test_code(self):
        node = TextNode("This is a code node.", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node.")
        
    def test_link(self):
        node = TextNode(None, TextType.LINK, "https://www.youtube.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, None) 
        self.assertEqual(html_node.props, {"href":"https://www.youtube.com"})
        
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.youtube.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, None) 
        self.assertEqual(html_node.props, {"src":"https://www.youtube.com", "alt":"This is an image node"})

if __name__ == "__main__":
    unittest.main()
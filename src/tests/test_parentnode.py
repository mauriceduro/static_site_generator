import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, lambda: parent_node.to_html())

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("b", "great grandchild")
        grandchild_node = ParentNode("p", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><p><b>great grandchild</b></p></span></div>",
        )

    def test_to_html_with_multi_layer_grandchildren(self):
        layer_1_great_grandchild_node = LeafNode("a", "layer 1 great grandchild", {"href":"https://youtube.com"})
        layer_1_grandchild_node = ParentNode("p", [layer_1_great_grandchild_node])
        layer_2_great_grandchild_node = LeafNode("b", "layer 2 great grandchild")
        layer_2_grandchild_node = ParentNode("p", [layer_2_great_grandchild_node])
        child_node = ParentNode("span", [layer_1_grandchild_node, layer_2_grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><p><a href=\"https://youtube.com\">layer 1 great grandchild</a></p><p><b>layer 2 great grandchild</b></p></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
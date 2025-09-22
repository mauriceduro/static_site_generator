from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        
        if not self.children:
            raise ValueError
        
        children_string = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
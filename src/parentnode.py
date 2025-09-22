from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: No tag set")
        
        if self.children is None:
            raise ValueError("Invalid HTML: No children set")
        
        children_string = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
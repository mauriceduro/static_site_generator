from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

    def to_html(self):
        if not self.value:
            raise ValueError
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
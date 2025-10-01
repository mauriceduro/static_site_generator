from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target) -> bool:
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url
    
    def __repr__(self) -> str:
        return f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', None, {"src":text_node.url, "alt":text_node.text})

    raise Exception("Error: Invalid text type")
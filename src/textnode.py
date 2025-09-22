from enum import Enum
from htmlnode import HTMLNode
class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
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


def text_node_to_html(text_node: TextNode) -> HTMLNode:
    pass
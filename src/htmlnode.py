class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        props_string = ""
        for key, value in self.props.items():
            props_string += f" {key}=\"{value}\""

        return props_string
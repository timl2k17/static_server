from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # tag of the node (e.g. "div", "p", "h1")
        self.value = value  # value of the node (e.g. text content)
        self.children = children  # list of child HTMLnodes
        self.props = props   # dicionary of properties (e.g. {"class": "my-class", "id": "my-id"})

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        string = ""
        if self.props is None:
            return string
        for prop, value in self.props.items():
            string += f' {prop}="{value}"'  # e.g. href="http://example.com"
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. 
# For example, a simple <p> tag with some text inside of it:
# <p>This is a paragraph</p>
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props
        self.children = None

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value  # just return raw text
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" #  e.g. <a href="http://example.com">Link</a>
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

# ParentNode Handles nesting of HTML nodes
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props
        self.value = None

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        html_start = f"<{self.tag}{self.props_to_html()}>"
        html_end = f"</{self.tag}>"
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"{html_start}{children_html}{html_end}"

      
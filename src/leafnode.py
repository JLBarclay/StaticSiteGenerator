from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All Leaf Nodes must have a value")
        if self.tag == None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"{self.tag}:(\n  Value: {self.value},\n  Props: {self.props}\n)"
    
    def __eq__(self, comparison):
        return self.tag == comparison.tag and self.value == comparison.value and self.props == comparison.props
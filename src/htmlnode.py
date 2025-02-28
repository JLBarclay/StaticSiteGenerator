

class HTMLNode:
    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be implemented by a subclass")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"{self.tag}:(\n  Value: {self.value},\n  Children: {self.children},\n  Props: {self.props}\n)"
    
    def __eq__(self, comparison):
        return self.tag == comparison.tag and self.value == comparison.value and self.children == comparison.children and self.props == comparison.props
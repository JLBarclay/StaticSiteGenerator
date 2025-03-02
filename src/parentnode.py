from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All Parent Nodes must have a tag")
        if self.children is None:
            raise ValueError("All Parent Nodes must have children")
        if self.props == None:
            return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

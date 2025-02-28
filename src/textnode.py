from enum import Enum

class TextType(Enum):
    NORMAL = 'Normal'
    BOLD = 'Bold'
    ITALIC = 'Italic'
    CODE = 'Code'
    ANCHOR = 'Anchor'
    IMAGE = 'Image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, comparison):
        return self.text == comparison.text and self.text_type == comparison.text_type and self.url == comparison.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
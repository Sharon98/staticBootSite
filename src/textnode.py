from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    IMAGE  = "image"
    TEXT   = "text"
    LINK   = "link"

class TextNode:
    def __init__(self, content, text_type, url=None):
        self.text = content
        self.text_type = text_type
        self.url = url

    def __eq__(self, node2): 
        if self.text == node2.text:
            if self.text_type == node2.text_type:
                if self.url == node2.url:
                    return True
        return False
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"        
           

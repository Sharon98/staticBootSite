class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, node2): 
        # if self.tag == node2.tag:    
        if self.value == node2.value:
            if self.props == node2.props:
                if self.children == node2.children:
                    # if self.tag == None and node2.tag == None:
                    #    return True
                    if self.tag == node2.tag:
                        return True
        return False

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        prop_string = " " + (" ").join(list(map(lambda k: f'{k}="{self.props[k]}"',self.props.keys())))
        # print(prop_string)
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"        
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None,children=None, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tags are required")
        if self.children == None:
            raise ValueError("Children are required")
        # return f"<{self.tag}{self.props_to_html()}>{list(map(lambda node: node.children.to_html(),self.children))}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.children.to_html()}</{self.tag}>"
            
            
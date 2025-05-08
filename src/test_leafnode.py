import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")    

    def test_link_eq(self):
        node  = LeafNode("a","link to site",{"href":"http://saturn.com"})
        # node2 = LeafNode("a","link to site",None,"http://saturn.com")
        # print("***: " + node.to_html())
        self.assertEqual(node.to_html(), '<a href="http://saturn.com">link to site</a>')

    def test_para_eq(self):
        node  = LeafNode("p","happy para",None)
        # node2 = LeafNode("p","happy para",None,None)
        self.assertEqual(node.to_html(),'<p>happy para</p>')
    
    def test_props_eq(self):
        node  = LeafNode("a","happy",{"href": "https://www.google.com","target": "_blank"})
        # node2 = LeafNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        # print(node)
        # print(node2)
        self.assertEqual(node.to_html(),'<a href="https://www.google.com" target="_blank">happy</a>')
    '''
    def test_props_link(self):
        node  = LeafNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        node2 = LeafNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        temp  = node.props_to_html()
        temp2 = node2.props_to_html()
        # print(temp)
        # print(temp2)
        self.assertEqual(temp, temp2) 
        '''
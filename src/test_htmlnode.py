import unittest
from textnode import TextType
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_link_eq(self):
        node  = HTMLNode("a","link to site",None,"http://saturn.com")
        node2 = HTMLNode("a","link to site",None,"http://saturn.com")
        self.assertEqual(node, node2)

    def test_para_eq(self):
        node  = HTMLNode("p","happy para",None,None)
        node2 = HTMLNode("p","happy para",None,None)
        self.assertEqual(node, node2)
    def test_props_eq(self):
        node  = HTMLNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        # print(node)
        # print(node2)
        self.assertEqual(node, node2)
    def test_props_link(self):
        node  = HTMLNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode("a","happy",None,{"href": "https://www.google.com","target": "_blank"})
        temp  = node.props_to_html()
        temp2 = node2.props_to_html()
        # print(temp)
        # print(temp2)
        self.assertEqual(temp, temp2)    
    def test_h1_eq(self):
        node  = HTMLNode("h1","happy para",None,None)
        node2 = HTMLNode("h1","happy para",None,None)
        self.assertEqual(node, node2)        
    def test_raw_eq(self):
        node  = HTMLNode(None,"happy para",None,None)
        node2 = HTMLNode(None,"happy para",None,None)
        self.assertEqual(node, node2)           
    def test_nested_eq(self):
        node  = HTMLNode("div",None,[("a","happy",None,{"href": "https://www.google.com","target": "_blank"}), ("a","link to site",None,"http://saturn.com")],None)
        node2 = HTMLNode("div",None,[("a","happy",None,{"href": "https://www.google.com","target": "_blank"}), ("a","link to site",None,"http://saturn.com")],None)
        self.assertEqual(node, node2)             
    def test_nested_neq(self):
        node  = HTMLNode("div",None,[("a","happy",None,{"href": "https://www.google.com","target": "parent"}), ("a","link to site",None,"http://saturn.com")],None)
        node2 = HTMLNode("div",None,[("a","happy",None,{"href": "https://www.google.com","target": "_blank"}), ("a","link to site",None,"http://saturn.com")],None)
        self.assertNotEqual(node, node2)                     
    # def test_neqType(self):
    #     node = HTMLNode("This is a text node", TextType.BOLD)
    #     node2 = HTMLNode("This is a text node", TextType.ITALIC)
    #     self.assertNotEqual(node, node2)
    # def test_urlCheck(self):
    #     node = HTMLNode("This is a text node", TextType.BOLD,"http:/yahoo.com")
    #     node2 = HTMLNode("This is a text node",TextType.BOLD,"http:/yahoo.com")
    #     self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
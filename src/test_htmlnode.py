import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        childNode = HTMLNode("div", "This is a child node")
        node = HTMLNode("div", "This is a text node", children=[childNode], props={'class': 'header'})
        node2 = HTMLNode("div", "This is a text node", children=[childNode], props={'class': 'header'})
        self.assertEqual(node, node2)

    def test_neq(self):
        childNode = HTMLNode("div", "This is a child node")
        node = HTMLNode("div", "This is a text node", children=[childNode], props={'class': 'header'})
        node2 = HTMLNode("div", "This is a different text node", children=[childNode], props={'class': 'header'})
        self.assertNotEqual(node, node2)
    
    def test_to_html(self):
        node = HTMLNode("div", "This is a text node")

        with self.assertRaises(NotImplementedError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), 'This method should be implemented by a subclass')


if __name__ == "__main__":
    unittest.main()


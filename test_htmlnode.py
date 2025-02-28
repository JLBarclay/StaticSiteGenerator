import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node")
        node2 = HTMLNode("div", "This is a text node")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()


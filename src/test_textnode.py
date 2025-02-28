import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_empty_text_node(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_string_representation(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode(This is a text node, Bold, None)")

    def test_string_representation_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(str(node), "TextNode(This is a text node, Italic, None)")

if __name__ == "__main__":
    unittest.main()
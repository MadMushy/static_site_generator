import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://google.com", "target": "_blank"},
        )
        # Compare actual output to expected value
        self.assertEqual(
            node.props_to_html(),
            'href="https://google.com"target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello", props={})
        self.assertEqual(
            node.props_to_html(),
            ""
        )

    def test_repr(self):
        node = HTMLNode(tag="p", value="Test", props={"class": "textbold"})
        output = repr(node)
        self.assertIn("HTMLTag = 'p'", output)
        self.assertIn("Value = 'Test'", output)
        self.assertIn("Props = {'class': 'textbold'}", output)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<a href=https://www.google.com>Click me!</a>")

    def test_leaf_to_html_none(self):
        node = LeafNode("p")
        self.assertRaises(ValueError)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

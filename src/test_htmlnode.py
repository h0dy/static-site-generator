import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html

class TestHTMLNode(unittest.TestCase):
  
  def test_eq(self):
    node_h2 = HTMLNode(tag="h2", value="check out our new featured products!")
    node_a = HTMLNode(tag="a", value="read more", props={"href": "https://hody.dev","target": "_blank"})
    node_a2 = HTMLNode(tag="a", value="read more", props={"href": "https://google.com","target": "_blank"})
    node_p = HTMLNode(tag="p", value="to know more about us", children=[node_a])
    node_div = HTMLNode(tag="div", children=[node_h2, node_p])
    node_div2 = HTMLNode(tag="div", children=[node_h2, node_p])

    self.assertNotEqual(node_a, node_a2)

    self.assertEqual(node_div, node_div2)
    self.assertIn(node_h2, node_div.children)
    self.assertIsInstance(node_a.props_to_html(), str)
    
  def test_leaf(self):
    leaf_p = LeafNode(tag="p", value="hello world")
    leaf_a = LeafNode(tag="a", value="my website", props={"href":"https://hody.dev"})
    leaf_a2 = LeafNode(tag="a", value="my website", props={"href":"https://google.com"})
    
    self.assertEqual(leaf_p.to_html(), "<p>hello world</p>")
    self.assertEqual(leaf_a.to_html(), '<a href="https://hody.dev">my website</a>')
    self.assertNotEqual(leaf_a.to_html(), leaf_a2.to_html())
    
  def test_leaf_err(self):
    with self.assertRaises(ValueError):
      LeafNode(tag="div", value=None).to_html()
  
  def test_parent_with_children(self):
    leaf_node = LeafNode(tag="i", value="hello")
    leaf_node2 = LeafNode(tag="span", value="world")
    parent_node = ParentNode(tag="div", children=[leaf_node, leaf_node2])
    
    
    self.assertEqual(parent_node.to_html(), "<div><i>hello</i><span>world</span></div>")
  
  
  def test_parent_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    grandchild_node2 = LeafNode("a", "grandchild", props={"href":"https://google.com", "target": "_blank"})
    child_node = ParentNode("span", [grandchild_node, grandchild_node2])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b><a href=\"https://google.com\" target=\"_blank\">grandchild</a></span></div>",
    )
  
  
  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html(node)
    
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
    
    node2 = TextNode("My website", TextType.LINK, url="https://hody.dev")
    html_node2 = text_node_to_html(node2)
    self.assertEqual(html_node2.tag, "a")
    self.assertEqual(html_node2.value, "My website")
    self.assertEqual(html_node2.props, {"href": node2.url})
  

if __name__ == "__main__":
  unittest.main()
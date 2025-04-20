import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link ,text_to_textnodes

class TestInlineMarkdown(unittest.TestCase):
  
  def test_single_code_block(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ]
    self.assertEqual(new_nodes, expected)

  def test_single_bold_phrase(self):
    node = TextNode("Hello **world**!", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected = [
      TextNode("Hello ", TextType.TEXT),
      TextNode("world", TextType.BOLD),
      TextNode("!", TextType.TEXT),
    ]
    self.assertEqual(new_nodes, expected)

  def test_multiple_bold_phrases(self):
    node = TextNode("**Hello** and **goodbye**", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected = [
      TextNode("Hello", TextType.BOLD),
      TextNode(" and ", TextType.TEXT),
      TextNode("goodbye", TextType.BOLD),
    ]
    self.assertEqual(new_nodes, expected)

  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
  
  def test_extract_markdown_links(self):
    matches = extract_markdown_links(
      "This is my website [hody](https://hody.dev)"
    )
    self.assertListEqual([("hody", "https://hody.dev")], matches)

  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),
        TextNode(
            "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
        ),
      ],
      new_nodes,
    )
    
    node2 = TextNode(
      "This is a kitty ![kitty](https://upload.wikimedia.org/wikipedia/commons/c/cd/Stray_kitten_Rambo002.jpg)",
      TextType.TEXT,
    )
    new_nodes2 = split_nodes_image([node2])
    self.assertListEqual(
      [
        TextNode("This is a kitty ", TextType.TEXT),
        TextNode("kitty", TextType.IMAGE, "https://upload.wikimedia.org/wikipedia/commons/c/cd/Stray_kitten_Rambo002.jpg"),
      ],
      new_nodes2,
    )
  
  
  def test_split_links(self):
    node = TextNode(
      "Hi, im full stack web developer and here is my website [hody](https://hody.dev) and my github [github](https://github.com/h0dy)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("Hi, im full stack web developer and here is my website ", TextType.TEXT),
        TextNode("hody", TextType.LINK, "https://hody.dev"),
        TextNode(" and my github ", TextType.TEXT),
        TextNode(
            "github", TextType.LINK, "https://github.com/h0dy"
        ),
      ],
      new_nodes,
    )
    
    node2 = TextNode(
      "no links here :)",
      TextType.TEXT,
    )
    new_nodes2 = split_nodes_link([node2])
    self.assertListEqual(
      [
        TextNode("no links here :)", TextType.TEXT),
      ],
      new_nodes2,
    )
    
  def test_text_to_textnodes(self):
    nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
    self.assertListEqual([TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev")], nodes)
  
if __name__ == "__main__":
  unittest.main()
from enum import Enum
from htmlnode import LeafNode, HTMLNode


class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url
  
  def __eq__(self, value):
    if not isinstance(value, TextNode):
      return False
    return (
        self.text == value.text and
        self.text_type == value.text_type and
        self.url == value.url
    )
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.name}, {self.url})"


def text_node_to_html(text_node):
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(tag=None, value=text_node.text)
    
    case TextType.BOLD:
      return LeafNode(tag="b", value=text_node.text)
    
    case TextType.ITALIC:
      return LeafNode(tag="i", value=text_node.text)
    
    case TextType.CODE:
      return LeafNode(tag="code", value=text_node.text)
    
    case TextType.LINK:
      return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    case TextType.IMAGE:
      return LeafNode(tag="a", value="", props={"src": text_node.url, "alt":text_node.text})
    case _:
      raise Exception("not a text type ")


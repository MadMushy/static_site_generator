class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotimplementedError("to_html method")

    def props_to_html(self):
        if not self.props:
            return ""

        return "".join(f'{key}="{value}"' for key,value in self.props.items())

    def __repr__(self):
        return f"HTMLTag = {self.tag!r}, Value = {self.value!r}, Children = {self.children!r}, Props = {self.props!r}"


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return f"{self.value}"

        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        props_str = self.props_to_htmls()
        return f"<{self.tag} {props_str}>{self.value}!</{self.tag}>"


    def props_to_htmls(self):
        if not self.props:
            return ""

        return "".join(f'{key}=https://www.{value}' for key,value in self.props.items())
          

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode needs a tag dont be a bitch and add one.")

        if not self.children:
            raise ValueError("ParentNode needs a child to be fufilled... dont we all")

        props_str = self.props_to_html()
        child_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_str}>{child_html}</{self.tag}>"
        



from textnode import *

def main():

    node_1 = TextNode("Hello World", TextType.TEXT)
    node_2 = TextNode("Click Me", TextType.LINK, url = "example.com")

    print(node_1)
    print(node_2)


if __name__ == "__main__":
    main()

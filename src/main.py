from textnode import TextNode, TextType

def main():
    node = TextNode("I am some random text.", TextType.TEXT)
    print(node)

if __name__ == "__main__":
    main()
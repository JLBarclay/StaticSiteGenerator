from textnode import TextNode, TextType

def main():
    test = TextNode('Hello', TextType.NORMAL_TEXT, 'https://www.google.com')
    print(test)


if __name__ == '__main__':
    main()

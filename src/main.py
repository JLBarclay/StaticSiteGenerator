from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    test = TextNode('Hello', TextType.NORMAL, 'https://www.google.com')
    test2 = HTMLNode('h1', 'Hello', ['test'], {'class': 'header'})
    print(test)
    print(test2)


if __name__ == '__main__':
    main()

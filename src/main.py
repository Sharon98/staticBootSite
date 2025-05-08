import textnode
#./main.sh

def main():
    a_node = textnode.TextNode("Hello World", textnode.TextType.BOLD, None)
    print(a_node)

if __name__ == "__main__":
    main()

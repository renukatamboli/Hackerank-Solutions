# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->",attr[0],">",attr[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n = input()
for i in range(0,int(n)):
    parser.feed(input())

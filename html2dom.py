#! /usr/bin/env python3
# -*- coding: utf_8 -*-


from html.parser import HTMLParser
from xml.dom.minidom import getDOMImplementation


class Html2dom(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__impl = getDOMImplementation()
        self.__document = self.__impl.createDocument(None, None, None)
        self.__elements = []

    def handle_starttag(self, tag, attrs):
        element = self.__document.createElement(tag)

        for attr in attrs:
            element.setAttribute(attr[0], attr[1])

        self.__elements.append(element)

    def handle_endtag(self, tag):
        element = self.__elements.pop()
        self.__elements[-1].appendChild(element)

    def handle_data(self, data):
        if(len(self.__elements) > 0):
            textnode = self.__document.createTextNode(data)
            self.__elements[-1].appendChild(textnode)

    def handle_comment(self, data):
        if(len(self.__elements) > 0):
            comment = self.__document.createComment(data)
            self.__elements[-1].appendChild(comment)

    def __append_all(self):
        while len(self.__elements) > 1:
            element = self.__elements.pop()
            self.__elements[-1].appendChild(element)

    def parse(self, data):
        self.feed(data)
        self.close()

        self.__append_all()

        return self.__elements.pop()


if __name__ == '__main__':
    pass


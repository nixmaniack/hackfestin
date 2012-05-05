#!/usr/bin/env python

import urllib
from xml.dom import minidom

def getMeFeeds():
    webxml = urllib.urlopen("http://www.phoronix.com/rss.php")
    xmldoc=minidom.parse(webxml)
    linksdata = xmldoc.getElementsByTagName("link")
    for ele in linksdata:
        print ele.firstChild.data

if __name__ == "__main__":
    getMeFeeds()

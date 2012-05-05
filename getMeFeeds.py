#!/usr/bin/env python

import urllib
from xml.dom import minidom

def getMeFeeds():
    webxml = urllib.urlopen("http://www.phoronix.com/rss.php")
    xmldoc=minidom.parse(webxml)
    linksdata = xmldoc.getElementsByTagName("link")
    titlesdata = xmldoc.getElementsByTagName("title")
    for i in xrange(linksdata.length):
        print linksdata[i].firstChild.data
        print titlesdata[i].firstChild.data

if __name__ == "__main__":
    getMeFeeds()

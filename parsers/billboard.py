import urllib2
import HTMLParser
import sys
import re

url = {
    "hp"  : "http://www.billboard.com/charts/r-b-hip-hop-songs",
    "alt" : "http://www.billboard.com/charts/alternative-songs",
    "top" : "http://www.billboard.com/charts/hot-100",
}[sys.argv[1]]

#get page
req = urllib2.urlopen(url)
the_page = req.read()

the_page = unicode(the_page, 'utf-8')

#unescape html special chars
h = HTMLParser.HTMLParser()
the_page = h.unescape(the_page)

#find songs
p = re.compile('row-title.*?h2>(.*?)</h2>.*?<h3>(.*?)</h3>', re.IGNORECASE | re.DOTALL)
res = p.findall(the_page)

#print songs
p = re.compile("\S*\*+\S*\s*")
p2 = re.compile("<.*?>")
for x in res:
    title = p.sub("", p2.sub("", x[0])).strip()
    artist = p.sub("", p2.sub("", x[1])).strip()
    artist = re.sub("feat.*", "", artist, flags=re.IGNORECASE)
    print(title + " " + artist)
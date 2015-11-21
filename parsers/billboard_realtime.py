import urllib2
import HTMLParser
import sys
import re

url = {
    "tr140" : "http://realtime.billboard.com/",
    "24h"   : "http://realtime.billboard.com/",
    "emrg"  : "http://realtime.billboard.com/",
}[sys.argv[1]]

#get page
req = urllib2.urlopen(url)
the_page = req.read()

the_page = unicode(the_page, 'utf-8')

#unescape html special chars
h = HTMLParser.HTMLParser()
the_page = h.unescape(the_page)

p = re.compile('<table.*?table>', re.IGNORECASE | re.DOTALL)
res = p.findall(the_page)

if (sys.argv[1] == "tr140"):
    the_page = res[1]
elif (sys.argv[1] == "24h"):
    the_page = res[2]
elif (sys.argv[1] == "emrg"):
    the_page = res[0]

#find songs
#p = re.compile('<tr> row-title.*?h2>(.*?)</h2>.*?<h3>(.*?)</h3>', re.IGNORECASE | re.DOTALL)
p = re.compile('<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.IGNORECASE | re.DOTALL)
res = p.findall(the_page)

#print songs
p = re.compile("\S*\*+\S*\s*")
p2 = re.compile("<.*?>")
for x in res:
    title = p.sub("", p2.sub("", x[2].split('\n', 1)[0]) ).strip()
    artist = p.sub("", p2.sub("", x[1].split('\n', 1)[0]) ).strip()
    artist = re.sub("feat.*", "", artist, flags=re.IGNORECASE)
    print((title + " " + artist).encode('utf-8'))
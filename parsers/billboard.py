import urllib2
import HTMLParser

req = urllib2.Request('http://www.billboard.com/charts/r-b-hip-hop-songs')
response = urllib2.urlopen(req)
the_page = response.read()

import re
p = re.compile('row-title.*?h2>\s+(.*?)\s+?</h2.*?<a.*?>\s+(.*?)\s+?</a', re.IGNORECASE | re.DOTALL)
res = p.findall(the_page)

p = re.compile("\S*\*+\S*\s*")
for x in res:
    title = p.sub("", x[0])
    artist = p.sub("", x[1])
    artist = re.sub("feat.*", "", artist, flags=re.IGNORECASE)
    print(title + " " + artist)
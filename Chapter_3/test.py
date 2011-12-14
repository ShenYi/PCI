feedlist = [line for line in open('feedlist.txt')]
import feedparser
out = open('1.txt','w')
for feedurl in feedlist:
    print("test:"+feedurl+"\n")
    d = feedparser.parse(feedurl)
    if hasattr(d.feed,'title'):
        out.write(feedurl+'\n')
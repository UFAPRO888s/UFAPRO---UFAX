# -*- coding: utf-8 -*-
import requests
import urllib.request
import json
import markdown
from datetime import datetime
now = datetime.now() # current date and time

url = 'https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Vk&u=public203323312&hide_reposts=on&format=Json'
req = urllib.request.Request(url)
date_time = now.strftime("%Y-%m-%d")
print("date and time:",date_time)
##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r)
counter = 0
patt = "\
--- \n\
layout: post \n\
--- \n\
"
##parcing json
for item in cont['items']:
    counter += 1
    print("Title:", item['author']['name'], "\Content_html:", item['content_html'])
    print("----")   
    with open("./_posts/"+date_time+"-"+str(item['_rssbridge']['post_id'])+".mdx", 'w') as f:
        f.write(patt+"\n\n"+item['content_html'])
        f.close() 


print("Number of titles: ", counter)

# with open("some_file.txt", "r", encoding="utf-8") as input_file:
#     text = input_file.read()
# html = markdown.markdown(text)
# with open("some_file.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
#     output_file.write(html)
# -*- coding: utf-8 -*-
import requests
import urllib.request
import json

url = 'https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Vk&u=public203323312&hide_reposts=on&format=Json'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r)
counter = 0

##parcing json
for item in cont['items']:
    counter += 1
    print("Title:", item['author'], "\nComments:", item['content_html'])
    print("----")

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
print("Number of titles: ", counter)

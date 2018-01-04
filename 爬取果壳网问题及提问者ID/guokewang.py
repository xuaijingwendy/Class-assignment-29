# -*- coding:utf-8 -*-
import urllib
import urllib2
import re




user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
for i in range (1,4):
    url = 'https://www.guokr.com/ask/hottest/?page'+str(i)+'.html'
    print url
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content_pattern = re.compile('<h2><a target="_blank" href=(.*?)</a></h2>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item.replace('https://www.guokr.com/question/', '').replace('>','').replace('"','')




    input = raw_input()
    if input == "":
        print "-------------"
        continue
    
    elif input=="Q":
        break

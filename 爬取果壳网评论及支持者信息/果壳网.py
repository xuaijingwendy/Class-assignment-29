# -*- coding:utf-8 -*-
import urllib
import urllib2
import re




user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
url = 'https://www.guokr.com/question/646324/'
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content_pattern = re.compile('<div class="answer-txt answerTxt gbbcode-content">(.*?)</div>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item.replace('<p>', '').replace('</p>', '').replace('<br>','')


content_pattern_d= re.compile('<div class="answer-diggers diggers" data-id="854273">(.*?)</div>', re.S)
content_d = re.findall(content_pattern_d, html)
for item in content_d:
    print item.replace('<span>', '').replace('</span>', '')

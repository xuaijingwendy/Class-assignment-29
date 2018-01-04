#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib,urllib2;



def getHtml(url):
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36Query String Parametersview sourceview URL encoded'
    headers = {'User-Agent': user_agent}
    request=urllib2.Request(url,headers=headers);
    page = urllib2.urlopen(request);
    html = page.read()
    return html



def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        print imgurl;
        urllib.urlretrieve('D:/maj','wb')
        x = x + 1


html = getHtml("http://www.lofter.com/like?act=qbdashboardlike_20121221_01")
getImg(html)

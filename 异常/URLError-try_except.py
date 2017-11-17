import urllib2
 
requset = urllib2.Request('http://www.baidu.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

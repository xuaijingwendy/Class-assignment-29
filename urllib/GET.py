Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values={}
>>> values['username']="2018933125@qq.com"
>>> values['password']="1....."
>>> data=urllib.urlencode(ralues)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data=urllib.urlencode(ralues)
NameError: name 'ralues' is not defined
>>> data=urllib.urlencode(values)
>>> url="http://passport.csdn.net/account/login"
>>> geturl=url+"?"+data
>>> request=urllib2.Requeset(geturl)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    request=urllib2.Requeset(geturl)
AttributeError: 'module' object has no attribute 'Requeset'
>>> request=urllib2.Requset(geturl)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    request=urllib2.Requset(geturl)
AttributeError: 'module' object has no attribute 'Requset'
>>> request=urllib2.Request(geturl)
>>> response=urllib2.urlopen(request)
>>> print response.geturl()
http://passport.csdn.net/account/login?username=2018933125%40qq.com&password=15251356767xaj
>>> 

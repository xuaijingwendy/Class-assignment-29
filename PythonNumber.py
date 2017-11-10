Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var='1'
>>> print type(var)
<type 'str'>
>>> a=int(var)+1
>>> print a
2
>>> var='abc'
>>> var=1
>>> page_name=1
>>> print "ตฺ",page_name,"าณ"
ตฺ 1 าณ
>>> var='abc
SyntaxError: EOL while scanning string literal
>>> var='abc'
>>> print type(var)
<type 'str'>
>>> import random
>>> random.Random
<class 'random.Random'>
>>> random.choice("['a','b','c']")
']'
>>> random.choice("['a','b','c']")
'a'
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
']'
>>> random.choice("['a','b','c']")
"'"
>>> 
KeyboardInterrupt
>>> random.choice("['a','b','c']")
"'"
>>> test_list = ['a','b','c']
>>> random.choice(test_list)
'b'
>>> random.choice(test_list)
'b'
>>>  random.choice("['a','b','c']")
 
  File "<pyshell#22>", line 2
    random.choice("['a','b','c']")
    ^
IndentationError: unexpected indent
>>> random.choice("['a','b','c']")
','
>>> random.choice("['a','b','c']")
'c'
>>> 

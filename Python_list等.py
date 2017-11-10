Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=['physics','chemistry',1997,2000];
>>> list1[0]
'physics'
>>> list1[3]
2000
>>> list1[0:1]
['physics']
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[1:3]
['chemistry', 1997]
>>> list[1:2]

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list[1:2]
TypeError: 'type' object has no attribute '__getitem__'
>>> list1[1:2]
['chemistry']
>>> list2=[1,2,3,4,5];
>>> list1+list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1=[1,2]
>>> list1*2
[1, 2, 1, 2]
>>> list*2

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list*2
TypeError: unsupported operand type(s) for *: 'type' and 'int'
>>> list2*2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> 
>>> 
>>> 3 in [1,2,3,4]
True
>>> if 3 in [1,2,3,4]
SyntaxError: invalid syntax
>>> if 3 in [1,2,3,4]:
	print "OK"

OK
>>> list =[]
>>> list.a("15")

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list.a("15")
AttributeError: 'list' object has no attribute 'a'
>>> list.append("15")
>>> list
['15']
>>> list=['physics','chemistry',1997,2000];
>>> list[3]
2000
>>> list[3]=1998
>>> list
['physics', 'chemistry', 1997, 1998]
>>> del list[2]
>>> list
['physics', 'chemistry', 1998]
>>> list1
[1, 2]
>>> list2
[1, 2, 3, 4, 5]
>>> cmp(list1,list2)
-1
>>> list1,list2=[123,'xyz'],[456,'abc']
>>> cmp(list1,list2)
-1
>>> list1[789,'www']

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    list1[789,'www']
TypeError: list indices must be integers, not tuple
>>> list1[789,'zzz']

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list1[789,'zzz']
TypeError: list indices must be integers, not tuple
>>> list1=[789,'www']
>>> cmp(list1,list2)
1
>>> len(list1)
2
>>> list1=[1,2,3,4]
>>> len(list1)
4
>>> t1=(1,2,3,4)
>>> list(t1)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list(t1)
TypeError: 'list' object is not callable
>>> aTuple=(123,'xyz','zara','abc')
>>> aList=list(aTuple)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    aList=list(aTuple)
TypeError: 'list' object is not callable
>>> list2
[456, 'abc']
>>> list1
[1, 2, 3, 4]
>>> list1.reverse()
>>> list1
[4, 3, 2, 1]
>>> 





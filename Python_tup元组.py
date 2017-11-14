Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=('physics', 'chemistry', 1997, 2000);
>>> tup2 = (1, 2, 3, 4, 5 );
>>> tup3 = "a", "b", "c", "d";
>>> tup1=()
>>> 



>>> print tup1
()
>>> tup1=('physics', 'chemistry', 1997, 2000);
>>> print tup1
('physics', 'chemistry', 1997, 2000)
>>> print "tup1[0]:",tup[0]
tup1[0]:

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print "tup1[0]:",tup[0]
NameError: name 'tup' is not defined
>>> print tup1[0]
physics
>>> print "tup1[0]: ", tup1[0]
tup1[0]:  physics
>>> print "tup2[1:4]",tup2[1:4]
tup2[1:4] (2, 3, 4)
>>> 
>>> 
>>> 
>>> tup4=tup1+tup2;
>>> print tup4;
('physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5)
>>> 
>>> 
>>> 
>>> 
>>> print tup1
('physics', 'chemistry', 1997, 2000)
>>> del tup1
>>> print "After deleting tup:"
After deleting tup:
>>> print tup

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print tup
NameError: name 'tup' is not defined
>>> len(tup2)
5
>>> ('Hi!')*4
'Hi!Hi!Hi!Hi!'

>>> if 3 in tup2:
	print "Y"

Y
>>> for x in (1,2,3):
	print x;

1
2
3
>>> 
>>> 
>>> 
>>> a=('spam', 'Spam', 'SPAM!')
>>> a[2]
'SPAM!'
>>> a[-1]
'SPAM!'
>>> a[1:]
('Spam', 'SPAM!')
>>> a[0:]
('spam', 'Spam', 'SPAM!')
>>> 
>>> 
>>> print 'abc','xyz',18+6.6j;
abc xyz (18+6.6j)
>>> x,y=1,2
>>> print x,y
1 2
>>> b=(1,2,3,4,0,55)
>>> print max(b)
55
>>> print len(b)
6
>>> tup=("all",)
>>> print tup
('all',)
>>> 

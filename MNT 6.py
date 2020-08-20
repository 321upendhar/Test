Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> a=5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> a=6
>>> b=type(a)
>>> a=6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b
6
>>> k=float(b)
>>> k
6.0
>>> k=7
>>> c=complex(b,k)
>>> c
(6+7j)
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> b>k
False
>>> b<k
True
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(False)
0
>>> lst[23,34,45,78,89]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    lst[23,34,45,78,89]
NameError: name 'lst' is not defined
>>> lst=[23,45,56,67,78]
>>> lst
[23, 45, 56, 67, 78]
>>> tuple=(11,33,22,44,66)
>>> tuple
(11, 33, 22, 44, 66)
>>> set={545,678,543,234,678}
>>> set
{545, 234, 678, 543}
>>> set=(22,23,45,67,89)
>>> set
(22, 23, 45, 67, 89)
>>> str="uppi"
>>> str
'uppi'
>>> str=('uppi')
>>> str
'uppi'
>>> str=['uppi']
>>> str
['uppi']
>>> str='uppi'
>>> str
'uppi'
>>> st=a
>>> \
  type(st)
<class 'int'>
>>> type(st)
<class 'int'>
>>> type(str)
<class 'str'>
>>> range(0,10)
range(0, 10)
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,11,2))
[2, 4, 6, 8, 10]
>>> type(range(10))
<class 'range'>
>>> st='a'
>>> 	st = 'a'
	
SyntaxError: unexpected indent
>>> st = 'a'
>>> \
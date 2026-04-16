Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1=()
>>> t3=(1,2,3,4,"leela",5.7,8)
>>> t4=(1,2,3,4)
>>> t5=('a','b','c','d')
>>> print(t4[2])
3
>>> t4.index(3)
2
>>> for i in t4:
...     print(i)
... 
...     
1
2
3
4
>>> t2=(1,)
>>> print(type(t2))
<class 'tuple'>
>>> print(length(t4))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(length(t4))
NameError: name 'length' is not defined
>>> print(len(t4))
4
>>> print(max(t4))
4
>>> print(min(t4))
1
>>> t6=t4+t5
>>> print(t6)
(1, 2, 3, 4, 'a', 'b', 'c', 'd')

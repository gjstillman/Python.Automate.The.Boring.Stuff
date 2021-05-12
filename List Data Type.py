Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> 
>>> 
>>> --list a value that containts values begins and ends with []
SyntaxError: invalid syntax
>>> -- items in a list are separated by commas
SyntaxError: invalid syntax
>>> 
>>> 
>>> #
>>> 
>>> [cat, bat, rat, elephant]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    [cat, bat, rat, elephant]
NameError: name 'cat' is not defined
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> 
>>> spam
['cat', 'bat', 'rat', 'elephant']
>>> # to access an item in a list you use an index number for the items position in the list
>>> # index begins and ends with []
>>> spam[0]
'cat'
>>> # frist item is a zero not 1
>>> spam[3]
'elephant'
>>> # LISTS OF LISTS can use multiple index
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0,0]\

	   
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    spam[0,0]\
TypeError: list indices must be integers or slices, not tuple
>>> spam[0,1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    spam[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> spam[0][1]
'bat'
>>> #index can count from the end, going backwards using negative values
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> # lists can be called into concatenate strings
>>> 'The ' + spam[-1] +
SyntaxError: invalid syntax
>>> 'The ' + spam[-1] + 'is afraid of the ' + spam[-3] + '.'
'The elephantis afraid of the bat.'
>>> 
#INDEX GETS A SINGLE VALUE
>>> # A SLICE CAN GET MULTIPLE VALUES FROM A LIST
>>> spam[1:3]
['bat', 'rat']
>>> #slice returns from and including the first index position, up to but not including the second value
>>> # spam = ['cat', 'bat', 'rat', 'elephant']
>>> # spam[1:3] slice returns bat because it is 2nd and up to but not including elephant which is index 3
>>> # a slice is a brand new list
>>> spam = [10, 20, 30, 40, 50]
>>> # UPDATING VALUES IN THE LIST
>>> spam[1] = 'Hello'
>>> spam
[10, 'Hello', 30, 40, 50]
>>> # Can update multiple items with SLICE
>>> spam[1:3] = ['CAT', 'DOG']
>>> spam
[10, 'CAT', 'DOG', 40, 50]
>>> spam[1:3]
['CAT', 'DOG']
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> # SHORTCUTS CAN EXCLUDE THE # before or after the :
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
>>> #DEL to DELETE items from a LIST
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> # DEL can be thought of as an UNASSIGNMENT statement
>>> # LEN can be used with a LIST
>>> len(spam)
3
>>> # Can concatenate LISTS together
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> # Can replicate LISTS with *
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> # LIST() function converts object into string
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> # IN and NOT IN operators to search for something in a LIST
>>> 'howdy' in ['hello','hi','heyo']
False
>>> 'howdy' in ['hello','hi','heyo','howdy']
True
>>> 'howdy' not in ['hello','hi','heyo']
True
>>> 

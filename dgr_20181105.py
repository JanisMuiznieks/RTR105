Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = '123'
>>> str3 = str3 + 1

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3 = str3 + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> print(name)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> name = input('Enter:')
Enter: John

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'John' is not defined
>>> name = input('Enter:')
Enter: int(John)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'John' is not defined
>>> name = input int('Enter:')
SyntaxError: invalid syntax
>>> name = input('Enter:')
Enter:Janis

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Janis' is not defined
>>> apple = input('Enter:')
Enter:100
>>> x=apple-10
>>> print(x)
90
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> name=input('Enter:')
Enter:Nils

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Nils' is not defined
>>> name = input ('Enter:')
Enter:Janis

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name = input ('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Janis' is not defined
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x-1]
>>> print(w)
n
>>> zot = 'abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> fruit = 'banana'
>>> print =(len(fruit))
SyntaxError: invalid syntax
>>> print(len(fruit))
6
>>> fruit = 'banana'
>>> x = (len(fruit))
>>> print(x)
6
>>> fruit = 'banana'
>>> index = 0
>>> 	while index < len(fruit):
		
  File "<pyshell#38>", line 1
    while index < len(fruit):
    ^
IndentationError: unexpected indent
>>> fruit = 'banana'
>>> for letter in fruit
SyntaxError: invalid syntax
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> fruit = 'AGNETA'
>>> for letter in fruit:
	print(letter)

	
A
G
N
E
T
A
>>> darzenis = 'NIUSIS'
>>> for letter in darzenis:
	print(letter)

	
N
I
U
S
I
S
>>> index = 0
>>> while index < len(fruit)
SyntaxError: invalid syntax
>>> while index < len(fruit):
	letter = fruit[index]
	print (letter)
	index = index - 1

	
A
A
T
E
N
G
A

Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> fruit = 'banana'
>>> index = 0while index < len(fruit):
	letter = fruit[index]
	print (letter)
	index = index - 1
	
SyntaxError: invalid syntax
>>> fruit = 'banana'index = while index < len(fruit):
	
SyntaxError: invalid syntax
>>> fruit = 'banana'
>>> index =while index < len(fruit):
	letter = fruit[index]
	print (letter)
	index = index - 1
	
SyntaxError: invalid syntax
>>> fruit = 'banana'
>>> index = while index < len(fruit):
	letter = fruit[index]
	print (letter)
	index = index - 1
	
SyntaxError: invalid syntax
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print (letter)
	index = index - 1

	
b
a
n
a
n
a
b

Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
	   count = count + 1
    print(count)
    
  File "<pyshell#75>", line 4
    print(count)
               ^
IndentationError: unindent does not match any outer indentation level
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
	   count = count + 1
print(count)
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
	   count = count + 1
     print(count)
     
  File "<pyshell#79>", line 4
    print(count)
               ^
IndentationError: unindent does not match any outer indentation level
>>> for letter in 'banana':
	print(letter)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[2:])
nty Python
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> a= 'Hello'
>>> b = a + 'There'
>>> print(b)
HelloThere
>>> c = a + '' + 'There'
>>> print(c)
HelloThere
>>> c = a + ' ' + 'There'
>>> print(c)
Hello There
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nana' in fruit
True
>>> if 'a' in fruit:
    print('Found it')

    
Found it
>>> if word == 'banana':
    print('All right bananas.')

    
All right bananas.
>>> 
>>> if word == 'banana':
    print('All right, bananas.')

    
All right, bananas.
>>> if word < 'banana':
	print( 'Your word,' + word + ',comes after banana.')
    elif word > 'banana':
	    
  File "<pyshell#114>", line 3
    elif word > 'banana':
                        ^
IndentationError: unindent does not match any outer indentation level
>>> if word < 'banana':
	print( 'Your word,' + word + ',comes after banana.')
    elif word > 'banana' :
	    
  File "<pyshell#115>", line 3
    elif word > 'banana' :
                         ^
IndentationError: unindent does not match any outer indentation level
>>> if word < 'banana':
	print( 'Your word,' + word + ',comes after banana.')
  elif word > 'banana':
	  
  File "<pyshell#116>", line 3
    elif word > 'banana':
                        ^
IndentationError: unindent does not match any outer indentation level
>>> greet = 'Hello John'
>>> zap = greet.lower()
>>> print(greet)
Hello John
>>> zap = greet.lower()
>>> print(greet)
Hello John
>>> print(zap)
hello john
>>> print('Hi There'.lower)
<built-in method lower of str object at 0xb6eda5a0>
>>> print('Hi There'.lower())
hi there
>>> stuff = 'Hello world'
>>> type(stuff)
<type 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob','John')
>>> print(nstr)
Hello John
>>> nstr = greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> greet = ' Hello Bob '
>>> greet.lstrip()
'Hello Bob '
>>> greet.rstrip()
' Hello Bob'
>>> greet.strip
<built-in method strip of str object at 0xb6edace0>
>>> greet.strip()
'Hello Bob'
>>> line = 'Please have a nice day'
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
>>> line.startswith('P')
True
>>> 

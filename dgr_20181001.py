Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __buil

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __buil
NameError: name '__buil' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 20
>>> a
20
>>> b = 1.56
>>> b
1.56
>>> b*b
2.4336
>>> c =`A`

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c =`A`
NameError: name 'A' is not defined
>>> c = `A`

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c = `A`
NameError: name 'A' is not defined
>>> c = 'A'
>>> vars()
{'a': 20, 'c': 'A', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> a
20
>>> A

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> 

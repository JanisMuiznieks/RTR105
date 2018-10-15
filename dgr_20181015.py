Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10;
SyntaxError: invalid syntax
>>> if x < 10:
	print('smaller')
	if x > 20:
		print('Bigger')

		
smaller
>>> x < 10
True
>>> x > 10
False
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bigger')
	print('Done with 2')

	
Bigger than 2
Still bigger
Done with 2
>>> for i in range(5)
SyntaxError: invalid syntax
>>> print(i)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> if i > 2:
	print('Bigger than 2')
	print('Done with i',i)
	print('All Done')

	

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    if i > 2:
NameError: name 'i' is not defined
>>> for i in range(5)
SyntaxError: invalid syntax
>>> x = 5
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print('Bigger')
		print('Finish')

		
Smaller
>>> 
>>> x > 2
True
>>> x < 2
False
>>> x > 2 < 6
True
>>> x < 4 >2
False
>>> 2 < x > 6
False
>>> 

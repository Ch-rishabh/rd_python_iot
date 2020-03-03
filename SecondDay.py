'''


New Question

Take input of 2 strings

Print true if they're anagrams, otherwise false.

Google anagrams if you don't know about them.



















'''

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.2
>>> type(a)
<class 'float'>
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a = true
NameError: name 'true' is not defined
>>> a = "true"
>>> type(a)
<class 'str'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> #I18N - Internationalization
>>> a = "राम "
>>> a
'राम '
>>> a.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae '
>>> b = "hello"
>>> b
'hello'
>>> a = "राम ram"
>>> a.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae ram'
>>> encodedForm = a.encode()
>>> type(encodedForm)
<class 'bytes'>
>>> encodedForm.decode()
'राम ram'
>>> a=10
>>> float(a)
10.0
>>> #Student obj = new Student();
>>> str(a)
'10'
>>> bool(a)
True
>>> bool(0)
False
>>> bool(-10)
True
>>> a = 10.2
>>> int(a)
10
>>> str(a)
'10.2'
>>> bool(a)
True
>>> a = "python"
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'python'
>>> int('a')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int('a')
ValueError: invalid literal for int() with base 10: 'a'
>>> ord('a')
97
>>> ord(' ')
32
>>> ord('abc')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ord('abc')
TypeError: ord() expected a character, but string of length 3 found
>>> #ordinal value -> ascii value
>>> chr(97)
'a'
>>> chr(32)
' '
>>> chr(65)
'A'
>>> bin(65)
'0b1000001'
>>> id(a)
4342198376
>>> hex(id(a))
'0x102d0b068'
>>> oct(123)
'0o173'
>>> bool("python")
True
>>> bool(" ")
True
>>> bool("")
False
>>> bool(None)
False
>>> int(0b1000001)
65
>>> bin(0x102d0b068)
'0b100000010110100001011000001101000'
>>> bin(102d0b068)
SyntaxError: invalid syntax
>>> bin("102d0b068")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    bin("102d0b068")
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(1020068)
'0b11111001000010100100'
>>> #to see directory of fns a particular object has got use dir()
>>> type(a)
<class 'str'>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> 10/20
0.5
>>> 10 // 20
0
>>> 22 / 7
3.142857142857143
>>> 22 // 7
3
>>> #/ -> classic division
>>> # // -> floor division
>>> 
>>> 2 * 3
6
>>> 2 ** 3
8
>>> 3 ** 2
9
>>> 3^2
1
>>> 100 ^ 23
115
>>> 123 ^ 90
33
>>> 12.3 ^ 90.9
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    12.3 ^ 90.9
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> 12.3 ^ 90
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    12.3 ^ 90
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> bin(10.2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    bin(10.2)
TypeError: 'float' object cannot be interpreted as an integer
>>> a=0
>>> a+=66
>>> 22 = 66
SyntaxError: can't assign to literal
>>> "22".isidentifier()
False
>>> "a22".isidentifier()
True
]
>>> oct = 10
>>> oct(10)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    oct(10)
TypeError: 'int' object is not callable
>>> oct1 = 10
>>> True = 10
SyntaxError: can't assign to keyword
>>> a = 10
>>> a++
SyntaxError: invalid syntax
>>> a + 1
11
>>> a
10
>>> a = a + 1
>>> a
11
>>> a += 1
>>> a = 09
SyntaxError: invalid token
>>> a = 0x9
>>> z += 1
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    z += 1
NameError: name 'z' is not defined
>>> z = 10
>>> z += 1
>>> z
11
>>> # a*=1 -> a = a * 1
>>> #  a **= 1
>>> a **= 3
>>> a
729
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py", line 4, in <module>
    print("A is " + a)
TypeError: can only concatenate str (not "int") to str
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
A is10
A is 10
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
A is10b is20
A is 10 b is 20
A is 10
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py", line 8, in <module>
    print("Sum of %d and %d is %d"%(a,b,"10"))
TypeError: %d format: a number is required, not str
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py", line 10, in <module>
    print("Sum of {} and {} is {}. Total result is {}".format(a,b,c))
IndexError: tuple index out of range
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py", line 10, in <module>
    print("Sum of {} and {} is {2}. Total result is {2}".format(a,b,c))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
Enter your name : Ram
Name is Ram
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
Enter your name : nmk
Name is nmk
Name is {name}
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
Enter your name : Ram
Name is Ram
Name is Ram
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
Enter your name : Ram
Name is Ram
Name is Ram
Ram
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py", line 12, in <module>
    print("Sum of {num} and {1} is {2}. Total result is {2}".format(a,b,c))
KeyError: 'num'
>>> 
=== RESTART: /Users/anmolrajarora/Documents/rd_college_python_iot/Demo.py ===
Sum of 10 and 20 is 10
Sum of 10 and 20 is 30. Total result is 30
Sum of 10 and 20 is 30. Total result is 30
Enter your name : Ram
Name is Ram
Name is Ram
Ram
First element is 1
>>> 0.1
0.1
>>> 0.2
0.2
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1000000001 + 0.200000000000003
0.300000000100003
>>> 0.1 + 0.3
0.4
>>> list1 = [1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
>>> list1[0]
1
>>> list1[1]
2
>>> list1[2]
3
>>> list1 = [1,2,3,4,5,"six"]
>>> import numpy
>>> arr1 = [1,2,3,4,5,"six"]
>>> arr1 = np.array(arr1)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    arr1 = np.array(arr1)
NameError: name 'np' is not defined
>>> arr1 = numpy.array(arr1)
>>> arr1
array(['1', '2', '3', '4', '5', 'six'], dtype='<U21')
>>> arr1 = numpy.array([1,2,3,4,5])
>>> arr1
array([1, 2, 3, 4, 5])
>>> list1= [1,2,3,4,5,"six"]
>>> list1
[1, 2, 3, 4, 5, 'six']
>>> list1.append(10)
>>> list1
[1, 2, 3, 4, 5, 'six', 10]
>>> list1.pop()
10
>>> tuple1 = [1, 2, 3, 4, 5, 'six']
>>> tuple1
[1, 2, 3, 4, 5, 'six']
>>> tuple1 = (1, 2, 3, 4, 5, 'six')
>>> tuple1
(1, 2, 3, 4, 5, 'six')
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> list1
[1, 2, 3, 4, 5, 'six']
>>> del list1[5]
>>> list1
[1, 2, 3, 4, 5]
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion

>>> tuple1 = (1,2,3,4,5, [11,22,33,44,55])
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> tuple1[5]
[11, 22, 33, 44, 55]
>>> tuple1[5].append(66)
>>> tuple1
(1, 2, 3, 4, 5, [11, 22, 33, 44, 55, 66])
>>> tuple1[5] = [1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    tuple1[5] = [1,2,3,4,5]
TypeError: 'tuple' object does not support item assignment
>>> list1
[1, 2, 3, 4, 5]
>>> list1 = [1, 2, 3, 4, 5, [1,2,3,4,5]]
>>> list1
[1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
>>> list2 = list1
>>> list2
[1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
>>> del list1[0]
>>> list1
[2, 3, 4, 5, [1, 2, 3, 4, 5]]
>>> list2
[2, 3, 4, 5, [1, 2, 3, 4, 5]]
>>> list3 = list1.copy()
>>> id(list1) == id(list2)
True
>>> id(list1) == id(list3)
False
>>> list1.append(100)
>>> list1
[2, 3, 4, 5, [1, 2, 3, 4, 5], 100]
>>> list2
[2, 3, 4, 5, [1, 2, 3, 4, 5], 100]
>>> list3
[2, 3, 4, 5, [1, 2, 3, 4, 5]]
>>> list1[4].append(200)
>>> list1
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200], 100]
>>> list2
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200], 100]
>>> list3
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200]]
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> id(list1) == id(list4)
False
>>> id(list1[4]) == id(list4[4])
False
>>> id(list1[4]) == id(list3[4])
True
>>> list1[4].append(1000)
>>> list1
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200, 1000], 100]
>>> list2
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200, 1000], 100]
>>> list3
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200, 1000]]
>>> list4
[2, 3, 4, 5, [1, 2, 3, 4, 5, 200], 100]
>>> a = 10
>>> b = 20
>>> a,b = 10,20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> a = 10,20
>>> a
(10, 20)
>>> name = "Ram"
>>> print("Welcome",name)
Welcome Ram
>>> msg = "Welcome",name
>>> msg
('Welcome', 'Ram')
>>> msg = "Welcome " + name
>>> msg
'Welcome Ram'
>>> id("Welcome")
4403113688
>>> id(name)
4403113800
>>> id(msg)
4402019696
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str1 = "python programming is easy"
>>> str1[0]
'p'
>>> str1[1]
'y'
>>> str1[len(str1) - 1]
'y'
>>> str1[-1]
'y'
>>> str1[0:5]
'pytho'
>>> str1[0:6]
'python'
>>> len(str1)
26
>>> str1[0:25]
'python programming is eas'
>>> str1[0:26]
'python programming is easy'
>>> str1[-1]
'y'
>>> str1[-len(str1)]
'p'
>>> str1[-1:-5]
''
>>> str1[0:26:1]
'python programming is easy'
>>> str1[0:26:2]
'pto rgamn ses'
>>> str1[0:26:3]
'ph oai  s'
>>> str1[0:26:5]
'pngisy'
>>> str1[-1:-5:-1]
'ysae'
>>> str1[-5:-1]
' eas'
>>> str1[-5:0]
''
>>> str1[-5:]
' easy'
>>> str1[:]
'python programming is easy'
>>> str1[26:0:-1]
'ysae si gnimmargorp nohty'
>>> str1[26:-1:-1]
''
>>> str1[26::-1]
'ysae si gnimmargorp nohtyp'
>>> str1[::-1]
'ysae si gnimmargorp nohtyp'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print("Welcome user!")
Welcome user!
>>> print("Welcome user!".center(100))
                                           Welcome user!                                            
>>> print("Welcome user!".center(110))
                                                Welcome user!                                                 
>>> "Welcome user!".center(110)
'                                                Welcome user!                                                 '
>>> "Welcome user!".center(110,"*")
'************************************************Welcome user!*************************************************'
>>> msg
'Welcome Ram'
>>> msg.endswith('Ram')
True
>>> msg.count("a")
1
>>> msg.count("Ram")
1
>>> msg = 'Welcome RamRam'
>>> msg.count("Ram")
2
>>> msg
'Welcome RamRam'
>>> msg.index("a")
9
>>> msg.rindex("a")
12
>>> msg = 'Welcome RamRamRam'
>>> msg.index("a")
9
>>> msg.rindex("a")
15
>>> msg.index("a", 10)
12
>>> msg.index("a", msg.index("a"))
9
>>> msg.index("a", msg.index("a") + 1)
12
>>> msg
'Welcome RamRamRam'
>>> msg.split('a')
['Welcome R', 'mR', 'mR', 'm']
>>> msg = 'Welcome RamRamRaam'
>>> msg.split('a')
['Welcome R', 'mR', 'mR', '', 'm']
>>> msg.partition('a')
('Welcome R', 'a', 'mRamRaam')
>>> msg.replace("a","x")
'Welcome RxmRxmRxxm'
>>> msg.replace("a","")
'Welcome RmRmRm'
>>> msg.replace("a"," ")
'Welcome R mR mR  m'
>>> msg.split("a")
['Welcome R', 'mR', 'mR', '', 'm']
>>> tokens = msg.split("a")
>>> tokens
['Welcome R', 'mR', 'mR', '', 'm']
>>> 'a'.join(tokens)
'Welcome RamRamRaam'
>>> 

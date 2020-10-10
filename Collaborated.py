'This is a Python Code'
print (" Hello World")

'Variable'
x=3
print(x)
print(x+3)
print(x)

'Variable'
spam ="eggs"
print(spam*3)


x=123.456
print(x)

x='This is a string'
print (x+"!")


#'In place operator:'
print ('x=')
x=2
print (x)

'''print('x=x+2')
x=x+2
print (x)'''

'''print('x=+x')
x=+x
print (x)'''

print('x+=x')
x+=x
print (x)

#These operators can be used on types other than numbers, as well, such as strings.

x='spam'
print (x)
x+='eggs'
print("x+='eggs'")
print(x)

#Boolean(True/False)
# ==
my_boolean=True
print(my_boolean)

x=(2==3)
print(x)

x=('hello'=='hello' )
print(x)

# !=
x=(12!=13)
print(x)

x=('window'!='window')
print(x)

#Greater than or smaller than (< and >)
x=(7>5)
print(x)

x=(7<5)
print(x)

#The greater than or equal to, and smaller than or equal to operators are >= and <=
x=(7>=7.0)
print(x)

x=(7<=7.0)
print(x)

#if Statements

if(2=2)
print('two is equal to 2')
#above code will show error [IndentationError: expected an indented block]

if(2=2)
    print('two is equal to 2')
#--------------------------------------
if 10 < 5:
   print("10 greater than 5")

print("Program ended")
#---------------------------------------
num = 12
if num > 5:
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")
#-----------------------------------------------
#else Statements
x = 4
if x == 5:
   print("Yes")
else:
   print("No")
#----------------------------------------------
num = 7
if num == 5:
  print("Number is 5")
else:
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else:
      print("Number isn't 5, 11 or 7")
#----------------------------------------------
#elif Statements
num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")

#----------------------------------------------
#Boolean Logic
#Python's Boolean operators are and, or, and not.
Boolean and

print(1 == 1 and 2 == 2)

print(1 == 1 and 2 == 3)

print(1 != 1 and 2 == 2)

print(2 < 1 and 3 >  6)

Boolean or

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 >  6)

Boolean Not

print(not 1 == 1)

print(not 1 > 7)
#-------------------------------------------

Operator Precedence
--parentheses
--exponentiation
--multiplication/division
--addition/subtraction

print(False == False or True)

print(False == (False or True))

print((False == False) or True)

#--------------------------------------------
while Loops

i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

#--------------------------------------------
while Loops
The infinite loop

while 1==1:
  print("In the loop")

# break used to end while statement

i = 0
while 1==1:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")
#---------------------------------------------

#continue

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")
#-------------------------------------------

Lists

words=("Hello","world","!")
print(words[0])
print(words[1])
print(words[2])

#Empty list
empty_list = []
print(empty_list)

#Types in the list
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

#List-string
str = "Hello world!"
print(str[6])

#List Operations
nums = [7, 7, 7, 7, 7]
nums[2] = 5
nums[3] = 5
print(nums)

#List Operations
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

#Lists can also be nested within other lists.
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

#Nested lists can be used to represent 2D grids, such as matrices.
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

print(m[1][2])

#The append method adds an item to the end of an existing list.
nums = [1, 2, 3]
nums.append(4)
print(nums)

#To get the number of items in a list, you can use the len function.
nums = [1, 3, 5, 2, 4]
print(len(nums))

#The insert method is similar to append, except that it allows you to insert a
#new item at any position in the list, as opposed to just at the end.

#Module quize
*What is the output of this code?

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

Ans: 8

What does this code do?

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

Ans: Print all the even numbers between 2 and 10

*How many lines will this code print?

while False:
  print("Looping...")

  Ans: 0

*Fill in the blanks to print the first element of the list, if it contains even number of elements.

list = [1, 2, 3, 4]
if len (list) % 2==0:
  print(list[0])

* What does this code output?

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])

Ans: y

*Fill in the blanks to iterate over the list using a for loop and print its values.

list = [1, 2, 3]
for var in list:
  print(var)
  -----------------------------

#Function and module
Code reuse is a very important part of programming in any language.
You've already used functions in previous lessons.
Any statement that consists of a word followed by information in parentheses is a function call.

print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)

The words in front of the parentheses are function names, and the comma-separated values
inside the parentheses are function arguments.

How many arguments are in this function call?
range(0, 100, 5)
Ans:3
------------------------------------
In addition to using pre-defined functions, you can create your own functions by using the def statement.
Here is an example of a function named my_func. It takes no arguments, and prints "spam" three times.
It is defined, and then called. The statements in the function are executed only when the function is called.

def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()

#You must define functions before they are called,
#in the same way that you must assign variables before using them.
#Most functions take arguments.

def print_with_exclamation(word):
   print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

You can also define functions with more than one argument; separate them with commas

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

''''Function arguments can be used as variables inside the function definition.
However, they cannot be referenced outside of the function's definition.
This also applies to other variables created inside a function.''''

def function(variable):
   variable += 1
   print(variable)

function(7)
print(variable)

''''Returning from Functions
Certain functions, such as int or str, return a value that can be used later.
To do this for your defined functions, you can use the return statement.'''

For example:
def max(x, y):
    if x >=y:
        return x
    else:
        return y

print(max(4, 7)
z = max(8, 5)
print(z)

'''''Fill in the blanks to define a function that compares
the lengths of its arguments and returns the shortest one.'''

def shortest_string(x, y):
  if len(x) <= len(y):
    return x
  else:
      return y

''''Returning from Functions:
Once you return a value from a function, it immediately stops being executed.
Any code after the return statement will never happen.''''

For example:
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))

''''Comments: Comments are annotations to code used to make it easier to understand.
They don't affect how code is run.
In Python, a comment is created by inserting an octothorpe ''''
(otherwise known as a number sign or hash symbol: #). All text after it on that line is ignored.
For example:
x = 365
y = 7
# this is a comment
print(x % y) # find the remainder
# print (x // y)
# another comment

''''Docstrings:Docstrings (documentation strings) serve a similar purpose to comments,
as they are designed to explain code. However, they are more specific and have a different syntax.
They are created by putting a multiline string containing an explanation of the function
below the function's first line.'''

def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")

shout("spam")

''''Functions: Although they are created differently from normal variables,
functions are just like any other kind of value.
They can be assigned and reassigned to variables, and later referenced by those names.'''

def multiply(x, y):
   return x * y
a = 4
b = 7
operation = multiply
print(operation(a, b))

''''Functions:Functions can also be used as arguments of other functions.'''

def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

""Fill in the blanks to pass the function "square" as an argument to the function "test":""

def square(x):
  return x * x
def test(func, x):
 print(func(x))
test(square, 42)

""""Modules:Modules are pieces of code that other people have written to fulfill
common tasks, such as generating random numbers, performing mathematical operations, etc."""

"""The basic way to use a module is to add import module_name at the top of your code,
and then using module_name.var to access functions and values with the name var in the module."""

"""For example, the following example uses the random module to generate random numbers:"""

import random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

#The code uses the randint function defined in the random module to
#print 5 random numbers in the range 1 to 6.

""""Modules:There is another kind of import that can be used if you only need certain
functions from a module."""
""""These take the form from module_name import var, and then var can be used as if it were
defined normally in your code."""
"""For example, to import only the pi constant from the math module:"""

from math import pi

print(pi)

""""Use a comma separated list to import multiple objects. For example:"""

from math import pi, sqrt

"""""* imports all objects from a module. For example: from math import *
This is generally discouraged, as it confuses variables in your code with variables in the external module."""

""""Modules:You can import a module or object under a different name using the as keyword.
This is mainly used when a module or object has a long or confusing name.
For example:"""

from math import sqrt as square_root
print(square_root(100))

Modules

""""There are three main types of modules in Python, those you write yourself,
those you install from external sources, and those that are preinstalled with Python.
The last type is called the standard library, and contains many useful modules.
Some of the standard library's useful modules include string, re, datetime, math,
random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys."""

"""Tasks that can be done by the standard library include string parsing, data serialization,
testing, debugging and manipulating dates, emails, command line arguments, and much more!
Python's extensive standard library is one of its main strengths as a language."""

"""The Standard Library
Some of the modules in the standard library are written in Python, and some are written in C.
Most are available on all platforms, but some are Windows or Unix specific.
We won't cover all of the modules in the standard library; there are simply too many.
The complete documentation for the standard library is available online at www.python.org."""

"""Modules

Many third-party Python modules are stored on the Python Package Index (PyPI).
The best way to install these is using a program called pip. This comes installed by
 default with modern distributions of Python. If you don't have it, it is easy to install online.
 Once you have it, installing libraries from PyPI is easy. Look up the name of the library you want to install,
 go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name.
 Once you've done this, import the library and use it in your code.

Using pip is the standard way of installing libraries on most operating systems,
but some libraries have prebuilt binaries for Windows. These are normal executable files
that let you install libraries with a GUI the same way you would install other programs.
It's important to enter pip commands at the command line, not the Python interpreter"""

"""What is the highest number output by this code?"""

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

# What is the output of this code?

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))


""""Exceptions: You have already seen exceptions in previous code. They occur when something goes wrong,
due to incorrect code or input. When an exception occurs, the program immediately stops.
The following code produces the ZeroDivisionError exception by trying to divide 7 by 0."""

num1 = 7
num2 = 0
print(num1/num2)

''''Exceptions:Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
Python has several other built-in exceptions, such as ZeroDivisionError and OSError.
Third-party libraries also often define their own exceptions.'''

'''''Exception Handling:To handle exceptions, and to call code when an exception occurs,
you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs,
the code in the try block stops being executed, and the code in the except block is run.
If no error occurs, the code in the except block doesn't run.'''
For example:

try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

#What is the output of this code

try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

""""Exception Handling : A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses,
to have the except block handle all of them."""

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

#What is the output of this code?
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

''''Exception Handling:An except statement without any exception specified will catch
all errors. These should be used sparingly, as they can catch unexpected errors
and hide programming mistakes.'''
For example:

try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")

-------
try:
  num1 = input(":")
  num2 = input(":")
  print(float(num1)/float(num2))
 except:
  print("Invalid input")

''''finally To ensure some code runs no matter what errors occur, you can use a finally statement.
The finally statement is placed at the bottom of a try/except statement.
Code within a finally statement always runs after execution of the code in the try,
and possibly in the except, blocks.'''

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

#What is the output of this code?
try:
  print(1)
except:
  print(2)
finally:
  print(3)

  Ans: 1 3

'''''finally:Code in a finally statement even runs if an uncaught exception occurs
in one of the preceding blocks.'''

try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print(unknown_var)
finally:
   print("This is executed last")

''''Raising Exceptions:You can raise exceptions by using the raise statement.'''
print(1)
raise ValueError
print(2)

#Which errors occur during the execution of this code?
try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

''''Raising Exceptions:Exceptions can be raised with arguments that give detail about them.'''
For example:
name = "123"
raise NameError("Invalid name!")

''''Assertions:An assertion is a sanity-check that you can turn on or turn off
when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.'''
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

''''Assertions:The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.'''
temp = -10
assert (temp >= 0), "Colder than absolute zero!"

Opening Files

''''You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited,
it must be opened, using the open function.'''

myfile = open("filename.txt")

''''Opening Files
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).'''
For example:
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

''''You can use the + sign with each of the modes above to give them extra access to
files. For example, r+ opens the file for both reading and writing.'''

''''Once a file has been opened and used, you should close it.
This is done with the close method of the file object.'''
file = open("filename.txt", "w")
# do stuff to the file
file.close()

''''We will read/write content to files in the upcoming lessons.'''

''''Reading Files:The contents of a file that has been opened in text mode can be read using the read method.'''
#This will print all of the contents of the file "filename.txt".
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

''''To read only a certain amount of a file, you can provide a number as an argument
to the read function. This determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte.
With no argument, read returns the rest of the file.'''

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

''''Just like passing no arguments, negative values will return the entire contents.'''

''''Reading Files:After all contents in a file have been read, any attempts to read
further from that file will return an empty string, because you are trying to read
from the end of the file.'''

file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

''''Reading Files:To retrieve each line in a file, you can use the readlines
method to return a list in which each element is a line in the file.'''
#For example:
file = open("filename.txt", "r")
print(file.readlines())
file.close()

''''

You can also use a for loop to iterate through the lines in the file:'''
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()

'''''In the output, the lines are separated by blank lines,
as the print function automatically adds a new line at the end of its output.'''

'''Writing Files:To write to files you use the write method, which writes a string to the file.'''
#For example:
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

#The "w" mode will create a file, if it does not already exist.
''''Writing Files: When a file is opened in write mode, the file's existing content is deleted.'''

file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

''''Writing Files: The write method returns the number of bytes written to a file,
if successful.'''
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

''''Working with Files:It is good practice to avoid wasting resources by making sure
that files are always closed after they have been used. One way of doing this is to use try and finally.'''
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

''''Working with Files:An alternative way of doing this is using with statements. This creates a temporary
variable (often called f), which is only accessible in the indented block of the with statement.'''

with open("filename.txt") as f:
   print(f.read())

''''The file is automatically closed at the end of the with statement, even if exceptions
occur within it.'''

''''None : The None object is used to represent the absence of a value.
It is similar to null in other programming languages.
Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
When entered at the Python console, it is displayed as the empty string.'''

'''The None object is returned by any function that doesn't explicitly return anything else.'''

def some_func():
  print("Hi!")

var = some_func()
print(var)

'''' Dictionaries:Dictionaries are data structures used to map arbitrary keys to values.
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.'''
#Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

''''Trying to index a key that isn't part of the dictionary returns a KeyError.'''
#Example:
primary = {
  "red": [255, 0, 0],
  "green": [0, 255, 0],
  "blue": [0, 0, 255],
}

print(primary["red"])
print(primary["yellow"])

''''Dictionaries:Only immutable objects can be used as keys to dictionaries.
Immutable objects are those that can't be changed. So far, the only mutable objects
you've come across are lists and dictionaries.
Trying to use a mutable object as a dictionary key causes a TypeError.'''

bad_dict = {
  [1, 2, 3]: "one two three",
}

''''Dictionaries:To determine whether a key is in a dictionary,
you can use 'in' and 'not in', just as you can for a list.'''
#Example:

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

''''Dictionaries:A useful dictionary method is get. It does the same thing as indexing,
 but if the key is not found in the dictionary it returns another specified value instead ('None', by default).'''
#Example:
pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

#What is the result of this code?
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
#Ans:8

''''Tuples:Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.'''
#Example:

words = ("spam", "eggs", "sausages",)

#You can access the values in the tuple with their index, just as you did with lists:
print(words[0])

#Trying to reassign a value in a tuple causes a TypeError.
words[1] = "cheese"

#Like lists and dictionaries, tuples can be nested within each other.

'''Tuples:Tuples can be created without the parentheses,
by just separating the values with commas.'''
#Example:
my_tuple = "one", "two", "three"
print(my_tuple[0])

#An empty tuple is created using an empty parenthesis pair.
tpl = ()

#Tuples are faster than lists, but they cannot be changed.

''''List Slices:List slices provide a more advanced way of retrieving values from a list.
Basic list slicing involves indexing a list with two colon-separated integers.
This returns a new list containing all the values in the old list between the indices.'''
#Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
Try It Yourself

''''Like the arguments to range, the first index provided
in a slice is included in the result, but the second isn't.'''

'''List Slices:If the first number in a slice is omitted,
it is taken to be the start of the list.
If the second number is omitted, it is taken to be the end.'''
#Example:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

#Slicing can also be done on tuples.

''''List slices can also have a third number, representing the step, to include only
alternate values in the slice.'''

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

''''[2:8:3] will include elements starting from the 2nd index up to the 8th with a
step of 3.'''

''''Negative values can be used in list slicing (and normal list indexing).
When negative values are used for the first and second values in a slice
(or a normal index), they count from the end of the list.''''

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

''''If a negative value is used for the step, the slice is done backwards.
Using [::-1] as a slice is a common and idiomatic way to reverse a list.'''

''''List comprehensions are a useful way of quickly creating lists whose contents
obey a simple rule.'''
# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

#List comprehensions are inspired by set-builder notation in mathematics.

''''A list comprehension can also contain an if statement to
enforce a condition on values in the list.'''
#Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

''''Trying to create a list in a very extensive range will result in a MemoryError.
This code shows an example where the list comprehension runs out of memory.'''

even = [2*i for i in range(10**100)]

#This issue is solved by generators.

'''String Formatting:So far, to combine strings and non-strings, you've converted the non-strings to
strings and added them.
String formatting provides a more powerful way to embed non-strings within strings.
String formatting uses a string's format method to substitute a number of arguments in the string.'''

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

''''Each argument of the format function is placed in the string at
the corresponding position, which is determined using the curly braces { }.'''

''''String formatting can also be done with named arguments.'''
#Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)

'''''String Functions: Python contains many useful built-in functions and methods to
accomplish common tasks.'''

join - joins a list of strings with another string as a separator.
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
To change the case of a string, you can use lower and upper.
The method split is the opposite of join, turning a string with a certain separator into a list.

#Some examples:
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

''''Numeric Functions:To find the maximum or minimum of some numbers or a list, you can use max or min.
To find the distance of a number from zero (its absolute value), use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum.'''
#Some examples:
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

'''''Often used in conditional statements, all and any take a list as an argument,
and return True if all or any (respectively) of their arguments evaluate to
True (and False otherwise).
The function enumerate can be used to iterate through the values and indices of
a list simultaneously.'''
#Example:
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

''''Text Analyzer:This is an example project, showing a program that analyzes
a sample file to find what percentage of the text each character occupies.
This section shows how a file could be open and read.'''

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

'''''Text Analyzer:This part of the program shows a function that counts
how many times a character occurs in a string.'''

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

''''This function takes as its arguments the text of the file and one character,
returning the number of times that character appears in the text.
Now we can call it for our file.'''

filename = input("Personal_Assistant.py")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))

#The character "r" appears 83 times in the file.

''''Text Analyzer:The next part of the program finds what percentage of
the text each character of the alphabet occupies.'''

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

#Let's put it all together and run the program:

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

''''Functional Programming: Functional programming is a style of programming that
(as the name suggests) is based around functions.'''
''''A key part of functional programming is higher-order functions. We have seen
this idea briefly in the previous lesson on functions as objects. Higher-order
functions take other functions as arguments, or return them as results.'''
#Example:
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

''''The function apply_twice takes another function as its argument,
and calls it twice inside its body.'''

''''Pure Functions:Functional programming seeks to use pure functions.
Pure functions have no side effects, and return a value that depends only on their arguments.
This is how functions in math work: for example, The cos(x) will,
for the same value of x, always return the same result.'''
#Below are examples of pure and impure functions.

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

Impure function:
some_list = []

def impure(arg):
  some_list.append(arg)
impure(4)
print(list)

'''The function above is not pure, because it changed the state of some_list.'''

''''Pure Functions:Using pure functions has both advantages and disadvantages.
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result
can be stored and referred to the next time the function of that input is
needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.
The main disadvantage of using only pure functions is that they majorly
complicate the otherwise simple task of I/O, since this appears to inherently
require side effects.
They can also be more difficult to write in some situations.'''

''''Lambdas:Creating a function normally (using def) assigns it to a variable automatically.
This is different from the creation of other objects - such as strings and
integers - which can be created on the fly, without assigning them to a variable.
The same is possible with functions, provided that they are created using lambda syntax.
Functions created this way are known as anonymous.
This approach is most commonly used when passing a simple function as an argument
to another function. The syntax is shown in the next example and consists of the lambda keyword
followed by a list of arguments, a colon, and the expression to evaluate and return.'''

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

''''Lambda functions get their name from lambda calculus, which is a model of computation
invented by Alonzo Church.'''

''''Lambdas:Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression - usually
equivalent to a single line of code.'''
#Example:
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#In the code above, we created an anonymous function on the fly and called
# with an argument.

''''Lambdas:Lambda functions can be assigned to variables,
and used like normal functions.'''
#Example:
double = lambda x: x * 2
print(double(7))

#However, there is rarely a good reason to do this - it is usually
#better to define a function with def instead.

''''map: The built-in functions map and filter are very useful higher-order
functions that operate on lists (or similar objects called iterables).
The function map takes a function and an iterable as arguments, and returns
a new iterable with the function applied to each argument.'''
#Example:
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#We could have achieved the same result more easily by using lambda syntax.
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#To convert the result into a list, we used list explicitly.

''''filter:The function filter filters an iterable by removing items
that don't match a predicate (a function that returns a Boolean).'''
#Example:
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

''''Like map, the result has to be explicitly converted to
a list if you want to print it.'''

'''Generators: Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can
still be iterated through with for loops.
They can be created using functions and the yield statement.'''
#Example:
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1

for i in countdown():
  print(i)

  ''''Generators: Due to the fact that they yield one item at a time, generators don't have
  the memory restrictions of lists.
  In fact, they can be infinite!'''

  def infinite_sevens():
    while True:
      yield 7

  for i in infinite_sevens():
    print(i)

''''In short, generators allow you to declare a function that behaves like an iterator,
  i.e. it can be used in a for loop.'''

''''Generators: Finite generators can be converted into lists by passing them
as arguments to the list function.'''
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

''''Using generators results in improved performance, which is the result of the lazy
(on demand) generation of values, which translates to lower memory usage.
Furthermore, we do not need to wait until all the elements have been generated
before we start to use them.'''

#What is the result of this code?
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

''''Decorators: Decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you
don't want to modify.'''
#Example:
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()

''''We defined a function named decor that has a single parameter func. Inside decor,
we defined a nested function named wrap. The wrap function will print a string,
then call func(), and print another string. The decor function returns the wrap
function as its result.
We could say that the variable decorated is a decorated version of print_text - it's
print_text plus something.
In fact, if we wrote a useful decorator we might want to replace print_text with
the decorated version altogether so we always got our "plus something" version of print_text.
This is done by re-assigning the variable that contains our function:'''

print_text = decor(print_text)
print_text()

#Now print_text corresponds to our decorated version.
''''Decorators: In our previous example, we decorated our function by replacing
the variable containing the function with a wrapped version.'''

def print_text():
  print("Hello world!")

print_text = decor(print_text)

''''This pattern can be used at any time, to wrap any function.
Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
If we are defining a function we can "decorate" it with the @ symbol like:'''

@decor
def print_text():
  print("Hello world!")


#This will have the same result as the above code.

#A single function can have multiple decorators.

''''Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions calling themselves.
It is used to solve problems that can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the factorial
function, which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this
recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on.
Generally, n! = n * (n-1)!.
Furthermore, 1! = 1.
This is known as the base case, as it can be calculated without performing
any more factorials.
Below is a recursive implementation of the factorial function.'''

def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x-1)

print(factorial(5))

#The base case acts as the exit condition of the recursion.

''''Recursive functions can be infinite, just like infinite while loops.
These often occur when you forget to implement the base case.
Below is an incorrect version of the factorial function.
It has no base case, so it runs until the interpreter runs out of
memory and crashes.'''

def factorial(x):
  return x * factorial(x-1)

print(factorial(5))

#What is the result of this code?
def sum_to(x):
   return x + sum_to(x-1)
print (sum_to(5))

''''Recursion can also be indirect.
One function can call a second, which calls the first, which calls the second,
and so on. This can occur with any number of functions.'''
#Example:
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(17))
print(is_even(23))

''''Sets are data structures, similar to lists or dictionaries.
They are created using curly braces, or the set function. They share some functionality with lists, such as the use of in to check whether they contain a particular item.
num_set = {1, 2, 3, 4, 5}'''

word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

#To create an empty set, you must use set(), as {} creates an empty dictionary.
''''Sets: Sets differ from lists in several ways, but share several list operations such as len.
They are unordered, which means that they can't be indexed.
They cannot contain duplicate elements.
Due to the way they're stored, it's faster to check whether an item is part of a set,
rather than part of a list.
Instead of using append to add to a set, use add.
The method remove removes a specific element from a set; pop removes an arbitrary element.'''

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

''''Basic uses of sets include membership testing and the elimination of duplicate entries.'''

''''Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.'''

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

''''Data Structures: As we have seen in the previous lessons,
Python supports the following data structures:
lists, dictionaries, tuples, sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified.
    Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access.
Try to choose lists when you need a simple, iterable collection that is modified
frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.
Many times, a tuple is used in combination with a dictionary, for example,
a tuple might represent a key, because it's immutable.'''

''''itertools: The module itertools is a standard library that contains several
functions that are useful in functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable (for instance a list or string).
The function repeat repeats an object, either infinitely or a specific number of times.'''
#Example:
from itertools import count

for i in count():
  print(i)
  if i >=11:
    break

''''There are many functions in itertools that operate on iterables,
in a similar way to map and filter.
#Some examples:
takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in an iterable.'''

from itertools import accumulate, takewhile
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

''''There are also several combinatoric functions in itertool,
such as product and permutation.
These are used when you want to accomplish a task with all possible combinations
of some items.'''
#Example:

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

''''There are also several combinatoric functions in itertool,
such as product and permutation.
These are used when you want to accomplish a task with
all possible combinations of some items.'''
#Example:

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

''''Classes: We have previously looked at two paradigms of programming
- imperative (using statements, loops, and functions as subroutines),
and functional (using pure functions, higher-order functions, and recursion).

Another very popular paradigm is object-oriented programming (OOP).
Objects are created using classes, which are actually the focal point of OOP.
The class describes what the object will be, but is separate from the object itself.
In other words, a class can be described as an object's blueprint, description,
or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the keyword class and an indented block,
which contains class methods (which are functions).
Below is an example of a simple class and its objects.'''

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

''''This code defines a class named Cat, which has two attributes: color and legs.
Then the class is used to create 3 separate objects of that class.
Tap Continue to learn more!'''

''''__init__
The __init__ method is the most important method in a class.
This is called when an instance (object) of the class is created, using the
class name as a function.

All methods must have self as their first parameter, although it isn't explicitly
passed, Python adds the self argument to the list for you; you do not need to
include it when you call the methods. Within a method definition,
self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs.
These can be accessed by putting a dot, and the attribute name after an instance.
In an __init__ method, self.attribute can therefore be used to set the initial
value of an instance's attributes.'''
#Example:
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
Try It Yourself

''''In the example above, the __init__ method takes two arguments and assigns them
to the object's attributes. The __init__ method is called the class constructor.'''

''''Methods
Classes can have other methods defined to add functionality to them.
Remember, that all methods must have self as their first parameter.
These methods are accessed using the same dot syntax as attributes.'''
#Example:
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

''''Classes can also have class attributes, created by assigning variables
within the body of the class. These can be accessed either from instances
of the class, or the class itself.'''
#Example:
class Dog:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

#Class attributes are shared by all instances of the class.

''''Classes: Trying to access an attribute of an instance that isn't defined causes
an AttributeError. This also applies when you call an undefined method.'''

#Example:
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

rect = Rectangle(7, 8)
print(rect.color)

''''Inheritance
Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in
 some ways (only Dog might have the method bark), they are likely to be similar
 in others (all having the attributes color and name).
This similarity can be expressed by making them all inherit from a
superclass Animal, which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses
after the class name.'''
#Example:
class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")

class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

''''A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods,
it overrides them.'''

class Wolf:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")

husky = Dog("Max", "grey")
husky.bark()

#What is the result of this code?
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()

''''Inheritance can also be indirect. One class can inherit from another,
and that class can inherit from a third class.'''
#Example:
class A:
  def method(self):
    print("A method")

class B(A):
  def another_method(self):
    print("B method")

class C(B):
  def third_method(self):
    print("C method")

c = C()
c.method()
c.another_method()
c.third_method()

#However, circular inheritance is not possible.

#What is the result of this code?
class A:
  def a(self):
    print(1)
class B(A):
  def a(self):
    print(2)

class C(B):
  def c(self):
    print(3)

c = C()
c.a()

''''The function super is a useful inheritance-related function that refers to
the parent class. It can be used to find the method with a certain name in an
object's superclass.'''
#Example:
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()

B().spam()

''''super().spam() calls the spam method of the superclass.'''

''''Magic Methods
Magic methods are special methods which have double underscores at the beginning
and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and *
to be used on them.
An example magic method is __add__ for +.'''
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

''''The __add__ method allows for the definition of a custom behavior for the + operator
in our class.
As you can see, it adds the corresponding attributes of the objects and returns
a new object, containing the result.
Once it's defined, we can add two objects of the class together.'''

'''More magic methods for common operators:'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

''''The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types,
then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.'''
#Example:
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

#In the example above, we defined the division operation for our class SpecialString.

''''Python also provides magic methods for comparisons.
''''
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

''''If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
''''
#Example:
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

''''As you can see, you can define any custom behavior for the overloaded operators.''''

'''There are several magic methods for making classes act like containers.'''
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

''''There are many other magic methods that we won't cover here,
such as __call__ for calling objects as functions, and __int__, __str__, and the like,
for converting objects to built-in types.''''
#Example:
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

''''We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression.''''



''''Object Lifecycle
The lifecycle of an object is made up of its creation, manipulation, and destruction.

The first stage of the life-cycle of an object is the definition of the class
to which it belongs.
The next stage is the instantiation of an instance, when __init__ is called.
Memory is allocated to store the instance. Just before this occurs,
the __new__ method of the class is called. This is usually overridden only in special cases.
After this has happened, the object is ready to be used.
Other code can then interact with the object,
by calling functions on it and accessing its attributes.
Eventually, it will finish being used, and can be destroyed.''''

''''In some situations, two (or more) objects can be referred to by each other only,
and therefore can be deleted as well.
The del statement reduces the reference count of an object by one,
and this often leads to its deletion.
The magic method for the del statement is __del__.
The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name
or placed in a container (list, tuple, or dictionary). The object's reference
count decreases when it's deleted with del, its reference is reassigned, or
its reference goes out of scope.
When an object's reference count reaches zero, Python automatically deletes it.
''''#Example:
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42>
c = [a]  # Increase ref. count  of <42>

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42>
c[0] = -1  # Decrease ref. count  of <42>

#Lower level languages like C don't have this kind of automatic memory management.

''''Data Hiding

A key part of object-oriented programming is encapsulation, which involves packaging
of related variables and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of
a class should be hidden, and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes,
which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as
"we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class.
Hence there are no ways of enforcing a method or attribute be strictly private.
However, there are ways to discourage people from accessing parts of a class,
 such as by denoting that it is an implementation detail, and should be used at their own risk.''''

''''Data Hiding

Strongly private methods and attributes have a double underscore at the
beginning of their names. This causes their names to be mangled, which means
that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid
bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name.
The method __privatemethod of class Spam could be accessed externally
with _Spam__privatemethod.''''
#Example:
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)


#Basically, Python protects those members by internally changing the name to
#include the class name.

''''Class Methods

Methods of objects we've looked at so far are called by an instance of a class,
which is then passed to the self parameter of the method.
Class methods are different - they are called by a class, which is passed to the
cls parameter of the method.
A common use of these are factory methods, which instantiate an instance of a
class, using different parameters than those usually passed to the class
constructor.
Class methods are marked with a classmethod decorator.'''
#Example:
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

''''new_square is a class method and is called on the class, rather than on an
instance of the class. It returns a new object of the class cls.
Technically, the parameters self and cls are just conventions; they could be
changed to anything else. However, they are universally followed, so it is wise
to stick to using them.'''

'''Static Methods

Static methods are similar to class methods, except they don't receive any
additional arguments; they are identical to normal functions that belong to a
class. They are marked with the staticmethod decorator.'''
#Example:
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)

''''Static methods behave like plain functions, except for the fact that you can
call them from an instance of the class.''''

''''Properties

Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.'''
#Example:
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

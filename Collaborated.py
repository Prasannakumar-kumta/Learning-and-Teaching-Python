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

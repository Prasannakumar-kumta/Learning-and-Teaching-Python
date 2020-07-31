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

'''Writing Files:To write to files you use the write method, which writes a string to the file.'''
#For example:
file = open("Personal_Assistant.py", "w")
file.write("This has been written to a file")
file.close()

file = open("Personal_Assistant.py", "r")
print(file.read())
file.close()

#The "w" mode will create a file, if it does not already exist.

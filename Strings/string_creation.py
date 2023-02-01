# String in python is a sequence of characters. In python, string is a data type. 
# We can create a string by enclosing characters inside a single quote or double quotes. 
# For example −

string1 = "Hello Billionaire!"
print(string1)

string2 = 'He said "He is a Billionaire and will Help a lot of People" during an interview.'
print(string2)

string3 = '''This is how we can write
             multiple lines in python.'''
print(string3)

name  = "AyUsH"
string4 = " is my name"
print(string4 + name)

# Accessing the character in a string

print(name[0])
print(name[-1])
print(name[2:4])

# Looping through the string

for letter in string1:
    print(letter)

for letter in string2:
    print(letter,end=" ")


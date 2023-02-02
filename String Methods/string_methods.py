# Strings are immutable in Python

name = "AYUSH WASE"

print(len(name)) # Length of the string
print(name.upper()) # Convert to upper case
print(name.lower()) # Convert to lower case

name1 = "!!!! ayush wase !!!!!!!!!!!!!!!"
print(name1.rstrip("!")) # (right strip ) Remove the trailing characters only the last character and not the starting character
print(name1.lstrip("!")) # (left strip )Remove the leading characters only the first character and not the last character

print(name1.replace("ayush", "Ayush")) # Replace the string

name2 = "Ayush Wase"
print(name2.split(" "))  # Split the string into a list

blog = "introduction to python"
print(blog.capitalize()) # Capitalize the first letter of the string

str = "Welcome to the world of python programming"
print(str.center(100, "*")) # Center the string
print(len(str)) # Length of the string

print(str.count("o")) # Count the number of times "o" is present in the string

print(str.find("python")) # Find the index of the string

print(str.endswith("ing")) # Check if the string ends with "ing"

str1 = "Welcometotheworldofpythonprogrammingbaby"
print(str1.isalnum()) # Check if the string is alphanumeric if it is not then it returns false

print(str1.islower()) # Check if the string is in lower case

str2 = "I wish you all the very best"
print(str2.isprintable()) # Check if the string is printable

str3 = "      "
print(str3.isspace()) # Check if the string has space

str4 = "I Am A Billionaire"
print(str4.istitle()) # Check if the string is have each starting letter in upper case or capital letter

print(str4.startswith("I")) # Check if the string starts with "I" i.e. given input

print(str4.swapcase()) # Swap the case of the string i.e. from upper to lower and lower to upper

print(str2.title()) # Convert the string into title case

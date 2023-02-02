# string can be sliced using index
name = "AYUSH"
print(name[2:4])

# to print the last letter of the word we could use the -1 index
print(name[-1])

# to know the length of the string we can use len() function
print(len(name))

# to print first two letter of the word name
print(name[:2]) # here we are not giving the starting index so it will start from 0

print(name[:]) # here we are not giving any index so it will print the whole string 

print(name[:-2]) # here we are not giving the ending index so it will print the whole string except the last two letter

print(name[-4:-2]) # here we are giving the starting and ending index so it will print the string from the starting index to the ending index


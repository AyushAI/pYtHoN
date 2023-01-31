# typecasting in python is used to convert the data type of the variable to another data type
# there are two types of typecasting in python
# 1. Implicit Typecasting
# 2. Explicit Typecasting

# 1.Implicit Typecasting
# Implicit Typecasting is done by python interpreter automatically when we perform operations on different data types
# for example

a = 10
b = 10.5
c = a + b
print(c)
print(type(c))

# or

a = "1"
b = "2"
c = a + b
print(c)
print(type(c))


# 2. Explicit Typecasting 
# Explicit Typecasting is done by python programmer manually by using predefined functions like int(), float(), str(), etc.
# for example

a = 10
b = 10.5
c = a + int(b)
print(c)
print(type(c))

# or

a = "1"
b = "2"
c = int(a) + int(b)
print(c)
print(type(c))

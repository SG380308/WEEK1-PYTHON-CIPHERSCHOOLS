num1=2
print(num1)
num1=4
print(num1)

# we can store string, number and characters.

name="PC"
print(name)
name="PC"
print(name) # This shows python is a dynamic language.

# Rules-

# first letter should be a letter or _ and not be a number or character.
# 1number = 3 (wrong variable type)

name="PC"
_name="PC"

user_one_name = "PC"  # Snake case writing
UserOneName = "PC"  # Camel case writing

# we can n't use space between words used in name of a variable.

#         Assigning values to variables-

# Different values to multiple variables-
name,age = "PC",19
print("Hello " + name + " your age is " + str(age))

# Same value to multiple variables-
x=y=z=3
print(x+y+z)
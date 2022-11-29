# Strings
# Collection Of Characters inside single quotes or double quotes.

first_name = "Hello"
last_name = "World"

# Concatenation of Strings- This refer to adding to strings

print(first_name +" " + last_name)
# or
full_name = first_name + last_name
print(full_name)

# In concatenating of string we can not add a number to a string it gives type error
# print(first_name + 9) To write this make 9 a string
print(first_name + '9') 
print(first_name + str(9))

# To print a string multiple time so, make use of *
print(first_name*4)
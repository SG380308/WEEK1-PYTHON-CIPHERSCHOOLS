# Problem- take two comma separated inputs from user
#       1. user's name , example - "PC"
#       2. a single character , "P"

# Output- 2 print lines
#      1. user's name length
#      2. count the character that user input (bonus : case insensitive count)

name,char = input("Enter your name and character that you want to count :").split(",")
print(len(name))
name_l=name.lower()
char_l=char.lower()
print(name_l.count(char_l))
# From module sys import argv object.
# sys module allow interact with 
# python interpreter
from sys import argv

# 'argv' handle two arguments.
# This arguments are passed through console
script, filename = argv

# This variable use the filename unpacked via 'argv'
txt = open(filename)

# Print what is in file name
print("Here's your file %r:" % filename)
# Print what is in the file
print(txt.read())
txt.close()

# Print that: type the filename again
print("Type the filename again:")
# Varibale to handle input from user
file_again = input("> ")

# Variable to open file_again variable
txt_again = open(file_again)

# Print what is in the file
print(txt_again.read())
txt_again.close()


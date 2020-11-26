# From sys module import just on object: 'argv
# Remember, sys provide interaction with 
# python interpreter
from sys import argv

# Two arguments variables: script and filename
script, filename = argv

# To erase in the 'filename'
print("We're going to erase %r." % filename)
# If not... erase
print("If you don't want that, hit CTRL-C (^C).")
# If yes... erase
print("If you do want that, hit RETURN.")

# Just prompt without assign to a variable
input("?")

# Open the file
print("Opening the file...")
# Assign to 'target' variable the file object in write
# mode. When we don't specify the mode; default mode 'read: r'
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# Empty the file
target.truncate()

# What are going to write...
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Write the text and add new line (\n)
# \n: escape sequence
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

# Always close the file...
print("And finally, we close it.")
target.close()

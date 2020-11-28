# From module sys import the object argv
from sys import argv

# Argument variable (argv) takes 
# two arguments from console
script, input_file = argv

# Function that read the 
# content of the file
def print_all(f):
    print(f.read())

# Function that sets the file's 
# current position at the offset
def rewind(f):
    f.seek(0)

# Function that print line_count
# and f.readline()
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file
current_file = open(input_file)

# More print...
print("First let's print the whole file:\n")

# Call function
print_all(current_file)

# More print...
print("Now let's rewind, kind of like a tape.")

# Call function
rewind(current_file)

# More print...
print("Let's print three lines:")

# Variable to store current line
current_line = 1
# Call function
print_a_line(current_line, current_file)

# Variable to store current line
current_line += 1
# Call function
print_a_line(current_line, current_file)

# Variable to store current line
current_line += 1
# Call function
print_a_line(current_line, current_file)

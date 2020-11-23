# variable 'x' with a string value and formatter 
x = "There are %d types of people." % 10
# string variable
binary = "binary"
# string variable
do_not = "don't"
# variable 'y' with a string value and two formatters 
y = "Those who know %s and those who %s." % (binary, do_not)

# printing 'x' and 'y' variables
print(x)
print(y)

# printing 'x' variable in formatte character
print("I said: %r." % x)
# printing 'y' variable in formatte character
print("I also said: '%s'." % y)

# hilarious variable with a boolean value
hilarious = False
# string variable used formatte character
joke_evaluation = "Isn't that joke so funny?! %r"
# printing through formatte character
print(joke_evaluation % hilarious)

# string variables
w = "This is the left side of..."
e = "a string with a right side."

# printing 'w' and 'e' variables
print(w + e)
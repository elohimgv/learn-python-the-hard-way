# Function or command: chesese_and_crackers.
# It takes two arguments.
def chesese_and_crackers(cheese_count, boxes_of_crackers):
    # Print cheese_count var with format string
    print("You have %d cheeses!" % cheese_count)
    # Print boxes_of_crackers var with format string
    print("You have %d boxes of characters!" % boxes_of_crackers)
    # More printing...
    print("Man that's enough for a party!")
    # ...more printing and implement a new line 
    # with escape sequence: '\n'
    print("Get a blanket.\n")

# Explain a way of implement the function
print("We can just give the function numbers directly:")
# Call function
chesese_and_crackers(20, 30)

# Explain a way of implement the function
print("OR, we can use variables from our script:")
# Some variables 
amount_of_cheese = 10
amount_of_crackers = 50

# Call function
chesese_and_crackers(amount_of_cheese, amount_of_crackers)

# Explain a way of implement the function
print("We can even do math inside too:")
# Call function
chesese_and_crackers(10 + 20, 5 + 6)

# Explain a way of implement the function
print("And we can combine the two, variables and math:")
# Call function
chesese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
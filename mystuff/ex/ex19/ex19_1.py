# 10 different ways to run a function

def text_with_escape(txt, num, escape):
    print("%s %s" % (escape, txt) * num)

# Call functions
text_with_escape('Sun', 10, '\t') # First way 
text_with_escape('Moon', 5, '\v') # Second way
text_with_escape('Mercury', 6, '\n') # Third way
text_with_escape('Venus', 5, '\\') # Fourth way
text_with_escape('Mars', 9, '\'') # Fiveth way
text_with_escape('Jupiter', 8, '\"') # Sixth way
text_with_escape('Saturn', 7, '\b') # Seventh way
text_with_escape('Uran', 4, '\f') # Eigth way
text_with_escape('Neptune', 3, '\\\n') # Nineth way
text_with_escape('Pluton', 4, '\"\v') # Tenth way
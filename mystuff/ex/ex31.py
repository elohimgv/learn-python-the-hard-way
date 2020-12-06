doors = """
You enter a dark room with five doors. 
Do you go through door #1, #2, #3, #4 or #5
""" 

# Unformated console output
print(doors) 

door = input("> ")

# 1th DOOR
if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats you legs off. Good job!")
    else:
        # Formatted string
        print("Well, doing %s is probably better. Bear runs away." % bear)
# 2nd DOOR
elif door == "2":
    print("Your state into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
# 3rd DOOR
elif door == "3":
    print("Don't worry! you have the power to break your fears.")
    print("What need to know to be able?")
    print("1. Consciousness")
    print("2. Peace")
    print("3. Love")

    triad = input("> ")

    if triad == "1":
        print("Consciousness is synonym of light.\n"
              "Every act must be in one state: 'light'.\n"
              "Light is knowing what to do in each moment;\n"
              "using the necessary amount of energy,\n"
              "no more no less, just enough."
             )
    elif triad == "2":
        print("Whe I am at peace with myself...")
        print("I am in state of grace with everything.")
    elif triad == "3":
        print("Love in its purest form is pure energy.")
# 4th DOOR
elif door == "4":
    print("What is the internal force?")
    input("would you like to know? type ENTER")
    print()
    print("The internal force are energy emanating")
    print("from ourselves because are peace inside us.")
    print("No matter external noise... if we do not")
    print("react to external stimuli the internal")
    print("force are big...")
# 5th DOOR
elif door == "5":
    print("Here is nothing! XD")
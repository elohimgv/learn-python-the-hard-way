# Global variables of type integer
people = 30
cars = 40
buses = 15

# if true and if not, go to the next condition
if cars > people:
    print("We should take the cars.")
# if true and if not, go to the next condition
elif cars < people:
    print("We should not take the cars.")
# if no one is true, the the last condition is true
else:
    print("We can't decide.")

# if true and if not, go to the next condition
if buses > cars:
    print("That's too many buses.")
# if true and if not, go to the next condition
elif buses < cars:
    print("Maybe we could take the buses.")
# if no one is true, the the last condition is true
else:
    print("We still can't decide.")

# if true and if not, go to the next condition
if people > buses:
    print("Alright, let's just take the buses.")
# the the last condition is true
else:
    print("Fine, let's stay home then.")
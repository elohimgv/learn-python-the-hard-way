def while_loop(count, increment):
    i = 0
    numbers = []

    while i < count:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

def foor_loop(min, max):
    numbers = []

    for i in range(min, max):
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

# call function
#while_loop(8, 2)
foor_loop(0, 6)
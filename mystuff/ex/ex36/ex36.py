# Program that reduce any 
# numerical figure to a digit. 
from sys import argv

# Argument variable
script, num = argv

def iterator(num):
    """Function the iterate over the numerical figure, 
       and know its numerical composition; How many times 
       does 0, 1, 2, 3... appear? Multiply the occurrences 
       by the value of each number, to know the total value 
       (value occurrences of the number). Finally add up all 
       the total values and give me a final total."""
    total_one = 0
    total_two = 0
    total_three = 0
    total_four = 0
    total_five = 0
    total_six = 0
    total_seven = 0
    total_eight = 0
    total_nine = 0

    main_total = 0

    count_one = 0
    count_two = 0
    count_three = 0
    count_four = 0
    count_five = 0
    count_six = 0
    count_seven = 0
    count_eight = 0
    count_nine = 0
    
    for cycle in num:
        if cycle == '0':
            pass    
        elif cycle == '1':
            one = 1
            count_one += 1
            total_one = one * count_one
        elif cycle == '2':
            two = 2
            count_two += 1
            total_two = two * count_two
        elif cycle == '3':
            three = 3
            count_three += 1
            total_three = three * count_three
        elif cycle == '4':
            four = 4
            count_four += 1
            total_four = four * count_four
        elif cycle == '5':
            five = 5
            count_five += 1
            total_five = five * count_five
        elif cycle == '6':
            six = 6
            count_six += 1
            total_six = six * count_six
        elif cycle == '7':
            seven = 7
            count_seven += 1
            total_seven = seven * count_seven
        elif cycle == '8':
            eight = 8
            count_eight += 1
            total_eight = eight * count_eight
        elif cycle == '9':
            nine = 9
            count_nine += 1 
            total_nine = nine * count_nine
        else:
            print("Is not a number!")

    main_total = (total_one + total_two + total_three + 
                  total_four + total_five + total_six + 
                  total_seven + total_eight + total_nine)

    #return main_total
    if main_total < 10:             
        return main_total
    else:
        return iterator(str(main_total))

# Call function
print(iterator(num))
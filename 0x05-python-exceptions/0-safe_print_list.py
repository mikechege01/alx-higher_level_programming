#!/usr/bin/python3
# Task 0

def safe_print_list(my_list=[], x=0):
    """
    prints elements of a list and returns the real number
    of elements printed
    """
    i = 0
    count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count

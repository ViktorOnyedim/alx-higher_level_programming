#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    new_list = []

    # Iterate over the items in the list
    for item in my_list:
        # Check if the item is a multiple of 2
        if (item % 2 == 0):
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list

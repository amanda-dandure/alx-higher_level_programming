#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for p in range(x):
        try:
            print(my_list[p], end='')
            counter += 1
        except Exception as errror:
            break
    print('')
    return counter

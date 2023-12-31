#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for p in range(list_length):
        result = 0
        try:
            result = my_list_1[p] / my_list_2[p]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            div.append(result)
    return div

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp = 0
    for a in range(0, list_length):
        try:
            temp = my_list_1[a] / my_list_2[a]
        except TypeError:
            temp = 0
            print("wrong type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            pass
        new_list.append(temp)
    return (new_list)

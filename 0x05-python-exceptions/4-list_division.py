#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    newlist = []
    while i < list_length:
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            i += 1
            if len(newlist) < i:
                newlist.append(0)
    return (newlist)

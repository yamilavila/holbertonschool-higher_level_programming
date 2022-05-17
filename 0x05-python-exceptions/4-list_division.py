#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    reslt = 0
    for a in range(list_length):
        try:
            reslt = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newlist.append(reslt)
            reslt = 0
    return newlist

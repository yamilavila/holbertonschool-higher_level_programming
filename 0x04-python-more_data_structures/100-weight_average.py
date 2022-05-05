#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    item = 0
    valor = 0
    for score, weight in my_list:
        item += score * weight
        valor += weight
    return item / valor

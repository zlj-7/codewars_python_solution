#!/bin/bash
# -*- encoding: utf-8 -*-
'''
    @File	:	parseInt.py
    @TIme	:	2021/07/24 17:52:52
    @Author	:	code7thday
    @Email	:	coldzlj@gmail.com
'''

# here put the import package


class Parametets(object):
    def __init__(self) -> None:
        """
        initalize
        """
        pass
    
    @property
    def number_map(self) -> dict:
        """
        get number dictionary
        """
        number_map = {
            "": 0,
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90
        }
        return number_map
    
    @property
    def quantity_map(self) -> dict:
        """
        get quantity dictionary
        """
        
        quantity_map = {
            "hundred": 100,
            "thousand": 1000,
            "million": 1000000,
        }
        return quantity_map

params = Parametets()
number_map = params.number_map
quantity_map = params.quantity_map

def parse_int(string) -> int:
    """
    parsing number string to integer. 
    args:
        string -> str: number string
    returns:
        number -> int: parsing result
    """
    if string == "":
        return 0
    string = string.replace(" and", "").replace("-", " ")
    number_list = string.strip().split(" ")
    if len(number_list) == 1 or (len(number_list) == 2 and number_list[-1] == ""):
        return number_map[number_list[0]]
    elif "million" in string:
        p = string.split("million")
        return quantity_map["million"] * parse_int(p[0]) + parse_int(p[1])
    elif "thousand" in string:
        p = string.split("thousand")
        return quantity_map["thousand"] * parse_int(p[0]) + parse_int(p[1])
    elif "hundred" in string:
        p = string.split("hundred")
        return quantity_map["hundred"] * parse_int(p[0]) + parse_int(p[1])
    else:
        return parse_int(number_list[0]) + parse_int(number_list[1])

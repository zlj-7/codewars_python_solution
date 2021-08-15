# -*- encoding: utf-8 -*-
"""
    @File	:	Elemental Words.py
    @TIme	:	2021/08/13 10:12:32
    @Author	:	code7thday
    @Email	:	coldzlj@gmail.com
"""

# here put the import package
from queue import Queue

ELEMENTS = {}
        
def elemental_forms(word):
    """elemental forms

    Args:
        word (str): word string

    Returns:
        result (list): combinations
    """
    
    Q, result, prefix = Queue(), [], ""
    upper_normal_mapping = dict()
    for key in ELEMENTS:
        upper_normal_mapping[key.upper()] = key    
        
    Q.put(([], 0))
    word = word.upper()
    while not Q.empty():
        combo, left = Q.get()
        if left == len(word):
            tmp = []
            for key in combo:
                true_key = upper_normal_mapping[key]
                tmp.append("{} ({})".format(ELEMENTS[true_key], true_key))
            result.append(tmp)
            continue
        prefix = ""
        for i in range(left, min(left + 3, len(word))):
            prefix += word[i]
            if prefix in upper_normal_mapping:
                Q.put((combo + [prefix], i + 1))
    
    return result
    
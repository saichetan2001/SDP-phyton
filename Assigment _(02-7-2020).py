# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:36:19 2020

@author: HP
"""



#1.Write a Python program to create a tuple
tuple = ( 3.2, 1)
print(tuple)

#2.Write a Python program to create a tuple with different data types
tuple = ("tuple", False, 3.2, 1)
print(tuple)

#3.Write a Python program to convert a tuple to a string
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

tuple = ('g', 'e', 'e', 'k', 's') 
str = convertTuple(tuple) 
print(str) 

#4.Write a Python program to slice a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)
_slice = tuplex[5:]
print(_slice)
_slice = tuplex[:]
print(_slice)

#5.Write a Python program to find the length of a tuple.
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(len(tuplex))

#6.Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

#7.Write a Python program to reverse a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex[::-1])

#8.Write a Python program to convert a list of tuples into a dictionary
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)

#9.Write a Python program to convert a list to a tuple.
def convert(list): 
    return tuple(list) 
 
list = [1, 2, 3, 4] 
print(convert(list)) 
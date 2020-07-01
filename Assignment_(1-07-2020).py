# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:52:34 2020

@author: HP
"""



#1. Write a Python program to sum all the items in a list.
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

#2. Write a Python program to create a list of empty dictionaries
n = 5
l = [{} for _ in range(n)]
print(l)

#3. Write a Python program to access dictionary keys element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])

#4. Write a Python program to iterate over dictionaries using for loops
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 

#5. Write a Python program to sum all the items in a dictionary.
     
   my_dict = {'data1':100,'data2':-54,'data3':247}
   print(sum(my_dict.values()))

#6. Write a Python script to concatenate following dictionaries to create a new
    # one. Sample Dictionary :
   dic1={1:10, 2:20}
   dic2={3:30, 4:40}
   dic3={5:50,6:60} 
   dic4={}
   for d in (dic1,dic2,dic3): dic4.update(d)
   print(dic4)
. 
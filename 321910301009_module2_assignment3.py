#1. Write a Python program to find area of a circle using math function.
import math

r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r

print("Area of the circle is : %.2f" %area)


#2. Write a program to find Area of Regular Polygon using math function.
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

#3. Write a program to find Area of a Segment of a Circle Formula using
math function.

def sectorarea():
    pi=22/7
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (pi*radius**2) * (angle/360)
    print("Sector Area: ", sur_area)

sectorarea()

# 4 Write a python program to shuffle list l1=[100,1,2,3,30,40,”hai”,”hello”].
import random

# initializing list
l1=[100,1,2,3,30,40,"hai","hello"]

# Printing original list
print ("The original list is : " + str(l1))

# using random.shuffle()
# to shuffle a list
random.shuffle(l1)

# Printing shuffled list
print ("The shuffled list is : " +  str(l1))

# 5. Write a program to generate random numbers between 1,10000 and
difference between each random number is 50.

print(list(range(1,10000,50)))

#6. Write a python program by using math module to find
#i. Sin60
import math
print(math.Sin60)
#ii. cos(pi)
from math import pi
print(math.cos(pi))
#iii. tan90 0
print(math,tan(90))
#iv. angle of sin(0.8660254037844386)
print('The angle of sin(0.8660254037844386): ' + str(math.degrees(math.asin(0.8660254037844386))))
#v. 5^8
print('The value of 5^8: ' + str(math.pow(5, 8)))
#vi. Square root of 400
print('Square root of 400: ' + str(math.sqrt(400)))
#vii. The value of 5^e
print('The value of 5^e: ' + str(math.exp(5)))
#viii. The value of Log(1024), base 2
print('The value of Log(1024), base 2: ' + str(math.log2(1024)))
#ix. The value of Log(1024), base 10
print('The value of Log(1024), base 10: ' + str(math.log10(1024)))
#x. The Floor and Ceiling value of 23.5
import math
print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

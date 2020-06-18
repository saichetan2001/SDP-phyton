#1>phyton program for simple calculator
#Addition
a=float(input("enter a"))
b=float(input("enter b"))
add=a+b
print ("sum= ",float(add))

#subraction
if a>b:
    sub=a-b
else:
    sub=b-a
print("differece is ",float(sub))

#multiplication/product
product=a*b
print("product is ",float(product))

#division
if a>b:
    div=a/b
else:
    div=b/a
print("divisior is ",float(div))

#modulus
if a>b:
    mod=a%b
else:
    mod=b%a
print("reminder is ",float(mod))

#exponent
if a>b:
    exp=a**b
else:
    exp=b**a
print("exponent is ",float(exp))

#floor division
if a>b:
    fd=a//b
else:
    fd=b//a
print("floor division is ",float(fd))

#2> calculate simple instrest
p=float(input("enter priciple amount"))
t=float(input("enter time period"))
r=float(input("enter rate of intrest"))
SI=(p*t*r)/100
print("Simple intrest is ",float(SI))

#3> area of circle
r=float(input("enter the radius of circle"))
area=3.14*(r**2)
print("area of circle is ",float(area))

#4> area of triangle
h=float(input("enter the height of triangle"))
b=float(input("enter base of triangle"))
area=0.5*h*b
print("area of triangle is ",float(area))

#5> celceius to farenhit
c=float(input("enter temperature in celsius"))
farenhit=(c*1.8)+32
print("temperature in farenhit is ",float(farenhit))

#6> area of rectangle
h=float(input("enter the length of rectangle"))
b=float(input("enter base of triangle"))
area=h*b
print("area of rectangle is ",float(area))

#7> perimeter of square
s=float(input("enter the side length of square"))
per=4*s
print("perimeter of square is ",float(per))

#8> circumference of a circles
r=float(input("enter the radius of circle"))
cir=2*3.14*r
print("circumference of a circle is ",float(cir))

#9> swapping of two numbers
a=float(input("enter a num"))
b=float(input("enter a num"))
print("a=",a)
print("b=",b)
c=a
a=b
b=c
print("after swapping")
print("a=",a)
print("b=",b)

# 1> TAke inputs from the and check weather they are equal or not
a= float(input("enter a number"))
b= float(input("enter a number"))
if a==b:
    print("both inputs are equal")
else:
    print ("entered inputs are not equal")

# 2> Take 3 inputs and check weather all are equal,any two are equal or not equal
a= float(input("enter a number"))
b= float(input("enter a number"))
c= float(input("enter a number"))
if a==b and b==c:
    print(" all the values are equal")
elif a==b or b==c or a==c:
    print("two values are equal")
else:
    print("either of the values are not equal")

# 3>Take 2 numbers and find waether the sum the nums are greater or lessthan or equal to five
a= float(input("enter a number"))
b= float(input("enter a number"))
c=a+b
if c==5:
    print("sum of two numbers is equal to five")
if c>5:
    print("sum of two numbers is greaterthan five")
if c<5:
    print("sum of two numbers is lessthan five")

# 4>take the marks of the subject and check they are graeter than pass marks are not
a=float(input("enter the marks"))
if a>=35:
    print(a>=35)
else:
    print(a<35)

# 5> max of three numbers
a= float(input("enter a number"))
b= float(input("enter a number"))
c= float(input("enter a number"))
if a>b and a>c:
    print("a is maximum")
if b>a and b>c:
    print("b is maximum")
if c>b and c>a:
    print("c is maximum")

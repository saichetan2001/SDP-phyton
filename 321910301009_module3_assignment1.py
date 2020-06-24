#2. Generate first N number of Fibonacci numbers. Take N value from user
i1=0
i2=1
x=int(input('enter upto to which fibonacci series should print'))
z=0
while z<=x:
    print(i1)
    nth=i1+i2
    i1=i2
    i2=nth
    z=z+1

#3. Display multiplication table of K. Take k value from user
#Ex: 7 x 1 =7
#7 x 2 = 14 .....
k=int(input('enter the value of k upto which it should print'))
i=1
while i<=k:
    z=7*i
    print("7 x ",k,"=",z)
    i=i+1

#4. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
def gcd(a,b):

    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a

    # base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

# Driver program to test above function
a = int(input("enter the first num"))
b = int(input("enter the another num"))
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

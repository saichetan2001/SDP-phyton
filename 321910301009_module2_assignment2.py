# 1> max of three numbers
a= float(input("enter a number"))
b= float(input("enter a number"))
c= float(input("enter a number"))
if a>b and a>c:
    print("a is maximum")
if b>a and b>c:
    print("b is maximum")
if c>b and c>a:
    #print("c is maximum")

# 2> program for reverse of a string

txt = "Hello World"[::-1]
print(txt)


# pallindrome
try:
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
except:
    print("eneter a valid num")
finally:
    print( "code is working")

 #prime nums
 num = int(input("Enter a number: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")

# sum of squares of n natural numbers
def squaresum(n) :
    return (n * (n + 1) * (2 * n + 1)) // 6
  
n = 4
print(squaresum(n))

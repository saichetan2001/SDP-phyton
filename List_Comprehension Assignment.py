#1.Use for, .split(), and if to create Statement that will print out words that start
#with 's':
 #st = 'Print only the words that start with s in this sentence'

mystring = 'Print only the words that start with s in this sentence'

for word in mystring.split():
    if word[0] == 's':
        print(word)

#2. Use range() to print all the even numbers from 0 to 10.

x=range(0,10,2)
for y in x:
    print(y)
    
#3. Use a List Comprehension to create a list of all numbers between 1 and 50that are divisible by 3.
mylist=[x for x in range(1,50) if x%3==0]
print(mylist)

#4.Go through the string below and if the length of a word is even print "even!"
 #st = 'Print every word in this sentence that has an even number of letters'
 
 
def printWords(s): 
      s = s.split(' ')  
      for word in s:  
          if len(word)%2==0: 
              print(word)  
   
s =  'Print every word in this sentence that has an even number of letters'
printWords(s)

#5. Use List Comprehension to create a list of the first letters of every word in thestring below:
 #st = 'Create a list of the first letters of every word in this string' 
mystring = 'Create a list of the first letters of every word in this string' 
words = mystring.split()
for char in words:
    first_char_list = char[0]
    print(list(first_char_list)) 
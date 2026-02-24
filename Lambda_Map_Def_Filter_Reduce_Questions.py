"""
Python Programming Questions
(Function,lamda,map,filter,reduce)

#1.Question on def(Function)
#Basic




#1.Write a function to add two numbers.
def add(n1,n2):
    return n1+n2
print(add(50,60))
#Expected output:110



#2.Write  a function to fine square  of a number.

def squar(num):
    return num**2
print(squar(9))
#Expected output:81

#3.Write a function to check even or odd.
def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(check(17))
#Expected output:odd


#4.Write a funtion to find maximum of two numbers.
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(50,96))
#Expected output: 96


#5.Write a function to count vowels in string.
def count(st):
    vowels = "AEIOUaeiou"
    count = 0
    for ch in st:
        if ch in vowels:
            count = count+1
    return count

print(count("Programming"))
#Expected output: 3





#Medium
#6.Write  a function  to check palindrome string.
def check(st):
    if st==st[: : -1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(check("madam"))
#Expected output:-Palindrome

#7.Write a function to find factorial of a number.
def factorial(num):
    f = 1
    for x in range(1,num+1):
        f = f*x
    return f
print(factorial(8))

#Expected output: 40320



#8.Write a  function  to return second largest numbers from a list.
def secondlargest(li):
    li = [12,56,89]
    li.sort()
    s = li[-2]
    return s
print(secondlargest([12,56,89]))

#Expected output: 56



#9.Write a function  to remove duplicate from a list.
def duplicate(li):
    li = [12,45,78,65,12,59,12]
    li = list(set(li))
    return li
print(duplicate([12,45,78,65,12,59,12]))
#Expected output: [65, 12, 45, 78, 59]



#10.Write  a function  calculate fibonacci series.



#Advanced


#11.Write a recursive function for factorial.
def factorial(num):
    if num==1:  
        return 1
    else:
        return num * factorial(num-1)
print(factorial(9))
    
#Expected output: 362880


#12.Write a function  to find GCD of two numbers.
def find(a,b):
    gcd = 1
    for x in range(1,11):
        if a%x==0 and b%x==0:
            gcd = x
    return gcd
print(find(20,35))
#Expected output: 5

#13.Write  a function to check prime number.
def check(num):
    for x in range(2,num):
        if num%x==0:
            return False
        return True
    
if check(7):
    print("Prime")
else:
    print("Not prime")
 

#14.Write a function to count frequency of characters in a string.
def frequency(st):
    freq = []
    for ch in set(st):
        freq.append((ch,st.count(ch)))
    return freq
print(frequency("Python is a language"))
        

#15.Write  a function that accepts any number of arguments and return sum.
def  number(*a):
    s = 0
    for x in a:
        s += x
    return s
print(number(82,69,74,63))
#Expected output: 288


#2.Questions on Lambda
#1.Write a lambda function to add two numbers.
add = lambda n1,n2: n1+n2
print(add(52,63))
#Expected output: 115


#2.Write a lambda function to check even number.
even = lambda num : "Even" if num%2==0 else  "Odd"
print(even(12))


#3.Write a lambda function to find maximum fo two numbers.
maximum = lambda a,b: a if a>b else b
print(maximum(45,80))
#Expected output:  80


#4.Write a lambda to return square of a number.
square = lambda num: num**2
print(square(6))
#Expected output: 36

#5.Write  a lambda to return "Pass" if marks>40 else "Fail".
ret = lambda marks: "Pass" if marks>40 else "Fail"
print(ret(80))
#Expected output: Pass

#3Question on map()
#1.Use map() to square all elements in a list.
square =  lambda num: num**2
li = [x for x in range(1,11)]
s = list(map(square,li))
print(s)
#Expected output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#2.Use map () to convert list of strings into uppercase.
li = [ "Programming"]
upper = list(map(lambda st: st.upper(),li))
print(upper)

#Expected output: ['PROGRAMMING']


#3.Use map() to convert list of strings into integers.
st = ["45","89","12","42"]
integ = list(map(int,st))
print(integ)
#Expected output: [45, 89, 12, 42]

#4.Use map() to add elements of two lists.
li1 = [1,2,3,4,5,6,7,8]
li2 = [9,10,11,12,13,14]
li3 = list(map(lambda a,b: a+b,li2,li2))
print(li3)


#5.Use map() to find length of each word in a list.
li = ["Kishan","Komal"]
word = list(map(len,li))
print(word)
#Expected output:[6, 5]


#Questions on filter()
#1.Use filter () to get even numbers from a list.
li = [12,6,13,18,14]
even = list(filter(lambda num: num%2==0,li))
print(even)
#Expected output: [12, 6, 18, 14]


#2.Use filter() to get odd numbers from a list.
li = [3,5,7,12,14,19]
odd = list(filter(lambda num: num%2==1,li))
print(odd)
#Expected output:  [3, 5, 7, 19] 


#3.Use filter ()to get numbers greater than 50.
get = lambda num: num>=50
li = [45,78,90,88,99]
greater = list(filter(get,li))
print(greater)
#Expected output: [78, 90, 88, 99]


#4.Use filter () to get words starting with vowel.
st = ["Apple","Banana","Orange"]
vowel = "AEIOUaeiou"
words = list(filter(lambda word: word[0] in vowel,st))
print(words)
#Expected output: ['Apple', 'Orange']


#5.Use filter() to get prime numbers from a list.


#5.Question on reduce()
#(Use from functools import reduce)
#1.Use reduce() to find sum of elements in a list.
from functools import reduce
li = [34,56,78,90,12]
s  = reduce(lambda a,b:a+b ,li)
print(s)
#Expected output:270


#2.Use reduce () to find product of elements in a list.
from functools import reduce
li = [1,2,3,4,5]
product = reduce(lambda a,b: a*b,li)
print(product)
#Expected output:120


#3.Use reduce ()to find maximum element in list.
from functools import reduce
li = [23,45,67,89,12,99]
maximum = reduce(lambda *num: max(num),li)
print(maximum)
#Expected output: 99

#4.Use reduce() to  concatenate a list of strings.
from functools import reduce
li = ["Kishan","kumra"]
concaten = reduce(lambda a,b: a+b,li)
print(concaten)
#Expected output:Kishankumra

#5.Use reduce() to flatten a list of lists.
def flatten(li2,x):
    li2 = []
    for x in li:
        if isinstance(x,list):
            li2.extend(x)
        else:
            li2.append(x)
    return li2
from functools import reduce
li = [1,2,[3,4],[5,6]]
flatt = reduce(flatten,li,[])
print(flatt)
#Expected output:[1, 2, 3, 4, 5, 6]


#6.Mixed practice Questions
#1.Use map() and lambda to square all numbers in a list.
li = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda num: num**2,li))
print(square)


#2.Use filter () and lambda to get numbers greater than 10.
li = [8,9,45,67,89]
get = list(filter(lambda num: num>=10,li))
print(get)
#Expected output:[45, 67, 89]

#3.Use map() and filter() to square only even numbers.
li = [1,2,3,4,5,6,7,8]
square = list(map(lambda num: num**2,filter(lambda num: num%2==0,li)))
print(square)
#Expected output: [4, 16, 36, 64]

#4.Use reduec () to find factorila of a number.
from functools import reduce
n = 5
fact = reduce(lambda n1,n2:n1*n2,range(1,n+1))
print(fact)
#Expected output:120


#5.From a list,remove duplicates and return only even numbers.
li = [1,2,3,4,5,6,2,4,6]
even = set(filter(lambda num: num%2==0,li))
print(even)

#Interview Basics (Write Answers for these Questions)
#1. Difference between def and lambda.
#2. Difference between map() and filter().
#3. Difference between filter() and list comprehension.
#4. Why reduce() is not a built-in function in Python?
#5. Can lambda have multiple statements

"""

































    
            
        



































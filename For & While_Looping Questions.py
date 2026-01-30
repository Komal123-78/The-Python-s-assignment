"""
For Loop-Programming questions

#1.Write a program to print numbers from 1  ot 100
n = int(input("Enter a number: "))
for z in range(1,n+1):
        print(z)

#2.Write a program to print  all even numbers between 1 and 50.
n = int(input("Enter a  number: "))
for z in range(1,n+1):
    if n%z==0:
        print(z)
#Expected output:1,2,5,10,25,50


#3.Write  a program to print the sum of first n natural numbers.
n = int(input("Enter a number: "))
s =0
for i in range(1,n+1):
    s = s+i
print("Sum of natural_number: ",s)
#Expected output:Sum of natural_number:  55

#4.Write a program  to print the multiplication table of a given number.
n = int(input("Enter a number: "))
for i in range(1,n+1):
        print(n*i)
        
#5.Write a program to print all elements of a list using a for loop.
li = [78,90,45,23,13,56,70]
for y in li:
    print(y)


#6.Write a program to count the number of vowels in a string.
stri = "aieou"
count =0
for i in stri:
    print(i)
    count=count+1
print("Count of vowels: ",count)
#Expected output:Count of vowels:  5


#7.Write a program  to find  the largest number in a list.
number = [56,89,1,23,41,90,]
largest = number[0]
for num in number:
    if num>largest:
        largest = num
print("Largest number: ",largest)
#Expectr output:Largest number:  90



#8.Write a program  to count all prime numbers between 1 and 100.
num = int(input("Enter a number: "))

       

#9.Write a program  to calculate the factorial of a number using  a for loop.
num = int(input("Enter a number: "))
fact = 1
for y in range(1,num+1):
    fact = fact*y
print("Number of factorial: ",fact)
#Expected output:Number of factorial:  720



#10.Write a program to print the reverse of a string using a for loop.
st = "ramgrop"
reverse =" "
for i in st:
    reverse = i+reverse
print(reverse)
#Expect output:porgmar 

#While loop- Programming questions
#11.Write a program to print numbers from 1 to 50 using a while loop.
num = int(input("Enter a number: "))          
a =1
while a<=num:
    print(a)
    a = a+1

#12.Write a program  to print all odd numbers between 1 and 50.
num = int(input("Enter a number: "))
a = 1
while a<=num:
    if num%a==1:
        print(a)
    a = a+1
#Expected output:7,49



#13.Write  a program to calculate the sum of digits of a number.
num = int(input("Enter a number: "))
digit = 0
a = 1
while a<=num:
    rem = num%10
    digit = digit+rem
    num = num//10
print(digit)
#Expected output:14


#14.Write a program to reverse a number  using  a while  loop.
num = int(input("Enter a number: "))
reverse = 0
a = 1
while a<=num:
    rem = num%10
    reverse = reverse*10+rem
    num = num//10
print(reverse)
#Expected output:235



#15.Write a  to find the factorial of a  number using a while loop.
num = int(input("Enter a number: "))
fact = 1
a = 1
while a<=num:
    fact = fact*a
    a = a+1
print("Number of factorial:",fact)
#Expected output:Number of factorial: 362880


#16.Write  a program to keep taking input from the user until the user enters 0.
num = int(input("Enter a number: "))
a = 0
while num!=a:
    num = int(input("Enter a number: "))
    if num==a:
        print("Found a number")
#Expected output:Found a number


#17.Write a program to find the largest digi in a number.
#Write a program  to check whether a number is  a palindrome.
num =  int(input("Enter a number: "))
copy = num
add = 0
a = 1
while a<=num:
    rem = num%10
    add = add*10+rem
    num = num//10
if copy==add:
    print("Palindrome: ",add)
else:
    print("Not Palindrome: ",add)
#Expected output:Palindrome:  121

#19Write a program to print the  fibaoncci series up to n terms.
# 0,1,1,2,3,5,8,13,21,34,
a = 0
b = 1
while a<=10:
    c = a+b
    a = b
    b = c
    print(a)
#Expected output:
1    
1
2
3
5
8
13





#20.Write a program  to  implement a number guessing game using a  while loop.
num = int(input("Enter a number:"))
a = 11
while a!=num:
    num = int(input("Enter a number: "))
    if num==a:
        print("Winner")
#Expected output:Winner


#21.Write a program  to print a number patten using loop.
st = ""
for x in range(1,6):
    st = st+str(x)
    print(st)
#Expected output:
1    
12
123
1234
12345


#22.Write a program to count the frequency of each character in a strin.
st = "Programing"
dic = dict()
for ch in st:
    dic.update({ch:st.count(ch)})
    print(dic)
    
#23.Write  a program to print all armstrong numbers between 1 and 1000.




#24.Write a program  to simulate an ATM menu using  a while loop.
#25.Write  a program  to find the GCD of two numbers using loops.
num_1 = 20
num_2 = 35
gcd = 1
for x in range(1,num_1+1):
    if num_1%x==0 and num_2%x==0:
        gcd = x
print(gcd)
#Expected output:5
        
"""

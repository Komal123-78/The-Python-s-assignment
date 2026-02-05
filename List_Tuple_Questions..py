"""
List_Tuple_Questions
Python Programming questions-List
Basic Level

#1.Write a python program to create a list of integers and print its elements.
li = [45,67,48,32,89,10,]
print( li )
#Expected output:[45, 67, 48, 32, 89, 10]



#2.Write a program to find the sum and average of all elements in a list
li = [45,67,48,32,89,10,]
print( sum(li)/len(li) )
#Expected output:48.5




#3.Write a program to find the largest and smallest elements in a list.
li = [19,23,52,70,34,29,76]
print(max(li))
print(min(li))
#Expected output:[Largest element, 76],[smallest element,19]



#4.Write a python program to count the number of elements in a list without using len().
li = [47,80,34,28,16,80,59]
count = 0
for i in li:
    print(i)
    count=count+1
print("Number of elements:",count)    
#Expected output:Number of elements: 7


#5.Write a program to reverse a list without using buli-in functions.
li = [25,39,43,71,98,52,36,47]
print( li [ : : -1] )
#Expected output:[47, 36, 52, 98, 71, 43, 39, 25]


#6.Write  a program to check if an element exists in a list.
li = [45,67,89,23,16,72,19]
a = 72
if a in li:
    print("element is exists")
else:
    print("element is not exists")
#Expected output:element is exists.


#7.Write a program to  remove duplicate elements from a list.
li = [34,67,89,90,67,23]
uniq_list = set(li)
print(uniq_list)
#Expected output:{34, 67, 23, 89, 90}   

#8.Write  a program to sort a list in ascending and descending order.
li1 = [34,56,78,91,83,80,23]
li2 = [2,67,89,13,60]
li1.sort()
print( (li1) )
li2.reverse()
print( (li2) )
#Expected output:sort.[23, 34, 56, 78, 80, 83, 91]
#                sort.  [60, 13, 89, 67, 2]

#Intermediate Level
#9.Write a program to merge two lists and remove duplictes.
li1 = [1,2,3,4,5,6]
li2 = [5,4,7,8,9,6]
li3 = list(set(li1+li2))
print(li3)
#Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



#10.Write a program to find common elements between two lists.
li1 = [45,67,89,12,6,90]
li2 = [45,43,89,12,4,85]
common = list(set(li1)& set(li2))
print( common )
#Expected output: [89, 12, 45]




#11.Write  a program  to split a list into even and odd numbers.
li = [32,52,74,86,94,12,1,8,67,43,90]
even = []
odd = []
for x in li:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(f"Even_numbers:{even}")
print(f"Odd_numbers:{odd}")
#Expected output: Even_numbers:[32, 52, 74, 86, 94, 12, 8, 90]
Odd_numbers:[1, 67, 43]

#12.Write  a program  to rotate a list by n psitions.
li = [0,1,2,3,4,5,6,7,8,9]
n = int(input("How many Rotation: "))
for x in range(n):
    li. insert(0,li[len(li)-1])
    li.pop(len(li)-1)
print(f"Rotation{li}")
#Expected output: Rotation[4, 5, 6, 7, 8, 9, 0, 1, 2, 3]


#13.Write a program to find the second largest number in a list.
li = [56,40,12,80,90,58]
li.sort()
print(f"second largest_number {li[-2]}")
#Expected output:second largest_number 80


#14.Write a program  to flatten a nested list/
nested_list = [2,3,[56,80],[67,41],89]
flat = []
for x in nested_list:
    if isinstance(x,list):
        flat.extend(x)
    else:
        flat.append(x)
print(flat)
#Expecte output: [2, 3, 56, 80, 67, 41, 89]


#15.Write  a program  to replace all negative number with zero in a list.
numbers = [7,8,5,-1,-2,-3,-9]
for i in range(len(numbers)):
    if numbers[i]<0:
        numbers[i]=0
print(numbers)
#Expected output:[7, 8, 5, 0, 0, 0, 0]
#16.Write  a program  to count frequency of each element in a list.
li = [5,4,1,5,3,4,2,1,8,9,8]
dic = dict()
for x in li:
    dic.update({x : li . count(x)})
print(dic)
#Expected output: {5: 2, 4: 2, 1: 2, 3: 1, 2: 1, 8: 2, 9: 1}






#17.Write a program  to remove all   occurrences of a given element from a list.
li = [1,2,3,4,5,6,7,3]
element = 3
while element in li:
    li.remove(element)
print(li)


#18.Write  a program to check a list is a palindrome.
li = [1,2,3,4,5,4,3,2,1]
if li==li[: : -1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Expected output:Palindrome

#19.Write a python program  to find missing numbers in a given list of consecutive integers.


#20.Write a  program to perform element-wise addition of two lists.
li_1 = [1,2,3,4,5]
li_2 = [6,7,8,9,10]
new_list = []
for x in range(len(li_1)):
    new_list.append(li_1[x] + li_2[x])
print(f"new_list{new_list}")
#Expected output:new_list[7, 9, 11, 13, 15]
    



#21.Write a python program  to find the longest increasing subsequence in a list.
li = [23,56,99,78,6,23,4,56,67,78,99,23,56,99]
lon_ss = []
x = 0
while x<len(li)-1:
    temp = []
    for z in range(x+1,len(li)):
       if li[x]<li[z]:
           temp.append(li[x])
           x=x+1
       else: 
            temp.append(li[x])
            x=x+1
            break
    if len(temp)>len(lon_ss):
            lon_ss = temp.copy()
print(lon_ss)
#Expected output: [4, 56, 67, 78, 99]
        
                        

#22.Write a program to group elements based on frequency.
li = [3,4,2,7,8,5,3,8,9,1,2,3,5,6,7,8,9,4,3,5,6,7,]
group = []
temp = []
for x in li:
    if x not in temp:
        temp.append(x)
        group.append([x]*li.count(x))
print(group)
#Expected output: [[3, 3, 3, 3], [4, 4], [2, 2], [7, 7, 7], [8, 8, 8], [5, 5, 5], [9, 9], [1], [6, 6]]




#Python Programming question-Tuple
#Basic Level
#23.Write  a pyhton program  to create  a tuple  and  print its elements.
tu = (23,45,67,8,9)
print(f"Its elements{tu}")
#Expected output:Its elements(23, 45, 67, 8, 9)

#24.Write  a program  to find the length of a tuple.
tup = (34,56,12,61,71,89,8967)
print(f"Lenght of elements: {len(tup)}")
#Expected output:Lenght of elements: 7



#25.Write  a program  to find the maximum and minimum element in a tuple.
tup = (34,12,56,32,90,78,654)
print(f"maximum: {max(tup)}")
print(f"minmum: {min(tup)}")
#maximum: 654
#minmum: 12



#26.Write a  program to convert  a tuple into a list.
tup = ([23,45,1,46,89,567,32,79])
print(tup)
#Expected output:[23, 45, 1, 46, 89, 567, 32, 79]


#27.Write  a program to check if an element exists in a tuple.
tup = (32,14,56,78,90,98,70,654)
element = 56
if element in tup:
    print("element is exists")
else:
    print("element is not exists")
#Expected output:element is exists



#28.Write a program  to count occurrences of an element in a tuple.
tup = (34,67,345,67,8,90)
element = 67
count = 0
for x in tup:
    if x==element:
        count+=1
print(element,":",count)
#Expected output:67 : 2


#29.Write  a program  to slice a tuple and display the result.
tup = (45,67,12,56,90,23,24)
print(tup[0:6])
#Expected output:(45, 67, 12, 56, 90, 23)


#30.Write  a program  to  find  repeated elements in a tuple.
tup = (34,61,71,89,79,90,34,82,34)
repeated = []
for x in tup:
    if tup.count(x)>1 and x not in repeated:
        repeated.append(x)
print(repeated)
#Expected output:[34]


#31.Write  a program  to merge two tuples.
tup_1 = (45,12,89,36,20,39,51)
tup_2 = (34,29,56,78,91,40,60)
merge = tuple(tup_1+tup_2)
print(merge)
#Expected output:(45, 12, 89, 36, 20, 39, 51, 34, 29, 56, 78, 91, 40, 60)



#32.Write a  program  to unpack elements of a tuple into variables.
tup = (34,56,78)
a,b,c = tup
print(a)
print(b)
print(c)
#Expected output:34
#Expected output56
#Expected output78


#33.Write a python program  to sort  tuple.
tup = (23,1,45,6,7,89,5,)
tup = list(tup)
tup.sort()
tup = tuple(tup)
print(tup)
#Expected output:(1, 5, 6, 7, 23, 45, 89)

#34.Write  a program  to convert a list of  tuples into a dictionary.
elements = [(1,23),(2,56),(3,78)]
dic = dict(elements)
dic.update(elements)
print(dic)
#Expected output:{1: 23, 2: 56, 3: 78}


#35.Write  a program  to find the index of an element in a tuple.t
tup = (34,56,12,78,90,52)
element = 56
if element in tup:
    print(f"Element is in tuple,{tup.index(element)}")
else:
    print("Element is not in tuple")
#Expected output: Element is in tuple,1
 

#36.Write  a program  to remove  an element from a tuple(Without directly modifying it).
tup = (56,12,78,23,90,41,71)
tup = list(tup)
tup.remove(78)
tup = tuple(tup)
print(tup)
#Expected output: (56, 12, 23, 90, 41, 71)



#37.Write a program  to find common element between two tuples.
tup_1 = (34,67,89,12,40,61,78)
tup_2 = (68,34,84,90,40,61,78)
commen = tuple(set(tup_1)& set(tup_2)) 
print(commen)
#Expected output:(40, 34, 61, 78)


#38.Write a  python program  to check if a tuple is a palindrome.
tup = (1,2,3,4,3,2,1)
if tup==tup[: : -1]:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")
#Expected output:  The tuple is a palindrome


#39.Write  a program  to find the element with maximum frequency in a tuple.
tup = (4,67,8,23,69,4,67,4,67,90,67)
max_count = 0
max_element = 1
for x in tup:
    count = tup.count(x)
    if count>max_count:
        max_count = count
        max_element = x
print("element",max_element,"frequency",max_count)
#Expected output: element 67 frequency 4




#40.Write  a program  to create  a nested tuple and access its elements
tup = (32,45,6,8,(89,90,75),80)
for x in tup:
    if isinstance(x,tuple):
        for j in x:
            print(j)
    else:
        print(x)
#Expected output:
32
45
6
8
89
90
75
80



"""







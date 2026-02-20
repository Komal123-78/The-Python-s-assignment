"""
#1.Write a program to count the number of vowles in a string.
st = "Good Morning"
count = 0
vowle = "AEIOUaeiou"
for x in st:
    if x in vowle:
        count +=1
print(count)
#Expected output:4

#2.Reverse a string  without using built-in functions.
st = "aidnI olleH"
reverse = " "
for x in range (len(st)-1,-1,-1):
    reverse = reverse + st[x]
print(reverse)    
    

#3.Check whether a string is a palindrome.
st = "madam"
if st==st[: : -1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#4.Count uppercase and lowercase letters in a string.
st = "Python Programming"
upper_count = 0
lower_count = 0
for ch in st:
    if ch.isupper():
        upper_count +=1
    elif ch.islower():
         lower_count +=1
print(f"Uppercase,{upper_count},Lowercase ,{lower_count}")
#Expected output:Uppercase,2,Lowercase ,15

#5.Replace all spaces in a string with_.
st = "Bye India"
print(st.replace(" ","_"))
#Expected output:Bye_India

# Intermediate
#6.Find the frequency of each character in a string.
st = "Programming"
for x in set(st):
    print(st.count(x),x)
#Expected output:2 m
                 2 r              
                 2 g
                 1 o
                 1 n
                 1 i               
                 1 P
                 1 a    

#7.Remove duplicate characters from a string.
st = "Programming"
for z in set(st):
        print(z)


#8.Find the first non-repeating character in a string.
st = "Sanajana"
for ch in  range (len(st)):
    count = 0
    for j in range(len(st)):
        if st[ch] == st[j]:
             count +=1
    if count ==1:
        print(f" Found non_repeating character,{st[ch]}")
        break
        
else:
    print(f"Not found non_repeating character,{st[j]}")

#Expected output:Found non_repeating character,S

#9.Check if two string are anagrams.
st_1 = "LISTEN"
st_2 = "SILENT"
if len(st_1)==len(st_2):
    for ch in st_1:
        if st_1.count(ch)!=st_2.count(ch):
            print("Strings are not anagram")
            break
    else:
        print("Strings are anagram")
else:
    print("Strings are not anagram")
#Expected output:-  Strings are anagram






#10.Convert "hello world"-> "Hello world (title case without using.title()).
st = "hello world"
convert_word = st[0].upper() + st[1:]
print(convert_word)
#Expected output:Hello world
 

#Tricky
#11.Find the longest word in a sentence.
st = "Data analysts is a amezing course"
words = st.split()
longest_word = words[0]
for ch in words:
    if len(ch)>len(longest_word):
        longest_word = ch
print(f"Longest word: {longest_word}")
#Expected output:- Longest word: analysts



#12.Compress a string like "aaabbc"->"a3b2c1".
st = "aaabbc"
com = ""
count = 1
for ch in range(1,len(st)):
    if st[ch]== st[ch -1]:
        count += 1
    else:
        com += st[ch -1]+ str(count)
        count = 1
com += st[-1] + str(count)        
print(com)
#Expected output:  a3b2c1


#13.Count words,Characters,and digits in a string.
st = "Python programming 12345"
count_words = st.split()
char = 0
digits = 1
for ch in st:
    if ch!=" ":
        char += 1
        if ch.isdigit():
            digits +=1
count_words = len(st.split())            
print(f"Characters:{char},count word:{count_words},Digits: {digits}")        
#Expected output:  Characters:22,count word:2,Digits: 6


#14.Rotate a string left by n positions.
#15.Find all substrings of a given string.

#Set Programming Questions.
#Basic
#1. Create a set and add elements dyamically.
elements = [1,2,3,4,5,6]
st = set()
for x in elements:
    st.add(x)
print(st)
#Expected output: {1, 2, 3, 4, 5, 6}

#2.Find the union and intersection of two sets.
s_1 = {1,2,4,3,5,7}
s_2 = {4,3,5,7,8,9}
print(s_1.union (s_2))
print(s_1.intersection(s_2))
#Expected output:{1, 2, 3, 4, 5, 7, 8, 9}
#                {3, 4, 5, 7}

#3.Remove duplicate elements from a list using a set.
st = {1,2,3,6,7,8,9,5,6,4,7,9}
print(st)
#Expected output:- {1, 2, 3, 4, 5, 6, 7, 8, 9}

#4.Check if an elements exists in a set.
st = {1,23,4,5,6,7,89,}
my_set = 5
if my_set in st:
    print("Elements is exists in  set")
else:
    print("Elements is not exists in set")

#5.Find the difference between two sets.
se_1 = {1,2,3,4,5,6,7}
se_2 = {3,4,5,6,7,8,9}
print(se_1.difference(se_2))
#Expected output:-{1, 2}

#Intermediate

#6.Find common elements in two lists using sets.
li_1 = [1,2,3,4,5,6,7,8]
li_2 = [3,4,5,6,7,8,9,11]
common = set(li_1)& set(li_2)
print(common)
#Expected output:- {3, 4, 5, 6, 7, 8}

#7.Check whether one set  is subset of another.
se_1 = {1,2,3,4,5,}
se_2 = {1,2,3,4,5,6,7,89,}
if se_1 in se_2:
    print("set_1 is in set_2")
else:
    print("set_1 is not in set_2")
#Expected output:- set_1 is not in set_2


#8.Find symmetric difference of two sets.
se_1 = {1,2,3,4,5,6,7,8,9}
se_2 = {3,4,5,6,7,8,9,10,11}
print(se_1^se_2)
#Expected output:- {1, 2, 10, 11}

#9.Count unique elements from two sets.
se_1 = {1,2,3,4,5,6,7,8}
se_2 = {1,2,5,67,89,67}
my_set = (se_1 .union (se_2))
count = len(my_set)
print(count)
#Expected output:- 10


#10.Remove all common elements from two sets.
se_1 = {1,2,3,4,5,6,7,8}
se_2 = {3,4,5,6,7,8,9,11}
print(se_1^se_2)
#Expected output:- {1, 2, 9, 11}



#Triky
#11.Find missing numbers from 1 to n using sets.
se = {1,2,3,5,6,8,9,10}
for x in range(1,max(se)+1):
    if x not in se:
        print(x)
#Expected output:4
#                7


#12.Check if two lists have any common elemnets.
li_1 = [1,2,3,4,5,6,7,8,9]
li_2 = [3,4,5,6,7,8,9,11,12]
commen = []
for x in li_1:
    if x in li_2:
        commen.append(x)
print(commen)
#Expected output:  [3, 4, 5, 6, 7, 8, 9]


#13.Convert a set of strings into uppercase.
st = {"Komal", "Kishan"}
uppercase = set()
for words in st:
    uppercase.add(words.upper())
    print(uppercase)
#Expected output:{'KISHAN'}
#                {'KOMAL', 'KISHAN'}


#14.Identify unique vowels in a given string using a set.
st = "programming"
vowels = {'a','e','i','o','u'}
unique = set()
for ch in st.lower():
    if ch in vowels:
        unique.add(ch)
print(f"Unique vowels: {unique}")
#Expected output: -Unique vowels: {'o', 'i', 'a'}




#15.Find elements that appear only once in a list.
li = [1,2,3,4,5,4,3,9]
appear = []
for elements in li :
    if li.count(elements)==1:
        appear.append(elements)
print(appear)
#Expected output:[1, 2, 5, 9]


#Dictionary Programming questions
#Basic
#1.Create a dictionary and print all keys and values.
dic = {1:23,2:34,3:56,4:78}
print(dic)

#2.Count frequency of each word in a sentence.
sen = "Python is amezing tual"
dic = dict()
for ch in sen:
    dic.update({ch:sen.count(ch)})
print(dic)
    

#3.Merge two dictionaries.
di_1 = {1:23,2:45,3:56}
di_2 = {4:78,6:89,3:90}
di_1.update(di_2)
print(di_1)

#4.Find the length of a dictionary.
di = {1:23,2:56,3:78,4:89}
print(f"Length of dictionary:{len(di)}")

#5. Check if a key exists in a dictionary.
di = {1:3,2:56,3:89,4:89,5:90}
key = 1
if key in di:
    print("Key is exists in dictionary")
else:
    print("Key is not exists in dictionary")
#Expected output: -    Key is exists in dictionary


#6.Sort a dictionary by values.
di = {1:90,2:56,3:12,4:70}
di = list(di.values())
di.sort()
print(di)


#7.Find the key with the maximum value.
di = {1:45,2:67,3:89,4:90,5:30}
print(max(di.keys()))

#8.Remove a key from a dictionary.
di = {1:67,2:90,3:61,4:91,5:81}
del di[3]
print(di)

#9.Convert two lists into a dictionary.
li_1 = [1,2,3,4,5,6,7]
li_2 = [23,56,78,12,90,41,67]
di = dict()
for x in range(len(li_1)):
    di.update({li_1[x]:li_2[x]})
print(di)
#Expected output:-{1: 23, 2: 56, 3: 78, 4: 12, 5: 90, 6: 41, 7: 67}

#10.Count character frequency using a dictionary.
ch = "Programming"
di = dict()
for x in ch:
    di.update({x:ch.count(x)})
print(di)

#11.Invert a dictionary (swap keys and values).
di = {23:1,45:2,78:3,56:4}
invert = {v:k for k,v in di.items()}
print(invert)
#Expected output:-{1: 23, 2: 45, 3: 78, 4: 56}

#12.Group elements by frequency using a dictionary.
li = [1,2,3,4,5,6,7,8,91,2,3,4,5,6,7,8]
freq = dict()
for elements in li:
    freq.update({elements:li.count(elements)})
print(freq)
#Expected output:-{1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 91: 1}

#13.Find duplicate values in a dictionary.
di = {1:23,2:56,3:89,4:90,5:23}
dupli = list(di.values())
count = 1
for x in dupli:
    if dupli.count(x)>=2: 
        print(f"Duplicate: {x}")
   

#14.Create a nested dictionary for student records.


#Mixed (String + Set + Dictionary)


#1. Count unique words in a sentence.
s = "Python is a  language and Python is a amezing  "
st_1 = s.split()
st_2 = set(st_1)
print(len(st_2))

#2. Find common characters between two strings.2
s_1 = "India is a good country"
s_2 = "India is not safe for girls"
se = set(s_1)& set(s_2)
print(se)

#3.Find the most frequent character in a string.
st = "Python is  language"
for x in set(st):
    print(st.count(x),x)
    

#4.Remove duplicate words from a sentence.
st = "Python is language"
se = set(st)
print(se)


#5. Find words with the same letters (anagram groups).
    
 """





















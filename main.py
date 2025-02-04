#1)
#Accept two numbers and print the greatest number#
# num1 = int(input("enter the number \n"))
# num2 = int(input("enter the number \n "))

# if num1 > num2 :
#     print(f"{num1} is greater!")
# elif num2 > num1 :
#     print(f"{num2} is greater!")  
# else :
#     print(f"{num1} is eqaul to {num2}")  



# #2)
# #Accept the gender from the user as char and print the respective greeting message#
# gender = input("what is your gender? M or F \n")

# if gender == "M" or gender == "m":
#     print(f"Good morning SIR")
# elif gender == "F" or gender == "f":
#     print(f"Goof morning MAM")
# else :
#     print(f"Wrong input")



#3)Accept an integer and check whether it is an even number or odd#
# n=int(input("Enter the number: "))
# if n%2==0:
#         print("Even")
# else:
#         print("ODD")


#4)Accept name and age from the user. Check if the user is a valid voter or not.#
# name = input("What's your name?\n")
# age = int(input("What' your age?\n"))
# if age >= 18:
#     print(f"{name}, congo you can vote!")
# elif age < 18 and age >0:
#     print(f"{name}, you cannot vote!")
# else:
#     print(f"{age} is not a valid number!")



# #5)Accept a year and check if it's a leap year or not#
# a = int(input("Enter the year: "))
# if a % 4 == 0 and a % 100 != 0:
#     print(f"{a} is a leap year")
# elif a % 100 == 0 and a % 400 == 0:
#     print(f"{a} is a leap year")
# else:
#     print(f"{a} is not a leap year")



# #6)Accept an English alphabet from user and check if it's a consonant or a vowel#
# a=input("Enter an alphabet: ")
# for i in a:
#         if i in ("aeiouAEIOU"):
#                 print("Vowel")
#         else:
#                 print("Consonent")




#7) Print natural number up to n.
# n=int(input("Enter a natural number: "))
# for i in range(1,n+1,1):
#         print(i)



#8) Reverse for loop. Print n to 1.
# n=int(input("Enter a natural number: "))
# for i in range(n,0,-1):
#         print(i)

#9)Take a number as input and print its table upto 10 terms
# n=int(input("Enter the number: "))
# for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")



# #10)Sum upto n terms#
# n=int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1,1):
#         sum = sum + i
# print(sum)



#11)Factorial of the number#
# n = int(input("Enter the number: "))
# fact=1
# for i in range(1,n+1,1):
#         fact=fact*i
# print(fact)



#12)Print all the factors of the number
# n = int(input("Enter the number:"))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i, end = "")



#13)Accept a number and check it it a perfect number or not(EXCLUDE ITSELF)
# n = int(input("Enter the Number: "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum+i
# if sum == n:
#     print("Perfect number")
# else:
#     print("Not a perfect number")



#14)Check whether the numebr is prime or composite
# n = int(input("Enter the Number: "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2 :
#     print("Prime")
# else:
#     print("Composite")



#15)Seperate each digit of a number and print it on the new line
# a = int(input("Enter the num: "))
# while a > 0:
#     print(a%10)
#     a = a//10 #to break the number at the end or it will print continously



#16)Accept a number and check if its a pallindromic number, basically number should equal to its reverse number
# n = int(input("Enter the num: "))
# copy = n
# rev = 0
# while n > 0:
#     z=(n%10)
#     rev = rev *10 +z
#     n = n//10
# if copy == rev:
#     print("pallindromic")
# else:
#     print("Not a pallindromic")



#17) Check all the prime numbers in a range
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)


#18) Print a right triangle star pattern
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print('*' * i)




#QUESTIONS FOR STRINGS, LIST, TUPPLES, SETS, DICT#
#-------------------------------------------------#

#STRING#
#---------#
#1)Print the string in reverse, its length, in uppercase, lowercase and copy into another string
# a = "parampatel"
# print(a.lower())
#-------------------
# a="parram"
# b=a
# print(b)
#-------------------
# a="param"
# print(len(a))
#-------------------
# a="param"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b= b +a[i]
# print(b);
        #or#
# a="param"
# print(a[::-1])



#2)Arrange string characters such that the lowercase letters should come first in another sttring.
# a="yooo BroTHER How are You"
# b=""
# for i in a:
#     if i.islower():
#         b = b + i
# for i in a:
#     if i.isupper():
#         b = b + i
# print(b)



#3)Count all the letters, digits, and special symbols from a given string
# str = "P@#yn26at^&i5ve"
# chr=0
# dig=0
# spchr=0
# for i in str:
#     if i.isdigit():
#         dig = dig +1
#     elif i.isalpha():
#         chr=chr+1
#     else:
#         spchr=spchr+1
# print(chr,dig,spchr)



#4)Count vowels from the given strings
# def vowelCounter(x):
#     vowels=0
#     consonents=0
#     for i in x:
#         if i in "aeiouAEIOU":
#             vowels=vowels+1
#         elif i == " ":
#             continue
#         else:
#             consonents=consonents+1
#     return f"vowels={vowels},consonants={consonents}"
# a="Param Patel"
# print(vowelCounter(a))



#5)Check string is pallindrome or not
# a = input("What's your name: ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if a==b:
#     print(f"{a} is pallindrome")
# else:
#     print(f"{a} is not a pallindrome")



#LISTS QUESTIONS#
#-----------------#
#1)Accept the list elements and reprint it
# l=[]
# count=int(input("How many number you want: "))
# for i in range(count):
#     z= int(input("Tell your number and press enter: "))
#     l.append(z)
# print(l)



#2)Print the elements in reverse order
# count=int(input("How many number you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and press enter: "))
#     l.append(z)
# print(l)
# b=[]
# for i in range(len(l)-1,-1,-1):
#     b.append(l[i])
# print(b)



#3)Print positive and negative elements of an list in seperate lists
# count=int(input("Enter the number: "))
# l=[]
# for i in range(count):
#         z=int(input("Tell the number and press enter: "))
#         l.append(z)
# print(f"ARRAY -> {l}")
# p=[]
# n=[]
# for j in l:
#         if j >= 0:
#                 p.append(j)
#         else:
#                 n.append(j)
# print(f"POSITIVE-{p} , NEAGTIVE-{n}")

        



#4)Find the greatest element and print it's index too.
# count=int(input("Enter the total number of element you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and enter: "))
#     l.append(z)
# print(l)
# max=0
# index=0
# for j in range(len(l)):      //note- we used range() function instead of for j in l , beacuse we want to find index as well as value so 
#     if l[j] > max:      
#         max=l[j]
#         index=j
# print(f"largest number = {max} and it's index is {index}")



#5)Find the second greatest element and print its index
# count=int(input("Enter the total number of elements you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and press enter: "))
#     l.append(z)
# print(f"array -> {l}")
# max=0
# max2=0
# index=0
# index2=0
# for j in range(len(l)):
#     if l[j] > max:
#         max2 = max
#         max=l[j]
#         index2 = index
#         index=j
#     elif l[j] > max2:
#         max2 = l[j]
#         index2 = j
# print(f"Second greatest elem = {max2} and it's index = {index2}")



#6)Check if list is sorted or not 
# count=int(input("Enter the total number of element you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and enter: "))
#     l.append(z)
# print(f"array -> {l}")
# for j in range(len(l)-1):
#     if l[j] <= l[j+1]:
#         continue
#     else:
#         print("Not sorted!")
#         break
# else:
#     print("Sorted")



#7)Check its pallandromic or not.
# count=int(input("Enter the total number of element you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and enter: "))
#     l.append(z)
# print(f"array -> {l}")
# b=[]
# for j in range(len(l)-1,-1,-1):
#     b.append(l[j])
# if l==b:
#     print("Pallindrome")
# else:
#     print("Not a pallindrome")



#8)How many seperate elements are there in the list excluding repetation
# count=int(input("Enter the total number of element you want: "))
# l=[]
# for i in range(count):
#     z=int(input("Tell the number and enter: "))
#     l.append(z)
# print(f"array -> {l}")
# b=set(l)
# print(len(b))



#DICTIONARIES
#-------------------------
#1)Merging two dictionaries.
# a = {1:10,2:20,3:30}
# b = {4:40,5:50,6:60}
# a.update(b)
# print(a)



#2)Sum all the value in dictionary.
# count = int(input("Enter the number of elements you want in the dictionary: "))
# d = {}
# for i in range(count):
#         key = input("Enter the key: ")
#         value = int(input("Enter the value: "))
#         d[key] = value
# print(f"Dictionary: {d}")
# sum = 0
# for j in d.values():
#         sum = sum + j
# print(sum)



#3)Count the frequency of each elements in a list.
# count = int(input("Enter the number of elements you want: "))
# l=[]
# for i in range(count):
#         z=int(input("Tell the numbers and press enter: "))
#         l.append(z)
# print(f"List -> {l}")
# d={}
# for j in l:
#         if j in d.keys():
#                 d[j] = d[j] + 1
#         else:
#                 d[j]=1
# print(f"Frequency -> {d}")



#4)Combine two dict by adding values for common keys.
# count = int(input("Enter the number of elements you want in the dictionary: "))
# d = {}
# for i in range(count):
#         key = input("Enter the key: ")
#         value = int(input("Enter the value: "))
#         d[key] = value
# print(f"Dictionary: {d}")
# count2 = int(input("Enter the number of elements you want in the dictionary: "))
# d2 = {}
# for j in range(count2):
#         key2 = input("Enter the key: ")
#         value2 = int(input("Enter the value: "))
#         d2[key2] = value2
# print(f"Dictionary1: {d}")
# print(f"Dictionary2: {d2}")
# for a in d2.keys():
#         if a in d.keys():
#                 d[a]=d[a]+d2[a]
#         else:
#                d[a]=d2[a]
# print(f"ADDED -> {d}") 



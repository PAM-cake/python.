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
# a = int(input("Enter the number \n"))

# if a % 2 ==0 :
#     print(f"{a} is an even number!")
# else:
#     print(f"{a} is an odd number!")



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
# a = input("Enter an alphabet: ")
# if a in "aeiouAEIOU":
#     print(f"{a} is vowel.")
# else:
#     print(f"{a} is consonant")



#7) Print natural number up to n.
# n = int(input("Please tell a number: "))
# for i in range(1,n+1,1):
#     print(i)



#8) Reverse for loop. Print n to 1.
# n = int(input("Please tell a number: "))
# for i in range(n,0,-1):
#    print(i)

#9)Take a number as input and print its table upto 10 terms
# n = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")



# #10)Sum upto n terms#
# n = int(input("Write a num: "))
# sum = 0 
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)



#11)Factorial of the number#
# n = int(input("Please tell your number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i

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
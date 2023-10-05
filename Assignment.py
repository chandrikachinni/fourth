#Write a program to display all prime numbers within a range.

# num=int(input("enter the number:"))
# if num==1:
#     print("is not prime number")
# if num>1:
#     for i in range(2,num):
#         if num%2==0:
#             print(num,"is not prime number")
#             break
#         else:
#             print(num,"is prime number")
       

##Display Fibonacci series up to 10 terms.

# series=[0,1]
# for i in range(2,10):
#     num=series[-1]+series[-2]
#     series.append(num)
# print("series upto 10:")
# print(series)

##Find the factorial of a given number

# num=int(input("enter a number:"))
# f=1
# for i in range(1,num+1):
#     f*=i
# print("Factorial of",num,"is:",f)


##Reverse a given integer number.

# num=int(input("enter an integer number:"))
# reversed_num=0
# while num !=0:
#     remainder=num%10
#     reversed_num=reversed_num*10+remainder
#     num=num//10
# print("reversed number:",reversed_num)

##Use a loop to display elements from a given list present at odd index positions

# list=[1,2,3,4,5,6,7,8,9,10]
# print("elements at odd index positions:")
# for i in range(1,len(list),2):
#     print(list[i])

##Calculate the cube of all numbers from 1 to a given number.

# given_number=int(input("enter a number:"))
# print("cubes of numbers from 1 to", given_number,":")
# for num in range(1,given_number+1):
#     cube=num**3
# print(cube,end=" ")

##Find the sum of the series upto n terms.

# n=int(input("enter the value of  n:"))
# sum_of_series=(n*(n+1))/2
# print("sum of the series upto",n,"terms is:",sum_of_series)

##Append new string in the middle of a given string.

# given_string=input("enter the given string:")
# new_string=input("enter the new string to append:")
# index=len(given_string)//2
# string=given_string[:index]+new_string+given_string[index:]
# print("resultant string:",string)



























































































































































































































































































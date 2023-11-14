## assignment user define function

# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# def zero_exception():
#     try:
#         x=5
#         y=0
#         print(x/y)
#     except ZeroDivisionError:
#         print(10/2)

# zero_exception()
## 5.0

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.


# def n1():
#     try:
#         n=int(input("enter the value"))
#         m=int(input("enter the value"))
#     except ValueError:
#         print("correct input")
# n1()       
## enter the value="9"
#correct input

# # 3.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# def type_exception():
#     try:
#         n=(input("enter the number"))
#         m=(input("enter the number"))
#         print(n/m)
#     except TypeError:
#         a=int(input("enter the number"))
#         b=int(input("enter the number"))
#         print(a/b)
#     finally:
#         print("the code is handled")

# type_exception()
        
## enter the number="2"
## enter the number="3"
## enter the number=5
## enter the number=2
# 2.5
# the code is handled

# 4. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

# def n1():
#     try:
#         a=input("enter the number")
#         b=input("enter the number")
#         c=input("enter the number")
#         a=[a,b,c]
#         print(a[5])
#     except IndexError:
#         print("list index is out of range")
# n1()
## output
# enter the number 9
# enter the number 10
# enter the number 15
# list index is out of range 

# 5. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.


# def n1():
#     try:
#         y=int(input("enter the value"))
#     except KeyboardInterrupt:
#         print("chandu")
# n1()

## output

#6. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.


# def n1():
#     try:
#         x=int(input("enter the number"))
#         y=int(input("enter the number"))
#         print(x/y)
#     except ArithmeticError:
#         z=int(input("enter the number"))
#         n=int(input("enter the number"))
#         print(z/n)
# n1()

#output--enter the number 10
# enter the number 5
# 2.0





















































































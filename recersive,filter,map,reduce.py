## Recursive

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num = 3
# print("The factorial of", num, "is", factorial(num))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print (factorial(0))
# print (factorial(1))
# print (factorial(2))
# print (factorial(3))
# print (factorial(4))

# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(5):
#     r=fibonacci(i)
#     print(r)

# def f1(x):
#     if x==1:
#         return 1
#     else:
#         return x+f1(x-1)
# r=f1(5)
# print(r)

# def Recur_facto(n):
# 	if (n == 0):
# 		return 1
# 	return n * Recur_facto(n-1)
# print(Recur_facto(6))

## filter()

# n=[1,2,3,4,5,6,7]
# result=(filter(lambda x:x%2==0,n))
# print(list(filter(lambda x:x%2==0,n)))  ##[2, 4, 6] even num

# n=[1,2,3,4,5,6,7,8]
# result=filter(lambda x:x%2!=0,n)
# print(list(result))  ##[1, 3, 5, 7] ## odd numbers

# n=[1,2,3,4,5,6,7,8]
# result=filter(lambda x:x%2<=0,n)
# print(list(result))  ##[2, 4, 6, 8]

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,40,50,6,7,8,9]
# l1=list(filter(even,l))
# print(l1)   ##[2, 40, 50, 6, 8]

# def odd(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# l=[1,2,3,40,50,6,7,8,9]
# l1=list(filter(odd,l))
# print(l1)  ##[1, 3, 7, 9]

### map()

# n=[1,2,3,4,5]
# result=list(map(lambda x:x*2,n))
# print(result)  #3[2, 4, 6, 8, 10]

# n=[1,2,3,4,5]
# result=list(map(lambda x:x**2,n))
# print(result)  ##[1, 4, 9, 16, 25]

# n=[1,2,3,4,5]
# result=list(map(lambda x:x==2,n))
# print(result)  ##[False, True, False, False, False]

# l1=[1,2,3,4,5]
# l2=[10,20,30,40]
# result=list(map(lambda x,y:x+y, l1,l2))
# print(result)  ##[11, 22, 33, 44]

# words=["mango","apple","orange"]
# result=list(map(len,words))
# print(result)  ##[6, 5, 6]

## reduce

# from functools import*
# l=[5,9,6,2,10,3]
# n=reduce(lambda x,y:x if x>y else y, l)
# print(n)  #10

# from functools import*
# l=[10,20,30,40]
# n=reduce(lambda a,b:a-b,l)
# print(n)  ##-80

# from functools import*
# l=[1,2,3,4]
# n=reduce(lambda a,b:a*b,l)
# print(n) ##24

# from functools import*
# l=["hi","all","!"]
# n=reduce(lambda a,b:a+b,l)
# print(n)  ##hiall!

# from functools import*
# l=[30,4,50,6,70,8]
# n=reduce(lambda x,y:x%2==0,l)
# print(n) #True even


# from functools import*
# l=[30,4,50,6,70,9]
# n=reduce(lambda x,y:x%2!=0,l)
# print(n)   # False odd

### Functions

# def function(a,b,c):
#     res=a-b+c
#     print(res)
# function(20,10,40) ##50


# def function(a,b,c):
#     d=c
#     del c
#     print("i like",a,b,"and",d)
# function("math","science",c="history")   ##i like math science and history

# def greet(name):
#     print("hello",(name))
# greet("chandu")

# def greet(name="person"):
#     print("hey",(name))
# greet()
# greet("chandu")

# def info(name,gender="female"):
#     print("hello",(name))
# info()
# info("rani") ## invalid becoz positional argument 

# def info(name,age,rollno=10):
#     print("name:",name)
#     print("age:",age)
#     print("rollno:",rollno)
#     return              
# info(25,"ram")

# def print_name(name="varun"):
#     print("my name is:",name)
# print_name("arun")   ##my name is: arun

# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
# print(factorial(6))  ##720
    
# def function(a,b,c):
#     res=a+b+c
#     print(res)
# function(20,10,40)  #70

# def function(n):
#     return 5*n
# print(function(3))
# print(function(2))
# print(function(4))

# def function(a,b,c):
#     res=a*b*c
#     print(res)
# function(10,20,30)  ## 6000

# def function(a,b,c,d=5):
#     res=a-b+c*d
#     print(res)
# function(20,10,4) ##30

# a=100
# def n():
#     print(a)
# def n1():
#     a=50
#     print(a)
# n()
# n1()

# a=100
# def n():
#     print(a)
# def n1():
#     global a
#     a=50
#     print(a)
# n1()   
# n()

# a=100
# def n():
#     global a
#     print(a)
# def n1():
#     global a
#     print(a)
# n()
# n1()

# a=100
# def n():
#     global a
#     a=20
#     print(a)
# def n1():
#     global a
#     b=30
#     print(b)
# n1()
# n()



# def n():
#     print("function")
#     def b(a,b):
#         print(a*b)
#         print(a-b)
#         print(a+b)
#     b(5,6)  
# n()

# a=10
# def n1():
#     print(a)
#     def n2():
#         a=10
#         print(a)
#     def n3():
#         print(a)
#     n2()
#     n3()
# n1() #10,10,10

# def table(n):
#     for i in range(1,11):
#         result=n*i
#         print("{n}x{i}={result}")
# table(2)

# def a():
#     print("ram is good boy")
#     def b():
#       print("sam is bad boy")
#     b()  
# a()














































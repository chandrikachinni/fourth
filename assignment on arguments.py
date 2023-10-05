## positional argument

# def a1(x,y):
#     print(x-y)
# a1(10,20)  ## -10

# def a1(x,y):
#     z=x**y
#     print(z)
# a1(5,2)  ## 25

# def info(name,age):
#     print(name, age)
# info("sam",20)

# def f1(x,y,z):
#     print(x,y,z)
# f1(10,20) ## its an error becoz we are missing 1 positional argument

# def int(a,b,c):
#     z=a+b-c
#     print(z)
# int(20,35,90) #-35

## keyword argument

# def info(name,age):
#     print("name:",name)
#     print("age:",age)
#     return              
# info("ram",25) ##name: ram  age: 25


# def info(name,age):
#     print("name:",name)
#     print("age:",age)
#     return              
# info(25,"ram") ##name 25,age ram

# def info(name,age):
#     print("name:",name)
#     print("age:",age)
#     return              
# info(age=25,name="ram")   ## name : ram,age:25

# def info(name,age,rollno=10):
#     print("name:",name)
#     print("age:",age)
#     print("rollno:",rollno)
#     return              
# info(25,"ram") 

# name: 25
# age: ram
# rollno: 10

# def int(a,b):
#     print("python",a,"programming",b)
# int(a="is good",b="language")  ##python is good programming language

# def f1(a,b):
#     print("sam scored",a,"ram scored",b)
# f1(a=10,b=20)   ##sam scored 10 ram scored 20

# def f1(a,b):
#     print(a=10,b=20)
# f1(a="sam scored",b="ram scored") ## a is an invalid keyword argument for print()

##  Default argument

# def f1(x="sam"):
#     print("hey",x,"where are you")
# f1("ram")

# def print_name(name="varun"):
#     print("name:",name)
# print_name()  ## varun

# def print_name(name="varun"):
#     print("my name is:",name)
# print_name("arun")   ##my name is: arun

# def add(a=10,b=20):
#     print(a+b)
# add()  ##30

# def add(a,b=20):
#     print(a+b)
# add(50,10)   ##60

# def add(a=10,b=20):
#     print(a+b)
# add(50,30)  ##80


## Difference between positional argument, keyword and deault argument

# def addition(a,b,c=30):
#     sum=a+b+c
#     print(sum)
# addition(50,b=30,c=30)   ##110


# def addition(a,b,c=30):
#     sum=a+b+c
#     print(sum)
# addition(10,30,b=20)   ## inavlid becoz b has multiple values

# def movie(moviename,hero,heroine="genelia"):
#     print("moviename is",moviename)
#     print("hero is",hero)
#     print("heroine is",heroine)
# movie("ready",hero="ram")     ## valid

#moviename is ready
# hero is ram
# heroine is genelia

# def minus(a,b,c=10,d):
#     sum=a-b-d
#     print(sum)
# minus(10,30,d=20)  ## inavlid becoz it is not default argument follows default argument


# def minus(a,b,c=10,d=5):
#     sum=a-b-d
#     print(sum)
# minus(10,30,d=20)   ##-40


# def minus(a,b,c=10,d=5):
#     sum=a-b-d
#     print(sum)
# minus(d=20,10,40) ## inavlid becoz positional argument follows keyword argument


# def info(name,college,branch="computer"):
#     print("name is",name)
#     print("college is",college)
#     print("branch is",branch)
# info("chandu",college="cutm",rollno=72) ## invalid becoz rollno is unexcepted keyword argument

# def a1(a,b,d,c="favourite"):
#     print("science",a,"maths",b,c,d)
# a1("and",b="are",d="subjects")  ## science and maths are favourite subjects

# def a1(a,b,c="favourite",d):
#     print("science",a,"maths",b,c,d)
# a1("and",b="are",d="subjects")  ##non-default argument follows default argument invalid

###  variable length argument

#1.write a pro to print sum of given numbers

# def sum(*n):
#     s=0
#     for i in n:
#         s+=i
#     print("required sum is",s)
# sum(10,20,30,40)
# sum(50,60,70,89)

# 2. write a program to enter student deatials and also view the stored student details 
# def info(**details):
#     for i,j in details.items():
#         print("{}':'{}".format(i,j))
# info(name="chandu",empid="5467",company="cutm")

##Functions

# 1.write a func which contains some number as arguments and print square of that number.

# def print_square(number):
#     square=number**2
#     print(f"square of {number} is {square}")
# number=9
# print_square(number)

# n=4
# square=n*n
# print(square)

# 2.write a program in function given number is even or odd

# def function(n):
#     if n % 2==0:
#         print("number is even")
#     else:
#         print("number is odd")
# function(3)

#3.write a func to find factorial of given number

# def factorial(m):
#     fact=1
#     for i in range(1,m+1):
#         fact=fact*i
#     print("factorial of",m,"is",fact)
# n=int(input("enter a number"))
# factorial(n)

# 4.write a program to create calculator using functions (sum,sub,mul,div)

# def calculator(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     print("sum=",sum)
#     print("sub=",sub)
#     print("mul=",mul)
#     print("div=",div)
# calculator(30,20)

































































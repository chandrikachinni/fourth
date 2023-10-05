## Decorators

# def greet(func):
#     def wrapper():
#         print("Question : how you doing bro?")
#         func()
#         print("lets go to wonderla")

#     return wrapper

# @greet
# def greetReply():
#     print("Ans: I am doing good")
# greetReply()

# def decor(func):
#     def inner(name):
#         if name=='chandu':
#             print("hello chandu how are you")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("hello",name,"good morning")
# wish("ram")
# wish("shyam")
# wish("chandu")

# def s_division(func):
#     def inner(a,b):
#         if b==0:
#             print("how can we print zero")
#         else:
#             return func(a,b)
#     return inner
# @s_division
# def division(a,b):
#     return a/b
# print(division(10,2))
# print(division(10,5))
# print(division(10,0))

# def s_add(func):
#     def inner(a,b):
#         if b==2:
#             print("hey how are you")
#         else:
#             return func(a,b)
#     return inner
# @s_add
# def add(a,b):
#     return a+b
# print(add(10,2))
# print(add(10,5))






























































































































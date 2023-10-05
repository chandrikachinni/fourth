# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g=mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))   ### a,b,c

# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g=mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) ## error: stopIteration

# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for n in fibonacci():
#     if n>100:
#         break
#     print(n)

# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# for x in firstn(10):
#     print(x)

# def countdown(num):
#     while num>0:
#         yield num
#         num=num-1
# countdown_gen=countdown(5)
# for n in countdown_gen:
#     print(n)










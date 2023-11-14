### assig using else in try-except-finally

## case 1 -- no exception in try block
#1,3,4,5

# try:
#     print("try block")## st 1
# except :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

# case 2 exception is raised and handled in except block
#1,2,4,5

# try:
#     print("try block")## st 1
#     print(1/0)
# except ZeroDivisionError:
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 3 exception raised and not handled
#1,4

# try:
#     print("try block")## st 1
#     print(10/0)
# except TypeError :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 4 multiple statment in try block no exception
#1,3,4,5

# try:
#     print("try block")## st 1
#     x=10
#     y=29
# except :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 5 multiple statement in try block exception handled
#1,2,4,5

# try:
#     print("try block")## st 1
#     x=10
#     y=20
#     a=(x/y)
# except ZeroDivisionError:
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 6 multiple statement in try block exception not handled
#1,4

# try:
#     print("try block")## st 1
#     x=10
#     y=0
#     a=(x/y)
# except ValueError :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 7 exception in except block
#1,2,4

# try:
#     print("python")## st 1
#     x=10
#     y=0
#     a=(x/y)
# except ZeroDivisionError :
#     print("except")## st2
#     1/0
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

# case 8 exception in else block
#1,3,4

# try:
#     print("try block")## st 1
# except :
#     print("except")## st2
# else:
#     print("else")## st3
#     print(10/0)
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 9 exception in finally block
#1,3,4

# try:
#     print("try block")## st 1
# except :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
#     print(10/0)
# print("outside the blocks")##st5

## case 10 exception in both else block and finally
#1,3,4

# try:
#     print("try block")## st 1
# except :
#     print("except")## st2
# else:
#     print("else")## st3
#     print(10/0)
# finally:
#     print("finally")##st4
#     print(10/0)
# print("outside the blocks")##st5

## case 11 no statements in try block and no exception
#3,4,5

# try:
#     print
# except :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 12 if no statement in try block but exception in except block
#3,4

# try:
#     print
# except :
#     print("except")## st2
# else:
#     print("else")## st3
#     print(10/0)
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 13 no statement in try block but exception in finally block
#3,4,5

# try:
#     print
# except :
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
#     print(10/0)
# print("outside the blocks")##st5

## case 14 if no statement in try block exception raised in both else and finally.
#3,4

# try:
#     print
# except :
#     print("except")## st2
# else:
#     print("else")## st3
#     print(1/0)
# finally:
#     print("finally")##st4
#     print(1/0)
# print("outside the blocks")##st5

## case 15  exception raised at inner try
# 1,2,5,6,9,10,11

# try:
#     print("Outer try 1 ") #st 1
#     try:
#         print(10/0)
#     except ValueError:
#         print("Inner except 1")#st 2
#     except:
#         print("Inner except 2")#st 3
#     else:
#         print("inner else")# st4

#     finally:
#         print("Inner finally")#st5
#     print("Outer finally 1")#st6
# except ValueError:
#     print("outer except1")#st7
# except :
#     print("outer except 2")#st8
# else:
#     print("Outer else")#st9
# finally:
#     print("outer finally 2 ")#st10
# print("Thanks")#st11

## case 16 no exception raiesd
#1,2,5,6,8,10,11,12

# try:
#     print("Outer try 1 ") #st 1
#     try:
#         print(10/2)#st2
#     except ValueError:
#         print("Inner except 1")#st3
#     except:
#         print("Inner except 2")#st 4
#     else:
#         print("inner else")# st5

#     finally:
#         print("Inner finally")#st6
#     print("Outer finally 1")#st7
# except ValueError:
#     print("outer except1")#st8
# except :
#     print("outer except 2")#st9
# else:
#     print("Outer else")#st10
# finally:
#     print("outer finally 2 ")#st11
# print("Thanks")#st12

## case 17  exception raised at inner try block
# 1,3,5,6,9,10,11

# try:
#     print("Outer try 1 ") #st 1
#     try:
#         print(10/0)
#     except ValueError:
#         print("Inner except 1")#st 2
#     except:
#         print("Inner except 2")#st 3
#     else:
#         print("inner else")# st4

#     finally:
#         print("Inner finally")#st5
#     print("Outer finally 1")#st6
# except ValueError:
#     print("outer except1")#st7
# except :
#     print("outer except 2")#st8
# else:
#     print("Outer else")#st9
# finally:
#     print("outer finally 2 ")#st10
# print("Thanks")#st11


## case 18 if exception raised in outer try block
#1,(1),4,5,6,9,10,11

# try:
#     print("Outer try 1 ") #st 1
#     try:
#         print(10/2)#stement(1)
#     except ValueError:
#         print("Inner except 1")#st 2
#     except:
#         print("Inner except 2")#st 3
#     else:
#         print("inner else")# st4

#     finally:
#         print("Inner finally")#st5
#     print("Outer finally 1")#st6
# except ValueError:
#     print("outer except1")#st7
# except :
#     print("outer except 2")#st8
# else:
#     print("Outer else")#st9
# finally:
#     print("outer finally 2 ")#st10
# print("Thanks")#st11

## case 19 multiple exception in the except block
#1,2,4,5

# try:
#     print("try block")## st 1
#     print("10"+20)
# except (ValueError,ZeroDivisionError,TypeError):
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")# st 4
# print("outside the blocks")##st5

## case 20 exception not raised in any block
#1,4

# try:
#     print("try block")## st 1
#     x="chandu"
#     print(x[9])
# except ValueError:
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")# st 4
# print("outside the blocks")##st5

# x="chandu"
# print(x[9])(indexError)

## case 21  exception raised in finally block
#1,3,4

# try:
#     print("try block")## st 1
# except IndexError:
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")# st 4
#     x="chandu"
#     print(x[9])
# print("outside the blocks")##st5

## case 22 if exception raised in else block and finally block
#1,3,4

# try:
#     print("try block")## st 1
# except ValueError:
#     print("except")## st2
# else:
#     print("else")## st3
#     a=10
#     b=int("chandu")
#     print(b)
# finally:
#     print("finally")# st 4
#     a=10
#     b=int("chandu")
#     print(b)
# print("outside the blocks")##st5

# a=10
# b=int("chan")
# print(b)#(valueError)

## case 23 exception raised in try and finally
#1,2,4

# try:
#     print("try block")## st 1
#     print(10/0)
# except ZeroDivisionError:
#     print("except")## st2
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
#     print(10/0)
# print("outside the blocks")##st5

## case 24 multiple exception raised and handled one in try block
# 1,2,4,5

# try:
#     print("try block")## st 1
#     a=10
#     b=int("chan")
#     print(b)
#     print(10/0)
# except ValueError:
#     print("except")## st2
# except ZeroDivisionError:
#     print("except 1")
# else:
#     print("else")## st3
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5

## case 25 exception in try block, except block and else block
#1,2,4,5

# try:
#     print("try block")## st 1
#     a=10
#     b=int("chandu")
#     print(b)
# except ValueError:
#     print("except(valueError):")## st2 
# else:
#     print("else")## st3
#     a=10
#     b=int("chandu")
#     print(b)
# finally:
#     print("finally")##st4
# print("outside the blocks")##st5
























































































































### assignment

#  case1 if there is no exception raised(noraml termination)
#1,2,3,4,5,6,8,9,11,12
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2") #statment-2
#     print("outer try 3") #statment-3
    
#     try:
#       print("inner try 1")#statment-4
#       print("inner try 2")#statement-5
#       print("inner try 3") #statment-6
#     except ZeroDivisionError:
#       print("inner except block")#statment-7
#     finally:
#       print("inner ffinally block")#statment-8
#     print("noraml statment")#statment-9
# except ZeroDivisionError:
#   print("outer except block")#statment-10
# finally:
#   print("outer finally block")#statment-11
# print("outside the block")   #statment12

#case2 if  exception raised at st2 and except block matched
# 1,10,11,12(noraml termination)
# try:
#     print("outer try 1")#statment-1
#     print(199/0) #statment-2
#     print("outer try 3") #statment-3
    
#     try:
#       print("inner try 1")#statment-4
#       print("inner try 2")#statment-5
#       print("inner try 3") #statment-6
#     except ZeroDivisionError:
#       print("inner except block")#statment7
#     finally:
#       print("inner ffinally block")#statment-8
#     print("noraml statment")#statment-9
# except ZeroDivisionError:
#   print("outer except block")#statment10
# finally:
#   print("outer finally block")#statment11
# print("outside the block") #statment-12

# case3 if an exception raised at st2 and except block is not matched
# 1,11
# try:
#     print("outer try 1")#st1
#     print(199/0) #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print(199/0)#st5
#       print("inner try 3") #st6
#     except ZeroDivisionError:
#       print("inner except block")#st7
#     finally:
#       print("inner ffinally block")#st8
#     print("noraml statment")#st9
# except TypeError:
#   print("outer except block")#st10
# finally:
#   print("outer finally block")#st11
# print("outside the block") 

# case4 if an exception raised at st5 and corresponding inner except block matched
#1,2,3,4,7,8,9,11,12
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print(10/0)#st5
#       print("inner try 3") #st6
#     except ZeroDivisionError:
#       print("inner except block")#st7
#     finally:
#       print("inner ffinally block")#st8
#     print("noraml statment")#st9
# except ZeroDivisionError:
#   print("outer except block")#st10
# finally:
#   print("outer finally block")#st11
# print("outside the block") 

#case5 if exception raised at st5 and inner except block is not matched but outer except is matched.
# 1,2,3,4,8,10,11,12
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print(10/0)#st5
#       print("inner try 3") #st6
#     except TypeError:
#       print("inner except block")#st7
#     finally:
#       print("inner ffinally block")#st8
#     print("noraml statment")#st9
# except ZeroDivisionError:
#   print("outer except block")#st10
# finally:
#   print("outer finally block")#st11
# print("outside the block") 

# case6 if  exception raised at st5 and corresponding except not matched and outer except not matched
#1,2,3,4,8,11
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2") #statment-2
#     print("outer try 3") #statment-3
    
#     try:
#       print("inner try 1")#statment-4
#       print(10/0)#statment5
#       print("inner try 3") #statment-6
#     except TypeError:
#       print("inner except block")#statment-7
#     finally:
#       print("inner ffinally block")#statment-8
#     print("noraml statment")#statment-9
# except TypeError:
#   print("outer except block")#statment-10
# finally:
#   print("outer finally block")#statament-11
# print("outside the block") #statement-2


#case 7 if exception raised at inner except st7 and no handling code and exception raised at outer finnaly at st11
# 1,2,3,4,5,6,8,9(abnormal termination)
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2") #statement-2
#     print("outer try 3") #statament-3
    
#     try:
#       print("inner try 1")#statement-4
#       print("inner try 2")#statament-5
#       print("inner try 3") #statement-6
#     except TypeError:
#       print(10/0)#statement-7
#     finally:
#       print("inner ffinally block")#statement-8
#     print("noraml statment")#statement-9
# except TypeError:
#   print("outer except block")#statement-10
# finally:
#   print(10/0)#statement-11
# print("outside the block")#statement-12

#case 8 if  no exception raised(normal termination)
# 1,2,3,4,5,6,8,9,11,12
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except xxxx:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except yyyy:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# case 9-- if exception in outer try block(abnormal termination)
#1,2,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print(1/0)
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

## case 10-- exception in innner try block(abnormal)
#1,2,3,4,5,7,8,9,11,12
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except Exception:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except Exception:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# case 11 exception in inner except block(abnormal)
#1,2,3,4,5,6,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#         print(1/0)
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# case 12 exception in outer except block(normal)
#1,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print(1/0)#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except Exception:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# case 13 exception in outer finally block(abnormal)
#1,2,3,4,5,6,8,9,11

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception as e:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except Exception as e:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
#     print(1/0)
# print("outside the blocks")#statment-12

#case 14 multiple nested try blocks(abnormal termination)
#1,2,3,4,5,7,8,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#         print(1/0)
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statement 12

# case 15 exception in inner ffinally block(abnormal)
#1,2,3,4,5,6,8,10,11,12


# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception as e:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#         print(1/0)
#     print("normal statment ")#statment-9
# except Exception as e:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

# case 16 exception in normal statement(abnormal)
#1,2,3,4,5,6,8,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception as e:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#         print(1/0)
#     print("normal statment ")#statment-9
# except Exception as e:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

# case 17 exception propagation in nested tries(abnormal)
#1,2,3,4,5,7,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except Exception as e:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 18 exception propagation to outer finally block(abnormal)
#1,2,3,4,5,6,8,9,11

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception as e:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# except Exception as e:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
#     print(1/0)
# print("outside the blocks")# statement 12

## case 19 exception in both inner and outer(normal)
#1,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print(1/0)#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 20 custom exception handling(normal)
#1,2,3,4,5,6,8,11

# class CustomInnerException(Exception):
#     pass
# class CustomOuterException(Exception):
#     pass
# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except CustomInnerException:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#         print(1/0)
#     print("normal statment ")#statment-9
# except CustomOuterException:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 21 exception in inner and outer except blocks(abnormal)
#1,2,3,4,5,6,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except Exception:
#         print("inner except block")#statment-7
#         print(1/0)
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 22 if exception handling  different exception types
#1,2,3,4,5,6,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ValueError:
#         print("inner except block")#statment-7
#     except ZeroDivisionError:
#         print("inner except blocks")
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# except ValueError:
#     print("outer except block")#statment-10
# except ZeroDivisionError:
#     print("outer except blocks")
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 23 no outer except block
# 1,2,3,4,5,7,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(1/0)
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")# statement 12

## case 24 no outer finally block
#1,2,3,4,5,6,8,9,11

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8 
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# print("outside the blocks")# statment 11

##case 25 exception in inner except and finally block
#1,2,3,4,5,7,8,10,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#         print(10/0)
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

## case 26-- exception in outer except and ffinally block
#1,2,10,11

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print(1/0)
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
#     print(1/0)
# print("outside the blocks")#statment-12






















































































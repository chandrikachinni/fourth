# try and except statements

#case 1-if exception is not raised try,except,finally(noraml)

# try:
#     print(10/2) 
#     print("hello jeevan")
#     print("hi ram")
# except ValueError:
#     print("hi")
# print("aman")
#o/p--
#  5.0
# hello jeevan
# hi ram
# aman

# try:
#     print("hi chandu")
#     print(10/3)
#     print("hello ram")
# except ZeroDivisionError:
#     print("bad")
#output
# hi chandu
# 3.3333333333333335
# hello ram

#case 2 -- if exception raised at try block and it handled(noraml termination)

# try:
#     print("pyhton")
#     print(10/"ten")  ## type error
#     print("programming")
# except TypeError:
#     print("sindhu")

#o/p--
# pyhton
# sindhu

# try:
#     x="chandrika"
#     print(x[10])
#     print("chinni")
# except IndexError:
#     print(10/2)
# output-5.0

#case3--if exception is raised at try block and not handled(abnoraml termination)

# try:
#     print("apple")
#     print("10"//2) #typeError
#     print("mango")
# except ValueError:
#     print(10//2) # 5 is integer value(we will get interger values and float values depends upon arguments)
# print("thank you")
#  output--apple

## // floor division
## / normal division

# try:
#     print("jam")
#     print("t"*"2")## typeError we get error beacuse we gave 2 arguments in string formate actually it is a repeatation operator an one argument should be intger and string value
# except ZeroDivisionError:
#     print("max")
#output--jam

# print("t"*4) # repeation operator

# case 4--if an exception raised at except block it will be abnoraml termination.

# try:
#     print(10/2)
#     print("sai")
#     print("bunny")
# except ValueError:
#     n="name"
#     print(n/2)
# output--5.0,sai,bunny

# try:
#     print(20/2)
#     print("10"+"20")## it is string concatenate that why we got output in string formate(two arguments must be in string)
#     print("v")
# except IndexError:
#     print("10"+20)
#output- 10.0,1020,v

# print("10"*20)
# print("10"+"20")
   
#case 5-- if exception at raised at finally block not handled(abnormal termination)

# try:
#     print("jin")
#     print("v")
#     print("thyme")
# except KeyError:
#     print("suga")
# finally:
#     x={"a":2,"b":3}
#     print(x["c"]) ##keyError

# try:
#     print("suga")
#     print("cat")
# except ValueError:
#     print("tom")
# finally:
#     x="kota chandrika"
#     for i in range(x):##typeError i got typeerror becoz i mention the string in range.(we should always mentaion integer values in range function)
#         print(i) 
# print("teddy")
#output--suga,cat

#case 6--- if exception raise at out of the try-except ,finally block(abnoraml termination)

# try:
#     print("maroxil")
#     print(10/2)
# except ZeroDivisionError:
#     print("how are you")
# finally:
#     print("antony")
# print(jeevan)# nameError
#output--maroxli, 5.0,antony,

# try:
#     print("coster")
#     print("bag")
# except TypeError:
#     print("tata")
# finally:
#     print("laptop")
# print(10/0) ##ZeroDivisionError
##output--coster,bag,laptop

## finally statements

#case1-- if no exception raised in try and except.(noraml termination)

# try:
#     print("enter")
#     print(40/3)
# except:
#     print("what are u doing")
# finally:
#     print("had your lunch")
## output--enter,13.33333,had your lunch

# try:
#     x="sindhu is my bestfriend"
#     for i in x:
#         print(i)
# except BaseException:
#     print("it is exception block")
# finally:
#     print("chandu")  
# output-- sindhu is my bestfriend, chandu   

#case 2--if an exception raised but not handled.(abnoraml termination)

# try:
#     x="aman is my team lead"
#     x.append("rani")
#     print(x)
# except ValueError:
#     print("aman is a good trainer")
# finally:
#     print("aman works at marolix")

#output-aman works at marolix

# x=["aman is my team lead"]
# x.append("jeevan")
# print(x[0:2])

# try:
#     print("sorry for not submiting the assig on friday")
#     x=1
#     y="chandu"
#     print(x+y) #typeError
# except ValueError:
#     print("doing the task")
# finally:
#     print("task is done")

#output--sorry for not submiting the assig on friday
# task is done
# print("1"+"chandu")

#case3--if an exception raised and handled(normal termination)

# try:
#     x='1,2,3,4,5,6'
#     x.append(3)
#     print(x)
# except BaseException:
#     print("i like to travel more")
# finally:
#     print("i had a trip to manali")
# print("it is good and fun trip")
#output--
# i like to travel more
# i had a trip to manali
# it is good and fun trip

# try:
#     print("10"+20)
#     print("max")
# except BaseException:
#     print("sunny")
# finally:
#     print("ram")
# print("jonny")

##output--sunny,ram,jonny

#case 4 --- if there is no error in try.(noraml termination)

# try:
#     print("maxy")
#     print("laddu")
# except ValueError:
#     print("max",2)
# finally:
#     print("bunny")   ## if we give error in except block or we wont give aslo the finally block will be executed.
# outpu-- maxy,laddu,bunny

# try:
#     print("apple")
#     print("banana")
# except:
#     x=2
#     y="chandu"
#     print(x-y)
# finally:
#     print("friend")
#output--apple,banana,friend

#case 5-- if exception raised at try block and except block is handled.(noraml termination)

# try:
#     print(10/0)
#     print("jeevan")
# except ZeroDivisionError:
#     print("candy")
# finally:
#     print("single")
# output-- candy,single

# try:
#     print("10"+20)
#     print("20"+"30")
# except TypeError:
#     print("python")
# finally:
#     print("programming")
#output--python,programming

#case 6- if exception raised at try block but except is not handled.(abnormal termination)

# try:
#     x ='10'
#     y =5
#     result = x / y
#     print(result)
# except ZeroDivisionError:
#     print("The division by zero operation is not allowed.")
# finally:
#     print(10/5)
# print("it is divisible")

#output--2.0
# list_a =[3,46,5,9,"m",4]
# a =len(list_a)
# print(a)


# try:
#     list_a = [3,46,5,9,"m",4]
#     a =list_a.length
#     print(a)
# except ValueError:
#     print("List doesn't have length method")
# finally:
#     print("thank you")
#output--thank you

#case 7-- if exception raised at except block and it is not handled

# try:
#     print(10/2)
#     print(10/0)
#     print(20/2)
# except BaseException:
#     print(20/0)
# finally:
#     print("how are you")
# print("im not fine")
# output --5.0, how are you(abnoraml termination)

# try:
#     print(20/10)
#     print(20/3)
# except:
#     print("20"-10)
# finally:
#     print("thank you")  ## (abnoraml termination)

# output--2.0,6.666,thank you

##########################################################################################################

# case1 if there is no exception raised(noraml termination)
#1,2,3,4,5,6,8,9,11,12
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print("inner try 2")#st5
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
# print("outside the block")   #st12

#case2 if  exception raised at st2 and except block matched
# 1,10,11,12(noraml termination)
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print("inner try 2")#st5
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

# case3 if an exception raised at st2 and except block is not matched
# 1,11
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
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
#       print(10/2)#st5
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
# except TypeError:
#   print("outer except block")#st10
# finally:
#   print("outer finally block")#st11
# print("outside the block") #st12


#case 7 if exception raised at inner except st7 and no handling code and exception raised at outer finnaly at st11
# 1,2,3,4,5,6,8,9(abnormal termination)
# try:
#     print("outer try 1")#st1
#     print("outer try 2") #st2
#     print("outer try 3") #st3
    
#     try:
#       print("inner try 1")#st4
#       print("inner try 2")#st5
#       print("inner try 3") #st6
#     except TypeError:
#       print(10/0)#st7
#     finally:
#       print("inner ffinally block")#st8
#     print("noraml statment")#st9
# except TypeError:
#   print("outer except block")#st10
# finally:
#   print(10/0)#st11
# print("outside the block")#st12
































































































































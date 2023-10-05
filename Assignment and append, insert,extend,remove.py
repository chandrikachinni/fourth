### Assignment
## take a list of values and check whether given number is present in the list or not, if present
# excepted output should be 10 is available and  first occurence is at : index

# l=[5,10,15,20,25]
# i=10
# if i in l:
#     first_occurrence=l.index(i)
#     print(f"{i}is available and first occurrence is at index{first_occurrence}")
# else:
#     print(f"{i}is not present in the list")

##OUTPUT#  10is available and first occurrence is at index1

# take a list o elements from 1 t0 50 whenever use enter the value from 1 to 50 particular elements need to removed.


# lst=[]
# n=int(input("enter number of elements:"))
# for i in range(1,n+1):
#     lst.append(i)
# print(lst)
# p=int(input("enter number to be removed:"))
# if(p>n):
#     print("index out of range")
# elif(p not in lst):
#     print("number is already removed")
# else:
#     lst.remove(p)
#     print(lst)



# elements_list=list(range(1, 51))
# user_input = input("enter the number you want to remove:")
# number = int(user_input)
# if 1 <= number <= 50:
#        if number in elements_list:
#           elements_list.remove(number)
# print (elements_list)





## Append

# l=[1,2,3]
# l.append(4)
# print(l)  ## [1, 2, 3, 4]

# l1=[10,20,30]
# l2=[40,50,60]
# l1.append(l2)
# print(l1) ## [10, 20, 30, [40, 50, 60]]

# l=[10,20,30]
# for i in range(40,50):
#     l.append(i)
# print(l)  ### [10, 20, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# my_list=[]
# my_list.append('10')
# my_list.append('chandrika')
# my_list.append('20')
# print(my_list) ## ['10', 'chandrika', '20']

## insert()

# l=[1,2,3,4,5,6]
# l.insert(3,4)
# print(l)   ## [1, 2, 3, 4, 4, 5, 6]

# l=[10,20,30,60]
# l.insert(30,40)
# l.insert(40,50)
# print(l)  ## [10, 20, 30, 60, 40, 50]

# l=[1,2,3,6]
# l.insert(3,4)
# l.insert(4,5)
# print(l)  # [1, 2, 3, 4, 5, 6]

# l=[2,3,4,5]
# l.insert(0,1)
# print(l)   #[1, 2, 3, 4, 5]

# l=[1,2,3,4]
# l.insert(-1,5)
# print(l)  #  [1, 2, 3, 5, 4]

## Extend

# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)  #[1, 2, 3, 4, 5, 6]

# my_list=[1,2,3]
# my_string="chandrika"
# my_list.extend(my_string)
# print(my_list)  ##[1, 2, 3, 'c', 'h', 'a', 'n', 'd', 'r', 'i', 'k', 'a']

# my_list=[1,2,3]
# my_range=range(4,7)
# my_list.extend(my_range)
# print(my_list)  ##[1, 2, 3, 4, 5, 6]

# l1=[1,2,3]
# nested_list=[4,[5,6],7]
# l1.extend(nested_list)
# print(l1)   ## [1, 2, 3, 4, [5, 6], 7]

## remove

# l=[10,20,30,10,40,10]
# l.remove(10)
# print(l)   ## [20, 30, 10, 40, 10]

# l=[10,20,30,20,40]
# while 2 in l:
#     l.remove(2)
# print(l)  ## [10, 20, 30, 20, 40]

# l=["cherry","apple","mango","chandrika"]
# l.remove("mango")
# print(l)  ##['cherry', 'apple', 'chandrika']

# l=[1,2,3,4]
# l.clear()
# print(l)  ## []  clear method is used to remove all the elements from the list.

## Count

# l=[1,2,3,1,4,1,5]
# s=l.count(1)
# print(s) ## 3

# l = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# x =l.count(9)
# print(x)  ## 2

# l=["chandrika","is","Good","Girl","is"]
# s=l.count("is")
# print(s)  ##2

# l=[10,20,30,40,50,10,20,40,10,30,40]
# s=l.count(10)
# print(s)  ## 3

## Index


list = [1, 2, 3, 4, 1, 1, 1, 4, 5]
print(list.index(4, 4, 8))  ## 7


# list= ['cat', 'bat', 'mat', 'cat', 'pet']
# print(list.index('bat'))  ## 1

# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# print(list1.index(10))  ## value error

# list1 = [6, 8, 5, 6, 1, 2]
# print(list1.index(6, 1))  ## 3

## pop()


# l = [1, 2, 3, 4, 5, 6]
# print(l.pop(3))   ## 4 

# l = [1, 2, 3, 4, 5, 6]
# print(l.pop(3),l)  ##4 [1, 2, 3, 5, 6]

# f=["apple","mango","banana","orange"]
# a=f.pop()
# print(a)  ##orange
# print(f)##['apple', 'mango', 'banana']

# l=[10,20,30,40,50]
# r=l.pop(2)
# print(r)  ##30
# print(l) ##[10, 20, 40, 50]

## Reverse()

# l=[1,2,3,4,5]
# l.reverse()
# print(l)  ## [5, 4, 3, 2, 1]

# l=["chandrika","sindhu",1,"chandu",20,50]
# l.reverse()
# print(l)   ##[50, 20, 'chandu', 1, 'sindhu', 'chandrika']

# l1=[10,20,30,40,50]
# l2=[60,70,80,90]
# l1=l2.reverse()
# print(l1)  ## None

# l1=[10,20,30,40,50]
# l2=[60,70,80,90]
# l1=l2.reverse()
# print(l2)  ## [90, 80, 70, 60]

## sort()

# l=[5,6,3,4,2,1]
# l.sort()
# print(l)  ##[1, 2, 3, 4, 5, 6]

# f=["Banana","Apple","goat","CAt"]
# f.sort()
# print(f)  ##['Apple', 'Banana', 'CAt', 'goat']

# n=[5,2,8,1,3]
# n.sort(reverse=True)
# print(n)  ##[8, 5, 3, 2, 1]

# l=[90,40,50,60,70]
# l.sort()
# print(l)  ## [40, 50, 60, 70, 90]









































































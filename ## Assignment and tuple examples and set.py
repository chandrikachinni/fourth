## Assignment

# user_input=input("enter a string")
# vowels=[]
# for char in user_input:
#     if char.lower() in 'aeiou':
#         vowels.append(char)
# print("vowels present in the input:",vowels)

## Using list comprehension

# lst=['chandrika','makes','works','easy']
# l=[]
# l1=[i for i in lst[0] ]
# l+=l1
# print(l)

## using swapcase

# s="magic WONDERLAND"
# s1=s.swapcase()
# l=[i for i in s1]
# print(l)   ###['M', 'A', 'G', 'I', 'C', ' ', 'w', 'o', 'n', 'd', 'e', 'r', 'l', 'a', 'n', 'd']

## using uppercase

# s='PROGRAMMING'
# s2=s.lower()
# l=[i for i in s2 ]
# print(l)  ##['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

## using upper

# s='programming'
# s2=s.upper()
# l=[i for i in s2 ]
# print(l)  ##['P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']


## Tuple

# tuple=()
# print(tuple)  ## ()

# tuple=(10,20,30,40)
# print(tuple)    ##(10, 20, 30, 40)

# tuple=("Jhon","Mary","jack",20)
# print(tuple)  ## ('Jhon', 'Mary', 'jack', 20)

# tuple=("Hello",[1,2,3],(5,6,7))
# print(tuple)  ##('Hello', [1, 2, 3], (5, 6, 7))

# tuple=("hello")
# print(tuple) ## hello

# tuple=("hello welcome to marolix")
# print(tuple)  ## hello welcome to marolix

### COUNT()

# t = (1, 3, 4, 1, 6 ,1 )
# count = t.count(1)
# print(count) ## 3

# t = (1, 3, 4, 1, 6 ,1 )
# count = t.count(7)
# print(count)  ## 0


# t=("hello welcome to my world")
# t.count("helllo")
# print(t)  ###hello welcome to my world


# tuple = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
# count = tuple.count(('a', 'b'))
# print(count)  ##2

# tuple = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
# count = tuple.count([3, 4])
# print(count)  ## 1


## index()


# numbers = (0, 2, 4, 6, 8, 10)
# index = numbers.index(3)
# print(index)   ### value error x not in tuple

# t=(0,2,4,6,8,10)
# t.index(0)
# print(t)  ##(0, 2, 4, 6, 8, 10)

# t=("pYthon programming")
# index=t.index("pYthon")
# print(index)   ##pYthon programming

# vowles=('a','e','i','o','u','u')
# index=vowles.index('u')
# print(index)  ##4


# vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# index = vowels.index('e')
# print(index)  ##1


# vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# index = vowels.index('i')
# print(index) ## 2

## sorted()

# tuple = ('e', 'a', 'u', 'o', 'i')
# print(sorted(tuple))  ##['a', 'e', 'i', 'o', 'u']

# tuple=(1,4,6,3,2,9,7,5)
# print(sorted(tuple)) ## [1, 2, 3, 4, 5, 6, 7, 9]

# tuple=('c','h','a','n','d','r','i','k','a')
# print(sorted(tuple))  ##['a', 'a', 'c', 'd', 'h', 'i', 'k', 'n', 'r']

# t=(20,80,30,10,50,40)
# print(sorted(t))  ###[10, 20, 30, 40, 50, 80]

# t=("chandrika")
# print(sorted(t))  ##['a', 'a', 'c', 'd', 'h', 'i', 'k', 'n', 'r']

# t=("chandu",10,"sindhu",30,20)
# print(sorted(t))   ## type error 

## Set()

# s={10,20,30,40}
# print(set(s))  ##{40, 10, 20, 30}

# s={}
# print(set(s))  ##set()

s={"chandu"}
print(set(s))


##pro to take a tuple of numbers from keyboard and print Sum,average

# list=[]
# n=int(input("enter the number of elements: "))
# for i in range(0,n):
#     x=int(input("enter the elements: "))
#     list.append(x)
# t=tuple(list)
# sum=0
# print(t)
# for i in t:
#     sum+=i
# print("the sum of values of tuple is",sum)
# average=sum/len(t)
# print("average of tuple values is",average)


















































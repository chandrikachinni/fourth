# Assignment

s="ram is good boy"
l=s.split(" ")
# print(l)  ##['ram', 'is', 'good', 'boy']
l1=l[::-1]
# print(l1)  ## ['boy', 'good', 'is', 'ram']
output=' '.join(l1)
print(output)  ## boy good is ram


# str="ABCDAABBCCDDEEFFGGHI"
# print("input string:",str)
# str2=""
# for char in str:
#     if char not in str2:
#         str2=str2+char
# print("output string:",str2)   ### ABCDEFGHI



## strip

# x = "abaaab"
# print(x.strip('a'))  ##baaab
# print(x.strip('b'))   ### abaaa
# print(x.strip())    ## abaaab

# x = "10,20,30,40,50"
# print(x.strip('50'))  ## 10,20,30,40,
# print(x.strip('0'))   ## 10,20,30,40,5


# #lstrip

# s = "chandrika is good girl"
# print(s.lstrip('c'))        ##    handrika is good girl              
# print(s.lstrip('chandrika'))      ##  is good girl
# print(s.lstrip( ))   ## chandrika is good girl
# a=",,,$&^.....python"
# print(a.lstrip(",..$&^"))   ## python
# print(a.lstrip('python'))   ###,,,$&^.....python

# #rstrip

# s= "aaaaabcccddee"
# print(s.rstrip('a'))   ## aaaaabcccddee
# print(s.rstrip('e'))   ## aaaaabcccdd
# print(s.rstrip())     ## aaaaabcccddee
# a=",,,$&^.....python"
# print(a.rstrip('.'))   ## ,,,$&^.....python
# print(a.rstrip('python'))   ## ,,,$&^.....

# rsplit

# langs='c,pyhton,java,sql'
# print(langs.rsplit(',')) #['c', 'pyhton', 'java', 'sql']

# fruits='apple,banana,mango,orange'
# print(fruits.rsplit('.')) # ['apple,banana,mango,orange']

# fruits='apple*banana*mango*orange'
# print(fruits.rsplit('*')) #['apple', 'banana', 'mango', 'orange']

# txt="chandrika$is$a, good >girl"
# print(txt.rsplit('$,'))   # ['chandrika$is$a, good >girl']

# txt="chandrika$is$a, good >girl"
# print(txt.rsplit('>'))  # ['chandrika$is$a, good ', 'girl']

## split

# a="  pyhton is programming lanuage"
# print(a.split(" "))  ###['pyhton', 'is', 'programming', 'lanuage']
# print(a.split("python"))  ## ['pyhton is programming lanuage']

# a="Pyhton-is ,programming> lanuage"
# print(a.split("programming"))   ## ['Pyhton-is ,', '> lanuage']

# s="pyhton is programming lanuage"
# l=s.split(" ")
# l1=l[-1::-1]
# print(l1)   ### ['lanuage', 'programming', 'is', 'pyhton']
# output=' '.join(l1)
# print(output)  ###lanuage programming is pyhton

## count

# s="1,2,3,5,8,9,4,3,2,9,6"
# print(s.count("9"))   ## 2

# s="ram is good boy"
# print(s.count("is")) ## 1

# s="ram is good boy"
# print(s.count("is",20,len(s)))#  ## 0

# s="apple,banana,mango,orange,cherry"
# print(s.count("cherry")) ## 1

# s="ram is good boy good good good "
# print(s.count("good",10,len(s))) ### 3

### replace

# s = "one one was a race horse, two two was one too."
# x = s.replace("one", "five")
# print(x)  ### five five was a race horse, two two was five too.

# s="ram is good boy"
# print(s.replace("good","bad"))  ## ram is bad boy

# a="10,20,10,40,50,60,10,50,10"
# print(a.replace("10","90"))  ### 90,20,90,40,50,60,90,50,90

# s="ram is good boy"
# print(s.replace("o","10"))   ###ram is g1010d b10y

### join

# s=["python","is","a", "programming", "language"]
# print("#".join(s))  ###  python#is#a#programming#language

# s={"python":"is","a" :"programming" "lanuage"}
# print("generalpurpose".join(s))   ## pythongeneralpurposea

# s="a,b,c,d,e,f,g"
# print("$".join(s))  ### a$,$b$,$c$,$d$,$e$,$f$,$g

# s="ram is good boy"
# print("_".join(s))   ### r_a_m_ _i_s_ _g_o_o_d_ _b_o_y

# s="BTS is a popular band"
# print("*".join(s))   ### B*T*S* *i*s* *a* *p*o*p*u*l*a*r* *b*a*n*d

### capitalize### 

# s="BTS is a popular band"
# print(s.capitalize( ))   ### Bts is a popular band

# s="bts is a popular band"
# print(s.capitalize())   ###  Bts is a popular band

# s="5 years bTS is a Popular BAND"
# print(s.capitalize())    ###5 years bts is a popular band

# s="BTS IS A POPULAR BAND"
# print(s.capitalize())   ##  Bts is a popular band

### title

# s="bts is a popular band"
# print(s.title())   ### Bts Is A Popular Band

# s="BTS IS A POPULAR BAND"
# print(s.title())  ##Bts Is A Popular Band

# s="BTS$IS$A$POPULAR$BAND"
# print(s.title())   ### Bts$Is$A$Popular$Band

# s="welcome to my 3rd concert"
# print(s.title())   #### Welcome To My 3Rd Concert

### lower

# s="BTS IS A POPULAR BAND"
# print(s.lower())    ####bts is a popular band

# s="welCome tO my 3RD concERt"
# print(s.lower())   ###welcome to my 3rd concert

# s="BtS iS a PoPuLaR BaNd"
# print(s.lower())   ###bts is a popular band

# s="Scars To Your Beautiul"
# print(s.lower())   ####scars to your beautiul

#### upper

# s="Scars To Your Beautiul"
# print(s.upper())   ### SCARS TO YOUR BEAUTIUL

# s="BtS iS a PoPuLaR BaNd"
# print(s.upper())   ### BTS IS A POPULAR BAND

# s="welCome tO my 3RD concERt"
# print(s.upper())    ####WELCOME TO MY 3RD CONCERT

# s="BTS IS A POPULAR BAND"
# print(s.upper())  ###BTS IS A POPULAR BAND

### swapcase

# s="BTS is a popular band"
# print(s.swapcase())   ### bts IS A POPULAR BAND

# s="bTs Is a PO$Pular BAND"
# print(s.swapcase())    ###BtS iS A po$pULAR band

# a="BTS IS A POPULAR BAND"
# print(a.swapcase())   ###bts is a popular band

# s="ram is good boy"
# print(s.swapcase())   ### RAM IS GOOD BOY

# s="BTS 3 Is #a pOpuLar $ band"
# print(s.swapcase())   ### bts 3 iS #A PoPUlAR $ BAND

### startswith

# s="BTS IS A POPULAR BAND"
# print(s.startswith("BTS"))   ### True 

# s="BTS 3 Is #a pOpuLar $ band"
# print(s.startswith("pOpuLar"))   ### False

# s="ram is good boy"
# print(s.startswith("good"))   ### False

# a="welCome tO my 3RD concERt"
# print(a.startswith("3RD"))    ### False

# s="BTS is a POPULAR band"
# print(s.startswith("POPULAR"))   ## False

### isalnum

# s="BTS is a POPULAR band"
# print(s.isalnum())   ### False

# s="programming12"
# print(s.isalnum())   ###True

# s="programming 12"
# print(s.isalnum())  ###False
 
# s="BTS$IS$A$POPULAR$BAND"
# print(s.isalnum())   ### False

# s="Bts 12 is2 a3 popular $ band"
# print(s.isalnum())   ### False

### isalpha

# s="BTS is a POPULAR band"
# print(s.isalpha())   ### False

# s="ProgrammingL"
# print(s.isalpha())   ### True

# s="Programming 10"
# print(s.isalpha())  ### False

# s="Programming10"
# print(s.isalpha())   ### False

# s="BTS$IS$A$POPULAR$BAND"
# print(s.isalpha())   ###False


####islower

# s="Programming language"
# print(s.islower())   ###  False

# s="programming lanuage 453"
# print(s.islower())   ### True

# s="ram is good boy"
# print(s.islower())  ### True

# s="RAM IS GOOD BOY"
# print(s.islower())   ### False

# s="Ram IS a Good *** boy"
# print(s.islower())   ### False


####isupper

# s="BTS IS A POPULAR BAND"
# print(s.isupper())  ### True

# s="bts is popular band"
# print(s.isupper())    ####False

# s="programming lanuage 453"
# print(s.isupper())   ### False

# s="BTS@IS#A%POPULAR&BAND"
# print(s.isupper())   ###True

# s="BTS @ IS # A % POPULAR & BAND"
# print(s.isupper())  ### True

### istitle

# s="BTS IS POPULAR BAND"
# print(s.istitle())   ### False

# s="Bts Is A Popular Band"
# print(s.istitle())   ### True

# s="bts is a popular band"
# print(s.istitle())  ### False

# s="programming lanuage 453"
# print(s.istitle())  ###False

# s="programming lanuage453"
# print(s.istitle())   ###False

# s="Programming Lanuage453"
# print(s.istitle())  ###True


### isdigit

# s="BTS is a popular band"
# print(s.isdigit())   ###False

# s="Programming Lanuage453"
# print(s.isdigit())  ####False

# s="2023003"
# print(s.isdigit())    ###True

# s="\125.%90"
# print(s.isdigit())  ###False

# s="10,20,30,40,50"
# print(s.isdigit())  ##False

###isspace

# s="  "
# print(s.isspace())  ###True

# s=" c "
# print(s.isspace())  ## False

# s="Programming language"
# print(s.isspace())  ###False

# s="10  "
# print(s.isspace()) ###False

# s=" ."
# print(s.isspace())  ###False

### isdecimal

# s="print hello"
# print(s.isdecimal())  ##False

# s="12234"
# print(s.isdecimal())  ## True

# s=" "
# print(s.isdecimal())  ###False

# s=" \0047"
# print(s.isdecimal())  ####False


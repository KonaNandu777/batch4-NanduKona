#a,b=22
#print(a,b)
#a=1,2
#print(a)
#print(type(a))
#a,b=c=3,4
#print(a)
#print(b)
#print(c)

# swapping
#a=7
#b=5
#c=' '
#c=a
#a=b
#b=c
#print(a)
#print(b)

#a=a+b   #swapping numbers without using extra memory or variable
#b=a-b
#a=a-b
#print(a,b)

#a,b=b,a
#print(a,b)
#a=a*b
#b=a/b
#a=a/b
#print(a,b)

#id()---> used to find the memory address of the variable
#print(id(a))
#print(id(b))

#----> Keywords
# keywords are reserved words which provide special meaning to compiler or interpretor

#import keyword
#print(keyword.kwlist) #what are the keywords
#print(len(keyword.kwlist)) #how many no. of keywords --35
#print(type(keyword.kwlist)) #what is the type of the keywords --list

# to check if the string is keyword or not
#print(keyword.iskeyword("nandu")) # keyword is present are not just like testing

#if = 8
#print(if) #error bcz it is a keyword

 # !---->literals -- it is the constant value assigned to  a variable
# if only the variable is in capital then it is considered as a literal which is constant
#a=28 # a is variable
#A=28 # A is constant

#hash()--> it creates a hash value for constant datatypes and provides error
#for non constant datatypes
#n1=2+3j
#print(hash(n1)) # no error 

#n1=[1,2,3]
#print(hash(n1)) # error --> list is non-constant or mutable datatype

#a=9 #in python same values address will be same but different in c,java etc
#b=9
#print(id(a))
#print(id(b))

#---> OPERATORS
# they are symbols which is used to perform various operations btw 2 0r 3 operands

#Arithmetic
#assignment
#logical
#relational or comparison
#bitwise
#identity
#member ship

#--->ARITHMETIC   +,-,*,/,%,//,**
#EX:-
     #a=2
      #b=3
      #print(a+b)
#input() --> used to get the run time input
  #a=input("enter the value")
  #print(a)
 # print(type(a))  # string type
         #conversion of data type from string to int 
#a=int(input("enter the value") #(error--> if we give float bcz we given int )
#a=eval(input("enter the value") #eval--> used to get the runtime values of all datatypes

#a=2
#b=3
#print(a/b)  # is used to get the quotient value
#print(a%b)  # is used to get the remainder value
# // -->floor division

#a=98
#b=3
#print(a//b)--> the output will be in int whether the value is in float
# **--> used for power of a number
#print(2**4)

#Assignment--> *=,-=,+=,/=,&=,%=
#a=8
#a+=2
#print(a)

#a=30
#a|=2
#print(a)
#comparison --> >=,<,>,==,!=
# bitwise -->&,|,^,~,<<,>> (AND,OR,XOR,COMPLEMENT
#a=7
#b=5
#print(a&b)
#print(~10)
#  128   64  32  16  8   4  2  1   
#   o     0   0   0  1   0   0 1 --->9
#   1     1   1    1  0  1   1  0 --->-10
# first do 1's complement and then add 1 to it then we get negative value(-10)
# print (5<<3)
# 128   64  32  16  8   4  2  1   
#   0    0   0   0  0  1   0 1 --->9 3<
#    0    0  1   0   1  0  0  0
#    0    0   0  0   0  0  0   0 --  >3
# 16>4 --> ans 1

#Logical operator--> AND,OR,NOT --to check or compare the expressions
#a = 3
#print(a>4 and  a<5)  ---> FALSE
#print(a>4  or  a<5)  --->TRUE
#print(not(a>4 and a<10
#IDENTITY operator
# it is used to compare the memory location that are stored
#is, is not 
#a=8
#b=6
#print(a is b)
#a=[1,2,3]
#b=[1,2,3]
#print(a is not b)
 #Membership operator
 # in ,not in
#l1=[7,8,9,0,4,7]
#num=55
#print(num in l1)
#print(num not in l1)
#num=678
#print(8 in num) #error

# CONDITIONAL statement
#  if,elif,else
#ex: c syntax
#if(condition){
  #  statement;
    #statement;
   # }
# PYTHON syntax
#if condition:
 #    statement;
  #   statement;
   #  statement;
#ex:
#a=6
#if a:
 #   print("TRUE")
#EX"2
 #a=5
 #if a>3:
    # print("hello")
#else
   # print("NO")
#EX3:
#if7>8:
  #     print("hello")
#print("no")
  #ex4:
#a=0
#a=None
#a=False
#a=" "
#if a:
  #  print("yes")
#else:
  #  print("no")
#a=int(input("enter the number"))
#if a%2==0:
 #   print("even")
#else:
 #   print("odd")
a=int(input("enter the number"))
name=input("enter the name")
nationality=input("enter the nationality")
if(a>18 and nationality=="indian"):
    print("eligible")
else:
    print("not eligible")




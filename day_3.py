#EX:3
'''length=int(input())
breadth=int(input())
if length==breadth:
   print("its a square")
else:
   print("its not a square")'''
#Ex:4
'''integer=int(input("enter the number"))
if integer%5==0 and integer%7==0:
   print("number is multiple")
else:
    print("number is not multiple")'''
#Ex:4
'''cost=int(input("enter price"))
amount = 0
if cost>100000:
   discount=cost*(6/100)
   value=cost-discount
    amount=value*(15/100)
    print(value+amount)
else:
   am=cost*(5/100)
    amount=am+cost
    print(amount)'''

#if elif
#ex:1
'''a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
   print("b is greater")
else:
    print("c is greater")'''

'''mark=int(input("enter the marks"))
if mark>80:
    print("A")
elif mark>60 and mark<80:
    print("B")
elif mark>50 and mark<60:
    print("C")
elif mark>45 and mark<50:
    print("D")
elif mark>25 and mark<45:
    print("E")
else:
    print("F")'''

#---> short hand  if else
 #ex:
#a=9
#b=60
#if a>b:
   # print("A")
#else:
   # print("B")
#---> using short hand if else
#rules
#1 statement inside the if condition have to be present at first
#2 elif cannot be used in short hand if else
#3 always it have to end with else
#  ---> print("A") if a>b else print("B")

#le=input("enter the letter")
#print("Vowels") if (le=='a'or le=='e' or le=='i' or le=='o' or le=='u' ) else print("Consonents")

#str1="aeiouAEIOU"
#if char in str1:
 #   print("vowel")
#else:
 #   print("consonent")
#-----> looping
 #looping can be implemented using
 #for loop 
 #while loop
#--> for loop -- which is used for iteration if we know the number of times the loop have to run
 # it is used to iterate the iterables eg(string,list,tuple,etc...)

#todo -->syntax for loop
 # for syntax in c
 #for(i=0;i<10;i++){
 #printf("hello");
 #}

 
# for syntax in python
#for userdefined_variables in range (start,end,step):  default step value is 1
    #statement
    #statement
    #statement
#EX:1
# to pint the value from 1 to 10 using for loop
#for i in range (0,10): #(n,n-1)
 #   print(i)

#EX:2
#for val in range(23,30,2):
 #   print(val)
 #EX:3
#for val in range(10,0):#(blank-no output)
 #   print(val)
#for val in range(10,0,-1):# 10,9,8,....2,1
 #  print(val)
 
 # EX:4
 #print the output of 7th multiplication table from 21 to 43

#for val in range (1,10+1):
    #print(val*7)
 #   print('7','x',val,'=',val*7)-----> method:1
   
   #---> method:2
   # ans="7x{}={}"
    #print(ans.format(val,val*7))
  #---> method:3
#    print(f"7 x {val}={val*7}")
#ex:5


#break-------> used to terminate the loop
#for val in range(1,10):
 #   if val==6:
  #      break  # here the val 1st check the condition then later it 
   # print(val)  # will print 

#ex:6
#for val in range(1,10):
 #    print(val)    # here the val will print 1st then later it will check the 
  #   if val==6:     condition
  #       break
#ex:7
'''for val in range(1,10):
  if val==6:         # here the value 6 only will print
      print(val)
     break'''
 #continue 
#ex:1
'''for val in range (1,10):
    if val==6:
        continue  #here the value 6 will be skkipped and remaining wil be executed 
    print(val)'''

 #print even numbers between 20 to 40
#for val in range (20,40+2,2):
   # print(val)

'''for val in range (20,40):
    if val%2==0:
        continue
    print(val*2)'''
# while loop --> while is used when we do not know the number of times the loop have to run
# to iterate the non iterable elements while loop is used
 # todo syntax
'''
initialisation
  while condition:
      statement
      incre or decre
                   '''
#ex1
# to iterate number from 1 to 10
'''i=0
while i<11:
    print(i)
    i+=1'''
# decending order from 10 to 1 
'''i=10
while i>0:
    print(i)
    i-=1 '''
 ##          
'''for i in range n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)
#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)'''

n=int (input("enter number "))
sum=0
for val in range(1,n+1):
    sq=val*val
    if val%2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
print(sum)
n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)
#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reversn1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)
#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)e)

















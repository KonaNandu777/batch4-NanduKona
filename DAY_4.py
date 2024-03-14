#ex:1 iterate from 20 to 30 and break the loop in 27
#method:1
'''i=20
while i<31:
    if i==27: #20 to 26
        break
    print(i)
    i+=1 '''
#method :2
'''i=20
while i<31:
    print(i)# 20 to 27
    if i==27:
        break
    i+=1 '''
#method:3
'''i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1'''
 # continue   
'''i=20
while i<31:
     if i==27:
         continue
     print(i)
     i=i+1'''
#method 
'''i=20
while i<31:
     i=i+1
     if i==27:
         continue
     print(i)'''
#method while to iterate from 12 to 22 and find the sum of all numbers
'''i=12
temp=0
while i<23:
    temp=temp+i
    i+=1
print(temp)'''
#method
'''i=20
temp=0
while i<26:
    temp=temp+i
    i+=1
avg=(temp/5)
print(avg)'''
#method
'''i=20
temp=0
count=0
while i<26:
    temp=temp+i
    count+=1
    i+=1
print(count)
print(temp/count)'''

#sum of the digits
'''n = 278
sum = 0
while n > 0:
    digit = n%10
    sum+=digit
    n/=10
print( sum)'''

# nested for loop
#no. of for loop inside one another
#first inner for loop will execute completely then later to goes to first for loop
'''for i in range(1,3+1):
    for j in range (1,4+1):
        print (i,j)'''
#continues numbers
'''sum=0
for i in range(1,5):
    for j in range(1,5):
        sum=sum+1
        print(sum,end=" ")
    print()'''
#to print stars in right andle trianle
'''for i in range (0,6):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''
#reverse 
'''for i in range (0,6):
    for j in range(i,6):
         print("*",end=" ")
    print()'''
# hallow square
'''for i in range (0,6):
    for j in range (0,6):
        if j==0 or j==5 or i==0 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''for i in range (0,5):
    for j in range(0,6):
        if ((i==0 and j==3) or (i==1 and (j>=2 and j<=4) or (i==2 and j>=1 and j<=5))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# Hallow  right angled triangle)
'''for i in range (0,6):
    for j in range(0,6):
        if ((j==0 or i==5) or (i==j)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#  LIST
''' primary
    Number---> int,float,complex
    string
    boolean
    none
collection
   list
   tuple
   set
   dictionary'''
#list
'''---> if the collection of elements are surrounded by square brackets, it is considered to be list'''
#eg::
      # l1=[4,7,9,9.89,"hello",7+9j,[8,9,0]]

      
#characteristics of list
'''
   1) list have to be surrounded by []
   2) It is mutable (the elements in the list are changeable)
   3)Every element inside list is indexed
   4)The elements inside list will be ordered format
   5)It can hold duplicte values
   6)its heterogenous  '''
# to acess the elements in list
'''lst1=[1,2,3,4,4.56,"n","k"]
print(l1)'''
#-->Indexing: In the collection datatypes like list,tuple,string,the elements will be alloted
# with pre-defined unique value called index values

#We have 2 types of indexing
#positive indexing--> starts with 0 from left hand side
#negative indexing--> starts with -1 from right hand  side


'''positive indexing'''
#print(lst1[0])
#print(lst1[5])
#print(lst1[28])-->error

'''negative indexing'''
#print(lst1[-4])
#print(lst1[-1])
#print(lst1[-2])

#--->slicing

#example for positive
'''lst1=[1,2,3,4,4.56,"n","k"]
#lst1[start_index:end_index:step]
#print(lst1[0:4])
#print(lst1[:5])#from 0to 5
#print(lst1[3:])#from 3to 6
#print(lst1[:])#total all values
#print(lst1[0:6:1]) # lst1[0:6] --> both are same
#print(lst1[0:6:2])'''

#example for negative
'''lst1=[1,2,3,4,4.56,"n","k"]
#print(lst1[-1:-4]) -->empty list[]
#print(lst1[-4:-1:2])
#print(lst1[-4:-1])'''

#to insert at add element inside list
#append() --> used to add element at last position of list  

'''l1=[9,8,0,6]
l1.append("car")
print(l1)'''






















        
   
   

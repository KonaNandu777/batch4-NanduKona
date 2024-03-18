#assessment questions 
#q1
'''s1='string'
s1=s1[0:1].upper()+s1[1:len(s1)-1]+s1[len(s1)-1:len(s1)].upper()
print(s1)'''

'''s1=input("enter the string")
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)'''

#Q2
'''n=128
sum=0
f1=0
while n!=0:
    temp=n%10
    if temp==0:
       f1=1
       break
    check=sum%temp
    if check!=0:
       f1=1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")'''
#Q3
'''l1=[1,2,3,4]
l2=[5,6,7,8]
l4=[]
for i in range (len(l1)):
    l3=l1[i]+l2[i]
    l4.append(l3)
print(l4)'''

#--->set
#Characteristics of set 
'''
1)set can be created by {}
2)the elements inside the set are not indexed
3)does not allow duplicate elements
4)it unordered
5)heterogenous --> accept only unmutable datatype
6)mutable or changeble '''

#ex:1
'''s1={9,9,89,7.76,9+8j,(8,7,5),"fan",'r'}
print(s1)'''

#ex2
'''s2={7.9,9,6,7,[3,8]}
print(s2)'''#-->error

#ex3( common inbuit functions for  list ,tuple,set)
'''min(),max(),len()'''
#ex4
#to add elements inside set (add(),update())
#add() --> to add elements
'''s1={4,6,8,'i'}
s1.add(43)
print(s1)'''
#update()(it can take either in tuple or list format update(9,0)-->error then update((9,0))
'''s1={4,6,8,'i'}
s1.update((9,0))
print(s1)'''
#to delete elements inside the list
#pop()--> will delete randomly
'''s1={4,6,8,'i'}
s1.pop()
print(s1)'''
#remove() --> will delete directly
'''s1={4,6,8,'i'}
s1.remove(6)
print(s1)'''
#discard()(remove and  discard are same but in discard if we give the element
#which is not present in set we get as it is set as output)
'''s1={4,6,8,'i'}
s1.discard(8)
print(s1)'''
#clear()
'''s1={4,6,8,'i'}
s1.clear()
print(s1)'''#--> set()

'''s1={}
print(type(s1))'''#--><class 'dict'>
#to create the empty set
'''s1=set()
print(type(s1))'''#--><class 'set'>

'''s1={4,6,8,'i'}
del s1
print(s1)'''#-->error

#join the sets
#union()--> to combine 2 sets
'''s1={2,3,4}
s2={5,8,9}
s3=s1.union(s2)
print(s3)'''#-->(2,3,4,5,8,9)

'''s1={2,3,4}
s2={5,8,9}
s1.union(s2)
print(s1)'''#-->(2,3,4)

#intersection()--> to get common elements inside the set
'''s1={2,5,4}
s2={5,8,9}
print(s1.intersection(s2))'''#-->{5}
#difference()
'''s1={2,5,4}
s2={5,8,9}
print(s1.difference(s2))#{2, 4}
print(s2.difference(s1))
#to get the unique values inside the both sets in one set 
print(s1.symmetric_difference(s2))'''
#issubset()(if all elements in s1 are present in s2 then s1 is subset of s2)
'''s1={3,4,6}
s2={7,9,0,6,4,3}
print(s1.issubset(s2))'''#True
#issuperset()(if s2 contains all elements of s1 and then s2 is the parent set of s1) )
'''s1={3,4,6}
s2={7,9,0,6,4,3}
print(s2.issuperset(s1))'''#True

#joint set 
'''s1={1,2,3,4,5}
s2={3,2,7,8,9}
for i in s1:
    if i in s2:
        str1="yes"
print(str1)'''


#-->dictionary
#eg:1
'''d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))'''

#char of dictionary
'''
1)have to be surrounded by {}
2)It have to be in the form of key ,value pair(seperated by :)
3)duplicate keys and values are not allowed
4)it is mutable
5)it is unindexed
6)it is ordered
7)keys does not allow mutable datatypes,values allow mutable datatype'''

 #to cess elements in dictionary
'''d1={1:100,2:200,3:300,4:400}
print(d1)'''
#to access the value
'''d1={1:100,2:200,3:300,4:400}
print(d1[1])'''#-->100

#some common functions
#len(),min(),max()

#to find min and max but it is based on key not on values
'''d1={1:100,2:200,3:300,4:400}
print(min(d1))'''#-->1

'''d1={1:100,2:200,3:300,4:400}
print(max(d1))'''#-->4

#to find min and max but it is based on values
'''d1={1:100,2:200,3:300,4:400}
print(min(d1.values()))'''#-->100

'''d1={1:100,2:200,3:300,4:400}
print(max(d1.values()))'''#-->400

#to add element(key and value pair) in dict
'''d1={1:100,2:200,3:300,4:400}
d1[6]=600
print(d1)'''

#to replace a value in dictionary
'''d1={1:100,2:200,3:300,4:400}
d1[2]="water melon"
print(d1)'''

#to delete a value in dictionary
'''d1={1:100,2:200,3:300,4:400}
print(d1.popitem())#-->4:400
print(d1)''' #-->{1: 100, 2: 200, 3: 300} 

'''d1={1:100,2:200,3:300,4:400}
d1.pop(2) -->2 is the key
print(d1)'''#{1: 100, 3: 300, 4: 400}

#clear(),del(as sams as list,tuple)

#join 2 dictionary
'''d1={1:100,2:200,3:300,4:400}
d2={"a":"ambition","b":"bold","c":"character"}
d1.update(d2)
print(d1)''' #{1: 100, 2: 200, 3: 300, 4: 400, 'a': 'ambition', 'b': 'bold', 'c': 'character'}

#get()
'''d1={1:100,2:200,3:300,4:400}
print(d1.get(2))-->200
print(d1[2])-->200
print(d1.get(99))-->None
print(d1[99])-->error'''

#keys()-->to print all keys
'''d1={1:100,2:200,3:300,4:400}
print(d1.keys())#-->dict_keys([1, 2, 3, 4])
print(type(d1.keys()))#--><class 'dict_keys'>'''

#values()-->tp print all values
'''d1={1:100,2:200,3:300,4:400}
print(d1.values())'''#dict_values([100, 200, 300, 400])

#iterating dictionary
#to iterate keys alone
'''d1={1:100,2:200,3:300,4:400}
for i in d1:
    print(i)'''
#to iterate values alone
'''d1={1:100,2:200,3:300,4:400}
for i in d1.values():
    print(i)'''
#to iterate both keys and values 
'''d1={1:100,2:200,3:300,4:400}
for key,val in d1.items():
    print(key,val)'''

#problem1:
'''n=eval(input("enter the number of times"))
integer=[]
float_value=[]
string=[]
for i in range (n) :
    value=eval(input("print the input"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("provide data in int ,float,string")
print(integer)
print(float_value)
print(string)'''

# return a set elements present in set A or B, but not both
#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
'''set1={10,20,30,40,50}
set2={30,40,50,60,70}
lst=set()
for i in set1:
    if i not in set2:
        print(i)
        lst.add(i)
for i in set2:
    if i not in set1:
        print(i)
        lst.add(i)
print(lst)'''

l1=[1,2,3,4]
l2=["a","b","c","d"]
d1={}
for i in range (4):
    d1[l1[i]]=l2[i]
print(d1)


    
           
    
    

    










    
    



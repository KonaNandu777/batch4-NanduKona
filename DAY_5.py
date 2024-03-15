#lst1=[2,3,4,5]
'''print(len(lst1))
print(max(lst1))
print(min(lst1))'''
#lst1=[2,3,4,5,"n","k"]
'''print(max(lst1))--> error combination of int and string
print(min(lst1))--> error combination of int and string'''

#l1=[4,5,5,5,7.89,4,9,0.28]

'''print(min(l1)) --> wecan get output as 0.28 bcz int and float are considered as same datatype but not string'''
#count() --> how many num of times an element is repeated
'''print(l1.count(5))'''
#to add inside list
#insert(index_value,element)--> to add element at specific index position
'''l1.insert(2,"cars")
print(l1)'''

#to delete element from list
#pop()--> last element will be deleted itself but if we specifie any index value theen that index valued element will be deleted
'''l1.pop()
print(l1)'''

'''l1.pop(4)
print(l1)'''

#**remove (element) --> used to delete element directly
'''l1.remove(9)
print(l1)'''

#**clear() ---> to complete delete all element in list
'''l1.clear()
print(l1)'''

#del--> to delete the list
'''l1=[4,5,5,5,7.89,4,9,0.28]
del l1
print(l1)'''#--> error print(l1) is not defined

#--> join 2 list
'''l1=[9,0,7,8]
l2=[4,5,3,2,]
#print(l1+l2)'''
# another method
#extend() --> to combine 2 list (both methods are same but present one is it update itself with out using extra memory space)
'''l1.extend(l2)
print(l1)'''

#-->copy()
'''l1=[4,5,6,7,8,9,0]
l2=l1.copy()
print(l2)
print(l1)

print(id(l1))
print(id(l2))'''

#difference btw hallow copy and deep copy
#shallow copy

'''import copy
l1=[3,5,6,7,[3,4,5],[2,3]] # both are individual if changes done in one list other  can't be affected
l2=copy.copy(l1)
l2.append(6780)
print(l1)
print(l2)'''
#method 2
'''import copy # before copying if we add the element to  1st list then it will copy to the 2nd list also
l1=[3,5,6,7,[3,4,5],[2,3]]
l1.append(6780)
l2=copy.copy(l1)
print(l1)
print(l2)'''

#deep copy --> used to copy the list with nested list 
'''import copy
l1=[3,5,6,7,[3,4,5],[2,3]]
# print(l1[-1][1]) --> to index nested list
##(method)
l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)'''

# sort --> arrange elements in list in ascending or descending order
'''l1=[3,5,6,73,4,52,3]
l1.sort()
print(l1)'''#to arrange in ascending order

'''l1=[3,5,6,73,4,52,3]
l1.sort(reverse=True) 
print(l1)'''# to arrange in descending order

'''l1=['w',"r","u",9]
l1.sort()
print(l1)'''# error different data type

#///list constructor
#list() --> to convert other collection datatype to list

'''l3=((8,9,0))
print(list(l3))'''

'''l4=(4,5)
print(list(l4))'''

# nested list
'''l1=[8,9,[0,8,7],["w","e","t"],[8,'t']]
print(l1[-2][1])''' #--> e
#positive and negative
'''l1=[8,9,[0,8,7],["w","e","t"],[8,'t']]
print(l1[1:4])
print(l1[1:-1])'''

#to delete t in l1
'''l1=[8,9,[0,8,7],["w","e","t"],[8,'t']]
#print(l1[-1].remove('t')) #print and remove can't work together
l1[-1].remove('t')
print(l1)'''

# combine these ["p","o",'y'],[8,'t']
'''l1=[8,9,[0,8,7],["w","e","t"],[8,'t']]
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)'''

#----->tuple
#char of tuple
'''
1) tuple have to be surrounded by ()
2) the elements inside tuple are not changable
3) the elements inside tuple are indexed
4) the elements will execute in order
5) It is heterogenous
6) it allow duplicate elements'''

#eg:
'''t1=(6,7,8,9.08,[6,0],(3,6),'hello',7+8j)
print(t1)
print(type(t1))'''
# indexing ,slicing are all same as list
'''l1=[8]
print(type(l1))'''#list

#ways to create tuple
'''l1=(8)
print(type(l1))'''#int

'''l1=(8,)
print(type(l1))'''#tuple

'''t2=7,8
print(type(t2))'''#tuple (without brackets also)

'''t2=7,
print(type(t2))'''#tuple (without brackets also)

#len(),min(),max(),index(),count() ---> all are same as list

#to add element inside tuple--->cannot add and cannot delete also

#join the elements
'''t1=(6,9,0)
t2=(4,5,2)
print(t1+t2)'''
#to add all elements in list
'''l1=[4,5,6,7]
print(sum(l1))'''

#sort tuple
'''t1=(3,8,5,799,9)
t1.sort()
print(t1) '''# sortting is not present in tuple 

'''t1=(3,8,5,799,9)
print(tuple(sorted(t1))) #ascending
print(tuple(sorted(t1,reverse=True))) #descending '''

#iterate list and tuple

#iterate based on elements
'''l1=[9,5,8,7,0,5,4,2]
for i in l1:
    print(i)'''

#iterate based on index value
'''l1=[9,5,8,7,0,5,4,2]
for i in range (0,8):
    print(i)'''# index value 0 to 7

'''l1=[9,5,8,7,0,5,4,2]
 print(l1[4])'''# index value=0

'''l1=[9,5,8,7,0,5,4,2]
for i in range (0,len(l1)):
    print(l1[i])'''

# to access string
#s1="hello world"
'''#print(s1)
#print(s1[0:5])#-->hello
#print(len(s1))#-->11
#print(max(s1))#-->w
#print(min(s1))'''
#ord()-->used to find the ASCII value of a character
'''s1='n'
print(ord(s1))'''
#to convert all characters to upper case
'''s1="hello world"
print(s1.upper())'''

#to convert all characters to lower case
'''s1="HELLO WORLD"
print(s1.lower())'''
#strip()--> to eliminate the space in beginning(lstrip) at the end(rstrip)
'''s1="  where are you?  "
print(s1.lstrip())
print(s1.rstrip())'''
#s1="hey there dont sleep"
#print(s1.lstrip(7))

#split()--> to split the words in string based on spacing
'''s1="where are you?"
print(s1.split())#['where', 'are', 'you?']

print(s1.split("r"))#['whe', 'e a', 'e you?']'''

'''s1="where are you?"
print(s1.count('e'))'''#3

#replace()--> to replace the specific char in the string
'''s1="where are you?"
print(s1.replace('r','&&'))'''#whe&&e a&&e you?

#swapcase()--> to convert capital to small and vice versa at a time
'''s1="HEY there"
print(s1.swapcase())'''#hey THERE

#title()--> to write the string in the format of title
'''s1='never giveup'
print(s1.title())'''#Never Giveup

#capitalize--> 1st char of string will be converted to capital
'''s1='never giveup'
print(s1.capitalize())'''#Never giveup
#join the strings
'''s1="hello"
s2="world"
print(s1+s2)'''#helloworld
'''splitlines()--> used to split the string based on lines'''
#s1='''
#how are you
#i am fine
#hey there
#'''
#print(s1.splitlines())

#find()
'''s1="hello world"
print(s1.find('d'))'''#10
#print(s1.index('d')) #-->10

#both index and find  both are same but the difference is in index if the value is not present we get error but in find we get -1 value
'''print(s1.find('z'))-->-1
print(s1.index('z'))#-->error'''

#join()-->
'''l1=["hey","there"]
print(" ".join(l1))'''

'''s1="Welcome to all"
print(s1.endswith('l'))'''#True

'''s1="Welcome to all"
print(s1.startswith('W'))'''#True

'''s1="67"
print(type(s1))'''#<class 'str'>
'''s1="6k7"
print(s1.isdigit())'''#if the value in string are integers then true orelse false

'''s1="Welcome to all"
#print(s1[:])'''#from start to end index value (Welcome to all)

#to get the string in reverse
'''s1="Welcome to all"
print(s1[::-1])'''#lla ot emocleW

 #ex:1
#to find the lower case letters in string
'''s1="HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1
print(count)'''

#ex:2
'''#s1='restarter'
s1='IMAGIN'
fst=s1[0]
bal=s1[1:]
text=bal.replace(fst,'$')
print(fst+text)'''

#ex:3
s1='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
#print(len(s1)) (no. of characters in s1)
#words=s1.split(" ")(no.of words spaced )
#print(len(words))(how many no of words are spaced)
#print(len(s1.split(".")))
'''sentences=s1.split('.')
for val in sentences:
    if val==' ':
        index=sentences.index('')
        sentences.pop(index)
print(len(sentences))'''
#method1 for finding spaces
'''spaces=s1.count(' ')
print(spaces)'''
#method 2 
'''space=0
for i in s1:
    if i==" ":
        space=space+1
print(space)'''
        













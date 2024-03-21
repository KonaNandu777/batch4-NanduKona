#EXAMPLE3
'''def profile(name,age,place):
    txt="my nameis {}.I am {} years old. I am from {}"
    print(txt.format(name,age,place))
profile("nandu",19,"kadapa")'''
#example 4
#function with return statement
'''1)A variable declared inside the function can be accessed outside the function using return
2) return doesnot print anything
3) we cannot write any code below return statement'''
#ex
'''def f1():
    z=7
f1()
print(z)'''#error can't  use outside the function
#method1
'''def f1(a,b):
    c=a*b
    return c
obj=f1(5,4)

def gracemark():
    print(obj+8)
gracemark()'''
 #method2   
'''def f1(a,b):
    c=a*b
    return c
obj=f1(int(input("enter a val")),int(input("enter b val")))

def gracemark(object):
    print(object+8)
gracemark(obj)'''

#123 palindrome
'''def f1(n):
    string=str(n)
    rev=str(n)[::-1]
    print(string,rev)
    if string==rev:
        print("palindrome")
    else:
        print("not palindrome")
a=int(input("enter the value: "))
f1(a)'''

#Based on the declaration of parameters and arguments
# functions are divided into 5 catagories
'''
1)positional args
2)keyword args
3)default args
4)variable length args
5)keyword variable length args'''
#positional args
''' the position of parameter above to be same as position as arguments'''
#ex1
'''def profile(name,phone,mark):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile(7989628419,"nandu",95)'''#my name is 7989628419.My phone number is nandu.I got 95 marks.
#keyword argument
#ex1
'''to overcome the disadvantage of positional args,we use keyword args
 ** It is the process of initialising the parameter with the args while calling the function'''
##
'''def profile(name,phone,mark):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile(name='nandu',mark='95',phone='7989634551')'''#my name is nandu.My phone number is 7989634551.I got 95 marks.

#exception of keyword args function

'''def profile(name,phone,mark):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile(name='nandu',7989634551,mark='95')'''#error-->position args follows keyword args

'''def profile(name,phone,mark):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile(7989634551,name='nandu',mark='95')'''#error-->pofile() name hs multiple values

'''def profile(name,phone,mark):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile('nandu',7989634551,mark='95')'''#my name is nandu.My phone number is 7989634551.I got 95 marks.

##Default args: The method of assigning the argument to the parameter while declaring the function
#ex1
'''def profile(name,phone,mark=95):
    txt="my name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name,phone,mark))
profile('nandu',7989634551)'''
#ex:2 method1:
'''def profile(name,phone,place="kadapa"):
    txt="my name is {}.My phone number is {}.I am from  {}."
    if place!="kadapa":
        print("u are not from kadapa")
    else:
        print("kadapa")
        print(txt.format(name,phone,place))
profile('nandu',7989634551,"a")'''
#method 2
'''def profile(name,phone,place="kadapa"):
        if place=="kadapa" or place=="KADAPA" or place=="Kadapa":
            txt="my name is {}.My phone number is {}.I am from  {}."
            print(txt.format(name,phone,place))
        else:
            print("u are not from kadapa")     
profile('nandu',7989634551)'''
#Exception
'''def profile(name,place="kadapa",phone):   -->#error bcz default args should not folloe positional parameter
        if place=="kadapa" or place=="KADAPA" or place=="Kadapa":
            txt="my name is {}.My phone number is {}.I am from  {}."
            print(txt.format(name,phone,place))
        else:
            print("u are not from kadapa")     
profile('nandu',7989634551)'''

#variable length parameter :single variable parameter can hold multiple variable arguments
'''
1)to pass more then 1 arg to a parameter means we use variable length args
2)To convert normal parameter to variable length parameter,add * to the prefix  of parameter
'''
#ex:1
'''name="nandu",'name1','name2'
def profile(*name):
    for val in name:
        print("My name is",val)
profile("nandu",'name1','name2')'''

'''name="nandu",'name1','name2'
def profile(*name,age):
    for val in name:
        print("My name is",val,"my age is ",age)
profile("nandu",'name1','name2',19)'''#--> age has no args

'''name="nandu",'name1','name2'
def profile(age,*name):
    for val in name:
        print("My name is",val,"my age is ",age)
profile(19,"nandu",'name1','name2')'''


#keyword variable length args
##-->which is used to provide the args in the form of key value pair

#eg:1
'''def price(**price_list):
    print(price_list)
price(shirt=1000,iphone=80000)'''
    
##
'''d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)'''
#p1
'''def number(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
number(int(input("enter number")))'''

'''s1 = "Hello how are you"
s2 = "Hello how is"
for i in  s1:
    if i not in s2:
        s1.split(s2)
        print(s1)'''
#----->object oriented programming
'''
The paradigms of object oriented programming are
*class
*objects
*inheritance
*polymorphism
*abstraction
*encapsulation'''
#class is a blue print of an object
'''l1=[1,2,3,4,5]'''
#ex1-->without using object
'''class c1:
    name1="nandu"
    print(name1)'''
#ex2--> with using object
'''class person:
    name1="nandu"
c=person()-->object
The process of creation of an object is called an Instantiation
print(c.name1)'''
#ex3
#create of a method
#when the function is created with a class is called method
'''class person:
    def display(person):
        print("Hello welcome to classes")
p=person()
p.display()'''
#ex4
#Method with parameter
'''class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display('nandu',19)'''
#ex5
'''class person:
    fname="nandu"#attribute or static variable
    def display(person):
        print(person.name)
p=person()
p.display()'''

##
'''class person1:
    fname="nandu"#attribute or static variable
    lname="kona"
    
    def first_name(self):
        print(self.fname)
    def full_name(self):
          print(self.fname+" "+self.lname)
p=person1()
p.first_name()
p.full_name()'''
#ex6
#constructor--> __init__()
#This is a special method which has the ability to execute itself without calling it manually through the process of instantiation

'''class profile:
    def __init__(self):#constructor method
        print("hey")
p=profile()#with out calling it will print by __init__(execution of constructor through this process)
p.__init__()#without calling 1 time after calling one time'''














































#p2
'''def uncommonwords(s1,s2):
    s1=s1.split()
    s2=s2.split()
    l1=[]
    for i in s1:
        if i not in s2:
            l1.append(i)
    for i in s2:
        if i not in s1:
            l1.append(i)
    l1=list(set(l1))
    return l1
s1 = "Hello how are you"
s2 = "Hello how is"
print(uncommonwords(s1,s2))'''
#p3          
'''num=8
n1=0
n2=1
for i in range(8):
    n3=n1+n2
    n1=n2
    n2=n3
print(n3)'''
#p3 m2
'''def fibo(n):
for i in range(n):
    n3=n1+n2
    n1=n2
    n2=n3
n=8
fibo(n)
print(n3)'''

#constructors
#ex2
#unparametarised constructor
'''class profile:
    def __init__(self):
        print("hello")
obj=profile()
obj.__init__()'''

#ex3:
#parametarised constructor
'''class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj=profile(1,"nandu",19)'''

#ex4
#m1
'''class c1:
    name="nandu"
    place="kad"
    def m1(self):
        print(self.name,self.place)
obj=c1()
obj.m1()'''
#m2
'''class c1:
    def m1(self):
         name="nandu"
         place="kad"
         print(name,place)
obj=c1()
obj.m1()'''
#m3
'''class c1:
    email="nandu@gmail.com"
    def m1(self):
         name="nandu"
         place="kad"
         print(name,place)
         print(self.email)
obj=c1()
obj.m1()'''
#ex5
'''class c1:
    def  m1(self):
         name="nandu"
         place="kad"
         return name,place
    def display(self):
        print(self.m1())
obj=c1()
obj.display()'''

#Ex6
'''class c1:
    def __init__ (self):
        name="nandu"
        email="nandu@gmail.com" #error -->  cannot use return with constructor
        return name,email
    def display(self):
        print(self. __init__())
c11=c1()
c11.display()'''
#To use the variable inside the constructor in another methods    
'''class c1:
    email="nandu@gmail.com"##static variable
    def __init__ (self):
        self.name="nandu"##instance variable
        self.email="nandu@gmail.com" 
        
    def display(self):#instance method
        print(self.name,self.email)
c11=c1()
c11.display() '''

#-->inheritance:
'''The process of utilising the methods and attributes of parent class through the object of child class it is called inheritance'''

#5 types of inheritance

'''1)Single inheritance
2)Multilevel inheritance
3)Multiple inheritance
4)Hybrid inheritance
5)Heirarical inheritance'''

##Single Inheritance:
''' It has only one parent class and only one child class'''
#ex1
#m1
'''class parent:
    def m1(self):
        print("I am parent class")

class child(parent):# here parent is subclass
    def m2(self):
        print("I am child class")
c1=child()
c1.m1()'''

#m2
'''class parent(child):
    def m1(self):
        print("I am parent class")

class child:# here parent is subclass
    def m2(self):
        print("I am child class")#error we can't acces child from parent but parent can acces from child
c1=parent()
c1.m2() ''' 
#ex2
'''class c1:
    def __init__ (self):
        print("I am constructor from parent class")
class child1(c1):
    pass
obj=child1()'''#-->I am constructor from parent class
##
'''class c1(child1):
    pass
    
class child1:
    def __init__ (self):
        print("I am constructor from parent class")
obj=c1()'''#ERROR
#ex3
'''class parent:
    name="sindu"
class child(parent):
    def display(self):
        print(self.name)
d=child()
d.display()'''#-->sindu
        
'''class parent:
    name="sindu"
class child(parent):
     name="nandu"
    def display(self):
        print(self.name)
d=child()
d.display()'''#-->nandu

#-->Multilevel inheritance
#ex1
'''class voice:
    def sound(self):
        print("All the animals have their own voice")
class dog(voice):
    def dog_sound(self):
        print("bark")
class cat(dog):
    def cat_sound(self):
        print("meow")
class parrot(cat):
    def parrot_sound(self):
        print("speak")
all=parrot()
all.sound()
all.dog_sound()
all.cat_sound()
all.parrot_sound()'''
#ex2
'''class honda_city:
    def honda_city_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def honda_city_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class amaze(honda_city):
    def amaze_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def amaze_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class civic(amaze):
    def civic_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def civic_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class Honda(civic):
    pass
car=Honda()
car.honda_city_engine_specs(1500,230,2979,"petrol",4)
car.honda_city_body_specs("white",2000,5.5,8,"Hatchback")'''

#Multiple inheritance
''' It has multiple parent and only one child'''
#ex
'''class while_pertol:
    def function_w(self):
        print("used to Airplans")
class organic_pertol:
    def function_o(self):
        print("used for bike,cars")
class premium_petrol:
    def function_p(self):
        print("sports cars,bikes")
class petrol(while_pertol, organic_pertol,premium_petrol):
    def definition(self):
        print("petrol types")
p=petrol()
p.definition()
p.function_p()
p.function_o()
p.function_w()'''
# MRO--> Method Resolution Order
'''class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)#7#10'''



'''class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)'''#7#0
#Heirarical inheritance
'''one parent and multiple child'''
#ex1
'''class category:
    def weight(self,weight):
        print(weight)
    def display(self,color,taste):
        print(color,taste)
class tomato(category):
    def tomtato_specs(self):
        color="red"
        taste="neutral taste"
        self.display(color,taste)
class carrot(category):
    def carrot_specs(self):
        color="orange"
        taste="sweet"
        self.display(color,taste)
c=carrot()
c.carrot_specs()
c.weight("30gms")

t=tomato()
t.tomato_specs()
t.weight("20gms")'''
#Hybrid inheritance
#The combination of above 4 inheritance is called hybrid inheritance
'''class c1:
    def m1(self):
        print("class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("class3")
class c4(c3):
    def m4(self):
        print("class4")
class c5(c4):
    def m5(self):
        print("class5")
class c6(c5,c4,c3):
    def m6(self):
        print("class6")
obj=c6()
obj.m3()'''

#-->polymorphism
#poly-many,morph-->form
'''A function which has the ability to perform more than 1 functionality then it is considered to be as polymorphism
len()
index()
max()
min()
count()
pop() and more...'''

#polymorphism in operators
#+
'''print(4+4)
print('k'+'n')
print([1,2,3]+[5,6])'''
#*
'''print(7*9)
l1={12,3,4,5}
print(*l1)
def f1(*args)
l1=[1,2,3,4]
print(l1*10)'''#10 times will duplicate

#Polymorphism in classes
'''we can achieve polymorphism in 2 ways
1)Method overloading-->it is not possible in python
2)Method overriding'''












        








    



























    






















    

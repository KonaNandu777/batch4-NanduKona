'''def min_max(products):
   
    min_price_product = min(products, key=products.get)
    max_price_product = max(products, key=products.get)
    return min_price_product, max_price_product

def products_start_with_s(products):
    # Find products starting with 's' or 'S'
    s_products = [product for product in products if product.lower().startswith('s')]
    return s_products

d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "hankey": 30}

min_price, max_price = min_max_priced_product(d1)
print("Min priced product:", min_price)
print("Max priced product:", max_price)

s_products = products_start_with_s(d1)
print("Products starting with 's' or 'S':", s_products)'''


'''def isStrong(n: int) ->bool:
    sum = 0;
    temp = n
    while temp:
        rem = temp%10
        x = 1
        facto = 1
        while x <= rem:
            facto *= x
            x += 1
            sum += facto
            temp //= 10
     if sum == n:
        return True
    else:
        return False
num = int(input("Enter a number: "))
ans = isStrong(num)
if ans:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")'''


'''def number_list(lst, n):
    num = len(lst)- n
    rotated = lst[num:] + lst[:num]
    return rotated

l1 = [1, 2, 3, 4, 5, 6]

n = 2
result_1 = number_list(l1, n)
print(result_1)
n = 3
result_2 = number_list(l1, n)
print(result_2)'''
#!Method riding
#polymorphism in classes using inheritance
#ex1
'''class bank:
    def ratio(self):
        print("All banks has repo rate")
class SBI(bank):
    def ratio(self):
        print('SBI rate is 9%')
class IOB(bank):
    def ratio(self):
        print('IOB rate is 7.5%')
i=IOB()
i.ratio()
s=SBI()
s.ratio()
b=bank()
b.ratio()'''
#ex2
'''class USA:
    def language(self):
        print("English")
    def capital(self):
        print("Washington DC")
    def currency(self):
        print("doller")
class INDIA(USA):
    def language(self):
        print("ALL Languages")
    def capital(self):
        print("New delhi")
i=INDIA()
i.language()
i.capital()
i.currency()'''
#ex3
#polymorphism using objects
'''class c1:
    def f1(self):
        print("print class1")
class c2(c1):
    def f1(self):
        print("print class2")
c11=c2()
c11.f1()'''#-->print class2
#ex4
'''class c1:
    def f1(self):
        print("print class1")
class c2(c1):
    def f1(self):
        super().f1()
        print("print class2")
c11=c2()
c11.f1()'''#-->print class1#print class2

'''class c1:
    def f1(self):
        print("print class1")
class c2(c1):
    def f1(self):
        print("print class2")
c11=c2()
c12=c1()

def display(a):
    a.f1()
display(c11)
display(c12)'''#-->print class2#print class1

#changing the functionality of builtin functions
'''a=9
b=6
print(a+b)
print(a.__add__(b))'''#dunder method or magic method


'''class shopping:
    def __init__ (self,l1):
        self.items=l1
    def __len__(self):
        length = len(self.items)
        return length
s= shopping([1,2,3,4])
print(len(s))'''
#-->Method overloading
#Ex:1
'''class suming:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s=suming()
s.add(3,5)#error
s.add(4,8,9)'''
#ex2
'''class summing:
    def add (self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(5,8)
obj.add(2,9,6)'''

#--> Abstaction
#the process of hiding the implimentation details is abstraction
#Rules of Abstraction
'''
1)Abstract class cannot be instantiated
2)from abc import ABC,abstractmethod
3)subclass the normal class with ABC
4)convert the normal method inside the abstract class to abstract method
5)all child classes have to be subclassed with abstract class
6)the abstract method should be present in the child classes  
'''
#ex1
'''from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print('All shapes have sides except circle')
class triangles(shapes):
    def triangle_sides(self):
        print("3 sides")
    def name(self):
        print("I am triangle")
    def sides(self):
        pass
class square(shapes):
    def square(self):
        print("4 sides")
    def sides(self):
        pass
tr=triangles()
tr.triangle_sides()
tr.name()'''
#ex2
#super() -->used to acess the parent class method from child class method
'''from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("I am child 1")
    def m1(self):
        pass
class2=c2()
class2.m2()'''

#ex3
'''from abc import ABC,abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd="Nandu1305"
        return pswd
class login(password):
    def validate(self,name,password):
        if super().pwd()==password:
            print("Welcome",name,' !!')
            print("login Successful")
        else:
            print("please check the password")
    def pwd(self):
        pass
    
login =login()
name=input("enter the name: ")
pwd=input("Enter the password:  ")
login.validate(name,pwd)'''
#-->Encapsulation
#ex1
'''class car:
    __name="BMW"#private variable
c1=car()
print(c1.name)#error
c1.name="Audi"
print(c1.name)#error'''
#private variable
'''class car:
    __name="BMW"
    print(__name)#BMW'''
#Acessing private data outside the class
'''class c1:
    __phone="335646667"
    def display(self):
        print(self.__phone)
c=c1()
c.display()'''
#declare private method
#m1
'''class class1:
    def __m1(self):
        print("I am private method")
       
c=class1()
c.__m1()'''#error
#m2
'''class class1:
    def __m1(self):
        print("I am private method")
    def __init__(self):
        self.__m1()       
c=class1()'''
#ex
'''class class1:
    class class2:
        name="nandu"
        def display(self):
            print(name)
    obj1=class2()
obj=class1()
obj.obj1.display()'''


'''d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "hankey": 30}                    
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)'''






















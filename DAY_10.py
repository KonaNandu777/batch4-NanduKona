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
class summing:
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
obj.add(2,9,6)










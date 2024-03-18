#Assessment
#p1:
'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)'''
#p2-method1:
'''set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
for i in set1:
    if i not in set2:
        print('yes')
    else:
        print('no')
for i in set1:
    if i not in set3:
        print('yes')
    else:
        print('no')
for i in set2:
    if i not in set1:
         print('yes')
    else:
        print('no')
for i in set2:
    if i not in set3:
         print('yes')
    else:
        print('no')
for i in set3:
    if i not in set1:
         print('yes')
    else:
        print('no')
for i in set3:
    if i not in set2:
         print('yes')
    else:
        print('no')'''
# p2-method2
'''set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning','ML'}
c=0
flag=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print("disjoint")
else:
    print("joint")'''
#p3-Method1
'''l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]
l3=[]
i=0
while i<(len(l1)):
    s=l1[i]+l2[i]
    l3.append(s)
    i+=1
print(l3) '''
#p3-method2
'''l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]
l3=[]
for i in range (len(l1)):
    s=l1[i]+l2[i]
    l3.append(s)
print(l3)'''

#-->functions
'''
#function is a block of code which is used to perform a specific functionality
#function can be created using def keyword
# generlly functions has 3 parts
#function declaration
#function defanition
#function call'''
#example1
'''def greet():#function definition
    print("welcome user")
greet()'''#function calling

'''def adding():
    a=8
    b=6
    c=5
    d=a+b+c
    print(d)
adding()
adding()
adding()'''
#different input
'''def adding():
    a=int(input())
    b=int(input())
    c=int(input())
    d=a+b+c
    print(d)
adding()
adding()
adding()'''

#example:1
#function with parameter
'''def greeting(name):#name is parameter
    print("welcome",name)
for i in range(3):
    username=input("enter the name: ")
    greeting(username)#username is argument'''
def profile(name,age,place):
    print(name,age,place)
















        

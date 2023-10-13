a=100
b=2000

m=b-a

img2=1

bd=id(img2)

n1=len(str(a))
n2=len(str(b))
l=n2-n1
print(l)
print(id(bd))
res=int(str(bd)[-l-1:])
print(res)
r=res+m
if((res+m)>a):
    print(r)
else:
    print(r+a-m)



#address random and select by own



'''
from os import system
i='translate this something i wanted is not here'
i=i.split()
print(i)
if('translate' in i):
    a=i.index('translate')
    if(i[a+1]=='this'):
        i.remove('translate')
        i.remove('this')
    else:
        i.remove('translate')
    se='%20'.join(i)
    print(se)
    c='https://translate.google.co.in/?sl=auto&tl=te&text='+se+'%0A&op=translate'
    system(f'start chrome "{c}"')
    






txt='hi how are you 10/5'

res=txt.lower()
ret=res.split()
for i in ret:
    if('/' in i):
        ret.append('/')
        print(ret)
        ret.extend(i.split('/'))
        print(ret)
        ret.remove(i)
        print(ret)
print(ret)
nums=[]
chars=[]
for i in range(len(ret)):
    if(ret[i].isdigit()):
        nums.append(int(ret[i]))
    else:
        chars.append(ret[i])


print(chars,nums)



h,w=3.9,40.9
if(4.3<=h<=5.5):
    if((h*12)-5<=w<=(h*12)+5):
        print(1)
    else:
        print(0)
elif(5.5<h<=6.9):
    if((h*12)-5<=w<=(h*12)+5):
        print(2)
    else:
        print(0)
else:
    print(0)



for i in range(1,3):
    j=1
    while(i%j==2):
        j-=1
        j=j+3
    print(i)
    print(j)


from collections import Counter
a='hariii'
res=Counter(a)
print(res)


if(len(a)%2==0):
    n,p=sorted(list(set(map(str,a[:len(a)//2])))),sorted(list(set(map(str,a[len(a)//2:]))))
c=0
for i in n:
    if(i not in p):
        c+=1
print(len(p)-c)









class calci:
    def __init__(tvs,a,b):
        tvs.a=a
        tvs.b=b
    def add(tvs):
        print(tvs.a+tvs.b)
    def sub(tvs):
        print(tvs.a-tvs.b)
    def div(tvs):
        print(tvs.a/tvs.b)
calculator=calci(10,5)



class rectangle(calci):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
    def div(self):
        print(self.l/self.b)

        
obj=rectangle(2,3)
obj.add()

a=10
b=20

class hari:
    def __init__(shelf,name):
        shelf.name=name

    
    def pri(shelf):
        print(shelf.name)
    def pr1(shelf,name):
        print("hello",name)

obj1=hari("hari")
obj1.pri()
obj2=hari('dimple')
obj2.pr1('world')
'''
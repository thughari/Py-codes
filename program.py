# print("hello world")
# print(int(True))
# a=100
# b=type(a)
# print(b)
# print(type(b))

'''b=101
sum=0
r=0
while(b>0):
    r=b%10
    sum=(sum*10)+r
    b=int(b/10)

print(sum)
'''


'''a=int(input())
for i in range(2,a):
    if(a%i==0):
        print("not prime")
        pass
else:
    print("prime")'''



'''def fib(n):
    a,b=0,1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return a
print(fib(10))'''

'''a=10
print(type(type(type(a))))
lst=input().split()
print(lst)
n=5
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
print(l)'''


'''a=int(input())
c=str(a)
l=len(c)
t=0
for i in range(l):
    t=t+(int(c[i])**l)
if(t==a):
    print("armstrong",t)'''
    
'''b=102
sum=0
r=0
while(b>0):
    r=b%10
    sum=(sum*10)+r
    b=int(b/10)

print(sum)'''




'''

import sys
print(sys.platform)
print(os.environ)

print(os.lstat('johncena.mp3'))
'''


'''
b=13/3
print(type(b))
c=format(b,'.1f')
print(type(c))

a=13
for i in range(2,a-1):
    if(a%i==0):
        print("not prime")

else:
    print('prime')



import random



a='PIck 5 and 20'
res=a.lower()
a=a.split()
nums=[]
chars=[]
for i in range(len(a)):
    if(a[i].isdigit()):
        nums.append(int(a[i]))
    else:
        chars.append(a[i])

print(chars,nums,res)
for i in chars:
    if(i=='pick'):
        print(random.randint(nums[-2],nums[-1]))

'''
# chars=input()
# nums=[1,2,3]

# t=60 if 'a' in chars else nums[-1]*60

# print(t)


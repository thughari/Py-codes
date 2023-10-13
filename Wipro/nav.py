
a=int(input())
b=int(input())
c=list(map(int,input().split()))
s=0
for i in c:
    s+=i//b
print(s)
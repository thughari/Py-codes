#threshold

a=int(input())
b=list(map(int,input().split()))
c=int(input())
s=0
for i in range(a):
    if(c%b[i]==0):
        s+=1
print(s)
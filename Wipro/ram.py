#sum of digits

a=int(input())
b=list(map(int,input().split()))
res=[]
for i in b:
    res.append(sum(list(map(int,str(i)))))
print(*res)
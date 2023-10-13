#dna

a=int(input())
b=list(input().split())
c=int(input())
res=[]
for i in range(0,a,c):
    res.append(''.join(b[i:i+c]))
print(*res)
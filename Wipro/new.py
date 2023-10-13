#*-+

a=int(input())
b=int(input())
m,n=list(map(int,str(a))),list(map(int,str(b)))
r1=str(m[0]+n[0])+str(m[1]+n[1])
r2=str(abs(m[0]-n[0]))+str(abs(m[1]-n[1]))
r3=str(m[0]*n[0])+str(m[1]*n[1])
print(r1,r2,r3)
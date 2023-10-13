#baetriUto--->beitroAtu
vs=['a','e','i','o','u']
vc=['A','E','I','O','U']
a=list(input())
for i in range(len(a)):
    if(a[i] in vs):
        r=(vs.index(a[i])+1)%5
        a[i]=vs[r]
    elif(a[i] in vc):
        r=(vc.index(a[i])+1)%5
        a[i]=vc[r]
print(''.join(a))
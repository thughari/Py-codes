#sum of odd digits
a=input()
s=0
for i in range(len(a)):
    if(int(a[i])%2!=0):
        s+=int(a[i])
print(s)
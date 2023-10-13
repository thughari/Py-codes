#25643,3---->45253
a='25643'
b=3
s=''
for i in range(len(a)):
    if(int(a[i])%2==0):
        r=(len(a[:i])+b)%len(a)
        s+=a[r]
    else:
        s+=a[i]
print(s)

a=int(input())
b=int(input())
s=0
for i in range(a,b):
    if(i**(.5)==int(i**(.5))):
        s+=i
print(s)
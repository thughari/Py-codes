a=int(input())
b=int(input())
s=0
for n in range(a,b):
    if n > 0:
        for i in range(2, n):
            if (n % i==0):
                break
        else:
            s+=n  
    else:
        for i in range (n+1, -2):
            if (n % i==0):
                break
        else:
            s+=n
print(s)
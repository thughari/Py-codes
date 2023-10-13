
a=12
b=15
def lcm(a,b):
    m=max(a,b)
    r=1
    while(True):
        if(m%a==0 and m%b==0):
            return m
        m+=1
def hcf(a,b):
    res=1
    for i in range(1,min(a,b)):
        if(a%i==0 and b%i==0):
            res=i
    return res
print(lcm(a,b))
print(hcf(a,b))
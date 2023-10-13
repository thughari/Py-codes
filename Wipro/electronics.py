#electronics----> letois
a=input()
r=''
for i in range(2,len(a)+2,2):
    r+=max(a[i-2:i])
print(r)
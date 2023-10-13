#6,a v i k e l, 3 hint(conconents)

a=int(input())
b=list(input().split())
vowels=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in b:
    if(i not in vowels):
        c+=1
print(c)
n=int(input())
for i in range(n):
    try:
        num=list(map(int,input().split()))
        a,b=num[-2],num[-1]
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError:
        print('Error Code: invalid literal for int() with base 10:',b)

class sir:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def name(self):
        return(f'{self.a}\n{self.b}')
    def age(self):
        return(self.c)
class student(sir):
    def age(self):
        return self.c
y=sir('hari','L5',21)
t=sir('tvs','L0',21)
print(f'{y.name()}\n{y.age()}')
print(t.name(),t.age())


    
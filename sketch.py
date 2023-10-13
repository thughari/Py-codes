

'''
speed(10)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
'''




'''
pensize(1)
color('yellow')
bgcolor('black')
begin_fill()
speed(1000)
a=200
while(a>0):
	left(a)
	forward(a*3)
	a-=1
end_fill()
'''



from time import sleep
from turtle import *
color('red')
sleep(3)
bgcolor('white')
begin_fill()
pensize(10)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
done()

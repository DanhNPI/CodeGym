# Import thư viện đồ họa turtle
import turtle

kc = int(input('Nhập khoảng cách: '))

t = turtle.Turtle()
t.hideturtle()

d = 0.5
while (True):
    t.forward(d)
    t.left(5)
    dist = turtle.distance(t)
    print (dist)
    if dist > kc:
        break
    d +=0.01
turtle.done()
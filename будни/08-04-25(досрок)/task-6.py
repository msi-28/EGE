from turtle import *

lt(90)
m = 50
tracer(0)
screensize(1000, 1700)

rt(30)

for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        dot(3, 'red')
        goto(x * m, y * m)
done()

# ans -> 30
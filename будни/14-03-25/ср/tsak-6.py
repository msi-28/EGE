from turtle import *

lt(90)
m = 10
screensize(1000, 1000)
tracer(0)

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()

for x in range(-10, 20):
    for y in range(-10, 30):
        dot(3, 'red')
        goto(x * m, y * m)

done()

# ans -> 44
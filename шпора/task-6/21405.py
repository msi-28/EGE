from turtle import *

screensize(1000, 2000)
tracer(0)
lt(90)
m = 40

rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()
r = range(-20, 10)
for x in r:
    for y in r:
        goto(x * m, y * m)
        dot(3, 'red')

done()

# ans -> 30
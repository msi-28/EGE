from turtle import *

screensize(1000, 2000)
tracer(0)
lt(90)
m = 20

for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()

for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
r = range(-10, 50)
for x in r:
    for y in r:
        goto(x * m, y * m)
        dot(3, 'red')
done()

# ans -> 679
from turtle import *

screensize(1000, 1000)
tracer(0)
lt(90)
m = 20

for i in range(9):
    fd(27 * m)
    rt(90)
    fd(30 * m)
    rt(90)

up()
fd(3 * m)
rt(90)
fd(6 * m)
lt(90)
down()

for i in range(9):
    fd(77 * m)
    rt(90)
    fd(66 * m)
    rt(90)

up()
r =range(-10, 30)
for x in r:
    for y in r:
        goto(x * m, y * m)
        dot(3, 'white')
done()
# ans -> 96
from turtle import *

tracer(0)
lt(90)
m = 20
screensize(1000, 1000)

for i in range(10):
    fd(22 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(1 * m)
lt(90)
down()

for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)

up()
r = range(-10,30)
for x in r:
    for y in r:
        goto(x * m, y * m)
        dot(3, 'white')
done()

# ans -> 72
from turtle import *

lt(90)
m = 20
screensize(1000,1000)
tracer(0)

for i in range(7):
    fd(9 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
fd(3 * m)
rt(90)
fd(4 * m)
lt(90)
down()

for i in range(4):
    fd(7 * m)
    rt(90)
    fd(13 * m)
    rt(90)

up()
r = range(-30, 30)
for x in r:
    for y in r:
        dot(3, 'white')
        goto(x * m, y * m)
done()

# ans -> 36
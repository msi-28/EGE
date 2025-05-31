from turtle import *

lt (90)
m = 20
screensize(1000, 1000)
tracer(0)

for i in range(4):
    fd(16 * m)
    lt(90)
    fd(20 * m)
    lt(90)

up()
fd(4 * m)
lt(90)
fd(8 * m)
rt(180)
down()

for i in range(3):
    fd(35 * m)
    lt(90)
    fd(6 * m)
    lt(90)

up()
for x in range(-20, 30):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'white')
done()
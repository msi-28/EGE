from turtle import *

lt(90)
m = 20
screensize(1000, 1000)
tracer(0)

for i in range(9):
    fd(17 *  m)
    lt(90)
    fd(8 *  m)
    lt(90)
    fd(17 *  m)

up()
lt(90)
fd(3 *  m)
rt(90)
fd(5 *  m)
lt(90)
down()

for i in range(4):
    fd(97 *  m)
    rt(90)
    fd(132 *  m)
    rt(90)

up()
for x in range(-30, 70):
    for y in range(-30, 70):
        dot(3, 'white')
        goto(x *  m, y *  m)

done()

# ans -> 508
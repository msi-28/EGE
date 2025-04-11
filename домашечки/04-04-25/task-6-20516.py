from turtle import *

lt(90)
m = 40
tracer(0)

for i in range(3):
    fd(2 * m)
    rt(90)
    fd(3 * m)
    lt(90)

rt(180)
fd(6 * m)
rt(90)
fd(9 * m)
up()
bk(3 * m)
rt(90)
down()

for i in range(2):
    fd(1 * m)
    rt(90)
    fd(2 * m)
    lt(90)

rt(180)
fd(3 * m)
rt(90)
fd(4 * m)
rt(90)
fd(1 * m)

up()
for x in range(-10, 50):
    for y in range(-10, 50):
        dot(3,'white')
        goto(x * m, y * m)

done()

# ans -> 12
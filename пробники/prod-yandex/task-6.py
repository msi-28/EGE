from turtle import *

screensize(2000, 1000)
tracer(1000)
lt(90)
m = 20

for i in range(9):
    fd(7 * m)
    rt(90)
    fd(42 * m)
    rt(90)

up()
bk(10 * m)
lt(90)
bk(16 * m)
down()

for i in range(9):
    fd(42 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
for x in range(-30, 70):
    for y in range(-30, 70):
        dot(3, 'white')
        goto(x * m, y * m)

done()

# ans -> 170
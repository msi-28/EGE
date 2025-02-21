from turtle import *

tracer(0)
lt(90)
screensize(1000,1000)
m = 10
# 18 x 11
for i in range(2):
    fd(17 * m)
    lt(90)
    fd(10 * m)
    lt(90)

up()
bk(4 * m)
rt(90)
bk(3 * m)
lt(90)
down()

# 11 x 41
for i in range(2):
    fd(40 * m)
    rt(90)
    fd(10 * m)
    rt(90)
up()
for x in range(-100, 50):
    for y in range(-100, 50):
        dot(3, 'red')
        goto(x * m, y * m)

done()

# ans -> 577
from turtle import *

tracer(0)
lt(90)
m = 10

for i in range(5):
    fd(30 * m)
    rt(90)
    fd(40 * m)
    rt(90)
up()
fd(20 * m)
rt(90)
fd(15 * m)
rt(90)
down()

for i in range(7):
    fd(10 * m)
    rt(90)

up()
for x in range(0, 100):
    for y in range(0, 100):
        goto(x * m, y * m)
        dot(3, 'red')

done()
# 40 <- ответ
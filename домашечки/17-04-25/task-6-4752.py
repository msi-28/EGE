from turtle import *

screensize(1000, 1000)
tracer(0)
lt(90)
m = 60

for i in range(15):
    fd(4 * m)
    rt(60)

up()
for x in range(1, 20):
    for y in range(1, 20):
        dot(3, 'red')
        goto(x*m, y*m)

done()

# ans -> 28
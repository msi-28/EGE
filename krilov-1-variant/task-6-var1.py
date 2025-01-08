from turtle import *

tracer(0)
lt(90)
m = 7

for i in range(5):
    fd(30 * m)
    rt(90)
    fd(40 * m)
    rt(90)

up()
fd(20 * m)
rt(90)
fd(5 * m)
rt(90)
down()

for i in range(7):
    fd(10 * m)
    rt(90)

up()
for x in range(30, 60):
    for y in range(10, 60):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# (6 + 11)*2 = 34 <- ответ (-)
# примечание: при подсчете периметра лучше в ручную посчитать точки без какой-либо математики, либо от формулы из первого
# решения отнять 4 (повторяющиеся точки)

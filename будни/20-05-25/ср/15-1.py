def plosh(a, b, c):
    return a*b > c

def f(x, y):
    return (not(plosh(x, y, A + 13))) <= plosh(28, y, 520) or plosh(x, 25, 800)

r = range(1, 1000)
r1 = range(-20,0)
for A in r1:
    if all(f(x, y) for x in r for y in r):
        print(A)

# ans -> -13
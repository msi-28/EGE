def f(x, y):
    return (x**2 + y**2 > 1024 - x) or (y < -2*x + A)

r = range(1, 1000)
for A in r:
    if all(f(x, y) for x in r for y in r):
        print(A)
        break

# ans -> 71
def f(x, y, z):
    return ((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= (x % A == 0)

r = range(1, 100)
for A in r:
    if all(f(x, y, z) for x in r for y in r for z in r):
        print(A)

# ans -> 1
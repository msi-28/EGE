def f(x, y):
    return (x*y < A) or (x < y) or (9 < x)

r = range(1, 1000)
for A in range(1, 1000):
    if all(f(x, y) for x in r for y in r):
        print(A)
        break

# ans -> 82
def f(x, y):
    return (x >= 11) or (3*x < y) or (x*y < A)

r = range(1, 1000)
for A in r:
    if all(f(x, y) for x in r for y in r):
        print(A)
        break

# ans -> 301
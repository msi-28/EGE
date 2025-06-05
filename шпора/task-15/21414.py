def f(x, y):
    return (5 < y) or (x > 32) or (x + 2*y < A)
r = range(1000)
for A in r:
    if all(f(x,y) for x in r for y in r):
        print(A)
        break
# ans -> 43
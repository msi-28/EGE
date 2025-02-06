def f(x, y):
    return (x < 7) or ( y >= 3*x + A - 20) or (x >= 34) or (y < 121)

r = range(1, 1000)
ans = 0
for A in r:
    if all(f(x, y) for x in r for y in r):
        ans = A
print(ans)
# ans -> 42
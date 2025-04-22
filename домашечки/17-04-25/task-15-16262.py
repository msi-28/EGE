def f(x, y):
    return ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or (y**2 + 7*y+12 > 0))
r = range(-1000, 1)
cnt = 0
for A in r:
    if all(f(x, y) for x in r for y in r):
        cnt += 1

r1 = range(1, 1000)
for A in r1:
    if all(f(x, y) for x in r1 for y in r1):
        cnt += 1
print(cnt)

# ans -> 5
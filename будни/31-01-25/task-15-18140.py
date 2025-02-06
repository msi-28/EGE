def f(x, y):
    return (x - y >= 39) or (y <= x) or (y >= A - 20)

r = range(1, 1000)
ans = 0
for A in r:
    if all(f(x, y) for x in r for y in r):
        ans = A
print(ans)

# ans -> 22
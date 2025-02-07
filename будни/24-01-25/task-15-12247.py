def f(x):
    return (x & A == 0) or (x & 37 != 0) or (x & 12 != 0)

r = range(1, 1000)
ans = 0
for A in r:
    if all(f(x) for x in r):
        ans = A
print(ans)

# ans -> 45
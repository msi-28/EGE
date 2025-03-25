def f(x, y):
    return ((x + 2) <= 50) or (y < (x + 10)) or (x >= A)
r = range(1, 1000)
ans = []
for A in r:
    if all(f(x, y) for x in r  for y in r):
        ans.append(A)
print(max(ans))
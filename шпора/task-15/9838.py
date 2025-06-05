def f(x, y):
    return (x + 2*y > A) or (y < x) or (x < 30)
r = range(1000)
ans = []
for A in r:
    if all(f(x,y) for x in r for y in r):
        ans.append(A)
print(max(ans))
# ans -> 89
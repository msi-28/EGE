def f(x, y):
    return (x + 2*y > A) or (y < x) or (x < 30)

R = range(1,1000)
ans = 0
for A in R:
    if all(f(x, y) for x in R for y in R ):
        ans = A
print(ans)
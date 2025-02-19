def f(x):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

r = range(1,10000)
ans = []
for A in r:
    if all(f(x) for x in r):
        ans.append(A)
print(max(ans))

# ans -> 52
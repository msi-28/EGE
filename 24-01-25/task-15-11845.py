def f(x):
    return (A % x == 0) <= (x == A) or (x == 1)

r = range(1, 11_111)
cnt = 0
for A in r:
    if all(f(x) for x in r):
        cnt += 1
print(cnt)

# ans -> 1346
def f(x):
    return ((x % 10 == 0) and  (x % 26 == 0) and (x >= 300)) <= (A <= x)
ans = 0
for A in range(-100, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans = A
print(ans)
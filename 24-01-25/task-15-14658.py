def f(x):
    return ((x % 12 == 0) <= (x % 42 != 0)) or (x + A >= 4096)
r = range(1, 10000)
for A in r:
    if all(f(x) for x in r):
        print(A)
        break
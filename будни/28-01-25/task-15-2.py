def f(x):
    return ((x & 500 != 0) and (x & 200 == 0)) <= (x & A != 0)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
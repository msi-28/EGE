def f(x):
    return (x & 79 != 0) and ((x & 31 == 0) <= (x & A != 0))

r = range(1, 1000)
for A in r:
    if all(f(x) for x in range(90, 101)):
        print(A)
        break
# ans -> 32
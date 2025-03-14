def f(x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & A != 0)

r = range(1, 1000)
for A in r:
    if all(f(x) for x in r):
        print(A)
        break

# asn -> 16
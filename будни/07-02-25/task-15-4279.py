def f(x):
    return (x & 1097 == 0) <= ((x & 2047 != 0) <= (x & A != 0))

ox = range(1, 1000)
for A in ox:
    if all(f(x) for x in ox):
        print(A)
        break

# ans -> 950
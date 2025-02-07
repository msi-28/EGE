def f(x):
    return (x&57 == 0) or ((x&23 == 0) <= (not(x&A == 0)))

ox = range(1, 1000)
for A in ox:
    if all(f(x) for x in ox):
        print(A)
        break

# ans -> 40
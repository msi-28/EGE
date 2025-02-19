def f(x):
    return (A + x > 700 - A) and (((A%100) + (100 % x)) > 50)

ox = range(1, 1000)
for A in ox:
    if all(f(x) for x in ox):
        print(A)
        break

# ans -> 351
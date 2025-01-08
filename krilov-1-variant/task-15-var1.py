def f(x):
    return ((x//9) <= (not(x//6))) or (x + A >= 100)

for A in range(1, 10_000):
    if all(f(x) for x in range(1, 10_000)):
        print(A)
        break
def f(x):
    return ((A + x) > (700 - A)) and ((A % 100) + (100 % x) > 50)

for A in range(1, 10_000):
    if all(f(x) for x in range(1, 10_000)):
        print(A)
        break

# ans -> 351
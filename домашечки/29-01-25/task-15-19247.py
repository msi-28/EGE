def f(x, y):
    return (x - 3*y < A) or (y > 400) or (x > 56)

ox = range(1, 1000)
for A in ox:
    if all(f(x, y) for x in ox for y in ox):
        print(A)
        break

# ans -> 54
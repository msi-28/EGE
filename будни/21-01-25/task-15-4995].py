def f(x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# --------------------------

def f(A):
    for x in range(1, 1000):
        f1 = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)
        if not f1:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break

# --------------------------

for A in range(1, 1000):
    for x in range(1, 1000):
        f1 = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)
        if not f1:
            break
    else:
        print(A)
        break

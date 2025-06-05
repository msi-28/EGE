def f(x):
    return ((x%2 == 0) <= (x%3 != 0)) or (x + A >= 80)
r = range(1,1000)
for A in r:
    if all(f(x) for x in r):
        print(A)
        break
# ans -> 74
def f(x):
    B = range(60,81)
    return (x%A == 0) or ((x in B) <= (x%22 != 0))

r = range(1,1000)
for A in r:
    if all(f(x) for x in r):
        print(A)
# ans -> 66
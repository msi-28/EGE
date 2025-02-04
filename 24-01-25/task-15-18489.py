def num(x, y):
    return x%10 == y%10

def f(x):
    return (not(num(x, 5)) and num(x, 4)) <= (x > A - 11)

r = range(1, 1000)
ans = 0
for A in r:
    if all(f(x)for x in r):
        ans = A
print(ans)

# ans -> 14
from fnmatch import fnmatch

def f(x):
    ans = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ans |= {x//i, i}
    ans = [i for i in ans if fnmatch(str(i), '4*')]
    if len(ans) == 24:
        return max(ans)
    return 0


for i in range(1, 10**6):
    fx = f(i)
    if fx:
        print(i, fx)

# ans -> 997920 498960
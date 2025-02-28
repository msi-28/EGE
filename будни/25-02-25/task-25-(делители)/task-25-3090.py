def f(x):
    ans = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            ans |= {i, x//i}
    P = [i for i in ans if p(i)]
    E = [i for i in ans if i%2 == 0]
    return [len(P) == len(E), abs(sum(P)-sum(E))]

def p(x):
    if x == 1: return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

cnt = 0

for i in range(100_000_001, 10**10):
    l, a = f(i)
    if l:
        print(i, a)
        cnt += 1
        if cnt == 5: break

# ans:
# 100000034 50000017
# 100000042 50000021
# 100000094 50000047
# 100000118 50000059
# 100000126 50000063
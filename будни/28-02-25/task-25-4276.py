def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    if len(ans) > 6:
        return [sorted(ans, reverse=True)[6], len(ans)]
    return 0

cnt = 0
for i in range(400_000_001, 500_000_000):
    if f(i):
        print(f(i)[0], f(i)[1])
        cnt += 1
        if cnt == 5:
            break
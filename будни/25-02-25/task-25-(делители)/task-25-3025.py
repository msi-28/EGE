def f(x):
    ans = set()
    for i in range(2, int(x*0.5) + 1):
        if x % i == 0 and i%2 == 0:
            ans |= {i, x//i}
    if len(ans) < 6: return 0
    return sorted(ans)[5]

cnt = 0
for i in range(200_000_000, 10**10):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
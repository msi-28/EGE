def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            ans |= {i, x//i}

    if ans: return max(ans) + min(ans)
    return 0

cnt = 0
for i in range(800_000, 1_000_000):
    if f(i)%10 == 4:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
def f(x):
    ans = set()
    for i in range(2, int(x ** 0.5) + 1):
        if i != 7 and i%10 == 7:
            ans|={i}
        if x//i != 7 and (x//i) % 10 == 7:
            ans |= {x//i}
    if ans:
        return min(ans)
    return 0

cnt = 0
for i in range(700_001, 1_000_000):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:break


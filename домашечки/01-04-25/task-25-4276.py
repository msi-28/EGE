def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}

    ans = sorted(ans, reverse=True)
    if len(ans) >= 7:
        return [str(ans[6]), str(len(ans))]
    return 0

cnt = 0
for i in range(400_000_001, 500_000_000):
    if f(i) != 0:
        print(' '.join(f(i)))
        cnt += 1
        if cnt == 5:
            break

# ans:
# 34 10
# 2962963 14
# 1793722 30
# 21052632 62
# 754717 14
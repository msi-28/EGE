def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}

    ans = [i for i in ans if i % 2 != 0]
    if len(ans) >= 6:
        return sorted(ans, reverse=True)[5]
    else:
        return 0

cnt = 0
for i in range(200_000_001, 300_000_000):
    if f(i) > 0:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break

# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443
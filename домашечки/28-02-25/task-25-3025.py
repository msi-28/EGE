def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    ans = sorted([i for i in ans if i%2 != 0], reverse=True)
    if len(ans) >= 6:
        return ans[5]
    return 0

cnt = 0
for i in range(200_000_001, 300_000_000):
    if f(i) != 0:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break

# ans:
# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443
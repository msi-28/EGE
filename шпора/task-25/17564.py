def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {x//i, i}
    if len(ans) >=2:
        return max(ans) + min(ans)
    return 0

cnt = 0
for i in range(700_000, 800_000):
    if f(i)%10 == 4:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
# ans:
# 700004 350004
# 700009 41194
# 700023 233344
# 700024 350014
# 700044 350024
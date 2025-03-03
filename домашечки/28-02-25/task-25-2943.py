def f(x):
    ans = set()
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: ans |= {i, x//i}
    if ans:
        return max(ans) + min(ans)
    return 0

cnt = 0
for i in range(220_000, 300_000):
    if f(i)%10 == 4:
        print(i, f(i))
        cnt += 1
        if cnt == 5: break

# ans:
# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044
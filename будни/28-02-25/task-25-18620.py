def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    if len(ans) > 1:
        return sorted(ans)[-1] + sorted(ans)[-2]
    return 0

for i in range(112_500_000, 112_550_000+1):
    if f(i)%10000 == 1214:
        print(i)

# ans
# 112508413
# 112520369
# 112523549
# 112534952
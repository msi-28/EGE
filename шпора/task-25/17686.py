def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    ans = [i for i in ans if i%10 == 7 and i!= 7]
    if ans:
        return min(ans)
    return 0

cnt = 0
for i in range(700_000, 1000_000):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break

# ans:
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167
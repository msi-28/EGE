def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {x//i, i}
    ans = [i for i in ans if p(i)]
    if ans:
        return max(ans) + min(ans)
    return 0

def p(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return 0
    return 1

cnt = 0
for i in range(1_200_000, 2_000_000):
    M = f(i)
    if M > 2000 and M%10 == 8:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break

# ans
# 1200005 2248
# 1200011 2388
# 1200037 17978
# 1200067 109108
# 1200197 2598
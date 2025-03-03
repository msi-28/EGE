def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    ans = sorted([i for i in ans if i <= x//2])
    if len(ans) >= 3:
        return ans[-1] + ans[-2] + ans[-3]
    return 0

cnt = 0
ans = []
for i in range(1_200_000, 1, -1):
    if f(i) and f(i)%2022 == 0 and f(i) !=i:
        ans.append([i, f(i)])
        cnt += 1
        if cnt == 5:
            break
for i in sorted(ans):
    print(' '.join(map(str, i)))

# ans:
# 1091880 1182870
# 1116144 1209156
# 1140408 1235442
# 1164672 1261728
# 1188936 1288014
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
for i in range(1_200_000, 1, -1):
    if f(i)%2022 == 0 and f(i) !=i:
        cnt += 1
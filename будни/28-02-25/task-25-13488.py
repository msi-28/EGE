def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    ans = sorted(ans)
    ans = [str(i) for i in ans if i%2 != 0]
    if len(ans) == 3:
        return ans
    return 0

for i in range(18782, 18822+1):
    if f(i):
        print(' '.join(f(i)))
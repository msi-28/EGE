def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return False
    return True

def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {x//i, i}
    ans = [i for i in ans if prime(i)]
    if ans:
        return sum(ans)
    return 0
cnt = 0
for i in range(32_500_000, 40_000_000):
    if f(i) and f(i)%145 == 0:
        print(i, f(i))
        cnt += 1
        if cnt == 7:
            break
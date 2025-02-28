def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {x//i, i}
    ans = [i for i in ans if p(i)]
    if ans:
        return sum(ans)//len(ans)
    return 0

def p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

cnt = 0
for i in range(650_000, 700_000):
    if f(i)%37 == 23:
        print(i, f(i))
        cnt += 1
        if cnt == 4:
            break

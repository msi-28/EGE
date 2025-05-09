def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    return [i for i in list(ans) if i != 7 and i%10 == 7]

cnt = 0
for i in range(700_000, 1_000_000):
    if f(i):
        print(i, min(f(i)))
        cnt += 1
        if cnt == 5:
            break
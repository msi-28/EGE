def f(x):
    ans = set()
    for i in range(1, round(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    return [i for i in list(ans) if i != 8 and i != x and i%10 == 8]

cnt = 0
for i in range(500_000, 1_000_000):
    if f(i):
        print(i, min(f(i)))
        cnt += 1
        if cnt == 5:
            break

# ans:
# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348
def f(x):
    ans = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            ans |= {i, x//i}
    mult = 1
    for i in ans:
        mult *= i
    return [ans, mult]

cnt = 0
for i in range(800_001, 1_000_000):
    if sum(f(i)[0]) % 2 == 1 and f(i)[1] % 2 == 1 and len(f(i)[0]) > 10:
        print(i, len(f(i)[0]))
        cnt += 1
        if cnt == 6:
            break

# ans:
# 804609 27
# 815409 27
# 826281 15
# 837225 27
# 855625 15
# 859329 15
def f(x):
    ans = set()
    for i in range(1, int(x**0.5) + 1):
        if x%i == 0 and x != 1:
            ans |= {i, x//i}
    if ans:
        return ans
    return False

cnt = 0
for i  in range(10**6, 10**7):
    fx = f(i)
    if fx:
        ans2 = [j for j in fx if bin(j)[2:].count('1') == 1 and j != 1]
        if len(ans2) >= 20:
            print(i, sum(fx - {i, 1} - set(ans2)))
            cnt += 1
            if cnt == 5:
                break
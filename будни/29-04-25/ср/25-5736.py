def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}

    if ans and max(ans)%7 == 0:
        return max(ans)
    else:
        return 0


cnt = 0
for i in range(10**9, 10**10):
    palx = str(i) == str(i)[::-1]
    if palx:
        fx = f(i)
        if fx:
            print(i, fx)
            cnt += 1
            if cnt == 5:
                break
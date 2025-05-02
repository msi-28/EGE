def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

for x in range(1, 2006):
    num = 43**56 + 113**841 - x
    num = f(num, 4)
    ch = 0
    nch = 0
    two = num.count('2')
    for i in num:
        if int(i)%2 == 0:
            ch += 1
        else:
            nch += 1
    if ch%2 == 0 and nch%2 == 0 and two <= 712:
        print(x)
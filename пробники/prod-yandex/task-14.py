def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

for x in range(1, 2042)[::-1]:
    num = f(25**61 + 5**178 - x, 5)
    if num.count('0') == 60:
        print(x)

# ans -> 1875
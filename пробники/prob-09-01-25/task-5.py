def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

for N in range(11, 30):
    R = convert(N, 3)
    if R.count('1') + R.count('3') < R.count('2') + R.count('0'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        print(R)


# ans -> 227
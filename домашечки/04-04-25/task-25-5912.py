from itertools import product, repeat


def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            ans |= {i, x//i}
    return ans

for q in range(10):
    for i in range(4):
        for s in product('0123456789', repeat=i):
            s = ''.join(s)
            num = int(f'12{q}{s}45')
            k = f(num)
            if len(k) == 18 and num < 10**7:
                print(num, max(k))

# ans:
# 1202445 400815
# 1234845 411615
# 1251045 417015
# 1259145 419715
# 1283445 427815
# 1299645 433215
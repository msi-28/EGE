from itertools import product
def f(x):
    ans = set()
    for i in range(round(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    return sorted(ans)


cnt = 0
ans = []
for q1 in '12345679':
    for q2 in '012345679':
        for r in range(10):
            for l in range(10):
                for s1 in product('0123456789', repeat=r):
                    for s2 in product('0123456789', repeat=l):
                        s1 = ''.join(s1)
                        s2 = ''.join(s2)
                        num = int(f'{q1}6{s1}6{s2}{q2}6')
                        d = f(num)
                        if 6 in d and 7 in d and 8 in d:
                            cnt += 1
                            ans.append(num, sum(d))
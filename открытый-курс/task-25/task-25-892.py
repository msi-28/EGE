def div(x):
    ans = set()
    for i in range(1, x):
        if x % i == 0:
            ans |= {i, x//i}
    return sorted(ans)

for i in range(154026, 154044):
    if len(div(i)) == 4:
        print(' '.join(map(str,sorted(div(i))[-2:])))
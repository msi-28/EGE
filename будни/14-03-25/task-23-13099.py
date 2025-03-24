def f(s, e, c):
    if s == e and '11' not in c: return 1
    if s > e+1: return 0
    if '11' not in c:
        return f(s - 1, e, c+'1') + f(s * 2, e, c+'0') + f(s * 3, e, c+'0')
    return f(s * 2, e, c + '0') + f(s * 3, e, c + '0')

print(f(3, 15, ''))

# ans -> 6
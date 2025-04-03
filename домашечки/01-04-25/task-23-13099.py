def f(s, e, c = ''):
    if s == e and 'AA' not in c: return 1
    if s > e + 1 or 'AA' in c: return 0
    return f(s - 1, e, c + 'A') + f(s * 2, e, c + 'B') + f(s * 3, e, c + 'B')

print(f(3, 15))

# ans - > 6
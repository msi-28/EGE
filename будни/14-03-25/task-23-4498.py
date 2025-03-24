def f(s, e, c):
    if s == e and c.count('1') <= 4 and c.count('2') >= 2 and c.count('3') == 5: return 1
    if s > e: return 0
    return f(s * 5, e, c+'1') + f(s * 3, e, c+'2') + f(s + 45, e, c+'3')

print(f(1, 2970, ''))

# ans -> 74
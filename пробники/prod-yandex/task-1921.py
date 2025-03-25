def f(x1, x2, s):
    if x1 + x2 >= 181: return s % 2 == 0
    if s == 0: return False
    h = [f(x1 + 4, x2,  s - 1), f(x1 * 3, x2, s - 1), f(x1, x2 + 4, s - 1), f(x1, x2 * 3, s-1)]
    return any(h) if (s-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 156) if f(25, s, 1) == 0 and f(25, s, 2)]) # 51
print('20)', [s for s in range(1, 156) if f(25, s, 1) == 0 and f(25, s, 3)]) # 17 50
print('21)', [s for s in range(1, 156) if f(25, s, 2) == 0 and f(25, s, 4)]) # 46
def f(x1,x2,s):
    if x1 + x2 >= 127: return s%2 == 0
    if s == 0: return False
    h = [f(x1 + 2, x2, s - 1), f(x1 * 3, x2, s - 1), f(x1,x2 + 2, s - 1), f(x1, x2 *3, s - 1)]
    return all(h) if s % 2 == 0 else any(h)

print('19)', [s for s in range(1, 123) if f(2, s, 2)])
print('20)', [s for s in range(1, 123) if f(2, s, 1) == 0 and f(2, s, 3)])
print('21)', [s for s in range(1, 123) if f(2, s, 2) == 0 and f(2, s, 4)])
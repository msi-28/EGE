def f(x1, x2, s):
    if x1 + x2 >= 44: return s%2 == 0
    if s == 0: return False
    h = [f(x1+x2, x2, s - 1), f(x1, x1+x2, s - 1)]
    return any(h) if (s - 1)%2 == 0 else all(h)

print('19)', [s for s in range(1, 33) if f(11, s, 1)])
print('20)', [s for s in range(1, 33) if f(11, s, 2)])
print('21)', [(s1, s2) for s1 in range(1, 44) for s2 in range(1, 44)if f(s1, s2, 3)])
ls = [[abs(s1 - s2), (s1, s2)] for s1 in range(1, 44) for s2 in range(1, 44)if f(s1, s2, 3)]
print(min(ls))

# ans:
# 19) 17
# 20) 8
# 21) 7 7
def f(n, s):
    if n > 33: return s%2 == 0
    if s == 0: return False
    h = [f(n+1, s-1), f(n+2, s-1), f(n+3, s-1), f(n*2, s-1)]
    return
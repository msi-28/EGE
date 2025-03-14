def f(s, e, ans):
    if s == e and ans == 51: return 1
    if s > e: return 0
    return f(s *4, e, ans+1) + f(s + 1, e,  ans+1) + f(s * 3, e,  ans+1)

print(f(2, 404, 0))
# ans -> 319
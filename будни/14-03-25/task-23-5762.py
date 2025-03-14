def f(s, e, c=0):
    if s == e and c == b: return 1
    if s > e: return 0
    if int(s**0.5) == s**0.5:
        c += 1
        s -= 1
    return f(s + 2, e, c) + f(s + 3, e, c) + f(s * 3, e, c)

ans = []
for b in range(1, 10):
    ans.append(f(5, 50))
print(ans)

# ans -> 130771
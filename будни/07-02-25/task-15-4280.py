def f(x):
    return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0))

ox = range(1, 1000)
ans = []
for A in range(43, 56):
    if all(f(x) == 0 for x in ox):
        ans.append(A)
print(max(ans))

# ans -> 50
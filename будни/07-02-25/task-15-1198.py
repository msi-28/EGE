from itertools import combinations as cb

def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = A1 <= x <= A2
    return (B <= A) or ((not C) or A)

line = [x/10 for x in range(100, 550)]
ans = []
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))
# ans -> 23
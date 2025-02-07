from itertools import combinations as cb

def f(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = A1 <= x <= A2
    return Q <= ((P == Q) or ((not P) <= A))

line = [x/10 for x in range(670, 1140)]
ans = []
for A1, A2 in cb(line, 2):
    if all(f(x)for x in line):
        ans.append(A2 - A1)
print(min(ans))

# ans -> 23
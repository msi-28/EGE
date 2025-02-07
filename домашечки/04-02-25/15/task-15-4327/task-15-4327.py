from itertools import combinations as cb

def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = A1 <= x <= A2
    return not(((not P) <= Q) and R and (not A))

ans = []
line = [x for x in range(4, 55)]
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))

# ans -> 47
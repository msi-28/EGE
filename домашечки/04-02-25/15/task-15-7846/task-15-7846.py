from itertools import combinations as cb

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (P or Q) or (A <= (Q or P))

ans = []
line = [x for x in range(10, 30)]
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# ans -> 10
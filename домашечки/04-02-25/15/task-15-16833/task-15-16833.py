from itertools import combinations as cb

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

ans = []
line = [x for x in range(20, 120)]
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# ans -> 48
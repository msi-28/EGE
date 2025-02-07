from itertools import combinations as cb

def f(x):
    P = 117 <= x <= 158
    Q = 129 <= x <= 180
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

line = [x/10 for x in range(1000, 1800)]
ans = []
for A1, A2 in cb(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))

# ans -> 29
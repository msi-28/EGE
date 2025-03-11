from itertools import combinations as cb

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

line = [x for x in range(20, 120)]
ans = []
for A1, A2 in cb(line, r=2):
    if all(f(x) for x in range(1, 1000)):
        ans.append(A2 - A1)
print(max(ans))

# ans -> 48
from itertools import combinations as cb

def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = A1 <= x <= A2
    return not((Q <= (not R)) and A and (not P))

line = [x//10 for x in range(9*10, 50*10)]
ans = []
for A1,A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# ans -> 20

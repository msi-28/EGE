from itertools import permutations

def f1(arr):
    return max(arr) < sum(arr) - max(arr)

def f2(arr):
    return max(arr) + min(arr) == sum(arr) - max(arr) - min(arr)

def f3(arr):
    for s in permutations(arr):
        s = list(s)
        if s[0] + s[1] == s[2] + s[3]: return True
    return False


with open('9_4589.txt') as file:
    ls = [list(map(int, i.split())) for i in file]

cnt = 0
for i in ls:
    if f1(i) and f3(i):
        cnt += 1
print(cnt)

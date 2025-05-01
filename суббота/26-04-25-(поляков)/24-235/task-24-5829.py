from re import *

st = open('24-235.txt').readline()

pattern = r'X.P'
match = finditer(pattern, st)
ans = []

for i in match:
    s = i.group()
    ans.append(s[1])

print(max([[ans.count(i), i] for i in 'XYZWOP']))

# ans -> 4683
from re import *

st = open('24-186.txt').readline()

pattern = r'(?<=[A-Z])7[\d]{10}(?=[A-Z])'
match = finditer(pattern, st)
ans = []

for i in match:
    s = i.group()
    if sum(map(int, s[:2])) == sum(map(int, s[-2:])):
        ans.append(s)

print(ans)
print(len(ans))

# ans -> 89
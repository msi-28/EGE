from re import *

st = open('24-271.txt').readline()

pattern = r'#[0-9A-F]{6}'
match = finditer(pattern, st)
ans = []

for i in match:
    s = i.group()
    if int(s[1:3], 16) > int(s[3:5], 16) and int(s[1:3], 16) > int(s[5:], 16):
        ans.append(s)
print(ans)

# ans -> 3369
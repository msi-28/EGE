from re import *
with open('24_9791.txt') as file:
    st = file.readline()
pattern = r'([A-F]*\d*)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len)))
# ans -> 21
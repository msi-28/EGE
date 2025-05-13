from re import *

with open('24_1975.txt') as file:
    st = file.readline()

pattern = r'(P[QRS]+)+P'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(ans)
print(len(max(ans, key=len)))

# ans -> 188
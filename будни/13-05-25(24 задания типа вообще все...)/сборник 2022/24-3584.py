from re import *

with open('24_3584.txt') as file:
    st = file.readline()

pattern = r'(BA|DA)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())

print(len(max(ans, key=len))//2)

# ans -> 151
from re import *
with open('24_15339.txt') as file:
    st = file.readline()

pattern = r'(?<0)(\d[ABC])+\d?|([ABC]\d)+[ABC]?'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(ans)
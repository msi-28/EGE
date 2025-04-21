from re import *

st = open('24_18597.txt ').readline()

pattern = r'[1-9][0-9]{3}[.][0-9]+[&][1-9][0-9]{3}[.][0-9]+'

m = finditer(pattern, st)
ans = []
for i in m:
    ans.append(i.group())
print(len(max(ans, key=len)))

# ans -> 45
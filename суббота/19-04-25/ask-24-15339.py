from re import *

st = open('24_15339.txt').readline()
pattern = r'([ABC]\d)*|(\d[ABC])*'

m = finditer(pattern, st)
ans = []
for i in m:
    if i.group()!= '':
        ans.append((i.group()))
print((max(ans, key=len)))
# print(ans)
# ans -> 22
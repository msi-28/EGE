from re import *

st = open('24_8579.txt').readline()

pattern = r'\d[A-Z]+\d'

match = finditer(pattern, st)
ans = []

for i in match:
    s = i.group()
    if int(s[0])%2 != int(s[-1])%2:
        ans.append(s)

print(len(max(ans, key=len)))
# ans -> 49
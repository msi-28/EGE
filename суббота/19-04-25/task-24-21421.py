from re import *

st = open('24_21421.txt').readline()

pattern = r'[1-9AB][0-9AB]*[02468A]'

m = finditer(pattern, st)
ans = []
for i in m:
    ans.append(i.group())
print(len(max(ans, key=len)))

# ans -> 19
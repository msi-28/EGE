from re import *

st = open('24_17685.txt').readline()
pattern = r'(([1-9][0-9]*)|0[*|+])+([1-9][0-9]*)|0'

m = finditer(pattern, st)
ans = []
for i in m:
    if eval(i.group()) == 0:
        ans.append(i.group())
print((max(ans, key=len)))
print(len((max(ans, key=len))))
# ans -> 52
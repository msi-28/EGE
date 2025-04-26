from re import *

st = open('24-335.txt').readline()
# st = '(((56+-+00(0678-89)(7182-15)(3222+745))'

A = r'[1-9][0-9]*[^05]'
B = r'[1-9][0-9]*[05]'
pattern = rf'([(]{A}[+-]{B}[)])+'

match = finditer(pattern, st)
ans = []

for i in match:
    ans.append(i.group())

print(len(max(ans,key=len)))
print(ans)

# ans -> 55
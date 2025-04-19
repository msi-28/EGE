from re import *
from itertools import product

st = open('24_16269.txt').readline()
# st = 'YYZZZZYYXX'
pattern = rf'((?<!XX)(XX)(?!XX)*|(?<!YY)(YY)(?!YY)*|(?<!ZZ)(ZZ)(?!ZZ)*)+'

m = finditer(pattern, st)
ans = []
for i in m:
    if i.group()!= '':
        ans.append((i.group()))
# print(eval(max(ans, key=eval)))
print(len(max(ans, key=len)))
print(ans)
# ans -> 50 но должно быть 52
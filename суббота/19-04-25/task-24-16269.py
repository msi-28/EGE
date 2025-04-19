from re import *
from itertools import product

st = ')))' + open('24_16269.txt').readline() + '))))'
# st = ')))' +'YYZZZZYYXX'+ '))))'
pattern = r'((?<!XX)(XX)(?!XX)*|(?<!YY)(YY)(?!YY)*|(?<!ZZ)(ZZ)(?!ZZ)*)+'

m = finditer(pattern, st)
ans = []
for i in m:
    if i.group()!= '':
        ans.append(st[i.start()-3:i.end()+3])
print((max(ans, key=len)))
print(len('YYXXZZXXYYZZXXYYZZXXZZYYXXYYXXYYXXYYZZXXYYXXYYZZYYZZ'))
# ans -> 52
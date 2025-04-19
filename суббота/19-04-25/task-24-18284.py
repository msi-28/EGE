from re import *

st = open('24_18284.txt').readline()
# st = 'REVVVLAAORRVEARRLBOLRVER'

pattern = r'L[^L]*?O.*?V.*?E'

m = finditer(pattern, st)
ans = []
for i in m:
    ans.append(i.group())
print(len(min(ans, key=len)))
# print(ans)

# ans -> 2000031
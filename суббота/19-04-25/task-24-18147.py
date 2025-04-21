from re import *

st = open('24_18147.txt').readline()

pattern = r'([1-9][0-9]*[+])+[1-9][0-9]*'

m = finditer(pattern, st)
ans = []
for i in m:
    ans.append((i.group()))
print(eval(max(ans, key=eval)))
# ans -> 9988877898985
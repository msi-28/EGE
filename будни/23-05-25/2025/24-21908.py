from re import *
with open('24_21908.txt') as file:
    st = file.readline()

pattern = r'([1-9][0-9ABCD]*)+[02468AC]'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len)))
# ans -> 2598
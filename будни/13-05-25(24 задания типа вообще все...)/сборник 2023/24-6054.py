from re import *
with open('24_6054.txt') as file:
    st = file.readline()

pattern = r'([BC]{2}A)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len)))
# ans -> 6
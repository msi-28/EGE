from re import *
with open('24_6757.txt') as file:
    st = file.readline()
pattern = r'(CFE|FCE)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//3)
# ans -> 103
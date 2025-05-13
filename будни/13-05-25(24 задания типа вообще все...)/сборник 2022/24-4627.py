from re import *
with open('24_4627.txt') as file:
    st = file.readline()

pattern = r'(NPO|PNO)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//3)
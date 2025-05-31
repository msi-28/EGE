from re import *
with open('24_6636.txt') as file:
    st = file.readline()

pattern = r'([24][135])+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//2)
# ans -> 10
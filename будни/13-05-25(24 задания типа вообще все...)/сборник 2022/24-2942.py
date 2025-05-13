from re import *
with open('24_2942.txt') as file:
    st = file.readline()

pattern = r'(AB|AC)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//2)

# ans -> 2397
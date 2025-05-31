from re import *
with open('24_4602.txt') as file:
    st = file.readline()

pattern = r'([BCD][AO])+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//2)

# ans -> 174
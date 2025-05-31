from re import *
with open('24_4710.txt') as file:
    st = file.readline()

pattern = r'([CDF][AO])+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append((i.group()))
print(len(max(ans, key=len))//2)

# ans -> 95
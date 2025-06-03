from re import *
with open('24_17563.txt') as file:
    st = file.readline()

pattern = r'([1-9]\d*[-*])+[1-9]\d*'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len)))

# ans -> 40
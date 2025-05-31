from re import *
with open('24_6029.txt') as file:
    st = file.readline()
pattern = r'E?(FE)+F?'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len)))
# ans -> 11
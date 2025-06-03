from re import *
with open('24_6798.txt') as file:
    st = file.readline()

st = 'ACCADAADDADFDCA'
pattern = r'([CDf][A-Z][AO])+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(ans)
print(max(ans, key=len))
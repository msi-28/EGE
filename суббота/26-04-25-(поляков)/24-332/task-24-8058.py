from re import *

with open('24-332.txt') as file:
    st =' '.join(file.readlines())

pattern = r'[A-Z][a-z]*(\s[A-Z]?[a-z]+)*\.'
match = finditer(pattern, st)
ans = []

for i in match:
    ans.append(i.group())

print(max(ans, key=len))
print(len(max(ans, key=len)))

# ans -> 22
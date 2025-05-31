from re import finditer

with open('24_3228.txt') as file:
    st = file.readline()

pattern = r'(AB|AC)+'
match = finditer(pattern, st)
ans = []
for i in match:
    ans.append(i.group())
print(len(max(ans, key=len))//2)

# ans -> 19
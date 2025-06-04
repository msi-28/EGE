from re import *
with open('24_21421.txt') as file:
    st = file.readline()

pattern = r'([AB]+|([1-9]\d*))+'
match = finditer(pattern, st)
ans = []
for i in match:
    if int(i.group(), 12)%2 == 0:
        ans.append(i.group())
print(len(max(ans, key=len)))
# ans -> 19
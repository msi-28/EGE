from re import *

st = open('24-314.txt').readline()

pattern = r'(?<=F)(0|([1-7][0-7]*)[+*])+0|([1-7][0-7]*)'
match = finditer(pattern, st)
ans = []

for i in match:
    ans.append(i.group())

maxx = max(ans, key=len)
print(maxx)
ans = []
num = ''
for i in maxx:
    if i not in '+*':
        num += i
    else:
        ans.append(str(int(num, 8)))
        ans.append(i)
        num = ''
ans.append(str(int(num, 8)))
print(eval(''.join(ans)))

# ans -> 142844
from re import *

text = open('24_1866.txt').readline()
pattern = r'(?<=ad|da)\w+?(?=ad|da)'
matches = finditer(pattern, text)
ans = []
for match in matches:
    ans.append(match.group())

print(len(max(ans, key=len)) + 2)

# ans -> 2252
from re import *

text  = open('24_17563.txt').readline()
pattern = r'(((?!0)[0789]+)[*-]{1})+'
matches = finditer(pattern, text)
ans = []

for match in matches:
    ans.append(match.group())
# print(ans)
print(max(ans, key=len))
print(len(max(ans, key=len)) - 1)

# ans -> 40

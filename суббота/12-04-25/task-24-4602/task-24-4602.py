from re import *
from re import finditer

text = open('24_4602.txt').readline()
pattern = r'([BCD][AO])+'
matches = finditer(pattern, text)
ans = []

for match in matches:
    ans.append(match.group())
print(len(max(ans, key=len))//2)
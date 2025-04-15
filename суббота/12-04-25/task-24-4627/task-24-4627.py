from re import *

text = open('24_4627.txt').readline()
pattern = r'(NPO|PNO)+'
matches = finditer(pattern, text)
ans = []

for match in matches:
    ans.append(match.group())
print(len(max(ans, key=len))//3)

# asn -> 327
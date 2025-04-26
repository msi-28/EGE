from re import *
st = open('24-337.txt').readline()

pat = r'1[0-9A-D]+'

match = finditer(pat, st)
ans = []

for i in match:
    s = i.group()
    for j in range(len(s) - 1):
        if s[j] != '1':
            continue
        for k in range(j + 1, len(s)):
            if int(s[j:k + 1], 14)%7 == 0:
                ans.append(s[j:k + 1])

print(len(max(ans, key = len)))
# ans -> 71
from re import *
st = open('24-222.txt').readline()

pattern = r'(A[B-F]+){3}A'
match = finditer(pattern, st)
ans = []

for i in match:
    s = i.group()
    if len(set(s.split('A'))) == 2:
        ans.append(s)

print(len(max(ans, key=len)))

# ans ->23
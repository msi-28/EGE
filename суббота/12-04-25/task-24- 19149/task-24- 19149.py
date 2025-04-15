from re import *

text = open('24_19149.txt').readline()
pattern = r'[(]([1234]+[+])+([1234]+)[)]'
matches = finditer(pattern, text)
ans = []

for match in matches:
    if eval(match.group().lstrip('(').rstrip('+)'))%2 == 0:
        ans.append(match.group())
print(ans)
print(max(ans, key=len))
print(len(max(ans, key=len)))

# ans -> 78
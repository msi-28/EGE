from re import *
with open('24_17641.txt') as file:
    st = file.readline()

pattern = r'(([1-9]\d*|0)[*+])+([1-9]\d*|0)'
match = finditer(pattern, st)
ans = []
for i in match:
    if eval(i.group()) == 0:
        ans.append(i.group())
    else:
        for l in range(len(i.group()) + 1):
            for r in range(len(i.group()), l, - 1):
                sub_str = i.group()[l:r].strip('+*')
                if len(sub_str) < 2:
                    break
                if sub_str[0] == '0' and sub_str[1] not in '+*':
                    continue
                if eval(sub_str) == 0:
                    ans.append(sub_str)
                    break
print(len(max(ans, key=len)))
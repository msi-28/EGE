from itertools import product, repeat

cnt = 0
ans = []
for s in product(sorted('ЛУНАТИК'), repeat = 6):
    s = ''.join(s)
    s = s.replace('У', '*').replace('А', '*').replace('И', '*')
    cnt += 1
    if s[0] == 'Н' and s.count('*') == 1:
        ans.append(cnt)
        print(s)

print(max(ans))
# ans - > 83635

ans = []
for x in range(1,2030):
    num = 7**170 + 7**100 - x
    cnt = 0
    while num:
        if num%7 == 0:
            cnt += 1
        num //= 7
    ans.append([cnt, x])
print(max(ans))
# ans -> 1715
ans = []
for x in range(1,3000):
    num= 4**210 + 4**110 - x
    cnt = 0
    while num:
        if num%4 == 0:
            cnt += 1
        num //= 4
    ans.append([cnt, x])
print(sorted(ans, reverse=True))
# asn -> 1024
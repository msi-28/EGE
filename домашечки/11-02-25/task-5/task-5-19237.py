def convert(num,q):
    ans = ''
    while num: ans += str(num % q); num //= q
    return ans[::-1]
ans = []
for N in range(1,10000):
    R = convert(N,3)
    if N%3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(int,R)),3)
    R = int(R,3)
    if R > 220 and R%2 == 0:
        ans.append(R)
print(min(ans))
# ans -> 222
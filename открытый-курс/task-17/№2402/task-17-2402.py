def convert_and_last_char(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[0]

with open('17_2402.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
ans = []
for i in range(len(ls) - 2):
    c1 = convert_and_last_char(ls[i], 3) == '2' or convert_and_last_char(ls[i + 1], 3) == '2' \
         or convert_and_last_char(ls[i + 2], 3) == '2'
    if c1:
        cnt += 1
        ans.append(min(ls[i], ls[i + 1], ls[i + 2]))
print(cnt, sum(ans))
with open('17var01.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
ans = -10
for i in range(len(ls) - 1):
    sum = ls[i] + ls[i+1]
    c1 = ls[i] % 27 == min(ls[i], ls[i + 1]) or ls[i + 1] % 27 == min(ls[i], ls[i + 1])
    if c1:
        cnt += 1
        if sum > ans:
            ans = sum
print(cnt, ans)

# 6 99107 <- ответ
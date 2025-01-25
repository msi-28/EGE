with open('26.2_19727.txt') as file:
    line = file.readline().split()
    M = int(line[0])
    N = int(line[1])
    ls = [int(i) for i in file]

ls = sorted(ls)
ans_N = []
ans1 = 0
ans2 =0
cnt = 0
max_m = 0
for i in range(len(ls) - 1):
    if cnt < N and max_m  + ls[i+1] < M:
        cnt += 1
        max_m += ls[i]
    else:
        ans_N.append(cnt)
        cnt = 0
        max_m = 0

for i in ls:
    if max_m + i <= M:
        ans1 += 1

for i in ls[::-1]:
    if sum(ls[:ans1 -1]) + i > M:
        ans2 += 1
print(max(ans_N), ans2)


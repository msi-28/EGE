with open('26_7626.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    time = [list(map(int, i.split())) for i in file]

time = sorted(time)
cels = [0]*K
cnt = 0
last = 0
for start, end in time:
    for k in range(K):
        if cels[k] <= start:
            cels[k] = end + 1
            cnt += 1
            last = k + 1
            break
print(cnt, last)

# ans -> 581 59
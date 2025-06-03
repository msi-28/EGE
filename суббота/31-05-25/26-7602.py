with open('26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    time = [list(map(int, i.split())) for i in file]

time = sorted(time)
cels = [0]*K
cnt = 0

for start, end in time:
    for k in range(K):
        if cels[k] <= start:
            cels[k] = end + 1
            cnt += 1
            break
print(cnt, cels.index(max(cels)) + 1)
# ans -> 586 3
with open('24_11636.txt') as file:
    st = file.readline()

cnt = 0
for j in range(2, 10**7):
    for i in range(0, len(st) - j, j + 1):
        if st[i] == 'A' and st[i + j] == 'A':
            cnt += 1
print(cnt)

# ans -> 214352
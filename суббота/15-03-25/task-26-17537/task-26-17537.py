with open('26_17537.txt') as file:
    N, M, K = list(map(int, file.readline().split()))
    # N - кол-во занятых мест
    # M - кол-во рядов
    # K - кол-во столбцов
    seats = [list(map(int, i.split())) for i in file.readlines()]

seats = sorted(seats, key=lambda x: (x[1], -x[0]))
hall = [M + 1] * (K + 1)
correct = []

for h, v in seats:
    hall[v] = h

print(hall)
for i in range(1, K):
    s1, s2 = hall[i:i+2]
    correct.append([min(s1, s2)-1, i+1])
# min(s1, s2) - место
# i - ряд
correct = sorted(correct, key=lambda x: (-x[0], -x[1]))
print(correct[0])

# ans -> 9991 5643
with open('26var01.txt') as file:
    N, M, K = list(map(int ,file.readline().split()))
    # N - кол-во кораблей
    # M - горизонтальные клетки
    # K - вертикальные клетки
    boats = [list(map(int, i.split())) for i in file.readlines()]

boats = sorted(boats, key=lambda x: (x[1], -x[0]))
pole = [M + 1] * (K + 1)
correct = []

for h, v in boats:
    pole[v] = h

for i in range(1, len(pole) - 1):
    p1, p2 = pole[i:i+2]
    correct.append([min(p1, p2) - 1, i])

print(max(correct, key=lambda x: x[0]))

# ans -> 1952 2364
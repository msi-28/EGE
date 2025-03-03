with open('26_9171.txt') as file:
    M, K, N = [int(i) for i in file.readline().split()]
    passengers = [list(map(int, i.split())) for i in file.readlines()]

passengers = sorted(passengers, key=lambda x: (x[0], -x[1]))

stations = [0] * M
accepted = 0
free = [0] * K

for station in range(1, M + 1):
    for start, stop in passengers:
        if 0 in free:
            if station == start and stop not in free:
                stations[station] += 1
                free[free.index(0)] = stop
                accepted += 1
            if stop == station and stop in free:
                stations[station] -= 1
                free[free.index(stop)] = 0


print(accepted)
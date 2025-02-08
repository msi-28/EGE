with open('26_8512.txt')as f:
    K = int(f.readline()) # кол-во ячеек
    N = int(f.readline()) # кол-во пассажиров
    data = [list(map(int, i[:-1].split())) for i in f.readlines()]
# --------------------------------------

data = sorted(data)
cells = [0] * K
last_cell = 0
cnt = 0

for start, end in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = end
            last_cell = i+1
            cnt += 1
            break

print(cnt, last_cell)

# ans -> 389 133
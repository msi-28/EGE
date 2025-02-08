from turtledemo.penrose import start

with open('26_8168.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i[:-1].split())) for i in file.readlines()]

data = sorted(data)
# _______________________________________

cells = [0]*K
cnt = 0
time = 0
time_line = [0]*1500

for start,duration in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = start + duration
            cnt +=1

            for j in range(start+1, start + duration):
                time_line[j] += 1
            break

print(N - cnt, time_line.count(K))

# ans -> 523 534

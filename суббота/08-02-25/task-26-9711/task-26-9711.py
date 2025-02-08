with open('26_9711.txt') as file:
    line = file.readline().split()
    M = int(line[0])
    N = int(line[1])
    scooters=[]
    max_time = 0
    for i in file:
        a,b,c,d = map(int, i.split())
        scooters.append([a, a+b+1, c,d])
        if max_time < a+b+1:
            max_time = a+b+1
# ______________________________________

scooters = sorted(scooters)

start_scooters = [0]*(M+1)
used_scooters = []

for i in range(M + 1):
    used_scooters.append([])
# _______________________________________
# SOLUTION 1

time_line = [0] * max_time

for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    for i in range(start_time, end_time):
        time_line[i] += 1
# _______________________________________
# SOLUTION 2

for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    start_parking = scooter[2]
    end_parking = scooter[3]

    if (len(used_scooters[scooter[2]]) != 0
            and min(used_scooters[start_parking]) <= start_time):
        used_scooters[start_parking].remove(min(used_scooters[start_parking]))
    else:
        start_scooters[start_parking] += 1

    used_scooters[scooter[3]].append(scooter[1])
# _______________________________________
# ANS QUESTION 1 -> 400

print(time_line.index(max(time_line)))

# ANS QUESTION 2 -> 13

print(start_scooters.index(max(start_scooters)))


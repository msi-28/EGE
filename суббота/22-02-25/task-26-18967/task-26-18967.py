with open('26_18967.txt') as file:
    N,K = map(int, file.readline().split())
    guests = [list(map(int, i.split())) for i in file]

guests = sorted(guests, key=lambda x: (x[1], x[0]))
r = max(guests, key=lambda x: x[1])[1] + 1
angryID = []
accepted = []
timeline = [0] * r
angry_cnt = 0
free_places = N
# =============== QUESTION 1/2 ========================
for ID, time, persons in guests:
    if ID not in angryID and ID not in accepted:
        if free_places >= persons:
            free_places -= persons
            accepted.append(ID)
            for i in range(time, r):
                timeline[i] += persons
        else:
            angryID.append(ID)
            angry_cnt += persons
    elif ID in accepted:
        free_places += persons
        for i in range(time, r):
            timeline[i] -= persons
print(angry_cnt, timeline.count(N))

# ans -> 5190 294
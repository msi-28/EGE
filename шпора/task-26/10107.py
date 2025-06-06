with open('26_10107.txt') as file:
    N = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: x[1])

approved = [events[0]]
for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)

print(len(approved), approved[-1][0] - approved[-2][1])
# ans -> 32 15
with open('26.20_19726.txt') as file:
    N = int(file.readline())
    meetings = []
    for i in file:
        start,end = map(int, i.split())
        meetings.append([start, end, end - start])

meetings = sorted(meetings, key= lambda x: (x[1], x[2]))

approved = [meetings[0]]
for meet in meetings:
    if approved[-1][1] <= meet[0]:
        approved.append(meet)
print(len(approved), approved[-1][1])
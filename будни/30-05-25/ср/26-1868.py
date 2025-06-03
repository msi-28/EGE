with open('26_1868.txt') as file:
    N = int(file.readline())
    seats = [list(map(int, i.split())) for i in file]

seats = sorted(seats, key=lambda x: (-x[0], x[1]))
ans = []
for s1, s2 in zip(seats, seats[1:]):
    r1, c1 = s1
    r2, c2 = s2
    if r1 == r2:
        if c2 - c1 - 1 == 2:
            print(r1, c1 + 1)
            break

# ans -> 8631 7311
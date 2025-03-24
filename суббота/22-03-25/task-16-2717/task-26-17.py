from itertools import groupby

with open('26_2717.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file.readlines()]

cnt = 0
places = sorted(places)

for row, place in groupby(places, lambda x: x[0]):
    place = list(place)
    if len(place) >= 5:
        for i in range(len(place) - 4):
            places_5 = place[i:i+5]
            if places_5[-1][1] - places_5[0][1] <= 12:
                for j in range(4):
                    if places_5[j + 1][1] - places_5[j][1] > 3:
                        break
                else:
                    print(places_5)

# ans -> 1234 38468
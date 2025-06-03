with open('26_6031.txt') as file:
    N = int(file.readline())
    rings = [int(i) for i in file]

rings = sorted(rings, reverse=True)
ans = [rings[0]]
for i in rings:
    if ans[-1] - i >= 6:
        ans.append(i)
print(len(ans), min(ans))
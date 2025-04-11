with open('26.txt') as file:
    N = int(file.readline())
    ls = [int(i) for i in file]

ls = sorted(ls, reverse=True)
ans = [ls[0]]
for i in range(len(ls)):
    if ans[-1] - ls[i] >= 9:
        ans.append(ls[i])

print(len(ans), min(ans))
# ans -> 1040 57
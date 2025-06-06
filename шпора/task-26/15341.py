with open('26_15341.txt') as file:
    N = file.readline()
    ls = [int(i) for i in file]

ls = sorted(ls, reverse=True)
ans = [ls[0]]
for i in ls:
    if ans[-1] - i >= 8:
        ans.append(i)

print(len(ans), min(ans))
# ans -> 1198 54
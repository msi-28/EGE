with open('26_17786.txt') as file:
    line = file.readline().split()
    N = int(line[0])
    V = int(line[1]) * 1000
    ls = [int(i) for i in file if 7000 <= int(i) <= 12000]
print(N, V)

ls = sorted(ls, reverse=True)
mass = 0
ans1 = 0
ans2 = 0
for i in ls:
    if i + mass <= V:
        mass += i
        ans1 += 1
        ans2 = i
print(ans1, ans2)

# ans -> 75 9196
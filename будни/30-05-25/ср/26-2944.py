with open('26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)
print(data)
users = []
for file in data:
    if file <= S:
        S -= file
        users.append(file)
    else:
        break
S += users.pop()
data = sorted(data, reverse=True)
for file in data:
    if file <= S:
        users.append(file)
        break
print(len(users), max(users))

# ans -> 263 86
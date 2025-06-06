with open('26_17537 (1).txt') as file:
    N,M,K = map(int, file.readline().split())
    suitable = [M]  * (K + 1)
    for i in file:
        row, col = (map(int, i.split()))
        suitable[col] = min(suitable[col], row - 1)

ans = []
for i in range(2, K + 1):
    seat1, seat2 = suitable[i - 1], suitable[i]
    ans.append([min(seat1, seat2), i])

print(max(ans)[0], max(ans)[1])
# ans -> 9991 5643
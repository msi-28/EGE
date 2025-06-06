with open('17_17558.txt') as file:
    ls = [int(i) for i in file]
m = len([i for i in ls if abs(i)%32 == 0])
ans = []
for i in range(len(ls)-1):
    arr = ls[i:i+2]
    c1 = len([j for j in ls if j < 0]) >= 1
    c2 = sum(arr) < m
    if c1 and c2:
        ans.append(sum(arr))
print(len(ans), max(ans))
# ans -> 4969 299
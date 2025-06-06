with open('17_17680.txt') as file:
    ls = [int(i) for i in file]

m = min([i for i in ls if i > 0 and i%41 == 0])
ans = []
for i in range(len(ls) - 1):
    arr = ls[i:i+2]
    c1 = len(set(arr)) == len(arr)
    c2 = abs(arr[0] - arr[1])%m == 0
    if c1 and c2:
        ans.append(sum(arr))
print(len(ans), max(ans))

# ans -> 10 92404
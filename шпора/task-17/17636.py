with open('17_17636.txt') as file:
    ls = [int(i) for i in file]

m = max([j for j in ls if abs(j)%10 == 3 and len(str(abs(j))) == 3])
ans = []
for i in range(len(ls) - 2):
    arr = ls[i:i+3]
    c1 = len([j for j in arr if abs(j)%10 == 3 and len(str(abs(j))) == 3]) >= 1
    c2 = sum(arr) < m
    if c1 and c2:
        ans.append(sum(arr))
print(len(ans), max(ans))
# ans -> 147 944
ls = [int(i) for i in open('17_6791.txt')]

m = min(i for i in ls if abs(i)%100 == 68)**2
ans = []
for i in range(len(ls) - 1):
    arr = ls[i:i+2]
    c1 = len([j for j in arr if abs(j)%100 == 68]) == 1
    c2 = sum(j**2 for j in arr) >= m
    if c1 and c2:
        ans.append(sum(arr))

print(len(ans), max(ans))
# ans -> 26 19409
with open('17_17873.txt') as file:
    ls = [int(i) for i in file]
m = min(ls)
ans = []
for i in range(len(ls) - 1):
    arr = ls[i:i+2]
    c1 = len([i for i in arr if i%16 == m]) >= 1
    if c1:
       ans.append(sum(arr))
print(len(ans), max(ans))
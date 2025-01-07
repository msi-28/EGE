with open('17_2002.txt') as file:
    ls = [int(i) for i in file]
cnt = 0
min_sum = 100_000_000
for i in range(len(ls) - 3):
    arr = [ls[i], ls[i + 1], ls[i + 2], ls[i + 3]]
    c1 = sorted(arr, reverse=True) == arr
    c2 = max(arr) - min(arr) > 1000
    if c1 and c2:
        cnt += 1
        if sum(arr) < min_sum:
            min_sum = sum(arr)
print(cnt, min_sum)
with open('17_11949.txt') as file:
    ls = [int(i) for i in file]

def duo(arr):
    cnt = 0
    for i in arr:
        if len(str(i)) == 2:
            cnt += 1
    return cnt

def max_68(arr):
    ls_m = []
    for i in arr:
        if abs(i) % 100 == 68:
            ls_m.append(i)
    return max(ls_m)
cnt = 0
max_sum = -100_000_000_000
max_el = max_68(ls)
for i in range(len(ls)-3):
    arr = [ls[i], ls[i + 1], ls[i + 2], ls[i + 3]]
    c1 = duo(arr) == 1 or duo(arr) == 4
    c2 = sum(arr) >= max_el
    if c1 and c2:
        cnt += 1
        if sum(arr) > max_sum:
            max_sum = sum(arr)

print(cnt, max_sum)

# ans -> 34 247177
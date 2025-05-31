with open('17_6089.txt') as file:
    ls = [int(i) for i in file]
ans = []
m = max([i for i in ls if str(i)[-1] == '2'])
for i in ls:
    c1 = abs(i) % 3 == 0
    c2 = abs(i) % 7 != 0 and abs(i) % 17 != 0
    c3 = m % abs(i) == 0
    if c1 and c2 and c3:
        ans.append(i)
print(max(ans), len(ans))
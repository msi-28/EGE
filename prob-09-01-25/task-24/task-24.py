from pstats import count_calls

with open('24_11636.txt') as file:
    st = file.readline()

# cnt = 0
# for j in range(2, 10**7):
#     for i in range(0, len(st) - j, j + 1):
#         if st[i] == 'A' and st[i + j] == 'A':
#             cnt += 1
# print(cnt)

# ans -> 214352

# правильное решение

posA = [i for i in range(len(st)) if st[i] == "A"]
ans = 0
cntA = len(posA) - 1 # kol-vo bukv A

for i in range(len(posA) - 1):
    if posA[i + 1] - posA[i] > 1:
        ans += cntA
    else:
        ans += cntA - 1
    cntA -= 1

print(ans)

# ans -> 42587173055
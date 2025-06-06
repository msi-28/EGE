with open('26_16390.txt') as file:
    M,N = map(int, file.readline().split())
    boxes = [int(i) for i in file]
S = M
boxes = sorted(boxes)
ans = []
for i in boxes:
    if i <= S:
        ans.append(i)
        S -= i
    else:
        break
S += ans.pop()
boxes = sorted(boxes, reverse=True)
for i in boxes:
    if i <= S:
        ans.append(i)
        break

print(len(ans), max(ans))
# ans -> 2216 56
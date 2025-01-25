with open('26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = sorted([int(i) for i in file])

ans1 = 0
mass = 0
lbox = 0
for box in boxes:
    if mass + box <= S:
        mass += box
        ans1 += 1
        lbox = box

mass -= lbox
for box in boxes[::-1]:
    if mass + box <= S:
        lbox = box
        break
print(ans1, lbox)
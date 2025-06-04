with open('26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
inter = [boxes[0]]

for box in boxes:
    if inter[-1] - box >= 3:
        inter.append(box)
print(len(inter), min(inter))

# ans -> 2767 51
with open('26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
ans = [boxes[0]]
for i in boxes:
    if ans[-1] - i >= 3:
        ans.append(i)
print(len(ans), min(ans))

# ans -> 2767 51
with open('26_4684.txt') as file:
    N = int(file.readline())
    items = [int(i) for i in file]

items = sorted(items)
one = sum(items) - sum(items[:N//6])//2

items = sorted(items, reverse=True)
amount = sum(items) - sum(items[5::6])//2

print(amount, one)

# ans -> 46201709 49699604
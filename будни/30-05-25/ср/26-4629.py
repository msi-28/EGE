with open('26_4629.txt') as file:
    N = int(file.readline())
    items = [int(i) for i in file]

items = sorted(items)
shop = sum(items) - sum(items[:N // 4]) // 2

items = sorted(items, reverse=True)
cust = sum(items) - sum(items[:N//4]) // 2
print(cust, shop)

# 39434611 48825239
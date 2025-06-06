with open('26_17687 (1).txt') as file:
    N = int(file.readline())
    price = [int(i) for i in file]

price = sorted(price, reverse=True)
shop = sum(price) - sum(price[:N//9])

cust = sum(price) - sum(price[8::9])

print(shop, cust)
# ans -> 39450073 44329073
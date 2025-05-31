with open('26_6759.txt') as file:
    N = int(file.readline())
    prod = [int(i) for i in file]

prod = sorted(prod, reverse=True)
shop = sum(prod) - sum(prod[:N//3])

cust = sum(prod) - sum(prod[2::3])

print(shop, cust)
with open('26_4660.txt') as file:
    N = int(file.readline())
    items = [int(i) for i in file]

# одним чеком
items = sorted(items)
one = sum(items) - sum(items[:N//4])//2

items = sorted(items, reverse=True)
amount = sum(items) - sum(items[3::4])//2


print(amount, one)
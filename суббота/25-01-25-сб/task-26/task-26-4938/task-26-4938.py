with open('26_4938.txt') as file:
    L, N = map(int, file.readline().split())
    meetings = [map(int, i.split()) for i in file]

print(meetings)
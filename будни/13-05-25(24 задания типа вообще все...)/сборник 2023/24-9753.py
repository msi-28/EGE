with open('24_9753.txt') as file:
    st = file.readline()
m = 0
for r in range(len(st)):
    for l in range(r, len(st)):
        if l-r > m:
            s = st[r:l+1]
            if s.count('Y') <= 150:
                m = len(s)
                print(m)
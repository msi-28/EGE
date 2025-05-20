from itertools import *
with open('24_8510.txt') as file:
    st = file.readline()

for p in product('PNO', repeat = 2):
    p = ''.join(p)
    while p in st:
        st = st.replace(p, p[0] + ' ' + p[1])
st = st.split()
print(len(max(st, key=len)))

# ans -> 57
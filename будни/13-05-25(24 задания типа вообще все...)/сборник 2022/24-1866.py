from re import *
with open('24_1866.txt') as file:
    st = file.readline()

st = st.replace('ad', 'a d').replace('da', 'd a')
st = st.split()
print(len(max(st, key=len)))

# ans -> 2252
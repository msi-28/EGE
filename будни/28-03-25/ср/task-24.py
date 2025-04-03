with open('24_4643.txt') as file:
    st = file.readline()

st = st.replace('2', '1').replace('B', 'A')
st = st.replace('11A', '*')

st = st.replace('A', ' ').replace('1', ' ')
st = st.split()
print(len(max(st, key=len)))

# ans -> 67
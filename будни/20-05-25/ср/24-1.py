with open('24_4544.txt') as file:
    st = file.readline()

st = st.replace('XIX', 'XI IX')
st = st.split()
print(len(max(st, key=len)))

# ans -> 293
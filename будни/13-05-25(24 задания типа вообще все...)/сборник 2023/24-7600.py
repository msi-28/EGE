with open('24_7600.txt') as file:
    st = file.readline()

st = st.replace('Q', 'S').replace('R', 'S')
while 'SS' in st:
    st = st.replace('SS', 'S S')
st = st.split()
print(len(max(st, key=len)))

# ans -> 544
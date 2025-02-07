with open('24var01.txt') as file:
    st = file.readline()

st = st.replace('-', '+')

while '++' in st:
    st = st.replace('++', '+ +')
st = st.replace('+0', 'x')
while 'x0' in st:
    st = st.replace('x0', 'x')
st = st.replace('x', ' ')
st = st.replace(' +', ' ').replace('+ ', ' ')
st = st.split()

print(len(max(st, key=len)))
# ответ: 123
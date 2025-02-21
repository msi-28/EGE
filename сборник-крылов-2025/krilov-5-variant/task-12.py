for n in range(3, 10_001):
    st = '1' + '2'*n
    while '12' in st or '3322' in st or '2222' in st:
        st = st.replace('12', '33', 1)
        st = st.replace('2222', '1', 1)
        st = st.replace('3322', '21', 1)
    if sum(map(int,st)) == 218:
        print(n)
        break

# ans -> 177
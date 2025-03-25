for n in range(4, 57):
    st = '0' + '2'*n

    while '002' in st or '22' in st:
        if '002' in st: st = st.replace('002', '44', 1)
        else: st = st.replace('22', '0', 1)

        if '222' in st: st = st.replace('222', '2', 1)
    if sum(map(int, st)) == 42:
        print(n)

# хз че тут, что-то странное

# бож я дура
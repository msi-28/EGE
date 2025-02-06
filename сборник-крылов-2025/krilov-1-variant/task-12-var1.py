st = '1' * 2024
while '11111' in st or '222' in st:
    if '11111' in st:
        st = st.replace('11111', '22', 1)
    else:
        st = st.replace('222', '2', 1)

print(st)
# 221111 <- Ответ
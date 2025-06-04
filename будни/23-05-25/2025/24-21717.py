with open('24_21717.txt') as file:
    st = file.readline()
ans = []
st = st.split('RSQ')
for i in range(len(st) - 129):
    sub_str = 'RSQ' + 'RSQ'.join(st[i:i+129]) + 'RSQ'
    cnt = 0
    if st[i+129] == '':
        cnt += 1
    else:
        for j in st[i+129]:
            cnt += 1
            if j != 'Q':
                break

        ans.append(len(sub_str) + cnt)
print(min(ans))

# ans -> 497
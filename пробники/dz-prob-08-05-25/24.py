from string import ascii_uppercase as alf

with open('24_14502.txt') as file:
    st = file.readline()

hash_tab = {}
m = 1_000_000
for r in range(1, len(st) - 1):
    for l in range(r, len(st)):
        if 26 <= l - r < m:
            t_st = st[r:l + 1]
            for i in t_st:
                if i not in hash_tab:
                    hash_tab[i] = 1
            if len(hash_tab.values()) == 26:
                hash_tab.clear()
                m = len(t_st)
                print(m)

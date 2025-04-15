from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('0') < ip[16:].count('0'):
            break
    else:
        print(int((mask - 16)*'1' + '0'*(8 - mask + 16) , 2))
        break

# ans -> 252
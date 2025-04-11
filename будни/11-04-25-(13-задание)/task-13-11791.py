from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'246.51.128.202/{mask}', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            break
    else:
        print(int((mask-16)*'1' + '0'*(8 - mask+16), 2))

# ans -> 254
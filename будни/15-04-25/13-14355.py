from ipaddress import ip_network

for A in range(16, 25):
    net = ip_network(f'127.63.67.1/{A}', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            break
    else:
        print(net.netmask)

# ans -> 240
from ipaddress import *

for mask in range(16, 25):
    net = ip_network(f'238.51.1.202/{mask}', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            break
    else:
        print(net.netmask)
from ipaddress import ip_network, ip_address

for A in range(256):
    net = ip_network(f'217.109.{A}.94/255.255.254.0', 0)
    if ip_address(f'217.109.{A}.94') not in [net.broadcast_address, net.network_address]:
        for ip in net:
            ip = f'{int(ip):032b}'
            if ip[:16].count('0') > ip[16:].count('0'):
                break
        else:
            print(A)

# ans -> 129
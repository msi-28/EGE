from ipaddress import ip_network, ip_address

for A in range(32,1,-1):
    net = ip_network(f'143.131.211.37/{A}', 0)
    cnt = 0
    if ip_address('143.131.211.37') not in [net.broadcast_address, net.network_address]:
        for ip in net:
            ip = f'{int(ip):032b}'
            if ip.count('1') == 10:
                cnt += 1
        if cnt == 15:
            print(A)

# ans -> 17
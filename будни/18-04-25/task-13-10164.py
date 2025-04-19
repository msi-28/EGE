from ipaddress import ip_network, ip_address

net = ip_network('156.132.15.138/255.255.252.0', 0)
cnt = 0
for ip in net:
    if ip not in [net.broadcast_address, net.network_address]:
        cnt += 1
        if ip == ip_address('156.132.15.138'):
            print(cnt)
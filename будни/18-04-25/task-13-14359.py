from ipaddress import ip_network, ip_address

ip1 = ip_address('157.127.172.56')
ip2 = ip_address('157.127.191.78')

for A in range(33):
    net1 = ip_network(f'157.127.172.56/{A}', 0)
    net2 = ip_network(f'157.127.191.78/{A}', 0)
    if net1 != net2 and ip1 != net1.broadcast_address and ip2 != net2.broadcast_address:
        print(A)

# ans -> 20
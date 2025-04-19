from ipaddress import ip_network, ip_address

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

for A in range(32, 1, -1):
    net1 = ip_network(f'{ip1}/{A}', 0)
    net2 = ip_network(f'{ip2}/{A}', 0)
    if net1 == net2 and ip1 != net1.broadcast_address and ip2 != net2.broadcast_address:
        print(len(list(net1)))

# ans -> 64
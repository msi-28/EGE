from ipaddress import ip_network, ip_address

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')

for mask in range(32, 1, -1):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if (net1 == net2
        and ip1 not in [net1.broadcast_address, net1.network_address]
        and ip2 not in [net2.broadcast_address, net2.network_address]):
        print(mask)
        break
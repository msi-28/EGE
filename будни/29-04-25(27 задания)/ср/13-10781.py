from ipaddress import *

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')

for mask in range(32, 0, -1):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)

    if net1 == net2 and ip1 not in [net1.broadcast_address, net1.network_address] and ip2 not in [net2.broadcast_address, net2.network_address]:
        print(len(list(net1)))

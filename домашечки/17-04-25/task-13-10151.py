from ipaddress import *
ip = ip_address('111.81.192.0')
for mask in range(16, 25):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    if ip in net and ip not in [net.network_address, net.broadcast_address]:
        print(net.netmask)
from ipaddress import *

net = ip_network('143.168.72.213/255.255.255.240', 0)
print(''.join(str(max(net.hosts())).split('.')))
# ans -> 14316872222
from ipaddress import ip_network

for A in range(256)[::-1]:
    net = ip_network(f'223.167.{A}.167/26', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            break
    else:
        print(A)
        break

# ans -> 248

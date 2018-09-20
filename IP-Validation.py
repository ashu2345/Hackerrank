import re
ipv4 = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][1-9]|[1-9])[.]){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
ipv6 = r'^([0-9a-f]{1,4}[:]){7}[0-9a-f]{4}$'
for _ in range(int(input())):
    test = input().strip()
    if bool(re.match(ipv4,test)):
        print('IPv4')
    elif bool(re.match(ipv6,test)):
        print('IPv6')
    else:
        print('Neither')

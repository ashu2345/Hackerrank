from itertools import combinations_with_replacement as cwr
S,k = input().split()
k = int(k)
reqlist = []
comb = list(cwr(S,k))
for elem in comb:
    elem = list(elem)
    elem.sort()
    reqlist.append(elem)
reqlist.sort()
for elem in reqlist:
    print(''.join(elem))

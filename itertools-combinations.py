from itertools import combinations

S,k = input().split()
k = int(k)
for i in range(1,k+1):
    i_comb = list(combinations(S,i))
    lexlist = []
    for elem in i_comb:
        elem = list(elem)
        elem.sort()
        lexlist.append(elem)
    lexlist.sort()
    for elem in lexlist:
        print(''.join(elem))

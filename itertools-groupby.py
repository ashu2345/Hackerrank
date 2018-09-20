from itertools import groupby
string = input()
reqlist = []
for k,g in groupby(string):
    reqlist.append(str((len(list(g)),int(k))))
print(' '.join(reqlist).strip())

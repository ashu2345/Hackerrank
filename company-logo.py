def secondElem(a):
    return a[1]
def alphasort(a):
    a.sort(key=secondElem,reverse=True)
    for i in range(len(a)-1):
        if a[i][1] == a[i+1][1] and a[i][0] > a[i+1][0]:
            a[i],a[i+1] = a[i+1],a[i]
    return a
from collections import Counter
name = list(Counter(input()).items())
name = alphasort(name)
for i in range(3):
    print(name[i][0],name[i][1])

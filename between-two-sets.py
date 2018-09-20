def getTotalX(a, b):
    a.sort()
    b.sort()
    count=0
    acheck = [0]*len(range(a[-1],b[0]+1))
    bcheck = [0]*len(range(a[-1],b[0]+1))
    for i in range(a[-1],b[0]+1):
        aflag=1
        bflag=1
        for anum in a:
            if i%anum!=0:
                aflag=0
                break
        if aflag==1:
            acheck[i-a[-1]] = aflag
        for bnum in b:
            if bnum%i!=0:
                bflag=0
                break
        if bflag==1:
            bcheck[i-a[-1]] = bflag
    for i in range(0,b[0]+1-a[-1]):
        if acheck[i]==1 and bcheck[i]==1:
            count+=1
    return count
n,m = list(map(int,input().split()))
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
total = getTotalX(a,b)
print(total)

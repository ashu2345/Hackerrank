def subsets(a,ssets):
    if a:
        return subsets(a[1:],ssets)+subsets(a[1:],ssets+[a[0]])
    return [ssets]

def solve(a, k):
    count = 0
    reqsets = subsets(a,[])
    reqsets.remove([])
    for s in reqsets:
        if len(s) == 1 and s[0]<k:
            count+=1
        elif len(s)>1:
            subxor = s[0]
            for e in range(1,len(s)):
                subxor^=s[e]
            if subxor<k:
                count+=1
    return count

n,k = map(int,input().split())
a = list(map(int,input().rstrip().split()))
print(solve(a,k))

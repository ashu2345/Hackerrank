def appendAndDelete(s,t,k):
    for i in range(len(s),-1,-1):
        if t.startswith(s[:i]):
            break
        k-=1
    s=s[:i]
    while s!=t and k>0:
        s+=t[i]
        i+=1
        k-=1
    if k<0 or s!=t:
        return 'No'
    else:
        return 'Yes'
s = input()
t = input()
k = int(input())
result = appendAndDelete(s,t,k)
print(result)

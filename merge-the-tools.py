s = input()
k = int(input())
n = len(s)
for i in range(0,n-k+1,k):
    u=[]
    print(i,i+k)
    t = s[i:i+k]
    for j in range(len(t)):
        if j!=t.index(t[j]):
            continue
        else:
            u.append(t[j])
    print(''.join(u))

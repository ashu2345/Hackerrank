n = int(input())
dash = '-'
bottomsec = []
alphalist = list(map(chr,range(97,123)))
for i in range(n):
    middleP = ''
    for j in range(n,n-i-1,-1):
        middleP += (dash+alphalist[j-1])
    revp = list(middleP)
    revp.reverse()
    middleP+=''.join(revp[1:])
    line = dash*(2*(n-i)-3)+middleP+dash*(2*(n-i)-3)
    if i==n-1:
        print(line.strip('-'))
        break
    print(line)
    bottomsec.append(line)
for k in range(len(bottomsec)-1,-1,-1):
    print(bottomsec[k])
    

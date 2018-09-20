repo = []

def solve(n,memo):
    count = 0
    alimit = int(n**(1/3))
    blimit = n//2
    if len(repo)!=0:
        astart = repo[-1][0]+1
        count+=repo[-1][1]
    else:
        astart = 2
    for a in range(astart,alimit+1):
        for b in range(blimit,0,-1):
            if (a**3)*b<=n and (a**3)*b in memo:
                pass
            elif (a**3)*b<=n and (a**3)*b not in memo:
                print(a,b)
                memo.append((a**3)*b)
                count+=1
    repo.append((n,count))
    print(repo,memo)
    return count

for _ in range(int(input())):
    n = int(input().strip())
    memo = []
    result = solve(n,memo)
    print(result)

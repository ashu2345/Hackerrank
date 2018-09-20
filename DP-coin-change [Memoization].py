def getWays(n,c,mem):
    key = "{0}:{1}".format(n,c)
    if n == 0:
        return 1
    elif n<0 or len(c) == 0:
        return 0
    if c[-1] > n and key not in mem:
        mem[key] = getWays(n,c[:-1],mem)
    elif c[-1]<=n and key not in mem:
        mem[key] = getWays(n-c[-1],c,mem)+getWays(n,c[:-1],mem)
    return mem[key]

if __name__ == '__main__':
    n,m = map(int,input().split())
    c = list(map(int,input().strip().split()))
    c.sort()
    mem = {}
    ways = getWays(n,c,mem)
    print(ways)

def getWays(n,c):
    key = "{0}:{1}".format(n,c)
    if n == 0:
        return 1
    elif n<0 or len(c) == 0:
        return 0
    if c[-1] > n and key:
        return getWays(n,c[:-1])
    elif c[-1]<=n:
        return getWays(n-c[-1],c)+getWays(n,c[:-1])

if __name__ == '__main__':
    n,m = map(int,input().split())
    c = list(map(int,input().strip().split()))
    c.sort()
    ways = getWays(n,c)
    print(ways)

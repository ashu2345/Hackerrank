def solve(n):
    cubelovers = set()
    if n<8:
        return 0
    alimit = int(n**(1/3))
    for a in range(2,alimit+1):
        lterm = n//a**3
        cubelovers = cubelovers.union(set(range(a**3,(a**3)*lterm+1,a**3)))
    return len(cubelovers)
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input().strip())
        result = solve(n)
        print(result)

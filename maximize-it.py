from itertools import product
k,m = list(map(int,input().split()))
arr = []
cart_prod = []
maxS=0
for _ in range(k):
    lstN = list(map(int,input().split()[1:]))
    arr.append(lstN)
cart_prod = list(product(*arr))
for elem in cart_prod:
    sum1=0
    for i in elem:
        sum1+=i**2
    if sum1%m>maxS:
        maxS = sum1%m
print(maxS)

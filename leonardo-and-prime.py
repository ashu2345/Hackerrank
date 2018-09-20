
def isprime(n):
    cond = True
    if n>1:
        for i in range(2,n):
            if n%i==0:
                cond = False
                break
            else:
                continue
    else:
        cond = False
    return cond
#
# Complete the primeCount function below.
#

primelist = list(filter(isprime,range(1,10000)))


def primeCount(n):
    prod = 2
    count=0
    while prod<=n:
        prod*=primelist[count+1]
        count+=1
    return count
    #
    # Write your code here.
    #
q = int(input())

for q_itr in range(q):
    n = int(input())

    result = primeCount(n)
    print(result)

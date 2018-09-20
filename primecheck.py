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
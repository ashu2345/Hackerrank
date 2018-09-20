def makeAnagram(a, b):
    count = 0
    acopy = set(a)
    bcopy = set(b)
    for c in acopy.symmetric_difference(bcopy):
        print(c)
        if c in a:
            count+=a.count(c)
            a = a.replace(c,"")
            print(a,count)
        elif c in b:
            count+=b.count(c)
            b = b.replace(c,"")
            print(b,count)
    print(a,b)
    for c in set(a).union(set(b)):
        if a.count(c)!=b.count(c):
            count+=abs(a.count(c)-b.count(c))
    return count

a = input()
b = input()
res = makeAnagram(a,b)
print(res)

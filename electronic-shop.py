from itertools import product

def sumOfElem(arr):
    return arr[0]+arr[1]

def getMoneySpent(keyboards, drives, b):
    combos = list(product(keyboards,drives))
    combos.sort(key=sumOfElem,reverse=True)
    for elem in combos:
        if sumOfElem(elem)<=b:
            return sumOfElem(elem)
    return -1

bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)

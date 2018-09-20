def pickingNumbers(a):
    length = 0
    maxlength = 0
    for i in set(a):
        for j in set(a):
            if abs(i-j) == 1:
                length = a.count(i)+a.count(j)
            elif i == j:
                length = a.count(i)
            if length > maxlength:
                maxlength = length
    return maxlength

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

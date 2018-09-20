def equal(arr,count):
    arr.sort()
    if min(arr) == max(arr):
        return count
    elif min(arr) != max(arr):
        if abs(max(arr)-(min(arr)+1))<abs(max(arr)-(min(arr)+2)) and abs(max(arr)-(min(arr)+1))<abs(max(arr)-(min(arr)+5)):
            c = 1
            count+=1
        elif abs(max(arr)-(min(arr)+2))<abs(max(arr)-(min(arr)+1)) and abs(max(arr)-(min(arr)+2))<abs(max(arr)-(min(arr)+5)):
            c = 2
            count+=1
        elif abs(max(arr)-(min(arr)+5))<abs(max(arr)-(min(arr)+1)) and abs(max(arr)-(min(arr)+5))<abs(max(arr)-(min(arr)+2)):
            c = 5
            count+=1
        for j in range(len(arr)-1):
            arr[j]+=c
        count = equal(arr,count)
    return count
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        count = 0
        ways = equal(arr,count)
        print(ways)

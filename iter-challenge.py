from itertools import combinations
count=0
n = int(input())
arr = list(input().split())
k = int(input())
comb = list(combinations(arr,k))
print(comb)
for elem in comb:
    if 'a' in elem:
        count+=1
print(count/len(comb))

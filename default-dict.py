from collections import defaultdict
A = []
B = []
C = defaultdict(list)
n,m = list(map(int,input().split()))
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
for i in range(len(B)):
    for j in range(len(A)):
        if B[i]==A[j]:
            C[B[i]].append(j+1)
    strC = [str(ele) for ele in C[B[i]]]
    print(' '.join(strC))

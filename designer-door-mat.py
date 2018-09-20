dash = '-'
deco = '.|.'
n,m = list(map(int,input().split()))
for i in range(n//2):
    dashwidth = m//2-3*i-1
    decowidth = 2*i+1
    print(dash*dashwidth+decowidth*deco+dash*dashwidth)
print(dash*((m-7)//2)+'WELCOME'+dash*((m-7)//2))
for i in range(n//2):
    dashwidth = 3+3*i
    decowidth = (n//2-i)*2-1
    print(dash*dashwidth+deco*decowidth+dash*dashwidth)

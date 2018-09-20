s = input()
scoreK = 0
scoreS = 0
vowels = ['a','e','i','o','u']
for i in range(len(s)):
    if s[i].lower() in vowels:
        scoreK+=len(s)-i
    else:
        scoreS+=len(s)-i
if scoreK>scoreS:
    print('Kevin',scoreK)
elif scoreK<scoreS:
    print('Stuart',scoreS)
elif scoreK==scoreS:
    print('Draw')

import re
linelist = []
for _ in range(int(input())):
    linelist.append(input())
for _ in range(int(input())):
    word = input()
    ptrn = r'^%s\W|\W%s\W|\W%s\W*$'%(word,word,word)
    count=0
    for line in linelist:
        count+=len(re.findall(ptrn,line))
    print(count)

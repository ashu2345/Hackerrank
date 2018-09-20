import re
S = input()
flag = 0
for c in S:
    if c in map(str,range(10)):
        m = re.match(r'([%s])+'%c,S)
        print(m.group(0))
        if len(m.group(0))>1:
            flag=1
            repchar = c
            break
    else:
        continue

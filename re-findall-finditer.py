import re
S = input()
reqlist = re.findall(r'[^aeiou][aeiou]{2,}(?=[^aeiou])',S,re.IGNORECASE)
if len(reqlist)!=0:
    for ptrn in reqlist:
        print(ptrn[1:])
else:
    print(-1)

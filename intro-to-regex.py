import re
for _ in range(int(input())):
    n = input()
    ptrn = re.match(r'^[+-]?[0-9]*\.[0-9]+$',n)
    if ptrn:
        print(True)
    else:
        print(False)

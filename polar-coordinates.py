from cmath import phase
import re
comp = input()
m = re.match(r'([+-]{0,1}\d{1,2})([+-]{0,1}\d{1,2})j',comp)
print(m)
a = int(m.group(1))
b = int(m.group(2))
print(abs(complex(a,b)))
print(phase(complex(a,b)))

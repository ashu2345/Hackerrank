import re
try:
    reg = r'[,.]?'
    print('\n'.join(re.split(reg,input())))
except FutureWarning:
    

import re
n = int(input())
lines = []
emails = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
for line in lines:
    m = re.findall(r'[a-zA-Z_]+[@][a-zA-Z]+\.[a-z]{,3}',line)
    emails.extend(m)
emails.sort()
print(';'.join(emails).strip(';'))

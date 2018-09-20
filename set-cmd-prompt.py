n = int(input())
sum=0
s = set(map(int, input().split()))
for i in range(int(input())):
    command = input()
    if command.startswith('pop'):
        s.pop()
    elif command.startswith('remove'):
        s.remove(int(command.split()[1]))
    elif command.startswith('discard'):
        s.discard(int(command.split()[1]))
for i in s:
    sum+=i
print(sum)

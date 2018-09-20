def print_formatted(number):
    t = len(bin(number))-2
    for i in range(1,number+1):
        line = '{0:{t}d} {0:{t}o} {0:{t}x} {0:{t}b}'.format(i,width=t)
        print(line)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

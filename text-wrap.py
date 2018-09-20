def wrap(string,max_width):
    finalstring=''
    for i in range(0,len(string),max_width):
        if i+max_width > len(string):
            finalstring += string[i:]
            break
        finalstring += (string[i:i+max_width]+'\n')
    return finalstring

if __name__ == '__main__':
    string,max_width = input(),int(input())
    result = wrap(string,max_width)
    print(result)

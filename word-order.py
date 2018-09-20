from collections import OrderedDict
wordlist = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word not in wordlist.keys():
        wordlist[word]=1
    else:
        wordlist[word]+=1
print(len(wordlist.keys()))
for word in wordlist.keys():
    print(wordlist[word],end=' ')

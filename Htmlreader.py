from bs4 import BeautifulSoup
import os
url = input('Enter the url of the website which you want to save: ')
target_dir = input('Enter the directory where you want to save the website: ')
target = input('Enter the name of the file: ')
print(target_dir+target)
command = r'C:\wget\wget --no-check-certificate {0} {1}'.format(url,target_dir+target)
os.system(command)
f = open(target_dir+target)
html = ''
try:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        html+=line+'\n'
except:
    pass
f.close()
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())

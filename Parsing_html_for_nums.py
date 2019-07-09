
import re
import urllib.request
from bs4 import BeautifulSoup


sauce= urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_235102.html').read()

soup=BeautifulSoup(sauce,'html.parser')
tags=soup.find_all('span')

sum=0
for tag in tags:
    tag=tag.string  #get text of tag
    numbers = re.findall('[0-9]+', tag)
    for number in numbers:
        sum=sum + int(number)
print(sum)

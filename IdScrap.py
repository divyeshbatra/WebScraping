import re
import urllib3
from bs4 import BeautifulSoup

from Filewriter import Filewriter
from Scrap import Scrap

#specify page number here
page='8'
http= urllib3.PoolManager()
url= 'http://vin.place/complete.php?id='+page
response=http.request('GET',url)
soup=BeautifulSoup(response.data,"html.parser")
#print(soup)
urlbox=[]
special_divs = soup.find_all('div',{'class':'nooverflow'})
for text in special_divs:
    download = text.find_all('a',href = re.compile('\.html$'))
    for text in download:
        hrefText = (text['href'])
        urlbox.append(hrefText)

finalurlbox=[]

for num in urlbox:
    if num not in finalurlbox:
        finalurlbox.append(num)

print(finalurlbox)

scrapfinalforwrite=[[]]

for i in range(len(finalurlbox)):
    scrapfinal=Scrap(page,finalurlbox[i])
    scrapfinalforwrite.append((scrapfinal))

print(scrapfinalforwrite)
list2 = [x for x in scrapfinalforwrite if x != []]
print(list2)

Filewriter(list2)






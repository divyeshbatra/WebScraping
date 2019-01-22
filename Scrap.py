import urllib3
from bs4 import BeautifulSoup

import csv

def Scrap(page,url):
 http= urllib3.PoolManager()

 #url='/vin/jonathan-ramsey.95.html'
 urlstatic='http://vin.place'
 urlbinder= urlstatic + url
 print(urlbinder)
 finalinfo = []
 headers = []
 headersOriginal = ['Customer Name', 'Address', 'City', 'State', 'Zip', 'Phone', 'Year', 'Make', 'Model', 'VIN','Barrels 08']

 response=http.request('GET',urlbinder)
 soup=BeautifulSoup(response.data,"html.parser")


 name_box = soup.find('div', attrs={'class': 'section'})
 if name_box == None:
  pass
 else:
    info=[]

    info.append(name_box.find('h2').text)
    list_box = soup.find('ul', attrs={'class': 'list'})

    x= list_box.find_all('li')


    for i in range(len(x)):
     info.append(x[i].text)

    info = info[:-3]
    # del info[-2]
    # del info[-3]


    for i in range(len(info)):
        headers.append(info[i].split(":", 1)[0])
    for i in range(len(info)):
        finalinfo.append(info[i].split(":", 1)[1])

    differencelist = list(set(headersOriginal).difference(headers))
    # print(differencelist)
    for i in range(len(differencelist)):
        if differencelist[i] == 'Customer Name':
            differencelist[i] = 0
        elif differencelist[i] == 'Address':
            differencelist[i] = 1
        elif differencelist[i] == 'City':
            differencelist[i] = 2
        elif differencelist[i] == 'State':
            differencelist[i] = 3
        elif differencelist[i] == 'Zip':
            differencelist[i] = 4
        elif differencelist[i] == 'Phone':
            differencelist[i] = 5
        elif differencelist[i] == 'Year':
            differencelist[i] = 6
        elif differencelist[i] == 'Make':
            differencelist[i] = 7
        elif differencelist[i] == 'Model':
            differencelist[i] = 8
        elif differencelist[i] == 'Vin':
            differencelist[i] = 9
        elif differencelist[i] == 'Barrels 08':
            differencelist[i] = 10

    differencelist.sort()

    for i in range(len(differencelist)):
        finalinfo.insert(differencelist[i], 'NULL')
        # finalinfo.insert(0,page)


        # finalinfo.insert(0,page)

    finalinfo.insert(0,page)
    #print(finalinfo)

 return (finalinfo)










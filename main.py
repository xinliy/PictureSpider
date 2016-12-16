from urllib.request import  urlopen,urlretrieve
from bs4 import BeautifulSoup

def getLinks(articleUrl):
    html = urlopen(articleUrl)
    url1 = BeautifulSoup(html)

    for b in url1.find_all("div", class_="content"):
        print(b)
        d =b.find_all('img')
        print(d)
        r=0
        for c in b.find_all("img"):
          print('11--------------------------------------------')
          print(c.attrs['src'])
          path ='d:\\bs4\\'+str(r)+'.jpg'
          print(path)
          urlretrieve(c.attrs['src'], path)
          r=r+1
          print('已经下载')

links = getLinks("http://pic.yesky.com/c/6_22231.shtml")

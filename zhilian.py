#coding:utf-8

from urllib import request
import re
from bs4 import BeautifulSoup
import os


def getInfoOnePage():
    pass

def getAllUrlOnePage(html):
    htmlcontent =getHtml(html)
    hisfile = os.open('/home/bing/python/zlSpider/1.txt',os.O_RDWR)
    os.write(hisfile,htmlcontent.encode('utf-8'))
    os.close(hisfile)


    mainsoup = BeautifulSoup(htmlcontent, 'html.parser')  
    main = mainsoup.find_all('div',attrs={'id':'listContent'})

    urlcountdic={}
    urllist=[]
    try:
        for urlandcount in main:

            img_url = re.findall('href="(/\d{1,10}\.html)"',str(urlandcount))
            img_count = re.findall('<span>(\d{1,10})</span>',str(urlandcount))

            dict1={img_url[0]:img_count[0]}
            urlcountdic.update(dict1)
            urllist.append(img_url[0])
    except Exception as identifier:
        pass
   
    return urllist,urlcountdic

def getHtml(url):
    opener=request.build_opener()
    chaper_url= url
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')]
    request.install_opener(opener)
    respone = request.urlopen(chaper_url)
    html= respone.read().decode('utf-8')
    #html= respone.read()
     
    return html



def main():
    url = 'https://sou.zhaopin.com/?jl=530&kw=C#&kt=3'
    getAllUrlOnePage(url)

if __name__ == "__main__":
    main()
    
    print('程序结束')

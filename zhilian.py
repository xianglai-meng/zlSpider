#coding:utf-8

from urllib import request
import re
from bs4 import BeautifulSoup
import os
import json


class zpClass(object):
    def __init__(self):
        self.company= company
        self.jobName= jobName
        self.type = type
        self.size = size
        self.city = city
        self.updateDate= updateDate
        self.salary=salary
        self.eduLevel=eduLevel
        self.jobType=jobType
        self.workingExp=workingExp
        self.emplType=emplType
        self.url=url
        self.welfare=welfare
        self.businessArea=businessArea


def getInfoOnePage():
    pass

def getAllUrlOnePage(html):
    htmlcontent =getHtml(html)
    #print(str(htmlcontent))
    # hisfile = os.open('/home/bing/python/zlSpider/1.txt',os.O_RDWR)
    # os.write(hisfile,htmlcontent.encode('utf-8'))
    # os.close(hisfile)

    zpJson = json.loads(htmlcontent)
    #print(zpInfo)

    zpInfos = (zpInfo["data"])["results"]

    zp = zpClass
    for i in len(zpInfos):   
    zp.jobName = ((zpInfo["data"])["results"])[0]
    zp.url= zpInfo.url

    # mainsoup = BeautifulSoup(htmlcontent, 'html.parser')  
    # main = mainsoup.find_all('div',attrs={'id':'listContent'})

    # urlcountdic={}
    # urllist=[]
    # try:
    #     for urlandcount in main:

    #         img_url = re.findall('href="(/\d{1,10}\.html)"',str(urlandcount))
    #         img_count = re.findall('<span>(\d{1,10})</span>',str(urlandcount))

    #         dict1={img_url[0]:img_count[0]}
    #         urlcountdic.update(dict1)
    #         urllist.append(img_url[0])
    # except Exception as identifier:
    #     pass
   
    # return urllist,urlcountdic

def getHtml(url):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://sou.zhaopin.com',
        'Referer': 'https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=C',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    # 需要使用url和headers生成一个Request对象，然后将其传入urlopen方法中
    req = request.Request(url, headers=headers)
    respone = request.urlopen(req)
    html= respone.read().decode('utf-8')

    return html



def main():

    url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=15001,25000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=C%23&kt=3&=15001&userCode=125678027&at=7dd18a04c95e43de965b7b1769be77a8&rt=58faace82a0745e2bcdf6a98d29fe794&_v=0.57206713&x-zp-page-request-id=58b6e353b7434917a2e3ba77b41a7e63-1560413029089-47837&x-zp-client-id=765a2c81-adbe-4c98-958d-76b6383c74e6'
    getAllUrlOnePage(url)

if __name__ == "__main__":
    main()
    
    print('程序结束')

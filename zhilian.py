#coding:utf-8
import urllib 
import requests
import re
from bs4 import BeautifulSoup
import os
import json
#from prettytable import PrettyTable
import MySQLdb
import time
import pyecharts


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

def insertIntoDB(zpClass):
    conn = MySQLdb.connect("localhost", "root", "bing", "db_zpinfo", charset='utf8' )
    cur = conn.cursor()

    sqlstr ="insert into t_zljob \
    ( \
       company,job_name,city,update_str,salary,edu_level,job_type,working_exp,empl_type, \
       position_url,welfare,business_area,c_type  \
    ) \
    values ( '%s','%s','%s','%s', '%s','%s','%s','%s','%s','%s','%s','%s', '%s');" %(zpClass.company,
    zpClass.jobName,zpClass.city,zpClass.updateDate,zpClass.salary,  
    zpClass.eduLevel,zpClass.jobType,zpClass.workingExp,zpClass.emplType,zpClass.url, 
    ''.join(zpClass.welfare),zpClass.businessArea,zpClass.type)

    # sqlstr ="insert into t_zljob \
    # ( \
    #    job_name \
    # ) \
    # values \
    # (' %s');" %('ok') 

    cur.execute(sqlstr)

    cur.close()
    #必须有这句，否则不是真的插入
    conn.commit()
    conn.close()


def selectFromDB(sqlstr):
    pass


def getInfoOnePage():
    pass

def getAllUrlOnePage(html,data):
    htmlcontent =getHtml(html,data)
    #print(str(htmlcontent))
    # hisfile = os.open('/home/bing/python/zlSpider/1.txt',os.O_RDWR)
    # os.write(hisfile,htmlcontent.encode('utf-8'))
    # os.close(hisfile)

    zpJson = json.loads(htmlcontent)
    #print(zpInfo)

    zpInfos = (zpJson["data"])["results"]

   # x = PrettyTable(["jobName", "positionURL"])

    zp = zpClass
    x = len(zpInfos)
    #count = len(zpInfos[0])-1
    count = len(zpInfos)-1
    for i in range(count):   
        zp.jobName = (zpInfos[i])['jobName']
        zp.url= (zpInfos[i])['positionURL']
        zp.company = ((zpInfos[i])['company'])['name']
        zp.type= (zpInfos[i])['emplType']
       # zp.size = (zpInfos[i])['size']
        zp.city= ((zpInfos[i])['city'])['display']
        zp.updateDate = (zpInfos[i])['updateDate']
        zp.salary= (zpInfos[i])['salary']
        zp.eduLevel = ((zpInfos[i])['eduLevel'])['name']
        zp.jobType= ((((zpInfos[i])['jobType'])['items'])[0])['name']
        zp.workingExp = ((zpInfos[i])['workingExp'])['name']
        zp.emplType= (zpInfos[i])['emplType']
        zp.welfare = (zpInfos[i])['welfare']
        zp.businessArea= (zpInfos[i])['businessArea']

        insertIntoDB(zp)
        #x.add_row([(zpInfos[i])['jobName'],(zpInfos[i])['positionURL']])
   

def getHtml(url,data):
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Origin': 'https://sou.zhaopin.com',
        # 'Referer': 'https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=C',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

    ajdata = urllib.parse.urlencode(data).encode(encoding='UTF8') 
    # 需要使用url和headers生成一个Request对象，然后将其传入urlopen方法中
    req = urllib.request.Request(url,data=None, headers=headers)

    #req = urllib.request.Request(url, headers=headers)
    respone = urllib.request.urlopen(req)
    html= respone.read().decode('utf-8')

    return html

def setSearchUrl(page,wd):
     url='https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=530&salary=15001,25000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=15001&userCode=125678027&at=7dd18a04c95e43de965b7b1769be77a8&rt=58faace82a0745e2bcdf6a98d29fe794&_v=0.57206713&x-zp-page-request-id=58b6e353b7434917a2e3ba77b41a7e63-1560413029089-47837&x-zp-client-id=765a2c81-adbe-4c98-958d-76b6383c74e6'.format(page,wd)
     return url


def main():

   # url='https://fe-api.zhaopin.com/c/i/sou?pageSize=%s&cityId=530&salary=15001,25000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=C%23&kt=3&=15001&userCode=125678027&at=7dd18a04c95e43de965b7b1769be77a8&rt=58faace82a0745e2bcdf6a98d29fe794&_v=0.57206713&x-zp-page-request-id=58b6e353b7434917a2e3ba77b41a7e63-1560413029089-47837&x-zp-client-id=765a2c81-adbe-4c98-958d-76b6383c74e6'%
    url="https://fe-api.zhaopin.com/c/i/sou?cityId=530&salary=15001,25000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&=15001&userCode=125678027&at=7dd18a04c95e43de965b7b1769be77a8&rt=58faace82a0745e2bcdf6a98d29fe794&_v=0.57206713&x-zp-page-request-id=58b6e353b7434917a2e3ba77b41a7e63-1560413029089-47837&x-zp-client-id=765a2c81-adbe-4c98-958d-76b6383c74e6"
    #url="https://fe-api.zhaopin.com/c/i/sou?cityId=530&salary=15001,25000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&=15001&userCode=125678027&at=7dd18a04c95e43de965b7b1769be77a8&rt=58faace82a0745e2bcdf6a98d29fe794&_v=0.57206713&x-zp-page-request-id=58b6e353b7434917a2e3ba77b41a7e63-1560413029089-47837&x-zp-client-id=765a2c81-adbe-4c98-958d-76b6383c74e6&pageSize=90&kw=java"
    page =0
    language =['Java','C','Python','C++','Visual Basic .NET','C#','JavaScript','php','Sql','Go']
    formdata={
        # "pageSize":"90",
        # "kw":"java"
    }
    for x  in language:      
        tempwd= urllib.parse.quote(x)
        print(x)
        print(tempwd)
        #time.sleep(0.2)
        for num in range(1,11):
            page =num*90           
            #getAllUrlOnePage(setSearchUrl(page,tempwd))
            getAllUrlOnePage(url,formdata)

if __name__ == "__main__":
    main()
    
    print('程序结束')

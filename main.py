# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import pymysql
#from sqlalchemy import create_engine
from tosql import tosql

url_js='http://www.jshrss.gov.cn/rsrcfww/xwdt/tzgg/sydwzp/index_{page}.html'
# con=pymysql.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='foow',
#     passwd='foow',
#     db='for00work'
# )
ts = tosql('for00work', user='foow', passwd='foow')
#engine=create_engine("mysql+mysqldb://foow:"+'foow'+"@localhost/for00work",encoding='utf-8')
def getdata(url,page):
    res=requests.get(url.format(page=page))
    res_bs=BeautifulSoup(res.text,"html5lib")
    res_bs.encode('utf8')
    return res_bs
##just for JS RSJ
for page in range(1,50):
    res=getdata(url_js,page)
    res_bs_l=res.select(".z_mainbox > .files_left_box > .files_left_box_border > .xwdt_list > ul > li")
#res_bs_l=res_bs.select('a[href]')
    df=pd.DataFrame(columns=['date','name','url'])
    for i in range(len(res_bs_l)):
        list_m=res_bs_l[i]
        l_date=list_m.select('.date')[0].string.replace('(','').replace(')','')
        l_name=list_m.select('a')[0].string
        l_url=list_m.find_all('a')[0].get('href')
        print(l_date.encode())
#        df=df.append({'date':l_date.encode('utf8'), 'name':l_name.ecode('utf8'), 'url':l_url.encode('utf8')},ignore_index=True)
        df=df.append({'date':l_date, 'name':l_name, 'url':l_url},ignore_index=True)
    df1=pd.DataFrame({'date':'2017-8-2', 'name':'haha', 'url':'hah'},index=[0])
#    print(df)
    #df.to_sql('JS',engine ,index=False,if_exists='append')
    #l_date=list_main

    ts.insert(df,'JS')
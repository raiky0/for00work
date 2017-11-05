# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import pymysql
from sqlalchemy import create_engine

url_js='http://www.jshrss.gov.cn/rsrcfww/xwdt/tzgg/sydwzp/index_{page}.html'
# con=pymysql.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='foow',
#     passwd='foow',
#     db='for00work'
# )
engine=create_engine("mysql+mysqldb://foow:"+'foow'+"@localhost/for00work",encoding='utf-8')
res=requests.get(url_js.format(page=1))
res_bs=BeautifulSoup(res.text,"html5lib")
res_bs.encode('utf8')
res_bs_l=res_bs.select(".z_mainbox > .files_left_box > .files_left_box_border > .xwdt_list > ul > li")
#res_bs_l=res_bs.select('a[href]')
df=pd.DataFrame(columns=['date','name','url'])
print(df)
for i in range(len(res_bs_l)):
    list_m=res_bs_l[i]
    l_date=list_m.select('.date')[0].string.replace('(','').replace(')','')
    l_name=list_m.select('a')[0].string
    l_url=list_m.find_all('a')[0].get('href')
    print(l_date.encode())
    df=df.append({'date':l_date.encode('utf8'), 'name':l_name.encode('utf8'), 'url':l_url.encode('utf8')},ignore_index=True)
print(df)
df1=pd.DataFrame({'date':'2017-8-2', 'name':'haha', 'url':'hah'},index=[0])
df.to_sql('JS',engine ,index=False,if_exists='append')
#l_date=list_main
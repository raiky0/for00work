# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url_sd='http://www.sdhrss.gov.cn/pages/zxzx/zthd/sssydwzpzt/zpxx/index2.html'
res=requests.get(url_sd)
res.encoding='gbk'
res_list=BeautifulSoup(res.text,'html.praser')
print(res_list)
